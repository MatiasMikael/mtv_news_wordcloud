import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import STOPWORDS

# Step 1: Load cleaned data
print("Loading cleaned data...")
file_path = "C:\\Users\\Matias\\Desktop\\mtv_news_wordcloud\\3_cleaned_data\\cleaned_news_articles.csv"
data = pd.read_csv(file_path)
print(f"Data loaded successfully. Total rows: {len(data)}")

# Step 2: Prepare text and remove stop words
print("Processing text and removing stop words...")
stopwords = set(STOPWORDS)
custom_stopwords = {"jo", "MTV", "ja", "voi", "nämä", "näin", "sai", "-", "Tämä", "tämän", "tämä", "sitä", "ei", "Ei", "ole", "olla"}
stopwords.update(custom_stopwords)

# Combine all titles into one string
titles_combined = " ".join(data['title'])

# Split words and filter out stop words
words = [word.lower() for word in titles_combined.split() if word.lower() not in stopwords]

# Step 3: Count word frequencies
print("Counting word frequencies...")
word_counts = Counter(words)
top_words = word_counts.most_common(15)
print(f"Top 15 words: {top_words}")

# Step 4: Create bar chart
print("Creating bar chart...")
words, counts = zip(*top_words)
plt.figure(figsize=(12, 7))
bars = plt.bar(words, counts, color="green")
plt.title("Top 15 Most Common Words in MTV3 News Titles", fontsize=16)
plt.xlabel("Words", fontsize=14)
plt.ylabel("Frequency", fontsize=14)
plt.xticks(rotation=45, fontsize=12)

# Add values on top of bars
for bar, count in zip(bars, counts):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), str(count),
             ha="center", va="bottom", fontsize=10)

plt.tight_layout()

# Step 5: Save the chart
output_path = "C:\\Users\\Matias\\Desktop\\mtv_news_wordcloud\\4_results\\top_15_words_chart.png"
plt.savefig(output_path)
print(f"Bar chart saved successfully to: {output_path}")

# Show the chart (optional)
plt.show()