#import liab
import os
from dotenv import load_dotenv
import google.generativeai as genai
import pyodbc
import streamlit as st

#fetch API Key
load_dotenv()
API_KEY = os.environ["API_KEY"]

#Configure Datbase settings
DRIVER_NAME = 'SQL Server'
SERVER_NAME = 'SERVER_NAME\\SQLEXPRESS' 
DATABASE_NAME ='YOUR_DATABASE_NAME'
SQL_USER_NAME = os.environ["SQL_DB_USER_NAME"]
SQL_PASSWORD = os.environ["SQL_DB_PASSWORD"]

# onfigure Gemini
genai.configure(api_key=API_KEY)

#Function to load GooglE Gemini Model and provide sql query as response 
def get_gemini_response(question,prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt,question])
    return response.text


#Function to retrive query from the sql database
def read_sql_query(sql):
    conn = pyodbc.connect(
                        'Driver={SQL Server Native Client 11.0};'
                        'Server='+SERVER_NAME+';'
                        'Database='+DATABASE_NAME+';'
                        'Trusted_Connection=yes;'
                        'UID='+SQL_USER_NAME+';'
                        'PWD='+SQL_PASSWORD+';')
    curser = conn.cursor()
    curser.execute(sql)
    rows=curser.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
       row
    return rows

## Define Your Prompt
prompt_parts_1 = [
  "You are an expert in converting English questions to SQL code! The SQL database (MICROSOFT SQL SERVER) has the name TIGER_GRAPH.dbo.SAMPLE_SUPERSTORE_STAGING and has the following columns - OW_ID, ORDER_ID, ORDER_DATE, SHIP_DATE, SHIP_MODE, CUSTOMER_ID, CUSTOMER_NAME, SEGMENT, COUNTRY, CITY, STATE, POSTAL_CODE, REGION, PRODUCT_ID, CATEGORY, SUB_CATEGORY, PRODUCT_NAME, SALES, QUANTITY, DISCOUNT, PROFIT.\n\nFor example,\nExample 1 - WHAT DISTINCT SEGMENT WE HAVE?, the SQL command will be something like this\n``` SELECT DISTINCT SEGMENT FROM [TIGER_GRAPH].[dbo].[SAMPLE_SUPERSTORE_STAGING];\n```\n\nExample 2 - TELL ME THE TOTAL PROFIT OF SEGMENT CORPORATE?\n```\nSELECT SUM(PROFIT) AS TOTAL_SALES FROM [TIGER_GRAPH].[dbo].[SAMPLE_SUPERSTORE_STAGING] WHERE SEGMENT='Corporate' GROUP BY SEGMENT;\nsql code should not have ``` in beginning or end and sql word in output\nsql code should not have ```sql or ``` in beginning or end and sql word in output\nplease make sure you are generating sql queries which is used in Microsoft SQL Server",
]

question = "total profit ?"

#Function to return result as per Gemini Text to Sql 
def get_result(question):
    Gemini_Sql_Query=get_gemini_response(question,prompt_parts_1[0])

    try:
    # Code that might cause an exception
        result =read_sql_query(Gemini_Sql_Query)
    except Exception as e:
    # Code that runs if the exception occurs
        result = "Error occured, please contact your admin!"
    return result


if __name__=="__main__":
    get_result("total profit?")


##to run this script , run below command in powershell
# python -m streamlit run "c:/Users/RANOJIT SINGH/Desktop/LLM Project/Superstore GenAI Model/main.py"