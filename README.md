## MTV News Wordcloud Project
This project analyzes news headlines from the MTV Uutiset website by scraping, cleaning, and visualizing the data. The goal is to identify and present the most common words in the headlines using a word cloud and a bar chart.

### What This Project Does
* Scrapes news headlines and links from MTV Uutiset.
* Cleans the data by removing irrelevant entries and formatting text.
* Generates a word cloud to visualize the most frequent words.
* Creates a bar chart displaying the top 15 words and their frequencies.

### How to Run
* Clone the repository to your local machine.
* Set up a Python virtual environment and install the required libraries from **requirements.txt**.
* Run all steps with the command:
`python 1_scripts/run_all_scripts.py`
This will scrape the headlines, process the data, and generate the visual outputs.

### Outputs
* Cleaned data: Saved in 3_cleaned_data as a CSV file.
* Word cloud: Saved in 4_results as **mtv_wordcloud.png**, showing the most frequent words.
* Bar chart: Saved in 4_results as **top_15_words_chart.png**, providing a detailed view of the top words and their frequencies.
* The word cloud offers an artistic overview of headline trends, while the bar chart gives precise insights into word frequencies.

### License and Data Source
This project is licensed under the MIT License. The data is sourced from the MTV Uutiset website and is used for non-commercial purposes only.
