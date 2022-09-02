from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller

import csv

chromedriver_autoinstaller.install()
base_url="https://www.indeed.com"
driver = webdriver.Chrome()

driver.get("https://www.indeed.com/jobs?q=web+developer&l=Cupertino%2C+CA&start=10")
soup = BeautifulSoup(driver.page_source, 'html.parser')

pages = 100
with open("output200.csv", 'w', newline='', encoding="utf-8") as f:
    writer = csv.writer(f)
    while (pages > 0):
        link = soup.find("a", {"data-testid": "pagination-page-next"})
        if not link:
            link = soup.find("a", {"aria-label": "Next"})
        next_link = link['href']
        mydivs = soup.find_all("h2", {"class": "jobTitle"})
        print(mydivs)
        for div in mydivs:
            spec_link = div.select('a')[0]
            spec_link = base_url + spec_link['href']
            print(spec_link)
            driver.get(spec_link)
            new_soup = BeautifulSoup(driver.page_source, 'html.parser')
            info = []
            title = new_soup.find("h1", {"class": "jobsearch-JobInfoHeader-title"})
            title = title.text
            companyInfo = new_soup.find("div", {"class": "jobsearch-CompanyInfoContainer"})
            salaryInfo = new_soup.find("div", {"id": "salaryInfoAndJobType"})
            description = new_soup.find("div", {"id": "jobDescriptionText"})
            posting = new_soup.find("span", {"class": "jobsearch-HiringInsights-entry--text"})
            info.append(spec_link)
            info.append(title)
            info.append(companyInfo)
            info.append(salaryInfo)
            info.append(description)
            info.append(posting)
            writer.writerow(info)
        pages = pages - 1
        print(base_url + next_link)
        driver.get(base_url + next_link)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
    

