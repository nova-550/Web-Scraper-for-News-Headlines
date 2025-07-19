# 📰 **News Headline Web Scraper**

*A Python script to fetch and save news headlines from websites like BBC News, CNN, or Reuters.*

---

## **📌 Table of Contents :**

- Features
- Prerequisites
- Installation
- Usage
---

## **Features :**

- **Fetches headlines** from news websites (e.g., BBC, CNN).
- **Parses HTML** using BeautifulSoup to extract relevant titles.
- **Saves results** to a
  
  ```
  headlines.txt
  ```

---

## **Prerequisites :**

- Python 3.6+  
- Libraries:

  ```
   - request
   - BeautifulSoup4
  ```

---

## **Installation :**

1. **Clone the repository :**

   ```
   - git clone https://github.com/nova-550/Web-Scraper-for-News-Headlines.git
   - cd Web-Scraper-for-News-Headlines
   ```
2. **Install dependencies :** 

   ```
   pip install requests beautifulsoup4
   ```

---

## **Usage**

### **Basic Scraping**

Run the script to scrape BBC News:  

```
python news_scraper.py
```

Output saved to
  ```
  headlines.txt
  ```
  
### **Custom URL**

Modify url in the script:  
```
url = "https://edition.cnn.com/"  # Change to target site
```

### **CLI Version (Optional)**

Run with a dynamic URL:  

```
python news_scraper.py --url "https://www.reuters.com/"
```

---

🎉 **Happy Scraping!** Let me know if you need further enhancements. 🚀
