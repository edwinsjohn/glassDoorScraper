import csv
from Scraper import Scraper

with open('protagonist.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Rating", "Size","Industry","Job_Count","Location"])

print("Glass Door IT Employer in UK Scraping")
for i in range(1,1000):
    print(f"Scraping Page {i}")
    url=f"https://www.glassdoor.co.in/Reviews/index.htm?overall_rating_low=3&page={i}&locId=2&locType=N&locName=United%20Kingdom&sector=10013&filterType=RATING_OVERALL"
    csvWrite = Scraper(url)