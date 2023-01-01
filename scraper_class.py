from requests_html import HTMLSession

class Scraper:
    def __init__(self):
        self.session = HTMLSession()
        self.headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36'}
        self.baseurl = 'https://www.amazon.co.uk/dp/'

    def extract(self, asin):
        r = self.session.get(self.baseurl + str(asin), headers=self.headers)
        scraped_item = (
            r.html.find('span#productTitle', first=True).text,
            r.html.find('span.a-offscreen', first=True).text,
        )
        return scraped_item


info = Scraper()

prod = info.extract('B085G58KWT')

print(prod)