# Importing necessary libraries
from bs4 import BeautifulSoup as soup
import requests as rq
import pandas as pd
import os

# Scraping Ecoland Property's Pages-- UGANDA
base_url = 'https://www.ecolandproperty.com/uganda/houses-for-sale-in-kampala-uganda'
url_pages = []

# Since they are only 20 pages of the website
for page in range(1, 21):
    new_page = base_url + '/' + 'page' + '/' + str(page)
    url_pages.append(new_page)
    # print(new_page)

# print(url_pages)

# looping through our urls
for page_ in url_pages:
    render_page = rq.get(page_, headers={"Accept": "text/html"})
    # print(f'Render Page {render_page}') # check for success

    print(f'--> Status Code -> {render_page.status_code}')
    # print(f'--> Page Header -> {render_page.headers}')

    # Parsing the HTML Source in BS4
    my_soup = soup(render_page.content, 'html.parser')
    # print(f'--> HTML soup content -> {my_soup}')
    # print('----------------END OF PAGE----------------')

    # Getting the data I want, just by inspecting in the browser to get the html code titles
    my_data = my_soup.find_all(class_="title-and-meta")
    # print(f'--> my data ->{my_data}')

    # List compression for the filtered data ready for  more data manipulation
    my_scraped_data = [i.get_text() for i in my_data]
    # print(my_scraped_data)

    # Printing out my data as a list for now
    for data in my_scraped_data:
        print()
        print(data)
    # print(my_scraped_data, sep=" ")

    # In case you want to create a csv file that you can manipulate easily
    # path = 'my_real_data.csv'
    # assert os.path.isfile(path)
    # with open(path, "a") as file:
    #     my_scraped_data_ = pd.DataFrame({'my+data': my_scraped_data})
    #     my_scraped_data_.to_csv(file)
    # print(f'--> My Scrapped data {my_scraped_data_}')

# my_real_data.csv is now a file that you can manipulate, edit and save again.
# Check in the root folder where this file is saved too find the csv file


