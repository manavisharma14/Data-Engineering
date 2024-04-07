from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd
import time
from reviews import get_reviews

def main():
    url = 'https://www.amazon.in/Sony-PS5-Console-Modern-Warfare/dp/B0CMQPPMB1'

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get(url)

    # Optionally wait for the page to fully load
    time.sleep(5)

    # First, click on the "see more reviews" link
    see_all_reviews_link = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="reviews-medley-footer"]/div[2]/a'))
    )
    see_all_reviews_link.click()

    # Wait for the reviews page to load
    time.sleep(5)

    all_reviews = []

    while True:
        # Scroll to the bottom to ensure all elements are loaded
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)  # Adjust based on your connection speed

        # Process current page
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        current_page_reviews = get_reviews(soup)
        all_reviews.extend(current_page_reviews)

        # Check if the "Next" button exists and is clickable
        next_buttons = driver.find_elements(By.XPATH, '//*[@id="cm_cr-pagination_bar"]/ul/li[2]/a')
        if next_buttons:
            # Click the "Next" button and wait for the page to load
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="cm_cr-pagination_bar"]/ul/li[2]/a'))).click()
            time.sleep(5)  # Adjust based on your connection speed
        else:
            # No "Next" button found, exit the loop
            print("Reached the last page of reviews.")
            break

    # Convert all scraped reviews to DataFrame and save to CSV
    df = pd.DataFrame(all_reviews)
    df.to_csv('amz_reviews.csv', index=False)

    driver.quit()

if __name__ == '__main__':
    main()