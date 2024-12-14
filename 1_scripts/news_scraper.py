import os
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Print start
print("Starting news scraper...")

# Define URL and target file
url = "https://www.mtvuutiset.fi/"
base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../2_data"))
output_file = os.path.join(base_dir, "news_articles.csv")

# Ensure output directory exists
if not os.path.exists(base_dir):
    os.makedirs(base_dir)
    print(f"Created missing directory: {base_dir}")

# Fetch the HTML content
print(f"Fetching HTML content from {url}...")
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
print("HTML content fetched successfully.")

# Extract article titles and links
print("Extracting articles...")
articles = []
for article in soup.find_all("a", class_="group grow"):  # Updated class name
    title_element = article.find("h2")  # Look for the <h2> element inside the link
    if title_element:
        title = title_element.get_text(strip=True)
        link = article.get("href")
        if title and link:
            # Combine relative link with base URL
            full_link = f"https://www.mtvuutiset.fi{link}"
            articles.append({"title": title, "link": full_link})

print(f"Extracted {len(articles)} articles.")

# Save results to a CSV file
if articles:
    print(f"Saving articles to {output_file}...")
    df = pd.DataFrame(articles)
    df.to_csv(output_file, index=False)
    print(f"Articles saved successfully to {output_file}.")
else:
    print("No articles found. Nothing to save.")