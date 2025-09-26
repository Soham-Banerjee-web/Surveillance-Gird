from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

class SeleniumRunner:
    def __init__(self, url):
        self.url = url
        self.driver = None

    def start_driver(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get(self.url)

    def scrape_data(self):
        # Example of scraping logic
        time.sleep(3)  # Wait for the page to load
        data = self.driver.find_elements(By.TAG_NAME, 'h1')  # Change the tag as needed
        scraped_data = [element.text for element in data]
        return scraped_data

    def close_driver(self):
        if self.driver:
            self.driver.quit()

if __name__ == "__main__":
    url = "https://example.com"  # Replace with the target URL
    runner = SeleniumRunner(url)
    runner.start_driver()
    data = runner.scrape_data()
    print(data)
    runner.close_driver()