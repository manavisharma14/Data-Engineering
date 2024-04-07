import requests

def connection(web_url):

    sessions = requests.session()
    HEADERS = {'Accept-Language':'en-GB,en-US;q=0.9,en;q=0.8',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko),Chrome/58.0.3029.110 Safari/537.3',
        'Accept-Encoding':'gzip, deflate, br, zstd',
               'Connection':'keep-alive'}
    response = sessions.get(web_url, verify = False, headers = HEADERS)
    response.raise_for_status
    sessions.close()
    #print(response.request.headers)
    return response