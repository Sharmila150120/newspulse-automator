NewsPulse Automator
NewsPulse is an automated intelligence tool that scrapes real-time technology headlines and direct article links from global news outlets. This project demonstrates the ability to programmatically "read" the web and transform unstructured HTML into a clean, actionable data feed.

🚀 The Real-World Use Case
In the industry, web scraping is used for Competitive Intelligence, Price Monitoring, and Content Aggregation. NewsPulse proves I can:

Bypass manual browsing to save time.

Gather data from sites without official APIs.

Create a custom "Information Pipeline" for business needs.

✨ Key Features
Live Scraper Engine: Uses BeautifulSoup4 to parse the live Document Object Model (DOM) of news sites.

Clickable Intelligence: Extracts both titles and URLs, allowing users to jump directly to the source article.

Dynamic Link Repair: Automatically detects and fixes relative URL paths (e.g., converting /news/123 to a full https://... link).

Industrial UI: A high-contrast, dark-mode dashboard built with Tailwind CSS.

🛠️ Technical Stack
Language: Python 3.x

Scraping: BeautifulSoup4 & Requests

Web Framework: Flask

Styling: Tailwind CSS

📂 Project Structure
Plaintext
news/
├── app.py              
├── requirements.txt   
└── templates/
    └── index.html      
🧠 Technical Challenges Overcome
Handling Anti-Scraping: Implemented User-Agent headers to simulate real browser requests, ensuring the server doesn't block the script.

