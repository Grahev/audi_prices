import requests

cookies = {
    '_gid': 'GA1.2.1049774021.1649006612',
    'u:location': '%7B%22countryCode%22%3A%22GB%22%2C%22ccode3%22%3A%22GBR%22%2C%22timezone%22%3A%22Europe%2FLondon%22%2C%22ip%22%3A%22185.44.77.45%22%2C%22regionId%22%3A%22ENG%22%7D',
    '_ga': 'GA1.2.1094432626.1649006611',
    '_ga_G0V1WDW9B2': 'GS1.1.1649006610.1.1.1649009919.60',
}

headers = {
    'authority': 'www.fotmob.com',
    'accept': '*/*',
    'accept-language': 'en-GB,en;q=0.9,en-US;q=0.8,pl;q=0.7',
    'cache-control': 'no-cache',
    # Requests sorts cookies= alphabetically
    # 'cookie': '_gid=GA1.2.1049774021.1649006612; u:location=%7B%22countryCode%22%3A%22GB%22%2C%22ccode3%22%3A%22GBR%22%2C%22timezone%22%3A%22Europe%2FLondon%22%2C%22ip%22%3A%22185.44.77.45%22%2C%22regionId%22%3A%22ENG%22%7D; _ga=GA1.2.1094432626.1649006611; _ga_G0V1WDW9B2=GS1.1.1649006610.1.1.1649009919.60',
    'pragma': 'no-cache',
    'referer': 'https://www.fotmob.com/match/3657263/matchfacts',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36',
}

params = {
    'matchId': '3657263',
    'ccode3': 'GBR',
    'bettingProvider': 'Bet365_UK Version A Deep',
    'refresh': 'true',
    'includeBuzzTab': 'false',
}

response = requests.get('https://www.fotmob.com/api/matchDetails', headers=headers, params=params, cookies=cookies)

print(response.text)