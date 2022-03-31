from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import random
from search import search_query
import webbrowser

# opens the selenium Chrome options to run the first instance in a headless, gpu less browser (runs faster)
chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--headless")

# sets the url to the search_query function
url = search_query()
print(url)
driver = webdriver.Chrome(options=chrome_options)
# runs the browser in the background (headless)
driver.get(url)
listOfContent = []

# finds all HTML elements with the 'a' tag (used for hyperlinks)
links = driver.find_elements_by_tag_name('a')
for link in links:
    listOfContent.append(link.get_attribute('href'))

url = None
# checks if the list element is empty or if it is a channel
while url is None or 'watch' not in url:
    # selects a random video url in the list
    url = listOfContent[random.randint(0, len(listOfContent) - 1)]

# reloads webdriver to run normally
webbrowser.open(url)
