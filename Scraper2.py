import pandas as pd
import requests
from bs4 import BeautifulSoup
import numpy as np
import time

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

df_data = pd.read_csv('./data/processed_data.csv', index_col=[0])
list_of_hyperlinks = df_data['house_hyperlink'].values

# print(list_of_hyperlinks[0])
# ----------------------------#
# Try to request each page
try_another_request = 1
i = 0
size = len(list_of_hyperlinks)
# size = 3
houses_json = []

while i < size:

    try:
        # Request page
        requested_page = requests.get(url=list_of_hyperlinks[i], headers=PARAMS_REQUEST_HEADER)
        soup = BeautifulSoup(requested_page.content, 'lxml') # Convert request to html

        # Get div Detalhes and Localização from html
        div_class_details = 'sc-hmzhuo gqoVfS sc-jTzLTM iwtnNi'
        div_class_location = 'realEstateLocation'
        div_details = soup.find('div', {'class': div_class_details})
        div_location = soup.find('div', {'class': div_class_location})

        # Get house category from div
        house_category = div_details.find('a', {'class': 'sc-gPWkxV dsTsUE'}).contents[0]

        # Get house number of bathrooms from div
        div_details_categories = div_details.find_all('div', {'class': 'ad__duvuxf-0 ad__h3us20-0 kUfvdA'})
        house_n_bathrooms = np.nan

        for n_details in div_details_categories:

            aux = n_details.find('dt', {'class': 'ad__sc-1f2ug0x-0 dOlajQ sc-ifAKCX cmFKIN'}).contents[0]

            if aux == []:
                continue
            if aux != 'Banheiros':
                continue

            house_n_bathrooms = n_details.find('dd', {'class': 'ad__sc-1f2ug0x-1 cpGpXB sc-ifAKCX kaNiaQ'}).contents[0]
            break

        # Get house location CEP
        cep_class = 'ad__sc-1f2ug0x-1 cpGpXB sc-ifAKCX kaNiaQ'
        house_cep = div_location.find('dd', {'class': cep_class}).contents[0]

        # Get house logradouro
        logradouro_class = 'ad__duvuxf-0 ad__h3us20-0 kUfvdA'
        house_logradouro = ''
        list_div_location = div_location.find_all('div', {'class': logradouro_class})

        for item in list_div_location:
            
            aux = item.find('dt').contents[0]

            if aux == []:
                continue
            if aux != 'Logradouro':
                continue

            house_logradouro = item.find('dd').contents[0]
            break

        json_house = {
            'house_category': house_category,
            'n_bathrooms': house_n_bathrooms,
            'CEP': house_cep,
            'Logradouro': house_logradouro
        }

        houses_json.append(json_house)
        # print(f'Categoria: {house_category}')
        # print(f'Banheiros: {house_n_bathrooms}')
        # print(f'CEP: {house_cep}')
        # print(f'Logradouro: {house_logradouro}')
        # print('-------------------------------')
        print(f'Progress: {i} of {size}')
        try_another_request = 1
    except:
        if try_another_request == 4:
            print(f'Really could not request page {i}')

            json_house = {
                'house_category': '',
                'n_bathrooms': np.nan,
                'CEP': np.nan,
                'Logradouro': ''
            }
            houses_json.append(json_house)
            try_another_request = 1
        else:
            print(f'Could not request page {i} - Trying again attempt number {try_another_request}')
            try_another_request += 1
            i -= 1
            time.sleep(3)
    i += 1

df_json = pd.DataFrame(data=houses_json)
df_json.to_csv('new_data.csv')