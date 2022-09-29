import streamlit

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



import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

# Let's put a pick list here so they can pick the fruit they want to include 

my_fruit_list = my_fruit_list.set_index('fruit')

# Display the table on the page.

streamlit.dataframe(my_fruit_list)


