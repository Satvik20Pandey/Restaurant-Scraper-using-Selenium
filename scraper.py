import time
import random
import pandas as pd
import webbrowser
from flask import Flask, render_template
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.90 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"
]

options = webdriver.ChromeOptions()
options.add_argument(f"user-agent={random.choice(USER_AGENTS)}")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--start-maximized")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://www.google.com")

time.sleep(random.uniform(3, 5))

search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Best Restaurants in New Delhi")
search_box.send_keys(Keys.RETURN)

time.sleep(random.uniform(4, 7))

restaurants = []
max_pages = 5  

for page in range(max_pages):
    results = driver.find_elements(By.CLASS_NAME, 'VkpGBb')
    for result in results:
        try:
            ActionChains(driver).move_to_element(result).perform()
            time.sleep(random.uniform(1, 3))
            name = result.find_element(By.CLASS_NAME, 'dbg0pd').text
        except:
            name = "N/A"
        try:
            rating = result.find_element(By.CLASS_NAME, 'BTtC6e').text
        except:
            rating = "N/A"
        try:
            address = result.find_element(By.CLASS_NAME, 'rllt__details').text.split("\n")[-1]
        except:
            address = "N/A"
        try:
            phone_number = result.find_element(By.CLASS_NAME, 'rllt__details').text.split("\n")[1]
        except:
            phone_number = "N/A"
        
        restaurants.append({"Name": name, "Rating": rating, "Address": address, "Phone": phone_number})

    try:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(random.uniform(2, 5))
        next_button = driver.find_element(By.LINK_TEXT, 'Next')
        next_button.click()
        time.sleep(random.uniform(4, 7))
    except:
        break

driver.quit()

df = pd.DataFrame(restaurants)
df.to_csv("static/restaurants_new_delhi.csv", index=False)

print(f"Scraping complete! {len(restaurants)} restaurants saved in restaurants_new_delhi.csv ✅")

webbrowser.open("http://127.0.0.1:5000")
app = Flask(__name__)

@app.route('/')
def index():
    df = pd.read_csv("static/restaurants_new_delhi.csv")
    return render_template('index.html', tables=[df.to_html(classes='table table-striped', index=False)], titles=df.columns.values)

if __name__ == '__main__':
    app.run(debug=False)