from bs4 import BeautifulSoup
import requests
 
yelp_search = "https://www.yelp.com/search?find_desc=Restaurants&find_loc=Downtown%2C+San+Diego%2C+CA&ns=1"
yelp_html = requests.get(yelp_search).text
print(yelp_html[:300])