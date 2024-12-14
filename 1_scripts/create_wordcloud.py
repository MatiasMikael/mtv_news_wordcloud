import pandas as pd
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

# Step 1: Load cleaned data
print("Loading cleaned data...")
file_path = "C:\\Users\\Matias\\Desktop\\mtv_news_wordcloud\\3_cleaned_data\\cleaned_news_articles.csv"
data = pd.read_csv(file_path)
print(f"Data loaded successfully. Total rows: {len(data)}")

# Step 2: Prepare text for word cloud
print("Preparing text for word cloud...")
stopwords = set(STOPWORDS)
custom_stopwords = {"jo", "MTV", "ja", "voi", "nämä", "näin", "sai", "-", "Tämä", "tämän", "tämä", "sitä", "ei", "Ei", "ole", "olla"}
stopwords.update(custom_stopwords)

titles_combined = " ".join(data['title'])
print("Text combined from titles.")

# Step 3: Generate word cloud
print("Generating word cloud...")
wordcloud = WordCloud(
    width=800,
    height=400,
    background_color="white",
    stopwords=stopwords,
    colormap="viridis"
).generate(titles_combined)

# Step 4: Save word cloud as an image
output_path = "C:\\Users\\Matias\\Desktop\\mtv_news_wordcloud\\4_results\\mtv_wordcloud.png"
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.tight_layout()
plt.savefig(output_path)
print(f"Word cloud saved successfully to: {output_path}")

# Show the word cloud (optional)
plt.show()