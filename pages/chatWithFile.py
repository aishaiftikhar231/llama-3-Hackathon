from utils.llm import generate_response, generate_file_response, generate_from_file
from utils.helper import split_text_into_chunks, read_file
from utils.common import articles_show, video_show
from app import local_css
import streamlit as st

# Apply custom CSS for a professional look
local_css("pages/style.css")

# Page navigation link
st.sidebar.markdown("## Navigation")
st.sidebar.page_link('app.py', label='Back to Home')

# File upload section with a clearer prompt
st.markdown("### Upload a Document for Analysis")
uploaded_file = st.file_uploader("Please upload a file in PDF, DOCX, or TXT format", type=["pdf", "docx", "txt"])

if uploaded_file:
    # Read and display the content of the uploaded file
    file_content = read_file(uploaded_file)
    st.markdown("### File Preview")
    st.code(file_content[:100])  # Show the first 100 characters for context

    # Provide options for interacting with the uploaded file
    choice = st.radio("Select an action",
                      ("Analyze and chat with the document", "Generate ideas based on the document"))

    if choice == "Analyze and chat with the document":
        query = st.chat_input("Ask any specific questions about the document")
        if query:
            with st.spinner("Processing your query..."):
                combined_response = ""

                # Split file content into chunks and process each chunk
                for chunk in split_text_into_chunks(file_content):
                    prompt = generate_file_response(query, chunk)
                    response_text = generate_response(prompt)
                    combined_response += response_text + "\n"

                st.markdown(f"### Response Based on Your Query")
                query = query + file_content[:100]  # Query extended with content preview

                # Display sources in expandable sections
                with st.expander("Relevant Articles"):
                    articles_show(query)

                with st.expander("Relevant Videos"):
                    video_show(query)

                st.write(combined_response)

    elif choice == "Generate ideas based on the document":
        with st.spinner("Generating content ideas..."):
            combined_response = ""

            # Split file content into chunks and generate ideas from each chunk
            for chunk in split_text_into_chunks(file_content):
                prompt = generate_from_file(chunk)
                response_text = generate_response(prompt)
                combined_response += response_text + "\n"

            st.markdown(f"### Generated Ideas Based on the Document")
            query = file_content[:100]  # Content preview for source fetching

            # Display sources in expandable sections
            with st.expander("Relevant Articles"):
                articles_show(query)

            with st.expander("Relevant Videos"):
                video_show(query)

            st.write(combined_response)
