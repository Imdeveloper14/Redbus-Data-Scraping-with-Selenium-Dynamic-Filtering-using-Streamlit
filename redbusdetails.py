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
# **ANDHRA BUS DETAILS**

# %%
#READ THE CSV FILE
df_1=pd.read_csv("df_k.csv")
df_1

# %%
#retrive the bus details
driver_k=webdriver.Chrome()
Bus_name_k=[]
Bus_types_k=[]
start_time_k=[]
End_time_k=[]
Ratings_k=[]
Total_duration_k=[]
Prices_k=[]
Seats_available_k=[]
Route_names=[]
Route_links=[]

for i,r in df_1.iterrows():
    link=r["Route_Links"]
    routes=r["Route_Name"]

#loop through each link
    driver_k.get(link)
    time.sleep(2)

    #click on each element to revel bus details
    elements=driver_k.find_elements(By.XPATH, f"//a[contains(@href, '{link}')]")
    for element in elements:
        element.click()
        time.sleep(2)
    
    #click element to view bus
    try:
        clicks=driver_k.find_element(By.XPATH, "//div[@class='button']")
        clicks.click()
    except:
        continue
    time.sleep(2)

    scrolling = True
    while scrolling:
        old_page_source = driver_k.page_source

        #use actionchains to perform a PAGE DOWN
        ActionChains(driver_k).send_keys(Keys.PAGE_DOWN).perform()

        time.sleep(5)

        new_page_source = driver_k.page_source

        if new_page_source == old_page_source:
            scrolling = False

    #extract bus details
    bus_name = driver_k.find_elements(By.XPATH, "//div[@class='travels lh-24 f-bold d-color']")
    bus_type = driver_k.find_elements(By.XPATH, "//div[@class='bus-type f-12 m-top-16 l-color evBus']")
    start_time = driver_k.find_elements(By.XPATH, "//*[@class='dp-time f-19 d-color f-bold']")
    end_time = driver_k.find_elements(By.XPATH, "//*[@class='bp-time f-19 d-color disp-Inline']")
    Total_duration = driver_k.find_elements(By.XPATH, "//*[@class='dur l-color lh-24']")

    try:
        Rating = driver_k.find_elements(By.XPATH, "//div[@class='clearfix row-one']/div[@class='column-six p-right-10 w-10 fl']")

    except:
        continue
    price = driver_k.find_elements(By.XPATH, "//*[@class='fare d-block']")
    seats = driver_k.find_elements(By.XPATH, "//div[@class='seat-left m-top-30']")

    #Append the data into the respective lists
    for bus in bus_name:
        Bus_name_k.append(bus.text)
        Route_links.append(link)
        Route_names.append(routes)
    for bus_type_element in bus_type:
        Bus_types_k.append(bus_type_element.text)
    for start_time_element in start_time:
        start_time_k.append(start_time_element.text)
    for end_time_element in end_time:
        End_time_k.append(end_time_element.text)
    for Total_duration_element in Total_duration:
        Total_duration_k.append(Total_duration_element.text)
    for ratings in Rating:
        Ratings_k.append(ratings.text)
    for price_element in price:
        Prices_k.append(price_element.text)
    for seats_elements in seats:
        Seats_available_k.append(seats_elements.text)
print("all bus details retrived successfully")

driver_k.close()


# %%
#from the list covert into dataframe
data_1 = {
    'Bus_Name': Bus_name_k,
    'Bus_Type': Bus_types_k,
    'Start_Time': start_time_k,
    'End_Time': End_time_k,
    'Total_Duration': Total_duration_k,
    'Price': Prices_k,
    'Ratings': Ratings_k,
    'Route_link': Route_links,
    'Route_name': Route_names
}
df_buses_1 = pd.DataFrame(data_1)
#convert dataframe into csv
path = r"C:\Users\chand\Desktop\capstone-1\df_buses_1.csv"
df_buses_1.to_csv(path,index=False)

# %%
df_buses_1

# %% [markdown]
# **KERALA BUS DETAILS**

# %%
#READ THE CSV FILE
df_2=pd.read_csv("df_a.csv")
df_2

# %%
#retrive the bus details
driver_a=webdriver.Chrome()
Bus_name_a=[]
Bus_types_a=[]
start_time_a=[]
End_time_a=[]
Ratings_a=[]
Total_duration_a=[]
Prices_a=[]
Seats_available_a=[]
Route_names=[]
Route_links=[]

for i,r in df_2.iterrows():
    link=r["Route_Links"]
    routes=r["Route_Name"]

#loop through each link
    driver_a.get(link)
    time.sleep(2)

    #click on each element to revel bus details
    elements=driver_a.find_elements(By.XPATH, f"//a[contains(@href, '{link}')]")
    for element in elements:
        element.click()
        time.sleep(2)
    
    #click element to view bus
    try:
        clicks=driver_a.find_element(By.XPATH, "//div[@class='button']")
        clicks.click()
    except:
        continue
    time.sleep(2)

    scrolling = True
    while scrolling:
        old_page_source = driver_a.page_source

        #use actionchains to perform a PAGE DOWN
        ActionChains(driver_a).send_keys(Keys.PAGE_DOWN).perform()

        time.sleep(5)

        new_page_source = driver_a.page_source

        if new_page_source == old_page_source:
            scrolling = False

    #extract bus details
    bus_name = driver_a.find_elements(By.XPATH, "//div[@class='travels lh-24 f-bold d-color']")
    bus_type = driver_a.find_elements(By.XPATH, "//div[@class='bus-type f-12 m-top-16 l-color evBus']")
    start_time = driver_a.find_elements(By.XPATH, "//*[@class='dp-time f-19 d-color f-bold']")
    end_time = driver_a.find_elements(By.XPATH, "//*[@class='bp-time f-19 d-color disp-Inline']")
    Total_duration = driver_a.find_elements(By.XPATH, "//*[@class='dur l-color lh-24']")

    try:
        Rating = driver_a.find_elements(By.XPATH, "//div[@class='clearfix row-one']/div[@class='column-six p-right-10 w-10 fl']")

    except:
        continue
    price = driver_a.find_elements(By.XPATH, "//*[@class='fare d-block']")
    seats = driver_a.find_elements(By.XPATH, "//div[@class='seat-left']")

    #Append the data into the respective lists
    for bus in bus_name:
        Bus_name_a.append(bus.text)
        Route_links.append(link)
        Route_names.append(routes)
    for bus_type_element in bus_type:
        Bus_types_a.append(bus_type_element.text)
    for start_time_element in start_time:
        start_time_a.append(start_time_element.text)
    for end_time_element in end_time:
        End_time_a.append(end_time_element.text)
    for Total_duration_element in Total_duration:
        Total_duration_a.append(Total_duration_element.text)
    for ratings in Rating:
        Ratings_a.append(ratings.text)
    for price_element in price:
        Prices_a.append(price_element.text)
    for seats_elements in seats:
        Seats_available_a.append(seats_elements.text)
print("all bus details retrived successfully")

driver_a.close()

# %%
#from the list covert into dataframe
data_2 = {
    'Bus_Name': Bus_name_a,
    'Bus_Type': Bus_types_a,
    'Start_Time': start_time_a,
    'End_Time': End_time_a,
    'Total_Duration': Total_duration_a,
    'Price': Prices_a,
    'Ratings': Ratings_a,
    'Route_link': Route_links,
    'Route_name': Route_names
}

df_buses_2 = pd.DataFrame(data_2)
#convert dataframe into csv
path = r"C:\Users\chand\Desktop\capstone-1\df_buses_2.csv"
df_buses_2.to_csv(path,index=False)

# %%
df_buses_2

# %% [markdown]
# **TSRTC**

# %%
#READ THE CSV FILE
df_3=pd.read_csv("df_t.csv")
df_3

# %%
#retrive the bus details
driver_t=webdriver.Chrome()
Bus_name_t=[]
Bus_types_t=[]
start_time_t=[]
End_time_t=[]
Ratings_t=[]
Total_duration_t=[]
Prices_t=[]
Seats_available_t=[]
Route_names=[]
Route_links=[]

for i,r in df_3.iterrows():
    link=r["Route_Links"]
    routes=r["Route_Name"]

#loop through each link
    driver_t.get(link)
    time.sleep(2)

    #click on each element to revel bus details
    elements=driver_t.find_elements(By.XPATH, f"//a[contains(@href, '{link}')]")
    for element in elements:
        element.click()
        time.sleep(2)
    
    #click element to view bus
    try:
        clicks=driver_t.find_element(By.XPATH, "//div[@class='button']")
        clicks.click()
    except:
        continue
    time.sleep(2)

    scrolling = True
    while scrolling:
        old_page_source = driver_t.page_source

        #use actionchains to perform a PAGE DOWN
        ActionChains(driver_t).send_keys(Keys.PAGE_DOWN).perform()

        time.sleep(5)

        new_page_source = driver_t.page_source

        if new_page_source == old_page_source:
            scrolling = False

    #extract bus details
    bus_name = driver_t.find_elements(By.XPATH, "//div[@class='travels lh-24 f-bold d-color']")
    bus_type = driver_t.find_elements(By.XPATH, "//div[@class='bus-type f-12 m-top-16 l-color evBus']")
    start_time = driver_t.find_elements(By.XPATH, "//*[@class='dp-time f-19 d-color f-bold']")
    end_time = driver_t.find_elements(By.XPATH, "//*[@class='bp-time f-19 d-color disp-Inline']")
    Total_duration = driver_t.find_elements(By.XPATH, "//*[@class='dur l-color lh-24']")

    try:
        Rating = driver_t.find_elements(By.XPATH, "//div[@class='clearfix row-one']/div[@class='column-six p-right-10 w-10 fl']")

    except:
        continue
    price = driver_t.find_elements(By.XPATH, "//*[@class='fare d-block']")
    seats = driver_t.find_elements(By.XPATH, "//div[@class='seat-left']")

    #Append the data into the respective lists
    for bus in bus_name:
        Bus_name_t.append(bus.text)
        Route_links.append(link)
        Route_names.append(routes)
    for bus_type_element in bus_type:
        Bus_types_t.append(bus_type_element.text)
    for start_time_element in start_time:
        start_time_t.append(start_time_element.text)
    for end_time_element in end_time:
        End_time_t.append(end_time_element.text)
    for Total_duration_element in Total_duration:
        Total_duration_t.append(Total_duration_element.text)
    for ratings in Rating:
        Ratings_t.append(ratings.text)
    for price_element in price:
        Prices_t.append(price_element.text)
    for seats_elements in seats:
        Seats_available_t.append(seats_elements.text)
print("all bus details retrived successfully")

driver_t.close()

# %%
#from the list covert into dataframe
data_3 = {
    'Bus_Name': Bus_name_t,
    'Bus_Type': Bus_types_t,
    'Start_Time': start_time_t,
    'End_Time': End_time_t,
    'Total_Duration': Total_duration_t,
    'Price': Prices_t,
    'Ratings': Ratings_t,
    'Route_link': Route_links,
    'Route_name': Route_names
}

df_buses_3=pd.DataFrame(data_3)
#convert dataframe into csv
path =r"C:\Users\chand\Desktop\capstone-1\df_buses_3.csv"
df_buses_3.to_csv(path,index=False)

# %%
df_buses_3

# %% [markdown]
# **KTCL**

# %%
#READ THE CSV FILE
df_4=pd.read_csv("df_kt.csv")
df_4

# %%
#retrive the bus details
driver_kt=webdriver.Chrome()
Bus_name_kt=[]
Bus_types_kt=[]
start_time_kt=[]
End_time_kt=[]
Ratings_kt=[]
Total_duration_kt=[]
Prices_kt=[]
Seats_available_kt=[]
Route_names=[]
Route_links=[]

for i,r in df_4.iterrows():
    link=r["Route_Links"]
    routes=r["Route_Name"]

#loop through each link
    driver_kt.get(link)
    time.sleep(2)

    #click on each element to revel bus details
    elements=driver_kt.find_elements(By.XPATH, f"//a[contains(@href, '{link}')]")
    for element in elements:
        element.click()
        time.sleep(2)
    
    #click element to view bus
    try:
        clicks=driver_kt.find_element(By.XPATH, "//div[@class='button']")
        clicks.click()
    except:
        continue
    time.sleep(2)

    scrolling = True
    while scrolling:
        old_page_source = driver_kt.page_source

        #use actionchains to perform a PAGE DOWN
        ActionChains(driver_kt).send_keys(Keys.PAGE_DOWN).perform()

        time.sleep(5)

        new_page_source = driver_kt.page_source

        if new_page_source == old_page_source:
            scrolling = False

    #extract bus details
    bus_name = driver_kt.find_elements(By.XPATH, "//div[@class='travels lh-24 f-bold d-color']")
    bus_type = driver_kt.find_elements(By.XPATH, "//div[@class='bus-type f-12 m-top-16 l-color evBus']")
    start_time = driver_kt.find_elements(By.XPATH, "//*[@class='dp-time f-19 d-color f-bold']")
    end_time = driver_kt.find_elements(By.XPATH, "//*[@class='bp-time f-19 d-color disp-Inline']")
    Total_duration = driver_kt.find_elements(By.XPATH, "//*[@class='dur l-color lh-24']")

    try:
        Rating = driver_kt.find_elements(By.XPATH, "//div[@class='clearfix row-one']/div[@class='column-six p-right-10 w-10 fl']")

    except:
        continue
    price = driver_kt.find_elements(By.XPATH, "//*[@class='fare d-block']")
    seats = driver_kt.find_elements(By.XPATH, "//div[@class='seat-left']")

    #Append the data into the respective lists
    for bus in bus_name:
        Bus_name_kt.append(bus.text)
        Route_links.append(link)
        Route_names.append(routes)
    for bus_type_element in bus_type:
        Bus_types_kt.append(bus_type_element.text)
    for start_time_element in start_time:
        start_time_kt.append(start_time_element.text)
    for end_time_element in end_time:
        End_time_kt.append(end_time_element.text)
    for Total_duration_element in Total_duration:
        Total_duration_kt.append(Total_duration_element.text)
    for ratings in Rating:
        Ratings_kt.append(ratings.text)
    for price_element in price:
        Prices_kt.append(price_element.text)
    for seats_elements in seats:
        Seats_available_kt.append(seats_elements.text)
print("all bus details retrived successfully")

driver_kt.close()

# %%

#from the list covert into dataframe
data_4 = {
    'Bus_Name': Bus_name_kt,
    'Bus_Type': Bus_types_kt,
    'Start_Time': start_time_kt,
    'End_Time': End_time_kt,
    'Total_Duration': Total_duration_kt,
    'Price': Prices_kt,
    'Ratings': Ratings_kt,
    'Route_link': Route_links,
    'Route_name': Route_names
}

df_buses_4=pd.DataFrame(data_4)
#convert dataframe into csv
path =r"C:\Users\chand\Desktop\capstone-1\df_buses_4.csv"
df_buses_4.to_csv(path,index=False)

# %%
df_buses_4

# %% [markdown]
# **RSRTC**

# %%
#READ THE CSV FILE
df_5=pd.read_csv("df_Rt.csv")
df_5

# %%
#retrive the bus details
driver_Rt=webdriver.Chrome()
Bus_name_Rt=[]
Bus_types_Rt=[]
start_time_Rt=[]
End_time_Rt=[]
Ratings_Rt=[]
Total_duration_Rt=[]
Prices_Rt=[]
Seats_available_Rt=[]
Route_names=[]
Route_links=[]

for i,r in df_5.iterrows():
    link=r["Route_Links"]
    routes=r["Route_Name"]

#loop through each link
    driver_Rt.get(link)
    time.sleep(2)

    #click on each element to revel bus details
    elements=driver_Rt.find_elements(By.XPATH, f"//a[contains(@href, '{link}')]")
    for element in elements:
        element.click()
        time.sleep(2)
    
    #click element to view bus
    try:
        clicks=driver_Rt.find_element(By.XPATH, "//div[@class='button']")
        clicks.click()
    except:
        continue
    time.sleep(2)

    scrolling = True
    while scrolling:
        old_page_source = driver_Rt.page_source

        #use actionchains to perform a PAGE DOWN
        ActionChains(driver_Rt).send_keys(Keys.PAGE_DOWN).perform()

        time.sleep(5)

        new_page_source = driver_Rt.page_source

        if new_page_source == old_page_source:
            scrolling = False

    #extract bus details
    bus_name = driver_Rt.find_elements(By.XPATH, "//div[@class='travels lh-24 f-bold d-color']")
    bus_type = driver_Rt.find_elements(By.XPATH, "//div[@class='bus-type f-12 m-top-16 l-color evBus']")
    start_time = driver_Rt.find_elements(By.XPATH, "//*[@class='dp-time f-19 d-color f-bold']")
    end_time = driver_Rt.find_elements(By.XPATH, "//*[@class='bp-time f-19 d-color disp-Inline']")
    Total_duration = driver_Rt.find_elements(By.XPATH, "//*[@class='dur l-color lh-24']")

    try:
        Rating = driver_Rt.find_elements(By.XPATH, "//div[@class='clearfix row-one']/div[@class='column-six p-right-10 w-10 fl']")

    except:
        continue
    price = driver_Rt.find_elements(By.XPATH, "//*[@class='fare d-block']")
    seats = driver_Rt.find_elements(By.XPATH, "//div[@class='seat-left']")

    #Append the data into the respective lists
    for bus in bus_name:
        Bus_name_Rt.append(bus.text)
        Route_links.append(link)
        Route_names.append(routes)
    for bus_type_element in bus_type:
        Bus_types_Rt.append(bus_type_element.text)
    for start_time_element in start_time:
        start_time_Rt.append(start_time_element.text)
    for end_time_element in end_time:
        End_time_Rt.append(end_time_element.text)
    for Total_duration_element in Total_duration:
        Total_duration_Rt.append(Total_duration_element.text)
    for ratings in Rating:
        Ratings_Rt.append(ratings.text)
    for price_element in price:
        Prices_Rt.append(price_element.text)
    for seats_elements in seats:
        Seats_available_Rt.append(seats_elements.text)
print("all bus details retrived successfully")

driver_Rt.close()

# %%
#from the list covert into dataframe
data_5 = {
    'Bus_Name': Bus_name_Rt,
    'Bus_Type': Bus_types_Rt,
    'Start_Time': start_time_Rt,
    'End_Time': End_time_Rt,
    'Total_Duration': Total_duration_Rt,
    'Price': Prices_Rt,
    'Ratings': Ratings_Rt,
    'Route_link': Route_links,
    'Route_name': Route_names
}

df_buses_5=pd.DataFrame(data_5)
#convert dataframe into csv
path =r"C:\Users\chand\Desktop\capstone-1\df_buses_5.csv"
df_buses_5.to_csv(path,index=False)

# %%
df_buses_5

# %% [markdown]
# **SBSTC**

# %%
#READ THE CSV FILE
df_6=pd.read_csv("df_st.csv")
df_6

# %%
#retrive the bus details
driver_st=webdriver.Chrome()
Bus_name_st=[]
Bus_types_st=[]
start_time_st=[]
End_time_st=[]
Ratings_st=[]
Total_duration_st=[]
Prices_st=[]
Seats_available_st=[]
Route_names=[]
Route_links=[]

for i,r in df_6.iterrows():
    link=r["Route_Links"]
    routes=r["Route_Name"]

#loop through each link
    driver_st.get(link)
    time.sleep(2)

    #click on each element to revel bus details
    elements=driver_st.find_elements(By.XPATH, f"//a[contains(@href, '{link}')]")
    for element in elements:
        element.click()
        time.sleep(2)
    
    #click element to view bus
    try:
        clicks=driver_st.find_element(By.XPATH, "//div[@class='button']")
        clicks.click()
    except:
        continue
    time.sleep(2)

    scrolling = True
    while scrolling:
        old_page_source = driver_st.page_source

        #use actionchains to perform a PAGE DOWN
        ActionChains(driver_st).send_keys(Keys.PAGE_DOWN).perform()

        time.sleep(5)

        new_page_source = driver_st.page_source

        if new_page_source == old_page_source:
            scrolling = False

    #extract bus details
    bus_name = driver_st.find_elements(By.XPATH, "//div[@class='travels lh-24 f-bold d-color']")
    bus_type = driver_st.find_elements(By.XPATH, "//div[@class='bus-type f-12 m-top-16 l-color evBus']")
    start_time = driver_st.find_elements(By.XPATH, "//*[@class='dp-time f-19 d-color f-bold']")
    end_time = driver_st.find_elements(By.XPATH, "//*[@class='bp-time f-19 d-color disp-Inline']")
    Total_duration = driver_st.find_elements(By.XPATH, "//*[@class='dur l-color lh-24']")

    try:
        Rating = driver_st.find_elements(By.XPATH, "//div[@class='clearfix row-one']/div[@class='column-six p-right-10 w-10 fl']")

    except:
        continue
    price = driver_st.find_elements(By.XPATH, "//*[@class='fare d-block']")
    seats = driver_st.find_elements(By.XPATH, "//div[@class='seat-left']")

    #Append the data into the respective lists
    for bus in bus_name:
        Bus_name_st.append(bus.text)
        Route_links.append(link)
        Route_names.append(routes)
    for bus_type_element in bus_type:
        Bus_types_st.append(bus_type_element.text)
    for start_time_element in start_time:
        start_time_st.append(start_time_element.text)
    for end_time_element in end_time:
        End_time_st.append(end_time_element.text)
    for Total_duration_element in Total_duration:
        Total_duration_st.append(Total_duration_element.text)
    for ratings in Rating:
        Ratings_st.append(ratings.text)
    for price_element in price:
        Prices_st.append(price_element.text)
    for seats_elements in seats:
        Seats_available_st.append(seats_elements.text)
print("all bus details retrived successfully")

driver_st.close()

# %%
#from the list covert into dataframe
data_6 = {
    'Bus_Name': Bus_name_st,
    'Bus_Type': Bus_types_st,
    'Start_Time': start_time_st,
    'End_Time': End_time_st,
    'Total_Duration': Total_duration_st,
    'Price': Prices_st,
    'Ratings': Ratings_st,
    'Route_link': Route_links,
    'Route_name': Route_names
}

df_buses_6=pd.DataFrame(data_6)
#convert dataframe into csv
path =r"C:\Users\chand\Desktop\capstone-1\df_buses_6.csv"
df_buses_6.to_csv(path,index=False)

# %%
df_buses_6

# %% [markdown]
# **HRTC**

# %%
#READ THE CSV FILE
df_7=pd.read_csv("df_Ht.csv")
df_7

# %%
#retrive the bus details
driver_Ht=webdriver.Chrome()
Bus_name_Ht=[]
Bus_types_Ht=[]
start_time_Ht=[]
End_time_Ht=[]
Ratings_Ht=[]
Total_duration_Ht=[]
Prices_Ht=[]
Seats_available_Ht=[]
Route_names=[]
Route_links=[]

for i,r in df_7.iterrows():
    link=r["Route_Links"]
    routes=r["Route_Name"]

#loop through each link
    driver_Ht.get(link)
    time.sleep(2)

    #click on each element to revel bus details
    elements=driver_Ht.find_elements(By.XPATH, f"//a[contains(@href, '{link}')]")
    for element in elements:
        element.click()
        time.sleep(2)
    
    #click element to view bus
    try:
        clicks=driver_Ht.find_element(By.XPATH, "//div[@class='button']")
        clicks.click()
    except:
        continue
    time.sleep(2)

    scrolling = True
    while scrolling:
        old_page_source = driver_Ht.page_source

        #use actionchains to perform a PAGE DOWN
        ActionChains(driver_Ht).send_keys(Keys.PAGE_DOWN).perform()

        time.sleep(5)

        new_page_source = driver_Ht.page_source

        if new_page_source == old_page_source:
            scrolling = False

    #extract bus details
    bus_name = driver_Ht.find_elements(By.XPATH, "//div[@class='travels lh-24 f-bold d-color']")
    bus_type = driver_Ht.find_elements(By.XPATH, "//div[@class='bus-type f-12 m-top-16 l-color evBus']")
    start_time = driver_Ht.find_elements(By.XPATH, "//*[@class='dp-time f-19 d-color f-bold']")
    end_time = driver_Ht.find_elements(By.XPATH, "//*[@class='bp-time f-19 d-color disp-Inline']")
    Total_duration = driver_Ht.find_elements(By.XPATH, "//*[@class='dur l-color lh-24']")

    try:
        Rating = driver_Ht.find_elements(By.XPATH, "//div[@class='clearfix row-one']/div[@class='column-six p-right-10 w-10 fl']")

    except:
        continue
    price = driver_Ht.find_elements(By.XPATH, "//*[@class='fare d-block']")
    seats = driver_Ht.find_elements(By.XPATH, "//div[@class='seat-left']")

    #Append the data into the respective lists
    for bus in bus_name:
        Bus_name_Ht.append(bus.text)
        Route_links.append(link)
        Route_names.append(routes)
    for bus_type_element in bus_type:
        Bus_types_Ht.append(bus_type_element.text)
    for start_time_element in start_time:
        start_time_Ht.append(start_time_element.text)
    for end_time_element in end_time:
        End_time_Ht.append(end_time_element.text)
    for Total_duration_element in Total_duration:
        Total_duration_Ht.append(Total_duration_element.text)
    for ratings in Rating:
        Ratings_Ht.append(ratings.text)
    for price_element in price:
        Prices_Ht.append(price_element.text)
    for seats_elements in seats:
        Seats_available_Ht.append(seats_elements.text)
print("all bus details retrived successfully")

driver_Ht.close()

# %%
#from the list covert into dataframe
data_7 = {
    'Bus_Name': Bus_name_Ht,
    'Bus_Type': Bus_types_Ht,
    'Start_Time': start_time_Ht,
    'End_Time': End_time_Ht,
    'Total_Duration': Total_duration_Ht,
    'Price': Prices_Ht,
    'Ratings': Ratings_Ht,
    'Route_link': Route_links,
    'Route_name': Route_names
}

df_buses_7=pd.DataFrame(data_7)
#convert dataframe into csv
path =r"C:\Users\chand\Desktop\capstone-1\df_buses_7.csv"
df_buses_7.to_csv(path,index=False)

# %%
df_buses_7

# %% [markdown]
# **UPSRTC**

# %%
#READ THE CSV FILE
df_8=pd.read_csv("df_Ut.csv")
df_8

# %%
#retrive the bus details
driver_Ut=webdriver.Chrome()
Bus_name_Ut=[]
Bus_types_Ut=[]
start_time_Ut=[]
End_time_Ut=[]
Ratings_Ut=[]
Total_duration_Ut=[]
Prices_Ut=[]
Seats_available_Ut=[]
Route_names=[]
Route_links=[]

for i,r in df_8.iterrows():
    link=r["Route_Links"]
    routes=r["Route_Name"]

#loop through each link
    driver_Ut.get(link)
    time.sleep(2)

    #click on each element to revel bus details
    elements=driver_Ut.find_elements(By.XPATH, f"//a[contains(@href, '{link}')]")
    for element in elements:
        element.click()
        time.sleep(2)
    
    #click element to view bus
    try:
        clicks=driver_Ut.find_element(By.XPATH, "//div[@class='button']")
        clicks.click()
    except:
        continue
    time.sleep(2)

    scrolling = True
    while scrolling:
        old_page_source = driver_Ut.page_source

        #use actionchains to perform a PAGE DOWN
        ActionChains(driver_Ut).send_keys(Keys.PAGE_DOWN).perform()

        time.sleep(5)

        new_page_source = driver_Ut.page_source

        if new_page_source == old_page_source:
            scrolling = False

    #extract bus details
    bus_name = driver_Ut.find_elements(By.XPATH, "//div[@class='travels lh-24 f-bold d-color']")
    bus_type = driver_Ut.find_elements(By.XPATH, "//div[@class='bus-type f-12 m-top-16 l-color evBus']")
    start_time = driver_Ut.find_elements(By.XPATH, "//*[@class='dp-time f-19 d-color f-bold']")
    end_time = driver_Ut.find_elements(By.XPATH, "//*[@class='bp-time f-19 d-color disp-Inline']")
    Total_duration = driver_Ut.find_elements(By.XPATH, "//*[@class='dur l-color lh-24']")

    try:
        Rating = driver_Ut.find_elements(By.XPATH, "//div[@class='clearfix row-one']/div[@class='column-six p-right-10 w-10 fl']")

    except:
        continue
    price = driver_Ut.find_elements(By.XPATH, "//*[@class='fare d-block']")
    seats = driver_Ut.find_elements(By.XPATH, "//div[@class='seat-left']")

    #Append the data into the respective lists
    for bus in bus_name:
        Bus_name_Ut.append(bus.text)
        Route_links.append(link)
        Route_names.append(routes)
    for bus_type_element in bus_type:
        Bus_types_Ut.append(bus_type_element.text)
    for start_time_element in start_time:
        start_time_Ut.append(start_time_element.text)
    for end_time_element in end_time:
        End_time_Ut.append(end_time_element.text)
    for Total_duration_element in Total_duration:
        Total_duration_Ut.append(Total_duration_element.text)
    for ratings in Rating:
        Ratings_Ut.append(ratings.text)
    for price_element in price:
        Prices_Ut.append(price_element.text)
    for seats_elements in seats:
        Seats_available_Ut.append(seats_elements.text)
print("all bus details retrived successfully")

driver_Ut.close()

# %%
#from the list covert into dataframe
data_8 = {
    'Bus_Name': Bus_name_Ut,
    'Bus_Type': Bus_types_Ut,
    'Start_Time': start_time_Ut,
    'End_Time': End_time_Ut,
    'Total_Duration': Total_duration_Ut,
    'Price': Prices_Ut,
    'Ratings': Ratings_Ut,
    'Route_link': Route_links,
    'Route_name': Route_names
}

df_buses_8=pd.DataFrame(data_8)
#convert dataframe into csv
path =r"C:\Users\chand\Desktop\capstone-1\df_buses_8.csv"
df_buses_8.to_csv(path,index=False)

# %%
df_buses_8

# %% [markdown]
# **ASTC**

# %%
#READ THE CSV FILE
df_9=pd.read_csv("df_At.csv")
df_9

# %%
#retrive the bus details
driver_At=webdriver.Chrome()
Bus_name_At=[]
Bus_types_At=[]
start_time_At=[]
End_time_At=[]
Ratings_At=[]
Total_duration_At=[]
Prices_At=[]
Seats_available_At=[]
Route_names=[]
Route_links=[]

for i,r in df_9.iterrows():
    link=r["Route_Links"]
    routes=r["Route_Name"]

#loop through each link
    driver_At.get(link)
    time.sleep(2)

    #click on each element to revel bus details
    elements=driver_At.find_elements(By.XPATH, f"//a[contains(@href, '{link}')]")
    for element in elements:
        element.click()
        time.sleep(2)
    
    #click element to view bus
    try:
        clicks=driver_At.find_element(By.XPATH, "//div[@class='button']")
        clicks.click()
    except:
        continue
    time.sleep(2)

    scrolling = True
    while scrolling:
        old_page_source = driver_At.page_source

        #use actionchains to perform a PAGE DOWN
        ActionChains(driver_At).send_keys(Keys.PAGE_DOWN).perform()

        time.sleep(5)

        new_page_source = driver_At.page_source

        if new_page_source == old_page_source:
            scrolling = False

    #extract bus details
    bus_name = driver_At.find_elements(By.XPATH, "//div[@class='travels lh-24 f-bold d-color']")
    bus_type = driver_At.find_elements(By.XPATH, "//div[@class='bus-type f-12 m-top-16 l-color evBus']")
    start_time = driver_At.find_elements(By.XPATH, "//*[@class='dp-time f-19 d-color f-bold']")
    end_time = driver_At.find_elements(By.XPATH, "//*[@class='bp-time f-19 d-color disp-Inline']")
    Total_duration = driver_At.find_elements(By.XPATH, "//*[@class='dur l-color lh-24']")

    try:
        Rating = driver_At.find_elements(By.XPATH, "//div[@class='clearfix row-one']/div[@class='column-six p-right-10 w-10 fl']")

    except:
        continue
    price = driver_At.find_elements(By.XPATH, "//*[@class='fare d-block']")
    seats = driver_At.find_elements(By.XPATH, "//div[@class='seat-left']")

    #Append the data into the respective lists
    for bus in bus_name:
        Bus_name_At.append(bus.text)
        Route_links.append(link)
        Route_names.append(routes)
    for bus_type_element in bus_type:
        Bus_types_At.append(bus_type_element.text)
    for start_time_element in start_time:
        start_time_At.append(start_time_element.text)
    for end_time_element in end_time:
        End_time_At.append(end_time_element.text)
    for Total_duration_element in Total_duration:
        Total_duration_At.append(Total_duration_element.text)
    for ratings in Rating:
        Ratings_At.append(ratings.text)
    for price_element in price:
        Prices_At.append(price_element.text)
    for seats_elements in seats:
        Seats_available_At.append(seats_elements.text)
print("all bus details retrived successfully")

driver_At.close()

# %%
#from the list covert into dataframe
data_9 = {
    'Bus_Name': Bus_name_At,
    'Bus_Type': Bus_types_At,
    'Start_Time': start_time_At,
    'End_Time': End_time_At,
    'Total_Duration': Total_duration_At,
    'Price': Prices_At,
    'Ratings': Ratings_At,
    'Route_link': Route_links,
    'Route_name': Route_names
}

df_buses_9=pd.DataFrame(data_9)
#convert dataframe into csv
path =r"C:\Users\chand\Desktop\capstone-1\df_buses_9.csv"
df_buses_9.to_csv(path,index=False)

# %%
df_buses_9

# %% [markdown]
# **WBTC**

# %%
#READ THE CSV FILE
df_10=pd.read_csv("df_Wt.csv")
df_10

# %%
#retrive the bus details
driver_Wt=webdriver.Chrome()
Bus_name_Wt=[]
Bus_types_Wt=[]
start_time_Wt=[]
End_time_Wt=[]
Ratings_Wt=[]
Total_duration_Wt=[]
Prices_Wt=[]
Seats_available_Wt=[]
Route_names=[]
Route_links=[]

for i,r in df_10.iterrows():
    link=r["Route_Links"]
    routes=r["Route_Name"]

#loop through each link
    driver_Wt.get(link)
    time.sleep(2)

    #click on each element to revel bus details
    elements=driver_Wt.find_elements(By.XPATH, f"//a[contains(@href, '{link}')]")
    for element in elements:
        element.click()
        time.sleep(2)
    
    #click element to view bus
    try:
        clicks=driver_Wt.find_element(By.XPATH, "//div[@class='button']")
        clicks.click()
    except:
        continue
    time.sleep(2)

    scrolling = True
    while scrolling:
        old_page_source = driver_Wt.page_source

        #use actionchains to perform a PAGE DOWN
        ActionChains(driver_Wt).send_keys(Keys.PAGE_DOWN).perform()

        time.sleep(5)

        new_page_source = driver_Wt.page_source

        if new_page_source == old_page_source:
            scrolling = False

    #extract bus details
    bus_name = driver_Wt.find_elements(By.XPATH, "//div[@class='travels lh-24 f-bold d-color']")
    bus_type = driver_Wt.find_elements(By.XPATH, "//div[@class='bus-type f-12 m-top-16 l-color evBus']")
    start_time = driver_Wt.find_elements(By.XPATH, "//*[@class='dp-time f-19 d-color f-bold']")
    end_time = driver_Wt.find_elements(By.XPATH, "//*[@class='bp-time f-19 d-color disp-Inline']")
    Total_duration = driver_Wt.find_elements(By.XPATH, "//*[@class='dur l-color lh-24']")

    try:
        Rating = driver_Wt.find_elements(By.XPATH, "//div[@class='clearfix row-one']/div[@class='column-six p-right-10 w-10 fl']")

    except:
        continue
    price = driver_Wt.find_elements(By.XPATH, "//*[@class='fare d-block']")
    seats = driver_Wt.find_elements(By.XPATH, "//div[@class='seat-left']")

    #Append the data into the respective lists
    for bus in bus_name:
        Bus_name_Wt.append(bus.text)
        Route_links.append(link)
        Route_names.append(routes)
    for bus_type_element in bus_type:
        Bus_types_Wt.append(bus_type_element.text)
    for start_time_element in start_time:
        start_time_Wt.append(start_time_element.text)
    for end_time_element in end_time:
        End_time_Wt.append(end_time_element.text)
    for Total_duration_element in Total_duration:
        Total_duration_Wt.append(Total_duration_element.text)
    for ratings in Rating:
        Ratings_Wt.append(ratings.text)
    for price_element in price:
        Prices_Wt.append(price_element.text)
    for seats_elements in seats:
        Seats_available_Wt.append(seats_elements.text)
print("all bus details retrived successfully")

driver_Wt.close()

# %%
#from the list covert into dataframe
data_10 = {
    'Bus_Name': Bus_name_Wt,
    'Bus_Type': Bus_types_Wt,
    'Start_Time': start_time_Wt,
    'End_Time': End_time_Wt,
    'Total_Duration': Total_duration_Wt,
    'Price': Prices_Wt,
    'Ratings': Ratings_Wt,
    'Route_link': Route_links,
    'Route_name': Route_names
}

df_buses_10=pd.DataFrame(data_10)
#convert dataframe into csv
path =r"C:\Users\chand\Desktop\capstone-1\df_buses_10.csv"
df_buses_10.to_csv(path,index=False)

# %%
df_buses_10


