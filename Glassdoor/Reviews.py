from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep
from selenium.webdriver.chrome.options import Options
from random import randint
import csv
from fake_useragent import UserAgent
from webdriver_manager.chrome import ChromeDriverManager
import re
import math
import pandas as pd

options = Options()
options.add_argument("window-size=1400,600")
ua = UserAgent()
a = ua.random
user_agent = ua.random
print(user_agent)
options.add_argument(f'user-agent={user_agent}')
options.add_argument('--ignore-certificate-errors')
#options.add_argument("start-maximized")
options.add_argument('--incognito')
options.add_argument('--headless')
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.get('https://www.glassdoor.com/Reviews/Intel-Corporation-Reviews-E1519_P1.htm')
content = driver.page_source
soup = BeautifulSoup(content, 'html.parser')
# Count reviews
count = int(soup.find('div', {'class':'paginationFooter'}).get_text(strip=True).replace('Reviews', '').split()[-1])
print(count)
max_page = math.ceil(count/10)
heading, status, date, title, pros, cons = [], [], [], [], [], []

for page in range(1, max_page+1):
    sleep(2)
    print(page)
    #sleep(randint(2,5))
    # Headings
    url = 'https://www.glassdoor.com/Reviews/Intel-Corporation-Reviews-E1519_P' + str(page) + '.htm'
    driver.get(url)
    content = driver.page_source
    soup = BeautifulSoup(content, 'html.parser')
    for a in soup.findAll('h2', {'class':'mb-xxsm mt-0 css-5j5djr'}):
        heading.append(a.get_text(strip=True))
    # Employee status
    for a in soup.findAll('span', {'class':'pt-xsm pt-md-0 css-1qxtz39 eg4psks0'}):
        status.append(a.get_text(strip=True))
    for a in soup.findAll('span', {'class':'authorJobTitle middle common__EiReviewDetailsStyle__newGrey'}):
        # Dates
        date.append(a.get_text(strip=True).split(' - ')[0])
        # Titles
        #title.append(a.get_text(strip=True).split(' - ')[1])
    # Pros
    for a in soup.findAll('span', {'data-test':'pros'}):
        pros.append(a.get_text(strip=True))
    # Cons
    for a in soup.findAll('span', {'data-test':'cons'}):
        cons.append(a.get_text(strip=True))

print(len(heading), len(status), len(date), len(pros), len(cons))
df = pd.DataFrame(list(zip(heading, status, date, pros, cons)), columns =['Headline', 'Status', 'Date', 'Pros', 'Cons'])
df.to_excel('IntelReviews.xlsx', header=True, index=False)


