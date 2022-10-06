import streamlit
import pandas
streamlit.title('Arhaa - Lazy girl') 
streamlit.header('School Details') 
streamlit.text('Calss Jr.KG')
streamlit.text('IWS School')
streamlit.text('Pune')
streamlit.header('Breakfast Menu') 
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal') 
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
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
