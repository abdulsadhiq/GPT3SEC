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

# Get user input
user_input = st.text_input("Enter some text:")

# Process the input and get output
output = user_input.upper()

# Display the output in a text area with the CSS style
st.text_area("Output:", value=output, height=50)

st.text_area("Summary:", value=output, height=50)
