import streamlit as st 
from Our_LLM import generate_res_name_and_menu
# set title 
st.title('Restaurant Generator') 

# sidebar with box chossing resaurant name 
cusinie =st.sidebar.selectbox("Pick cuisine" , ('Moroccan' ,'Chinese', 'Indian', 'Italian', 'Japanese', 'Mexican', 'Thai' , 'Vietnamese', 'American'  ))


if cusinie : 
    response = generate_res_name_and_menu(cusinie)
    st.header(response['restaurant_name'])
    
    menu_item = response['menu_items'].split(',')
    st.header("Menu Items")
    for item in menu_item :
        st.write("-", item)