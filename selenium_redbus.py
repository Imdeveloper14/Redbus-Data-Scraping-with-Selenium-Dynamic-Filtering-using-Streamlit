# %%
#import required libraries
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

# %% [markdown]
# **ANDHRA PRADESH**
# 

# %%
#Open Browser

driver=webdriver.Chrome()

#load the red bus webpage

driver.get("https://www.redbus.in/online-booking/apsrtc/?utm_source=rtchometile");

time.sleep(3)

driver.maximize_window()

# %%
#retrive bus routes and links

wait = WebDriverWait(driver, 20)
def andhra_link_route(path):
    Link_andhra=[]
    Route_andhra=[]
    #retrive the route links
    for i in range(1, 6):
        paths=driver.find_elements(By.XPATH, path)

        for links in paths:
            d=links.get_attribute("href")
            Link_andhra.append(d)

        #retrive the name of routes
        for route in paths:
            Route_andhra.append(route.text)
        
        try:
            #wait for the pagination to appear
            pagination = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'DC_117_paginationTable')))
            next_button = pagination.find_element(By.XPATH, f'//div[@class="DC_117_pageTabs " and text()={1+i}]')
            actions = ActionChains(driver)
            actions.move_to_element(next_button).perform()
            time.sleep(3)
            next_button.click()

        except NoSuchElementException:
            print(f"No more pages to paginate at step {i}")

            break

    return Link_andhra,Route_andhra

Link_andhra, Route_andhra = andhra_link_route("//a[@class='route']")

driver.close()



# %%
#change to dataframe using pandas
df_k=pd.DataFrame({"Route_Name":Route_andhra,"Route_Links":Link_andhra})
df_k

# %%
#change dataframe to csv
path=r"C:\Users\chand\Desktop\capstone-1\df_k.csv"
df_k.to_csv(path, index=False)


# %% [markdown]
# **Kerala**

# %%
#Open Browser

driver=webdriver.Chrome()

#load the red bus webpage

driver.get("https://www.redbus.in/online-booking/ksrtc-kerala/?utm_source=rtchometile");

time.sleep(3)

driver.maximize_window()

# %%
#retrive bus routes and links

wait = WebDriverWait(driver, 20)
def kerala_link_route(path):
    Link_Kerala=[]
    Route_kerala=[]
    #retrive the route links
    for i in range(1, 6):
        paths=driver.find_elements(By.XPATH, path)

        for links in paths:
            d=links.get_attribute("href")
            Link_Kerala.append(d)

        #retrive the name of routes
        for route in paths:
            Route_kerala.append(route.text)
        
        try:
            #wait for the pagination to appear
            pagination = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'DC_117_paginationTable')))
            next_button = pagination.find_element(By.XPATH, f'//div[@class="DC_117_pageTabs " and text()={1+i}]')
            actions = ActionChains(driver)
            actions.move_to_element(next_button).perform()
            time.sleep(3)
            next_button.click()

        except NoSuchElementException:
            print(f"No more pages to paginate at step {i}")

            break

    return Link_Kerala,Route_kerala

Link_Kerala, Route_kerala = kerala_link_route("//a[@class='route']")

# %%
df_a=pd.DataFrame({"Route_Name":Route_kerala,"Route_Links":Link_Kerala})
df_a

# %%
#change dataframe to csv
path=r"C:\Users\chand\Desktop\capstone-1\df_a.csv"
df_a.to_csv(path, index=False)

# %% [markdown]
# **TSRTC**

# %%
#Open Browser

driver=webdriver.Chrome()

#load the red bus webpage

driver.get("https://www.redbus.in/online-booking/tsrtc/?utm_source=rtchometile");

time.sleep(3)

driver.maximize_window()

#retrive bus routes and links

wait = WebDriverWait(driver, 20)

def TSRTC_link_route(path):
    Link_TSRTC=[]
    Route_TSRTC=[]
    #retrive the route links
    for i in range(1, 6):
        paths=driver.find_elements(By.XPATH, path)

        for links in paths:
            d=links.get_attribute("href")
            Link_TSRTC.append(d)

        #retrive the name of routes
        for route in paths:
            Route_TSRTC.append(route.text)
        
        try:
            #wait for the pagination to appear
            pagination = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'DC_117_paginationTable')))
            next_button = pagination.find_element(By.XPATH, f'//div[@class="DC_117_pageTabs " and text()={1+i}]')
            actions = ActionChains(driver)
            actions.move_to_element(next_button).perform()
            time.sleep(3)
            next_button.click()

        except NoSuchElementException:
            print(f"No more pages to paginate at step {i}")

            break

    return Link_TSRTC,Route_TSRTC

Link_TSRTC, Route_TSRTC = TSRTC_link_route("//a[@class='route']")

time.sleep(10)

driver.minimize_window()



# %%
#change to dataframe using pandas
df_t=pd.DataFrame({"Route_Name":Route_TSRTC,"Route_Links":Link_TSRTC})
df_t

# %%
#change dataframe to csv
path=r"C:\Users\chand\Desktop\capstone-1\df_t.csv"
df_t.to_csv(path, index=False)


# %% [markdown]
# **KTCL**

# %%
#Open Browser

driver=webdriver.Chrome()

#load the red bus webpage

driver.get("https://www.redbus.in/online-booking/ktcl/?utm_source=rtchometile");

time.sleep(3)

driver.maximize_window()

#retrive bus routes and links

wait = WebDriverWait(driver, 20)

def KTCL_link_route(path):
    Link_KTCL=[]
    Route_KTCL=[]
    #retrive the route links
    for i in range(1, 6):
        paths=driver.find_elements(By.XPATH, path)

        for links in paths:
            d=links.get_attribute("href")
            Link_KTCL.append(d)

        #retrive the name of routes
        for route in paths:
            Route_KTCL.append(route.text)
        
        try:
            #wait for the pagination to appear
            pagination = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'DC_117_paginationTable')))
            next_button = pagination.find_element(By.XPATH, f'//div[@class="DC_117_pageTabs " and text()={1+i}]')
            actions = ActionChains(driver)
            actions.move_to_element(next_button).perform()
            time.sleep(3)
            next_button.click()

        except NoSuchElementException:
            print(f"No more pages to paginate at step {i}")

            break

    return Link_TSRTC,Route_TSRTC

Link_KTCL, Route_KTCL = KTCL_link_route("//a[@class='route']")

time.sleep(10)

driver.close()

# %%
#change to dataframe using pandas
df_kt=pd.DataFrame({"Route_Name":Route_TSRTC,"Route_Links":Link_TSRTC})
df_kt

# %%
#change dataframe to csv
path=r"C:\Users\chand\Desktop\capstone-1\df_kt.csv"
df_kt.to_csv(path, index=False)


# %% [markdown]
# **RSRTC**

# %%
#Open Browser

driver=webdriver.Chrome()

#load the red bus webpage

driver.get("https://www.redbus.in/online-booking/rsrtc/?utm_source=rtchometile");

time.sleep(3)

driver.maximize_window()

#retrive bus routes and links

wait = WebDriverWait(driver, 20)

def RSRTC_link_route(path):
    Link_RSRTC=[]
    Route_RSRTC=[]
    #retrive the route links
    for i in range(1, 6):
        paths=driver.find_elements(By.XPATH, path)

        for links in paths:
            d=links.get_attribute("href")
            Link_RSRTC.append(d)

        #retrive the name of routes
        for route in paths:
            Route_RSRTC.append(route.text)
        
        try:
            #wait for the pagination to appear
            pagination = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'DC_117_paginationTable')))
            next_button = pagination.find_element(By.XPATH, f'//div[@class="DC_117_pageTabs " and text()={1+i}]')
            actions = ActionChains(driver)
            actions.move_to_element(next_button).perform()
            time.sleep(3)
            next_button.click()

        except NoSuchElementException:
            print(f"No more pages to paginate at step {i}")

            break

    return Link_RSRTC,Route_RSRTC

Link_RSRTC, Route_RSRTC = RSRTC_link_route("//a[@class='route']")

time.sleep(10)

driver.minimize_window()

# %%

#change to dataframe using pandas
df_Rt=pd.DataFrame({"Route_Name":Route_RSRTC,"Route_Links":Link_RSRTC})
df_Rt

# %%
#change dataframe to csv
path=r"C:\Users\chand\Desktop\capstone-1\df_Rt.csv"
df_Rt.to_csv(path, index=False)

# %% [markdown]
# **SBSTC**

# %%
#Open Browser

driver=webdriver.Chrome()

#load the red bus webpage

driver.get("https://www.redbus.in/online-booking/south-bengal-state-transport-corporation-sbstc/?utm_source=rtchometile");

time.sleep(3)

driver.maximize_window()

#retrive bus routes and links

wait = WebDriverWait(driver, 20)

def SBSTC_link_route(path):
    Link_SBSTC=[]
    Route_SBSTC=[]
    #retrive the route links
    for i in range(1, 6):
        paths=driver.find_elements(By.XPATH, path)

        for links in paths:
            d=links.get_attribute("href")
            Link_SBSTC.append(d)

        #retrive the name of routes
        for route in paths:
            Route_SBSTC.append(route.text)
        
        try:
            #wait for the pagination to appear
            pagination = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'DC_117_paginationTable')))
            next_button = pagination.find_element(By.XPATH, f'//div[@class="DC_117_pageTabs " and text()={1+i}]')
            actions = ActionChains(driver)
            actions.move_to_element(next_button).perform()
            time.sleep(3)
            next_button.click()

        except NoSuchElementException:
            print(f"No more pages to paginate at step {i}")

            break

    return Link_SBSTC,Route_SBSTC

Link_SBSTC, Route_SBSTC = SBSTC_link_route("//a[@class='route']")

time.sleep(10)

driver.minimize_window()

# %%
#change to dataframe using pandas
df_St=pd.DataFrame({"Route_Name":Route_SBSTC,"Route_Links":Link_SBSTC})
df_St

# %%
#change dataframe to csv
path=r"C:\Users\chand\Desktop\capstone-1\df_St.csv"
df_St.to_csv(path, index=False)

# %% [markdown]
# **HRTC**

# %%
#Open Browser

driver=webdriver.Chrome()

#load the red bus webpage

driver.get("https://www.redbus.in/online-booking/hrtc/?utm_source=rtchometile");

time.sleep(3)

driver.maximize_window()

#retrive bus routes and links

wait = WebDriverWait(driver, 20)

def HRTC_link_route(path):
    Link_HRTC=[]
    Route_HRTC=[]
    #retrive the route links
    for i in range(1, 6):
        paths=driver.find_elements(By.XPATH, path)

        for links in paths:
            d=links.get_attribute("href")
            Link_HRTC.append(d)

        #retrive the name of routes
        for route in paths:
            Route_HRTC.append(route.text)
        
        try:
            #wait for the pagination to appear
            pagination = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'DC_117_paginationTable')))
            next_button = pagination.find_element(By.XPATH, f'//div[@class="DC_117_pageTabs " and text()={1+i}]')
            actions = ActionChains(driver)
            actions.move_to_element(next_button).perform()
            time.sleep(3)
            next_button.click()

        except NoSuchElementException:
            print(f"No more pages to paginate at step {i}")

            break

    return Link_HRTC,Route_HRTC

Link_HRTC, Route_HRTC = HRTC_link_route("//a[@class='route']")

time.sleep(10)

driver.close()

# %%
#change to dataframe using pandas
df_Ht=pd.DataFrame({"Route_Name":Route_HRTC,"Route_Links":Link_HRTC})
df_Ht

# %%
#change dataframe to csv
path=r"C:\Users\chand\Desktop\capstone-1\df_Ht.csv"
df_Ht.to_csv(path, index=False)

# %% [markdown]
# **UPSRTC**

# %%
#Open Browser

driver=webdriver.Chrome()

#load the red bus webpage

driver.get("https://www.redbus.in/online-booking/uttar-pradesh-state-road-transport-corporation-upsrtc/?utm_source=rtchometile");

time.sleep(3)

driver.maximize_window()

#retrive bus routes and links

wait = WebDriverWait(driver, 20)

def UPSRTC_link_route(path):
    Link_UPSRTC=[]
    Route_UPSRTC=[]
    #retrive the route links
    for i in range(1, 6):
        paths=driver.find_elements(By.XPATH, path)

        for links in paths:
            d=links.get_attribute("href")
            Link_UPSRTC.append(d)

        #retrive the name of routes
        for route in paths:
            Route_UPSRTC.append(route.text)
        
        try:
            #wait for the pagination to appear
            pagination = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'DC_117_paginationTable')))
            next_button = pagination.find_element(By.XPATH, f'//div[@class="DC_117_pageTabs " and text()={1+i}]')
            actions = ActionChains(driver)
            actions.move_to_element(next_button).perform()
            time.sleep(3)
            next_button.click()

        except NoSuchElementException:
            print(f"No more pages to paginate at step {i}")

            break

    return Link_UPSRTC,Route_UPSRTC

Link_UPSRTC, Route_UPSRTC = UPSRTC_link_route("//a[@class='route']")

time.sleep(10)

driver.close()

# %%
#change to dataframe using pandas
df_Ut=pd.DataFrame({"Route_Name":Route_UPSRTC,"Route_Links":Link_UPSRTC})
df_Ut

# %%
#change dataframe to csv
path=r"C:\Users\chand\Desktop\capstone-1\df_Ut.csv"
df_Ut.to_csv(path, index=False)

# %% [markdown]
# **ASTC**

# %%
#Open Browser

driver=webdriver.Chrome()

#load the red bus webpage

driver.get("https://www.redbus.in/online-booking/astc/?utm_source=rtchometile");

time.sleep(3)

driver.maximize_window()

#retrive bus routes and links

wait = WebDriverWait(driver, 20)

def ASTC_link_route(path):
    Link_ASTC=[]
    Route_ASTC=[]
    #retrive the route links
    for i in range(1, 6):
        paths=driver.find_elements(By.XPATH, path)

        for links in paths:
            d=links.get_attribute("href")
            Link_ASTC.append(d)

        #retrive the name of routes
        for route in paths:
            Route_ASTC.append(route.text)
        
        try:
            #wait for the pagination to appear
            pagination = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'DC_117_paginationTable')))
            next_button = pagination.find_element(By.XPATH, f'//div[@class="DC_117_pageTabs " and text()={1+i}]')
            actions = ActionChains(driver)
            actions.move_to_element(next_button).perform()
            time.sleep(3)
            next_button.click()

        except NoSuchElementException:
            print(f"No more pages to paginate at step {i}")

            break

    return Link_ASTC,Route_ASTC

Link_ASTC, Route_ASTC = ASTC_link_route("//a[@class='route']")

time.sleep(10)

driver.close()

# %%
#change to dataframe using pandas
df_At=pd.DataFrame({"Route_Name":Route_ASTC,"Route_Links":Link_ASTC})
df_At

# %%
#change dataframe to csv
path=r"C:\Users\chand\Desktop\capstone-1\df_At.csv"
df_At.to_csv(path, index=False)

# %% [markdown]
# **WBTC**

# %%
#Open Browser

driver=webdriver.Chrome()

#load the red bus webpage

driver.get("https://www.redbus.in/online-booking/wbtc-ctc/?utm_source=rtchometile");

time.sleep(3)

driver.maximize_window()

#retrive bus routes and links

wait = WebDriverWait(driver, 20)

def WBTC_link_route(path):
    Link_WBTC=[]
    Route_WBTC=[]
    #retrive the route links
    for i in range(1, 6):
        paths=driver.find_elements(By.XPATH, path)

        for links in paths:
            d=links.get_attribute("href")
            Link_WBTC.append(d)

        #retrive the name of routes
        for route in paths:
            Route_WBTC.append(route.text)
        
        try:
            #wait for the pagination to appear
            pagination = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@class="DC_117_paginationTable"]')))
            next_button = pagination.find_element(By.XPATH, f'//div[@class="DC_117_pageTabs " and text()={1+i}]')
            actions = ActionChains(driver)
            actions.move_to_element(next_button).perform()
            time.sleep(3)
            next_button.click()

        except NoSuchElementException:
            print(f"No more pages to paginate at step {i}")

            break

    return Link_WBTC,Route_WBTC

Link_WBTC, Route_WBTC = WBTC_link_route("//a[@class='route']")

time.sleep(10)

driver.close()

# %%
#change to dataframe using pandas
import pandas as pd
df_Wt=pd.DataFrame({"Route_Name":Route_WBTC,"Route_Links":Link_WBTC})
df_Wt

# %%
#change dataframe to csv
path=r"C:\Users\chand\Desktop\capstone-1\df_Wt.csv"
df_Wt.to_csv(path, index=False)

# %%
#concatenate all bus route names and links in one dataframe
df=pd.concat([df_a,df_At,df_Ht,df_k,df_kt,df_Rt,df_St,df_t,df_Wt,df_Ut],ignore_index=True)
df

# %%
#change data frame into csv
path=r"C:\Users\chand\Desktop\capstone-1\df_routes.csv"
df.to_csv(path,index=False)


