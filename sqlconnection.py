# %%
pip install mysql.connector

# %%
#IMPORTING LIBRARIES
import pandas as pd
import mysql.connector
import numpy as np


# %%
# CSV TO DATA FRAME
df_buses_1=pd.read_csv("df_buses_1.csv")
df_buses_2=pd.read_csv("df_buses_2.csv")
df_buses_3=pd.read_csv("df_buses_3.csv")
df_buses_4=pd.read_csv("df_buses_4.csv")
df_buses_5=pd.read_csv("df_buses_5.csv")
df_buses_6=pd.read_csv("df_buses_6.csv")
df_buses_7=pd.read_csv("df_buses_7.csv")
df_buses_8=pd.read_csv("df_buses_8.csv")
df_buses_9=pd.read_csv("df_buses_9.csv")
df_buses_10=pd.read_csv("df_buses_10.csv")

final_df=pd.concat([df_buses_1,df_buses_2,df_buses_3,df_buses_4,df_buses_5,df_buses_6,df_buses_7,df_buses_8,df_buses_9,df_buses_10],ignore_index=True)
final_df

# %% [markdown]
# **Data Cleaning**

# %%
#data about data
final_df.info()

# %%
#covert Prices to numeric
final_df["Price"]=final_df["Price"].str.replace("INR","")
final_df["Price"]=final_df["Price"].astype(float)
final_df["Price"].fillna(0)

# %%
#CONVERT RATINGS TO NUMERIC
final_df["Ratings"]=final_df["Ratings"].str.replace("NEW","")
final_df["Ratings"]=final_df["Ratings"].str.strip()
final_df["Ratings"]=final_df["Ratings"].str.split().str[0]
final_df["Ratings"]=pd.to_numeric(final_df["Ratings"],errors='coerce')
final_df["Ratings"].fillna(0,inplace=True)

# %%
#info after the data type change
final_df.info()

# %%
final_df=final_df[final_df["Price"]<= 7000]

# %%
final_df=final_df.replace({np.nan: None})

# %% [markdown]
# **CREATING MYSQL DATABASE**

# %%
#sql connection
conn=mysql.connector.connect(host="localhost", user="root", password="Chandrasekar1",database="RED_BUS_DETAILS")
my_cursor = conn.cursor()
my_cursor.execute("CREATE DATABASE IF NOT EXISTS RED_BUS_DETAILS")

# %%
# Table Creation
my_cursor.execute('''CREATE TABLE IF NOT EXISTS bus_details(
                  ID INT AUTO_INCREMENT PRIMARY KEY,
                  Bus_name VARCHAR(255) NOT NULL,
                  Bus_type VARCHAR(255) NOT NULL,
                  Start_time VARCHAR(255) NOT NULL,
                  End_time VARCHAR(255) NOT NULL,
                  Total_duration VARCHAR(255) NOT NULL,
                  Price FLOAT NULL,
                  Seats_Available VARCHAR(255) NOT NULL,
                  Ratings Float NULL,
                  Route_link VARCHAR(255) NULL,
                  Route_name VARCHAR(255) NULL
                  )''')
print("Table Created successfully")

# %%
# SQL query to insert data into bus_details table
insert_query = '''INSERT INTO bus_details(
                    Bus_name,
                    Bus_type,
                    Start_time,
                    End_time,
                    Total_duration,
                    Price,
                    Seats_Available,
                    Ratings,
                    Route_link,
                    Route_name)
                  VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''
data = final_df.values.tolist()

my_cursor.executemany(insert_query, data)

conn.commit()

print("Values inserted successfully")


