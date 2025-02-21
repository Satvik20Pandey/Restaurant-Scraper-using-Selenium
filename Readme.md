# Restaurant Scraper using Selenium
<br>📌 Project Overview
This project scrapes restaurant data from Google search results using Selenium and displays the retrieved data on a webpage. It mimics human-like browsing behavior to reduce bot detection and ensure smoother data extraction.<br>

<br>🛠 Features
✅ Scrapes multiple restaurants from Google Search

✅ Uses random delays and scrolling to mimic human behavior

✅ Stores restaurant data in a CSV file

✅ Automatically creates required directories

✅ Displays the scraped data on a web page

<br> 🚀Installation & Usage
1️⃣ Clone the Repository<br>
git clone https://github.com/yourusername/restaurant-scraper.git<br>
cd restaurant-scraper<br>
2️⃣ Install Dependencies<br>
pip install -r requirements.txt<br>
3️⃣ Run the Scraper<br>
python scraper.py<br>
This will scrape restaurant data from Google and save it in static/restaurants_new_delhi.csv.<br>

4️⃣ Start the Web Application<br>
python app.py<br>
Now, open http://127.0.0.1:5000/ in your browser to see the restaurant data.<br>

## 🖥 Technologies Used<br>
Python (Selenium, Flask, Pandas)<br>

HTML & CSS (Frontend UI)<br>

CSV (Data Storage)<br>

## ⚠️Notes<br>
Ensure Google Chrome and Chromedriver are installed.<br>

If you face the OSError: Cannot save file into a non-existent directory, manually create a static folder.

Google may block excessive requests. If CAPTCHA appears frequently, try using proxies or different user-agents.

🚀 Happy Scraping! 🎯
