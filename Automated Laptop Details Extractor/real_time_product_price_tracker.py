from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import csv

edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option(name='detach', value=True)
item_type = input("Enter item type: ")

driver = webdriver.Edge(options=edge_options)
driver.get(url='https://www.ebay.com/')

search_textbox = driver.find_element(by=By.XPATH, value='/html/body/div[4]/div/div/div/div[1]/header/section/form/div[1]/div/div/input')
search_textbox.send_keys(item_type, Keys.ENTER)
data = [['Product_Name', 'Secondary_Info', 'Product_Price', 'URL']]

def scraping_process1():

    time.sleep(6)

    links_list = driver.find_elements(by=By.XPATH, value='/html/body/div[5]/div[4]/div[3]/div[1]/div[3]/ul/li/div/div[1]/div/a')
    item_names_list = driver.find_elements(by=By.XPATH, value='/html/body/div[5]/div[4]/div[3]/div[1]/div[3]/ul/li/div/div[2]/a')
                                                             # ='/html/body/div[5]/div[4]/div[3]/div[1]/div[3]/ul/li/div/div[2]/a/div/span'
    prices_list = driver.find_elements(by=By.CSS_SELECTOR, value='span.s-item__price')
    secondary_info_list = driver.find_elements(By.CSS_SELECTOR, "span.SECONDARY_INFO")

    for index in range(links_list.__len__()):
        row = list()
        try:
            row.append(item_names_list[index].text)
        except:
            row.append('None')

        try:
            row.append(secondary_info_list[index].text)
            print(secondary_info_list[index].text)
        except:
            row.append('None')

        try:
            row.append(prices_list[index].text)
            print(prices_list[index].text)
        except:
            row.append('None')

        try:
            row.append(links_list[index].get_attribute(name='href')) #
        except:
            row.append('None')
        print(row)
        print('\n\n\n\n\n\n\n\n')
        data.append(row)


def scraping_process2():
    time.sleep(5)
    links = driver.find_elements(by=By.XPATH, value='/html/body/div[5]/div[4]/div[3]/div[1]/div[3]/ul/li/div/div[2]/a')
    items_name = driver.find_elements(by=By.XPATH, value='/html/body/div[5]/div[4]/div[3]/div[1]/div[3]/ul/li/div/div[2]/a/div/span')
    prices = driver.find_elements(by=By.CSS_SELECTOR, value='span.s-item__price')
    secondary_info = driver.find_elements(By.CSS_SELECTOR, "span.SECONDARY_INFO")

    for index in range(links.__len__()):
        row = list()
        try:
            row.append(items_name[index].text) #
        except:
            row.append('None')

        try:
            row.append(secondary_info[index].text) #
        except:
            row.append('None')

        try:
            row.append(prices[index].text)
        except:
            row.append('None')

        try:
            row.append(links[index].get_attribute(name='href')) #
        except:
            row.append('None')

        print(row)
        print('\n\n\n\n\n\n\n\n')
        data.append(row)


def scraping_process3():
    time.sleep(5)
    links2 = driver.find_elements(by=By.XPATH, value='/html/body/div[5]/div[4]/div[3]/div[1]/div[3]/ul/li/div/div[2]/a')
    items_name2 = driver.find_elements(by=By.XPATH, value='/html/body/div[5]/div[4]/div[3]/div[1]/div[3]/ul/li/div/div[2]/a/div/span')
    prices2 = driver.find_elements(by=By.CSS_SELECTOR, value='span.s-item__price')
    secondary_info2 = driver.find_elements(By.CSS_SELECTOR, "span.SECONDARY_INFO")

    for index in range(links2.__len__()):
        row = list()
        try:
            row.append(items_name2[index].text)  #
        except:
            row.append('None')

        try:
            row.append(secondary_info2[index].text)  #
        except:
            row.append('None')

        try:
            row.append(prices2[index].text)
        except:
            row.append('None')

        try:
            row.append(links2[index].get_attribute(name='href'))  #
        except:
            row.append('None')

        print(row)
        print('\n\n\n\n\n\n\n\n')
        data.append(row)

def quit_browser():
    driver.quit()

scraping_process1()


next_button2 = driver.find_element(by=By.XPATH, value='/html/body/div[5]/div[4]/div[3]/div[1]/div[3]/ul/li[64]/div[2]/div[1]/nav/ol/li[2]/a')
next_button2.click()

scraping_process2()

next_button3 = driver.find_element(by=By.XPATH, value='/html/body/div[5]/div[4]/div[3]/div[1]/div[3]/ul/li[63]/div[2]/div[1]/nav/ol/li[3]/a')
next_button3.click()

scraping_process3()

print(data)

quit_browser()
with open("data/scraped_data.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(data)