import pandas as pd 
from bs4 import BeautifulSoup
from connection import connection
from flipkart import get_headphones
import time

def main():
    url = 'https://www.flipkart.com/search?q=headphones&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'
    data_accquired = []
    for page_no in range(10):
        page_url = url + str(page_no)
        response = connection(page_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        data_accquired = data_accquired + get_headphones(soup)

    df = pd.DataFrame(data = data_accquired)
    df.to_csv('flipkart_headphones.csv', index= False)

if __name__ == '__main__':
    main()