from operator import index
import random
from requests_html import HTMLSession
from bs4 import BeautifulSoup
import pandas as pd
import time
import datetime

from functions import extract_details, clean_title, get_year
from db_connection import insert_car_to_db

#url = 'https://www.usedcarsni.com/search_results.php?make=1&model=102&keywords=&fuel_type=0&trans_type=2&age_from=0&age_to=0&price_from=0&price_to=0&user_type=0&mileage_to=0&body_style=9&distance_enabled=0&distance_postcode=&homepage_search_attr=1&tab_id=0&search_type=1'
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36'}

"""
url = 'https://www.usedcarsni.com/search_results.php?search_type=1&make=1&model=102'
page_no = 'pagepc0=2'
s = HTMLSession()
r = s.get(url, headers=headers)
soup = BeautifulSoup(r.content,'html.parser')



container = soup.find('div', class_ = 'car-list')

item = container.find('article', class_=['add-half-row','overflowed-flex', 'car-line'])

listings = container.find_all('article', class_=['add-half-row','overflowed-flex', 'car-line'])



title = clean_title(item.find('div', class_=['car-title', 'overflowed-flex', 'space-between']))
m = item.find('dl', class_ = ['dl-horizontal', 'other-ads']).find_next('dd')
milage = m.text.split(' ')[0]
details = extract_details(item.find('dl', class_ = ['dl-horizontal', 'other-ads']))
price = int(item.find('div', class_=['euroPrice']).text)
link = item.find('div', class_=['car-title', 'overflowed-flex', 'space-between']).find_next('a', href=True)
base_link = 'https://www.usedcarsni.com'+ link['href']
link = base_link.split('?')[0]
print(link)

"""


def car_full_info(item):
    full_title = item.find('div', class_=['car-title', 'overflowed-flex', 'space-between'])
    title = clean_title(item.find('div', class_=['car-title', 'overflowed-flex', 'space-between']))
    m = item.find('dl', class_ = ['dl-horizontal', 'other-ads']).find_next('dd')
    details = extract_details(item.find('dl', class_ = ['dl-horizontal', 'other-ads']))
    try:
        price = int(item.find('div', class_=['euroPrice']).text)
    except:
        price = ''
    link = item.find('div', class_=['car-title', 'overflowed-flex', 'space-between']).find_next('a', href=True)
    base_link = 'https://www.usedcarsni.com'+ link['href']
    link = base_link.split('?')[0]

    details = {
        'title': title,
        'year' : get_year(full_title),
        'price' : price,
        'milage': details['milage'],
        'transmission': details['transmission'],
        'fuel_type' : details['fuel_type'],
        'body_style' : details['body_style'],
        'engine_size' : details['engine_size'],
        'doors' : details['doors'],
        'location' : details['location'],
        'id' : link[-9:],
        'link' : link,
        'timestamp': datetime.datetime.now()
    }
    return details
    

output = pd.DataFrame()
brake_counter = 0

for i in range(0,150):
    if brake_counter < 20:
        #url = f'https://www.usedcarsni.com/search_results.php?search_type=1&make=1&model=102&pagepc0={i}' #a4 only
        #url = f'https://www.usedcarsni.com/search_results.php?search_type=1&make=1&model=3995&pagepc0={i}' #a4 allroad only
        url = f'https://www.usedcarsni.com/search_results.php?search_type=1&make=1&pagepc0={i}' #all audis


        s = HTMLSession()
        r = s.get(url, headers=headers)
        soup = BeautifulSoup(r.content,'html.parser')
        container = soup.find('div', class_ = 'car-list')
        item = container.find('article', class_=['add-half-row','overflowed-flex', 'car-line'])
        listings = container.find_all('article', class_=['add-half-row','overflowed-flex', 'car-line'])

        print(r.status_code)

        print(f'len of listings page is {len(listings)}')
        if len(listings) > 19:

            for item in listings:
                output = output.append(car_full_info(item), ignore_index=True)
                insert_car_to_db(car_full_info(item))


            print(f'page no {i} done')
            print('sleep for few seconds')
            time.sleep(random.randint(10,30))
        else:
            print('no listings in page')
            break
        brake_counter += 1
    else:
        print('time for longer brake')
        time.sleep(random.randint(60,90))
        brake_counter = 0
output.to_csv('test.csv')



