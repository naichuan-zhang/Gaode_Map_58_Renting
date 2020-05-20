import requests
from bs4 import BeautifulSoup
import csv


def get_html():
    url = 'https://bj.58.com/wangjing/pinpaigongyu/pn/{page}/?minprice=2000_3000'
    page = 0
    csv_file = open('renting.csv', 'w', encoding='utf-8', newline='')
    writer = csv.writer(csv_file, dialect='excel')
    while page < 10:
        page += 1
        html = requests.get(url.format(page=page)).text
        soup = BeautifulSoup(html, 'lxml')
        house_list_lis = soup.find_all('li', class_='house')
        loadmore = soup.find('div', class_='loadbtn')
        if loadmore is not None:
            text = loadmore.string
            if text == '加载更多':
                write_file(house_list_lis, writer)
            else:
                write_file(house_list_lis, writer)
                csv_file.close()
                break
        else:
            write_file(house_list_lis, writer)
            csv_file.close()
            break


def write_file(house_list, writer):
    print('Writing to file ...')
    for house in house_list:
        if house is not None:
            house_title = house.find('div', class_='img').img.get('alt')
            house_info_list = house_title.split()
            house_location = house_info_list[1]
            house_url = house.find('a').get('href')
            writer.writerow([house_title, house_location, house_url])


get_html()
