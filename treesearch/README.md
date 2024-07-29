# Project Guideline: TreeSearch

## Overview
The TreeSearch project involves creating a binary search tree (BSTree) to store and query tokens extracted from web pages. This project will enhance your understanding of data structures, web scraping, and search algorithms.

## Objectives
- Implement a binary search tree to store tokens.
- Scrape web pages to collect URLs and extract content.
- Tokenize the content of web pages.
- Insert tokens into the BSTree.
- Implement a search function to query tokens in the BSTree.
- Develop a basic search engine interface.

## Prerequisites
- Understanding of data structures, especially binary search trees.
- Familiarity with web scraping using libraries like `requests` and `BeautifulSoup`.

## Project Components

1. **BSTree Implementation**
   - Implement the `TreeNode` class to represent nodes in the binary search tree.
   - Implement the `BSTree` class with methods to insert, search, and traverse the tree.

2. **Web Scraping**
   - Write functions to scrape URLs from a given webpage.
   - Extract and tokenize the content from web pages.

3. **Search Engine**
   - Integrate the BSTree with the web scraping functions.
   - Implement a basic command-line interface to query the BSTree.

### Explanation of `max_scraped` URL Limit

In the TreeMapper project, we use the `max_scraped` parameter to limit the number of URLs processed during our web scraping. This is important for several reasons:

1. **Python's Recursion Depth**:
   Python has a default recursion depth limit of 3000. This means that a recursive function cannot call itself more than 3000 times before it results in a RecursionError. To avoid hitting this limit and causing our program to crash, we must limit the depth of our traversal and the amount of data ingested.

## Detailed Steps

### 1. TreeNode Class
- Define the properties of the node: key (token), data (URL), left child, and right child.
- Initialize these properties in the constructor.

### 2. BSTree Class
- Define the properties of the tree: root, initialized to `None`.
- **Insert Method**: Add a method to insert a new node into the tree. This method should recursively find the correct position based on the key.
- **Search Method**: Implement a method to search for a node by its key. This method should also be recursive and return the node if found, or `None` if not.
- **Inorder Traversal Method**: Create a method to traverse the tree in order and print each node's key and data. This helps verify the structure of the tree.

### 3. Web Scraping and Tokenizing
- **Tokenize Function**: Implement a function to convert a string of webpage content into a list of tokens. This involves converting the text to lowercase and splitting it on whitespace.
- **Scrape URLs Function**: Write a function to fetch the HTML content of a webpage, parse it, and extract all hyperlinks. Normalize these URLs to ensure they are absolute, and filter out duplicates. I suggest `urljoin` from the `urllib.parse` package to normalize the hyperlinks. 
- **Scrape and Tokenize Function**: 
  - Use a queue or list to manage the URLs to be visited and a list to keep track of visited URLs.
  - Fetch and parse the HTML content of each URL, tokenize the content, and insert these tokens into the BSTree.
  - Add new URLs to the queue if they haven't been visited and the maximum scrape limit hasn't been reached.
  - This approach ensures the scraping process is efficient and avoids revisiting the same URLs or getting stuck in infinite loops.

### 4. Search Engine Interface
- **Query Function**: Implement an interactive loop to query the BSTree. Prompt the user for search terms and display the URLs associated with the found tokens. Allow the user to exit the loop.
- **Run Search Engine Function**: Initialize the search engine by setting the root URL and maximum number of pages to scrape. Call the scraping and tokenizing function to build the BSTree, optionally display the tree's contents, and start the query loop.
