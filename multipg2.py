import streamlit as st

# Define the different pages
def page_home():
    st.title("Home Page")
    st.write("Welcome to the home page.")

def page_about():
    st.title("About Page")
    st.write("Welcome to the about page.")

# Define the page options in the left sidebar
pages = {
    "Home": page_home,
    "About": page_about,
}

# Create a function to select the page
def page_selector():
    st.sidebar.title("Select a Page")
    page = st.sidebar.radio("", tuple(pages.keys()))
    pages[page]()

# Display the selected page
page_selector()