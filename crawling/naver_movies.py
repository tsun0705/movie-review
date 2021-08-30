import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
url = 'https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=pnt&date=20210723'

for x in range(1,41):
    soup = BeautifulSoup(requests.get(url + '&page=' + str(x),headers=headers).text, 'html.parser')
    reviews = soup.select('#old_content > table > tbody > tr')
    for review in reviews:
        a_tag = review.select_one('td.title > div > a')

        if a_tag is not None:
            title = a_tag.text
            url_code = a_tag['href'].split('?')[1].split('=')[1]
            urls = 'https://movie.naver.com/movie/bi/mi/basic.naver?code=' + url_code
            star = review.select_one('td.point').text

            req = requests.get(urls, headers=headers)
            html = BeautifulSoup(req.text, 'html.parser')
            img_url = html.select_one('meta[property="og:image"]')['content']
            desc = html.select_one('meta[property="og:description"]')['content']
            genre = html.select('dl.info_spec dd p span:nth-of-type(1) a')

            genre_list = [g.text for g in genre]
            genre_str = ','.join(genre_list)

            doc = {
                'title': title,
                'url': urls,
                'img_url': img_url,
                'star': star,
                'desc': desc,
                'genre': genre_str
            }

            db.hansson_review.insert_one(doc)

