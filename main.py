from selenium import webdriver

query = input("Query from major e-commerce websites: ")
urlLazada = "https://www.lazada.com.my/catalog/?q=" + query.replace(" ", "+")
urlShopee = "https://www.shopee.com.my/search?keyword=" + query.replace(" ", "%20")

#####================================================#####
#####=============== LAZADA SCRAPPING ===============#####
#####================================================#####
print("Scrapping from Lazada...")
# Chrome v77^
option = webdriver.ChromeOptions()
option.add_argument("--disable-extensions")
option.add_argument("--incognito")
option.add_argument("--headless")   #Browser window silencer
browser = webdriver.Chrome(executable_path='chromedriver.exe', options=option)
browser.get(urlLazada)

# Get all current prices
prices_element = browser.find_elements_by_class_name("c3gUW0")  #Container class name
print(prices_element)
prices = [x.text for x in prices_element]

print('CURRENT PRICES:')
print(prices, '\n')


# Get all original prices
original_prices_element = browser.find_elements_by_class_name("c1-B2V")
original_prices = [x.text for x in original_prices_element]

print("ORIGINAL PRICES:")
print(original_prices, '\n')

# Get all product names
names_element = browser.find_elements_by_class_name("c16H9d")
names = [x.text for x in names_element]

print("PRODUCT NAMES:")
print(names, '\n')


# To pair product and their prices
print("Product : Current price")
for title, language in zip(names, prices):
    print(title + ": " + language, '\n')

if(names == []):
    print("Web scrapping activities temporarily blocked by lazada, try again in a moment...")

browser.quit()

#####================================================#####
#####=============== SHOPEE SCRAPPING ===============#####
#####================================================#####
print("Scrapping from shopee...")
# Chrome v77^
option = webdriver.ChromeOptions()
option.add_argument("--disable-extensions")
option.add_argument("--incognito")
option.add_argument("--headless")   #Browser window silencer
browser = webdriver.Chrome(executable_path='chromedriver.exe', options=option)
browser.get(urlShopee)

# Get all current prices
prices_element = browser.find_elements_by_css_selector("span._341bF0")  #Container class name
print(prices_element)
prices = [x.text for x in prices_element]

print('CURRENT PRICES:')
print(prices, '\n')


# Get all original prices
original_prices_element = browser.find_elements_by_class_name("_lw9jLI_37ge-4 _2XtIUk")
original_prices = [x.text for x in original_prices_element]

print("ORIGINAL PRICES:")
print(original_prices, '\n')

# Get all product names
names_element = browser.find_elements_by_css_selector("div._1JAmkB")
names = [x.text for x in names_element]

print("PRODUCT NAMES:")
print(names, '\n')


# To pair product and their prices
print("Product : Current price")
for title, language in zip(names, prices):
    print(title + ": " + language, '\n')

if(names == []):
    print("Web scrapping activities temporarily blocked by shopee, try again in a moment...")

browser.quit()