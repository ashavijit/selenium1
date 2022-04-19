from selenium import webdriver
from config import keys
import time

def timeme(method):
    def wrapper(*args, **kw):
        startTime = int(round(time.time() * 1000))
        result = method(*args, **kw)
        endTime = int(round(time.time() * 1000))
        print((endTime - startTime)/1000, 's')
        return result
    return wrapper


options = webdriver.ChromeOptions()
options.add_argument('user-data-dir=www.flipkart.com')

@timeme
def order(k):
    
    driver.get(k['product_url'])
    
    
    driver.find_element_by_xpath('//*[@id="container"]/div/div[1]/div[2]/div/div[1]/div[1]/div[2]/div/ul/li[2]/form/button').click()

    time.sleep(0.5)
    
    
    driver.find_element_by_xpath('//*[@id="container"]/div/div[1]/div/div[1]/div[1]/div/div/div/div/div[1]/div/form/div[1]/input').send_keys(k['email'])
    
    driver.find_element_by_xpath('//*[@id="container"]/div/div[1]/div/div[1]/div[1]/div/div/div/div/div[1]/div/form/div[2]/button').click()

    time.sleep(0.5)
   
    
    driver.find_element_by_xpath('//*[@id="container"]/div/div[1]/div/div[1]/div[1]/div/div/div/div/div[1]/div/form/div[2]/input').send_keys(k['password'])
    
   
    driver.find_element_by_xpath('//*[@id="container"]/div/div[1]/div/div[1]/div[1]/div/div/div/div/div[1]/div/form/div[3]/button').click()


if __name__ == '__main__':
    
    driver = webdriver.Chrome('./chromedriver')
    order(keys)