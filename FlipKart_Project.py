from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd
from selenium.webdriver.chrome.options import Options
import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()


time.sleep(random.uniform(1.5,4.5))
options.add_argument("--lang=en-US")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--start-maximized")
options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--disable-info-bars")
options.add_argument("--disable-extensions")

driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
wait = WebDriverWait(driver, 10)
all_data_urls = []
All_brand = []
All_price = []
All_name = []
all_rating = []
all_product_list = set()
def auto_scroll():    
    l_height = driver.execute_script("return document.body.scrollHeight")
    for i in range(0, l_height, 300):        
        driver.execute_script(f"window.scrollTo(0, {i});")        
        time.sleep(random.uniform(0.3, 0.8))
        # নতুন content load হলে page height পরিবর্তন হতে পারে
        n_height = driver.execute_script("return document.body.scrollHeight")
        if n_height != l_height:
            l_height = n_height

for all_pages in range(1,3):
    driver.get(f"https://www.flipkart.com/search?q=t+shirts&as=on&as-show=on&otracker=AS_Query_HistoryAutoSuggest_1_1_na_na_na&otracker1=AS_Query_HistoryAutoSuggest_1_1_na_na_na&as-pos=1&as-type=HISTORY&suggestionId=t+shirts&requestId=8c1994c4-ca1c-4b65-bc76-1613537f3601&page={all_pages}")
    time.sleep(random.uniform(2, 4)) 

    auto_scroll()

    wait.until(EC.presence_of_all_elements_located((By.XPATH, "//a[contains(@href, '/p/')]")))
    url_elements = driver.find_elements(By.XPATH, "//a[contains(@href, '/p/')]")

    for all_urls in url_elements:
        single_url = all_urls.get_attribute("href")
        # time.sleep(random.uniform(2.5, 4.5))
        all_product_list.add(single_url)
   



for demo_urls in all_product_list:
    driver.get(demo_urls)
    auto_scroll()
    time.sleep(random.uniform(2.5, 4.5))
    
    try:
        name = driver.find_element(By.XPATH,"//h1[contains(text(),'')]").text 
        time.sleep(random.uniform(2.5, 4.5))
    except:
        name = ""
    try:
        Rating = driver.find_element(By.XPATH,"((//div[contains(text(),'.')]) [1])").text
        time.sleep(random.uniform(2.5, 4.5))
    except:
        Rating = ""
    try:
        #price = driver.find_element(By.XPATH,"(//div[contains(text(),'₹')])[6]").text
        price = driver.find_element(By.XPATH,"(//div[contains(text(),'₹')])[6]").text
        time.sleep(random.uniform(2.5, 4.5)) 
    except:
        price = ""
    

    driver.execute_script("window.scrollTo(0, 600);")
    all_details = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, "//div[contains(text(),'All details')]")))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", all_details[0])
    driver.execute_script("arguments[0].click();", all_details[0])
    specification = driver.find_element(By.XPATH, "//div[contains(text(),'Specification')]")
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", specification)
    driver.execute_script("arguments[0].click();", specification)
    time.sleep(random.uniform(1.5, 5.5))
    try:
        brand = driver.find_element(By.XPATH,"(//div[contains(.,'Brand')]/following::div[1])[1]").text
        time.sleep(random.uniform(2.5, 4.5))
    except:
        brand = ""
    
    All_name.append(name)
    all_rating.append(Rating)
    All_price.append(price)
    All_brand.append(brand)

    Tshirt_details = {
            "name": All_name,
            "Rating": all_rating,
            "price": All_price,
            "brand": All_brand
        }
    all_data_urls.append(Tshirt_details)
    print(f"Scrape done {len(all_data_urls)}")
    if (len(all_data_urls) == 5):
        break
df = pd.DataFrame(Tshirt_details)
df.to_excel("Data_Extract_F20.xlsx", index=False)
driver.quit() 






                                                           