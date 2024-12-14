import subprocess
import os
import sys

# Path to the Python interpreter in the virtual environment
python_executable = os.path.join("venv", "Scripts", "python")

# List of scripts to execute in order
scripts = [
    "1_scripts/news_scraper.py",
    "1_scripts/clean_data.py",
    "1_scripts/create_wordcloud.py",
    "1_scripts/top_words_bar_chart.py"
]

def run_scripts():
    for script in scripts:
        try:
            print(f"Running {script}...")
            subprocess.run([python_executable, script], check=True)
            print(f"{script} executed successfully.\n")
        except subprocess.CalledProcessError as e:
            print(f"Error occurred while running {script}: {e}")
            break

if __name__ == "__main__":
    print("Executing all scripts in the correct order...\n")
    run_scripts()
    print("All scripts executed.")