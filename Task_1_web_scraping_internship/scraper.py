# # scraper.py - Scraping a website and saving data to CSV

# import requests
# from bs4 import BeautifulSoup
# import pandas as pd

# # Step 1: Fetch the webpage
# url = "https://books.toscrape.com/"
# print(f"Fetching data from {url}...")

# headers = {'User-Agent': 'Mozilla/5.0'}  # Prevent blocks
# response = requests.get(url, headers=headers)

# # Check if request was successful
# if response.status_code == 200:
#     print(" Successfully fetched the webpage!")
# else:
#     print(f" Error: Got status code {response.status_code}")
#     exit()

# # Step 2: Parse HTML with BeautifulSoup
# soup = BeautifulSoup(response.content, 'html.parser')

# # Step 3:  Extract book data
# books = []

# for book in soup.find_all('article', class_='product_pod'):
#     title = book.h3.a['title']
#     price = book.find('p', class_='price_color').text
#     rating = book.find('p')['class'][1]  # e.g., 'Star-rating-three'
    
#     books.append({
#         'title': title,
#         'price': price,
#         'rating': rating
#     })

# # Step 4: Save to CSV
# df = pd.DataFrame(books)
# df.to_csv('books_dataset.csv', index=False, encoding='utf-8')

# # Step 5: Show results
# print(f"\n Successfully scraped {len(books)} books!")
# print("\nFirst 5 books:")
# print(df.head())
# print("\nDataset saved as 'books_dataset.csv'")

# this is a simple web scraper that fetches book data from the "Books to Scrape" website,
#  extracts the title, price, and rating of each book, and saves the data into a CSV file.
#  The script also includes error handling for the HTTP request and prints out the results.


# scraper.py - Scraping Multiple Pages


import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

all_books = []

# Scrape 3 pages
for page in range(1, 4):  # Pages 1, 2, 3
    if page == 1:
        url = "https://books.toscrape.com/"
    else:
        url = f"https://books.toscrape.com/catalogue/page-{page}.html"
    
    print(f"\nFetching page {page}...")
    
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        for book in soup.find_all('article', class_='product_pod'):
            all_books.append({
                'title': book.h3.a['title'],
                'price': book.find('p', class_='price_color').text,
                'rating': book.find('p')['class'][1]
            })
        
        time.sleep(1)
        print(f" Page {page} done!")
    else:
        print(f" Error on page {page}: {response.status_code}")

# Save dataset
df = pd.DataFrame(all_books)
df.to_csv('books_dataset.csv', index=False, encoding='utf-8')

print(f"\n{'='*50}")
print(f"✓ SUCCESS! Scraped {len(all_books)} books from 3 pages")
print(f"{'='*50}")
print("\nFirst 10 books:")
print(df.head(10))
print("\nDataset saved as 'books_dataset.csv'")
print(f"\nDataset shape: {df.shape[0]} rows, {df.shape[1]} columns")