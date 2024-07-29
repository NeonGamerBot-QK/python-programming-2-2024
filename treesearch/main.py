from BSTree import *

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Function to tokenize the content
def tokenize(content):
    # YOUR CODE GOES HERE
    pass

# Function to scrape URLs from a given webpage
def scrape_urls(base_url):
    response = requests.get(base_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    urls = []
    # YOUR CODE GOES HERE
    return urls

def scrape_and_tokenize(url, max_scraped, search_tree=None):
    if search_tree is None:
        search_tree = BSTree()
        
    # YOUR CODE GOES HERE
    
    return search_tree

# Function to query the binary search tree
def query(search_tree):
    # YOUR CODE GOES HERE
    pass

# Function to run the search engine
def run_search_engine():

    # Scrape data and insert into binary tree
    start_url = "https://books.toscrape.com/"
    max_scraped = 10

    search_tree = scrape_and_tokenize(start_url, max_scraped)
    
    # Perform in-order traversal (optional for verification)
    search_tree.inorder_traversal()
    
    # Query the binary search tree
    query(search_tree)

if __name__ == "__main__":
    run_search_engine()