import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup
import json

PARAMS_REQUEST_HEADER =  {
        'authority': 'df.olx.com.br',
        'method': 'GET',
        'path': '/imoveis/aluguel',
        'scheme': 'https',
        'referer': 'https://df.olx.com.br/imoveis/aluguel',
        'sec-fetch-mode': 'navigate',
}


def searchData(neighbor = 'samambaia'):
    url_base = 'https://df.olx.com.br/imoveis/venda?'
    url_query_neighbor = 'q='+neighbor

    url_=url_base + url_query_neighbor; x=0

    while(x < 2):

        x += 1



    url_base = 'https://df.olx.com.br/imoveis/venda?q=samambaia'
    url_2 = 'https://df.olx.com.br/imoveis/venda?o=2&q=samambaia'
