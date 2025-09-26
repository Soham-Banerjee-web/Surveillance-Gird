from scraper.selenium_runner import run_scraper
from data.storage import save_data

def collect_data():
    scraped_data = run_scraper()
    processed_data = process_data(scraped_data)
    save_data(processed_data)

def process_data(data):
    # Implement data cleaning and preparation logic here
    cleaned_data = data  # Placeholder for actual cleaning logic
    return cleaned_data

if __name__ == "__main__":
    collect_data()