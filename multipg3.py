import streamlit as st

# Define a CSS style for the text area
css = """
div.stTextArea > div > div > div {
    background-color: #f5f5f5;
    padding: 0.5rem;
    border-radius: 0.25rem;
    font-family: monospace;
}
"""

# Set the page style
st.set_page_config(page_title="My Streamlit App")
st.write(f'<style>{css}</style>', unsafe_allow_html=True)

# Define functions for each page
def page1():
    # Get user input
    input_text = st.text_input("Enter some text")

    # Process input
    output_text = input_text.upper()

    # Display output
    st.write("Input Text:", input_text)
    st.write("Output Text:", output_text)
    st.text_area("Heading", value="Inside text area", height =60)

def page2():
    # Get user input
    input_num = st.number_input("Enter a number")

    # Process input
    output_num = input_num ** 2

    # Display output
    st.write("Input Number:", input_num)
    st.write("Output Number:", output_num)
    st.text_area("Heading p2", value="Inside text area p2", height =60)

# Define page navigation
PAGES = {
    "Page 1": page1,
    "Page 2": page2
}

# Create sidebar navigation
st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", list(PAGES.keys()))

# Display selected page
page = PAGES[selection]
page()
