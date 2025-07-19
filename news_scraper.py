import requests
from bs4 import BeautifulSoup

# Step 1: Fetch HTML content
url = "https://www.bbc.com/news"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Check for HTTP errors
except requests.exceptions.RequestException as e:
    print(f"Error fetching URL: {e}")
    exit()

# Step 2: Parse HTML and extract headlines
soup = BeautifulSoup(response.text, "html.parser")

# BBC uses h3 tags for headlines
headlines = soup.find_all("h2", class_="sc-9d830f2a-3 jqQlce")
headlines = soup.find_all("h2", class_="sc-9d830f2a-3 fWzToZ")

# Step 3: Save headlines to a text file
with open("headlines.txt", "w", encoding="utf-8") as file:
    for index, headline in enumerate(headlines, 1):
        headline_text = headline.get_text(strip=True)
        file.write(f"{index}. {headline_text}\n")

print("Successfully saved headlines to headlines.txt")
