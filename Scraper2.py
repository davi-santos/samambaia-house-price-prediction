import pandas as pd
import requests
from bs4 import BeautifulSoup

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

# print(list_of_hyperlinks)
# ----------------------------#

requested_page = requests.get(url=list_of_hyperlinks[0], headers=PARAMS_REQUEST_HEADER)
soup = BeautifulSoup(requested_page.content, 'lxml') # Convert request to html
div_class_details = 'sc-hmzhuo gqoVfS sc-jTzLTM iwtnNi'
div_class_location = 'realEstateLocation'
div_details = soup.find('div', {'class': div_class_details})
# div_location = soud.find('div', {'class': })

# Get house category: apartamento or casa
house_category = div_details.find('a', {'class': 'sc-gPWkxV dsTsUE'}).contents[0]

# Get house number of bathrooms
div_details_categories = div_details.find_all('div', {'class': 'ad__duvuxf-0 ad__h3us20-0 kUfvdA'})
n_bathrooms = 0

for n_details in div_details_categories:

    aux = n_details.find('dt', {'class': 'ad__sc-1f2ug0x-0 dOlajQ sc-ifAKCX cmFKIN'}).contents[0]

    if aux == []:
        continue
    if aux != 'Banheiros':
        continue

    n_bathrooms = n_details.find('dd', {'class': 'ad__sc-1f2ug0x-1 cpGpXB sc-ifAKCX kaNiaQ'}).contents[0]
    break

# i = 0
# while i in range(len(list_of_hyperlinks)):

#     try:
#         requested_page = requests.get(url=list_of_hyperlinks[i], headers=PARAMS_REQUEST_HEADER)
#         div_class_details = 'sc-bwzfXH ad__h3us20-0 ikHgMx'


#     except:
#         pass