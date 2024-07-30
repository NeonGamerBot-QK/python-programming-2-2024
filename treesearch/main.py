from BSTree import *
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def tokenize(content):
    return content.lower().split()

def scrape_urls(url, visited):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        urls = []
        for link in soup.find_all('a', href=True):
            full_url = urljoin(url, link['href'])
            if full_url not in visited and urlparse(full_url).netloc == urlparse(url).netloc:
                urls.append(full_url)
        return urls, soup.get_text()
    except Exception as e:
        print(f"Failed to scrape {url}: {e}")
        return [], ""

def scrape_and_tokenize(root_url, max_scraped):
    tree = BSTree()
    to_visit = [root_url]
    visited = set()
    
    while to_visit and len(visited) < max_scraped:
        current_url = to_visit.pop(0)
        if current_url in visited:
            continue
        visited.add(current_url)
        urls, content = scrape_urls(current_url, visited)
        tokens = tokenize(content)
        for token in tokens:
            tree.insert(token, current_url)
        to_visit.extend(urls)
    
    return tree
def query_tree(tree):
    while True:
        query = input("Enter a search term (or 'exit' to quit): ").strip().lower()
        if query == 'exit':
            break
        result = tree.search(query)
        if result:
            print(f"Token found! URLs: {result.data}")
        else:
            print("Token not found.")

# Function to run the search engine
def run_search_engine(root_url, max_scraped):
    tree = scrape_and_tokenize(root_url, max_scraped)
    for key, data in tree.inorder_traversal():
        print(f"Token: {key}, URLs: {data}")
    query_tree(tree)

root_url = "https://books.toscrape.com/"
max_scraped = 10
run_search_engine(root_url, max_scraped)

if __name__ == "__main__":
    run_search_engine()