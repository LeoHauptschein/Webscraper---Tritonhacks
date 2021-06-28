from bs4 import BeautifulSoup
import requests # Used to request webpages
import urllib   # Used for URL encoding (e.g. La Jolla San Diego CA -> La+Jolla%2C+San+Diego%2C+CA)

# HTTP header we'll use for getting the page
headers = {
  'Access-Control-Allow-Origin': '*',
  'Access-Control-Allow-Methods': 'GET',
  'Access-Control-Allow-Headers': 'Content-Type',
}

"""
String, String => ([ratings], [costs])
"""
def scrape_for(query, location, pages):
  # Builds the URL for what to scrape
  url = "https://www.yelp.com/search?"
  params = {"find_desc": query, "find_loc": location, "ns": 1}
  url += urllib.parse.urlencode(params)
  # Scrape the url with BeautifulSoup
  for i in range(pages):
    pageurl = url + "&start=" + str(i) + "0"
    page = requests.get(pageurl, headers)
    scraper = BeautifulSoup(page.content, 'html.parser')

  # Get all search results
    results = scraper.find_all("div", class_="container__09f24__21w3G")
  # Get all prices
    prices = scraper.find_all("span", class_="priceRange__09f24__2O6le") # <- TODO Add the span class here
  # Get all star ratings
    stars = scraper.find_all("div", class_="i-stars__09f24__1T6rz") # <- TODO Add the div class here
  # Get all images, store only source attributes
  page = requests.get(pageurl, headers)
  scraper = BeautifulSoup(page.content, 'html.parser')
  images = scraper.find_all(class_="css-xlzvdl")[:10]
  image_sources = [img["src"] for img in images]

  # turn prices(array of html tags) into numbers
  for i in range(len(prices)):
    prices[i] = prices[i].string

  # turn stars(array of html tags) into numbers as well
  for i in range(len(stars)):
    stars[i] = float(stars[i]["aria-label"][:-12])

  return (prices, stars, image_sources)