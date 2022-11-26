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


    for page in range(n_pages):

        if page == FIRST_PAGE:
            url_base = 'https://df.olx.com.br/imoveis/venda?q='+neighbor
        else:
            url_base = 'https://df.olx.com.br/imoveis/venda?o='+str(page+1)+'&q='+neighbor
        
        requested_page = requests.get(url=url_base, headers= PARAMS_REQUEST_HEADER)
        soup = BeautifulSoup(requested_page.content, 'lxml')
        ul_items = soup.find('ul', {'id': 'ad-list'})
        li_items = ul_items.find_all('li')
        #items = soup.find_all('li', {'class': 'sc-1fcmfeb-2 eNBJyg'})
        # print(len(items))
        
        for item in li_items:
            try:
                house_name = item.find_all('h2')[0].contents[0]
                house_price = item.find_all('span', {'class': 'm7nrfa-0 eJCbzj sc-ifAKCX jViSDP'})[0].contents[0]
                house_description = item.find_all('span', {'class': 'sc-1ftm7qz-0 doofcG sc-ifAKCX lgjPoE'})
                
                for _ in house_description:
                    print(_.contents[0])

                house_location = item.find_all('span', {'class': 'sc-1c3ysll-1 cLQXSQ sc-ifAKCX lgjPoE'})[0].contents[0]
                print(house_location)
                
                print('-----------')
            except:
                print('Error')
        


searchData(n_pages=1)

