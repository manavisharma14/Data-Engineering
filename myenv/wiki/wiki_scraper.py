from bs4 import BeautifulSoup
import os
import requests
import re

# Making request to 
#get the html body
def connection(web_url):
    '''
    Make a GET request to the specified URL and returns
    the reponse object.

    param web_url: URL of the web page to fetch
    return: Response object from requests.get()
    '''
    response = requests.get(web_url)
    response.raise_for_status
    return response 

def paragraphs_to_file(soup,filename):
    '''
    Extracts paragraphs from the BeautifulSoup object 
    and saves them to a text file.

    param 
    soup: Beautifulsoup object containing parsed HTML.
    filename: Name of the file where the paragraphs 
    will be saved
    '''
    # Extracting and dumping the paragraph data
    with open (filename,'w',encoding='utf-8') as file:
        pargraphs=soup.find_all('p')
        for i in pargraphs:
            file.write(i.text+'\n\n')

def filtered_links_to_file(soup,filename):
    '''
    Extracts and filters link from a specific content div
    in the Beautiful Soup object and saves the filtered link to a 
    text file.

    param
    soup: Beautifulsoup object containing parsed HTML.
    filename: Name of the file where the paragraphs 
    will be saved
    '''
    # Extracting and dumping the hrefs
    content_div=soup.find('div', class_= 'mw-body-content')
    with open (filename,'w',encoding='utf-8') as file:
        if content_div:
            links = content_div.find_all('a')
            for link in links:
                href = link.get('href')
                if href and not re.search('(^#)|(#cite_)|(^/wiki/File:)',href):
                    file.write(href+'\n')
        else:
            print('Content containeer not found')

if __name__ == '__main__':
    link = "https://en.wikipedia.org/wiki/Indian_Premier_League"
    response = connection(link)
    soup = BeautifulSoup(response.text, 'html.parser')
    paragraphs_filename ='wiki-ipl.txt'
    links_filename = 'links.txt'
    paragraphs_to_file(soup,paragraphs_filename)
    print(f'Paragraphs saved to {paragraphs_filename}')
    filtered_links_to_file(soup,links_filename)
    print(f'Hyper links saved to {links_filename}')