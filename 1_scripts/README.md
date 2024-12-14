## Scripts Overview

This folder contains the Python scripts used in this project. Each script performs a specific task in the workflow. Below is a description of each script and how to run it.

**news_scraper.py**
This script scrapes news article titles and links from the MTV Uutiset website and saves them to a CSV file.
Run the script using the command:
python 1_scripts/news_scraper.py

**clean_data.py**
This script cleans the scraped data by removing unnecessary characters and filtering out unwanted rows. The cleaned data is saved to a new CSV file.
Run the script using the command:
python 1_scripts/clean_data.py

**create_wordcloud.py**
This script generates a word cloud from the cleaned data and saves it as an image file.
Run the script using the command:
python 1_scripts/create_wordcloud.py

***top_words_bar_chart.py**
This script analyzes the most common words from the cleaned data, generates a bar chart of the top 15 words, and saves the chart as an image file.
Run the script using the command:
python 1_scripts/top_words_bar_chart.py

**run_all_scripts.py**
This script automates the entire workflow by executing all the scripts in the correct order.
Run the script using the command:
python 1_scripts/run_all_scripts.py

Before running any scripts, ensure you have installed the required libraries in your virtual environment. Activate the environment and install dependencies using the **requirements.txt** file.