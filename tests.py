import requests

response = requests.get('http://www.baidu.com')
print(response.status_code)
print(response.url)
print(response.headers)
print(response.cookies)
print(response.text)
print(response.content)  # in bytes

data = {'word': 'hello'}
response = requests.post('http://httpbin.org/post', data=data)
print(response.content)

response = requests.get('http://httpbin.org/get', params={'username': 'test', 'password': '123'})
print(response.text)
print(response.content)

print(
    '\n\n\n-------------------------------------------------------------------------------------------------------------\n\n\n')

from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc, 'lxml')
print(soup.prettify())
print(soup.title)
print(soup.title.name)
print(soup.title.string)
print(soup.p['class'])
print(soup.find(id='link2').get('class'))

print(
    '\n\n\n-------------------------------------------------------------------------------------------------------------\n\n\n')

import csv


headers = [
    'id', 'name', 'age', 'height'
]

rows = [
    ('1', 'lilly', 20, 170),
    ('2', 'john', 22, 180),
]

with open('re.csv', 'w', encoding='utf-8', newline='') as csv_file:
    spamwriter = csv.writer(csv_file)
    spamwriter.writerow(headers)
    spamwriter.writerows(rows)


with open('re.csv', 'w+') as csv_file:
    filenames = ['firstname', 'lastname']
    writer = csv.DictWriter(csv_file, filenames)
    writer.writeheader()
    writer.writerows([{'firstname': 'naichuan', 'lastname': 'zhang'}, {'firstname': 'shirley', 'lastname': 'liu'}])


with open('re.csv', 'r') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        print(row['firstname'], row['lastname'])
