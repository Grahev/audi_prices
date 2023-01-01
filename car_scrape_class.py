from requests_html import HTMLSession

class CarScrape:
    def __init__(self):
        self.session = HTMLSession()
        self.headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36'}
        self.baseurl = 'https://www.usedcarsni.com/search_results.php?'