import streamlit
streamlit.title('my parents new healthy dinner')
streamlit.header('Breakfast Menu')
streamlit.text('🥣Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗Kale, Spinach & Rocket Smoothie')
streamlit.text(' 🐔Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞avacado toast') 



streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected= streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
fruits_to_show = my_fruit_list.loc[fruits_selected]



# Display the table on the page.
streamlit.dataframe(fruits_to_show)

#new section to display fruityvice API response

streamlit.header('Fruityvice Fruit Advice!')
try:
fruit_choice=streamlit.text_input('What fruit would you like information about?')
if not fruit_choice:
  streamlit.error("please select a fruit to get information.")
  else:
    fruityvice_response=requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
    fruityvice_normalized=pandas.json_normalize(fruityvice_response.json())
    streamlit.dataframe(fruityvice_normalized)
    
    except URLError as e:
      streamlit.error()
  
  #streamlit.write('The user entered ', fruit_choice)


# take the json version of the response and normalise it

#output it in the screen as a table 



#dont run anything whilke troubleshooting

#streamlit.stop()

#import streamlit
#import pandas
#import requests
#import snowflake.connector
#from urllib.error import URLError


#my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
#my_cur = my_cnx.cursor()
#my_cur.execute("select * from PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST")
#my_data_rows = my_cur.fetchall()
#streamlit.header("The fruit load contains: ")
#streamlit.dataframe(my_data_rows)

#add_my_fruit = streamlit.text_input('What fruit would you like information about?','jackfruit')
#streamlit.write('Thanx for adding ',add_my_fruit)

#my_cur.execute("insert into PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST values('from streamlit')")


