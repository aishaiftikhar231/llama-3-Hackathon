import streamlit as st
from utils.llm import generate_response, generate_prompt
from utils.common import articles_show, video_show
from utils.helper import fetch_articles, fetch_videos
from utils.model import init_db, add_history
from app import local_css

# Initialize the database
init_db()

# Apply custom CSS styles for a clean and professional look
local_css("pages/style.css")

# Additional CSS for fonts and styles
st.markdown("""
    <style>
        body, h1, h2, h3, h4, h5, h6, p {
            font-family: 'Arial', sans-serif;
            color: #333333;
        }
        .css-1d391kg {
            font-size: 18px !important;
        }
        .stButton button {
            background-color: #4CAF50;
            color: white;
            border: none;
            padding: 10px 20px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            transition-duration: 0.4s;
            cursor: pointer;
        }
        .stButton button:hover {
            background-color: #45a049;
        }
        .st-expander {
            border: 1px solid #ddd;
            padding: 10px;
        }
        .st-expander p {
            margin-bottom: 5px;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar navigation links without emojis
st.sidebar.markdown("## Navigation")
st.sidebar.page_link('app.py', label='Home')
st.sidebar.page_link('pages/history.py', label='View History')

# Title and description with a more formal tone
st.markdown("<h1 style='text-align: center; color: #333;'>AI Research Assistant</h1>", unsafe_allow_html=True)


# Input field for user query
query = st.chat_input("Enter your query or research topic...", key="user_query")

if query:
    # Display the user query
    st.markdown(f"<h4 style='color: #333;'>Your Query: {query}</h4>", unsafe_allow_html=True)

    # Loading spinner while processing the query
    with st.spinner("Processing your request..."):
        prompt = generate_prompt(query)
        response_text = generate_response(prompt)

        # Fetch articles and videos based on the query
        articles = fetch_articles(query)
        video = fetch_videos(query)

        # Save the query history to the database
        add_history(query, response_text, articles, video)

        # Display the fetched information
        st.markdown("### Relevant Articles")
        with st.expander('View Articles'):
            articles_show(query)

        st.markdown("### Related Videos")
        with st.expander('View Videos'):
            video_show(query)

        # Display the generated AI response
        st.markdown("### AI Response")
        st.write(response_text)

# Footer with a minimalist design
st.markdown("<hr style='border: 1px solid #ddd;'/>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #aaa;'>Powered by AI Research Tools</p>", unsafe_allow_html=True)
