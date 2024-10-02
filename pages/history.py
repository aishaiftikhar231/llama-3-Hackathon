import streamlit as st
import json
from utils.model import get_history
from app import local_css
from utils.common import articles_show, video_show
import sqlite3

# Apply custom CSS for professional styling
local_css("pages/style.css")

# Page navigation links (without emojis)
st.sidebar.markdown("## Navigation")
st.sidebar.page_link('app.py', label='Back To Home')
st.sidebar.page_link('pages/chatWithWeb.py', label='Back To Chat With Web')

# Title for recent chats section
st.markdown("### Your Recent Chats")


def display_saved_notes(c, conn):
    """Function to fetch and display saved chat history from the database."""
    c.execute("SELECT id, query, response, articles, videos, timestamp FROM history ORDER BY timestamp DESC")
    rows = c.fetchall()

    if rows:
        # Display saved notes in a grid layout (3-column responsive)
        for i in range(0, len(rows), 3):
            cols = st.columns(3)
            for j, col in enumerate(cols):
                if i + j < len(rows):
                    row = rows[i + j]
                    note_id, query, response, articles, videos, timestamp = row
                    article_links = [article for article in json.loads(articles)]
                    video_links = [video for video in json.loads(videos)]
                    title = response[:50] + "..."  # Display the first 50 characters of the response

                    with col:
                        # Use the button to display note title and set session state for detailed view
                        if st.button(title, key=note_id):
                            st.session_state.selected_note_id = note_id
                            st.session_state.selected_note_content = {
                                "query": query,
                                "response": response,
                                "articles": article_links,
                                "videos": video_links
                            }
                            st.session_state.selected_note_timestamp = timestamp
                            st.rerun()  # Refresh the page to load the selected note
    else:
        st.markdown("No history available.")


def display_note_details():
    """Function to display detailed information of the selected note."""
    if "selected_note_id" in st.session_state:
        note_content = st.session_state.selected_note_content
        st.markdown(f"#### {note_content['query'].capitalize()}")  # Display the query as the note title

        # Display the fetched articles and videos with expanders
        with st.expander("Articles"):
            articles_show(note_content['query'])

        with st.expander("Videos"):
            video_show(note_content['query'])

        # Display the note's timestamp and AI-generated response
        st.markdown(f"**Timestamp:** {st.session_state.selected_note_timestamp}")
        st.markdown(f"**Response:** {note_content['response']}")


# Database connection setup
conn = sqlite3.connect('history.db')
c = conn.cursor()

# Display saved notes and selected note details
display_saved_notes(c, conn)
display_note_details()

# Close the database connection
conn.close()
