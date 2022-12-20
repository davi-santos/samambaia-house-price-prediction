<!--
*** Comments here
-->

<!-- PROJECT SHIELDS -->
<!--
***
*** [![Contributors][contributors-shield]][contributors-url]
*** [![Forks][forks-shield]][forks-url]
*** [![Stargazers][stars-shield]][stars-url]
*** [![Issues][issues-shield]][issues-url]
*** [![MIT License][license-shield]][license-url]
-->

[![LinkedIn][linkedin-shield]][linkedin-url]


<!-- PROJECT LOGO -->
<br />
<div align="center">
  

  <h3 align="center">Samambaia House Price Prediction</h3>

  <p align="center">
    Helping people making decision based on data
    <br />
    <br />
    <a href="https://github.com/davi-santos/samambaia-house-price-prediction/">View Dashboard</a>
    ·
    <a href="https://github.com/davi-santos/samambaia-house-price-prediction/">Report</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href='#Acquiring data'>Data acquisition</a>
    </li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

A few weeks ago, my parents and I decided to move to Distrito Federal state, Brazil. We were looking for a new house to buy and we asked my family for advise. My uncle João (ficticious name) told us that Samambaia city was the best place to buy a new house. So, in order to help my parents and make sure we could buy a good house in Samambaia city, I decided to make this project.

This project aims to:
* Create a jupyter notebook (and a pdf version for other people as a report) showing graphics, stats and indicators about samambaia houses;
* Create an interactive dashboard, so anyone can use it for understanding how house prices change in samambaia.

For this project, I will be using OLX house prices by web scraping and saving the data remotely.


### Built With

This project is built with:

* [![Laravel][Laravel.com]][Laravel-url]
* [![Bootstrap][Bootstrap.com]][Bootstrap-url]


<!-- DATA ACQUISITION -->
## Data Acquisition
### Web scraping
The data was acquired by web scraping olx pages using beautiful soup python library. This was a two step process for getting information about samambaia houses:

#### 1. Getting basic information about samambaia houses from olx search page

Just by searching "samambaia" in the search engine and choosing "Venda - casas e apartamentos" category, we could see many results. From these pages, I scraped the folling information: title, price, location, number of bedrooms, car parking, house size, link to more info. The python code for this process is in [Scrape.py](https://github.com/davi-santos/samambaia-house-price-prediction/blob/main/Scraper.py) file and the output file is [houses.xlsx](https://github.com/davi-santos/samambaia-house-price-prediction/blob/main/data/houses.xlsx), in the data folder.

#### 2. Getting more information about samambaia houses using the links from the proccess above.

In order to get more information about samambaia houses, I needed to access each link and scrape more information again. So, I did it! I wanted to get the number of bathrooms, CEP and Logradouro (street). The code for this is in [Scrape2.py](https://github.com/davi-santos/samambaia-house-price-prediction/blob/main/Scraper2.py) file and the output file is [new_data.csv](https://github.com/davi-santos/samambaia-house-price-prediction/blob/main/data/new_data.csv), in the data folder.

### Preprocessing Data

The [houses.xlsx](https://github.com/davi-santos/samambaia-house-price-prediction/blob/main/data/houses.xlsx) have a column named house_description with multiple information about samambaia hosues, so I splited those information to various columns. There were also non-samambaia houses in the search, so I needed to remove those lines. The [Processing data.ipynb](https://github.com/davi-santos/samambaia-house-price-prediction/blob/main/Processing%20data.ipynb) file has the code of this process and it outputs the [processed_data.csv](https://github.com/davi-santos/samambaia-house-price-prediction/blob/main/data/processed_data.csv), in the data folder.

### Final Data File

The [JoinCSV.py](https://github.com/davi-santos/samambaia-house-price-prediction/blob/main/JoinCSV.py) file join the data from [processed_data.csv](https://github.com/davi-santos/samambaia-house-price-prediction/blob/main/data/processed_data.csv) and [new_data.csv](https://github.com/davi-santos/samambaia-house-price-prediction/blob/main/data/new_data.csv) files and it outputs [samambaia_houses.csv](https://github.com/davi-santos/samambaia-house-price-prediction/blob/main/data/samambaia_houses.csv). So, [samambaia_houses.csv](https://github.com/davi-santos/samambaia-house-price-prediction/blob/main/data/samambaia_houses.csv) is the file I will be working on in the analysis, prediction and in the dashboard.

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/davi-datascientist/
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Python-FFCC55?style=for-the-badge&logo=Python&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
