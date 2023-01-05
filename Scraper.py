from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import csv
options = Options()
options.headless = True
options.page_load_strategy = 'eager'
driver = webdriver.Chrome(options=options)

class Scraper:

    def __init__(self,url):

        driver.get(url)
        with open('protagonist.csv', 'a') as file:
            writer = csv.writer(file)
            for element in driver.find_elements(By.CLASS_NAME, "css-errlgf"):
                try:
                    companyName = element.find_element(By.CSS_SELECTOR, '[data-test="employer-short-name"]').text
                except:
                    companyName = "Not Available"
                try:
                    rating = element.find_element(By.CSS_SELECTOR, '[data-test="rating"]').text
                except:
                    rating = "Not Available"
                try:
                    location = element.find_element(By.CSS_SELECTOR, '[data-test="employer-location"]').text
                except:
                    location = "Not Available"
                try:
                    companySize = element.find_element(By.CSS_SELECTOR, '[data-test="employer-size"]').text
                except:
                    companySize = "Not Available"
                try:
                    industry = element.find_element(By.CSS_SELECTOR, '[data-test="employer-industry"]').text
                except:
                    industry = "Not Available"
                try:
                    jobs = element.find_element(By.CSS_SELECTOR, '[data-test="cell-Jobs-count"]').text
                except:
                    jobs = "Not Available"

                print(companyName + " " + rating + " " + companySize + " " + industry + " " + jobs)

                try:
                    writer.writerow([companyName, rating, companySize,industry,jobs,location])
                except:
                    pass

