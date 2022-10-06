import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError
# To import the csv file
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
# Display the total table on the page.
streamlit.dataframe(my_fruit_list)
#To create the index
my_fruit_list = my_fruit_list.set_index('Fruit')
#Let's put a pick list here so they can pick the fruit they want to include 
#For provide the dropdown menu - uncomment below one
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
#To provide some default selections - uncomment below one
#streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
#Filter the table
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)
def get_fruityvice_data(fruit_choice)
streamlit.header("Fruityvice Fruit Advice!")
try
    fruit_choice = streamlit.text_input("What fruit would you like information about?")
    streamlit.write('The user entered ', fruit_choice)
  if not fruit_choice
streamlit.error("Please select a fruit to get information")
  else
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvice_normalized)

except URLError as e
streamlit.error()

fruit_choice = streamlit.text_input("What fruit would you like add?",fruit_choice)
streamlit.write('Thanks for adding ', fruit_choice)

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from pc_rivery_db.public.fruit_load_list")
my_data_row = my_cur.fetchall()
streamlit.text("The fruit load list contains:")
streamlit.dataframe(my_data_row)

my_cur.execute("insert into fruit_load_list values ('from streamlit')")

