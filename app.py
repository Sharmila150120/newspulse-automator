from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def home():
    # 1. Get the data from the web
    url = "https://www.bbc.com/news/technology"
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 2. Extract headlines and links
        news_list = []
        # This looks for all 'a' tags that have a 'h2' inside them
        for item in soup.find_all('a', href=True):
            title = item.find('h2')
            if title:
                link = item['href']
                # Fix the link if it's missing the website address
                full_link = link if link.startswith('http') else f"https://www.bbc.com{link}"
                
                news_list.append({
                    'title': title.get_text(strip=True),
                    'url': full_link
                })
        
        # Take only the top 10 stories
        top_news = news_list[:10]
        
    except Exception as e:
        print(f"Error: {e}")
        top_news = []

    return render_template('index.html', news=top_news)

if __name__ == "__main__":
    app.run(debug=True)