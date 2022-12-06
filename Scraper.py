import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup
import json

FIRST_PAGE = 0

PARAMS_REQUEST_HEADER =  {
        'authority': 'df.olx.com.br',
        'method': 'GET',
        'path': '/imoveis/aluguel',
        'scheme': 'https',
        'referer': 'https://df.olx.com.br/imoveis/aluguel',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
}

def searchData(neighbor = 'samambaia', n_pages = 2):

    houses_json = []

    for page in range(n_pages):

        if page == FIRST_PAGE:
            url_base = 'https://df.olx.com.br/imoveis/venda?q='+neighbor
        else:
            url_base = 'https://df.olx.com.br/imoveis/venda?o='+str(page+1)+'&q='+neighbor
        
        requested_page = requests.get(url=url_base, headers= PARAMS_REQUEST_HEADER)
        soup = BeautifulSoup(requested_page.content, 'lxml')
        ul_items = soup.find('ul', {'id': 'ad-list'})
        li_items = ul_items.find_all('li')
        
        for item in li_items:
            try:
                house_name = item.find_all('h2')[0].contents[0]
                house_price = item.find_all('span', {'class': 'm7nrfa-0 eJCbzj sc-ifAKCX jViSDP'})[0].contents[0]
                house_description = item.find_all('span', {'class': 'sc-1ftm7qz-0 doofcG sc-ifAKCX lgjPoE'})
                house_location = item.find_all('span', {'class': 'sc-1c3ysll-1 cLQXSQ sc-ifAKCX lgjPoE'})[0].contents[0]
                house_hyperlink = item.find('a', {'class': 'sc-12rk7z2-1 huFwya sc-htoDjs jEMWT'}).get("href")

                description = ''
                for _ in house_description:
                    # print(f'    {_.contents[0]}')
                    description = description + '\n' + _.contents[0]

                # print(description)
                # print(f'House name: {house_name}')
                # print(f'House price: {house_price}')
                # print(f'House description:')
                # print(f'House location: {house_location}')
                # print(f'House hyperlink: {house_hyperlink}')
                
                # print('-----------')
                json_house = {
                    'house_name': house_name,
                    'house_price': house_price,
                    'house_description': description,
                    'house_location': house_location,
                    'house_hypterlink': house_hyperlink
                }

                houses_json.append(json_house)
            except:
                pass

    return houses_json

json_data = searchData(n_pages=2)
# print(json_data)
df_json = pd.DataFrame(data=json_data)
df_json.to_excel('houses.xlsx')