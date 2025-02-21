Restaurant Scraper using Selenium
📌 Project Overview
This project scrapes restaurant data from Google search results using Selenium and displays the retrieved data on a webpage. It mimics human-like browsing behavior to reduce bot detection and ensure smoother data extraction.

🛠 Features
✅ Scrapes multiple restaurants from Google Search

✅ Uses random delays and scrolling to mimic human behavior

✅ Stores restaurant data in a CSV file

✅ Automatically creates required directories

✅ Displays the scraped data on a web page

📂 Folder Structure
📂 Scrape Data
├── 📂 static                # Stores scraped data
│   └── restaurants_new_delhi.csv  
├── 📂 templates             # Contains HTML file for UI
│   └── index.html
├── scraper.py              # Main script to scrape data
├── app.py                  # Flask app to display data
├── requirements.txt        # List of dependencies
└── README.md               # Project documentation
🚀 Installation & Usage
1️⃣ Clone the Repository
git clone https://github.com/yourusername/restaurant-scraper.git
cd restaurant-scraper
2️⃣ Install Dependencies
pip install -r requirements.txt
3️⃣ Run the Scraper
python scraper.py
This will scrape restaurant data from Google and save it in static/restaurants_new_delhi.csv.

4️⃣ Start the Web Application
python app.py
Now, open http://127.0.0.1:5000/ in your browser to see the restaurant data.

🖥 Technologies Used
Python (Selenium, Flask, Pandas)

HTML & CSS (Frontend UI)

CSV (Data Storage)

⚠️ Notes
Ensure Google Chrome and Chromedriver are installed.

If you face the OSError: Cannot save file into a non-existent directory, manually create a static folder.

Google may block excessive requests. If CAPTCHA appears frequently, try using proxies or different user-agents.

🚀 Happy Scraping! 🎯