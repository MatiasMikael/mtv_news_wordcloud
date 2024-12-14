import pandas as pd

# Step 1: Load data
print("Loading data from CSV file...")
file_path = "C:\\Users\\Matias\\Desktop\\mtv_news_wordcloud\\2_data\\news_articles.csv"
data = pd.read_csv(file_path)
print(f"Data loaded successfully. Total rows: {len(data)}")

# Step 2: Replace '–' with '-' in titles
print("Replacing long dashes (–) with hyphens (-) in titles...")
data['title'] = data['title'].str.replace('–', '-', regex=False)
print("Replacement completed.")

# Step 3: Filter out video links
print("Filtering out rows with video links...")
cleaned_data = data[~data['link'].str.contains('/videot/video/')]
print(f"Filtering completed. Remaining rows: {len(cleaned_data)}")

# Step 4: Save cleaned data to a new CSV file
print("Saving cleaned data to a new file...")
output_path = "C:\\Users\\Matias\\Desktop\\mtv_news_wordcloud\\3_cleaned_data\\cleaned_news_articles.csv"
cleaned_data.to_csv(output_path, index=False)
print(f"Cleaned data saved successfully to: {output_path}")