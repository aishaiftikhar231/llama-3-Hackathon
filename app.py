import streamlit as st

# Set page configuration
st.set_page_config(page_title="AI Research Assistant", initial_sidebar_state="collapsed")

# Function to load custom CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Load custom CSS
local_css("pages/style.css")

# Main function
def main():
    # Main title and subtitle
    st.markdown('<div class="main-title">LLaMA Genius</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="subheader">A Powerful AI Assistant for Research, powered by <a href="https://github.com/aishaiftikhar231" target="_blank">Aisha Iftikhar</a></div>',
        unsafe_allow_html=True
    )

    # Display options to navigate between features
    st.markdown('#### Select a Feature')
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button('Chat With File'):
            st.switch_page("pages/chatWithFile.py")

    with col2:
        if st.button('Chat With Web'):
            st.switch_page("pages/chatWithWeb.py")

    with col3:
        if st.button('See History'):
            st.switch_page("pages/history.py")

    # Overview section with improved descriptions
    st.markdown("""
        <div class="section-title">Overview of Features</div>
        <p>Welcome to LLaMA Genius, a cutting-edge AI research assistant designed to make your research process faster, smarter, and more efficient. With powerful capabilities to analyze documents, search the web, and provide you with relevant resources, LLaMA Genius is your one-stop solution for academic and professional research needs.</p>

        <div class="section-title">1. Chat with File</div>
        <p>The 'Chat with File' feature allows you to upload documents in PDF, DOCX, or TXT formats. Once uploaded, the assistant will extract the content, break it down into manageable parts, and enable you to interact with the file. You can ask questions or request insights, and the assistant will respond based on the file's content. Alternatively, you can choose to generate ideas or summaries based on the document's information.</p>

        <div class="section-title">2. Chat with Web</div>
        <p>In the 'Chat with Web' feature, you can input any query, and the AI will generate insightful responses based on its deep understanding of various topics. It also fetches related articles and YouTube videos, providing you with a wealth of information from credible sources. Whether you're conducting research or seeking inspiration, this feature offers a comprehensive view of the information landscape.</p>

        <div class="section-title">How to Use</div>
        <p>To get started with LLaMA Genius, follow these simple steps:</p>
        <ol>
            <li><b>Chat with File:</b> Upload a file, choose whether to chat with the content or generate ideas, and receive AI-driven insights based on the document.</li>
            <li><b>Chat with Web:</b> Input your query, and let the assistant generate responses along with relevant articles and YouTube videos.</li>
        </ol>
    """, unsafe_allow_html=True)

# Run the main function
if __name__ == "__main__":
    main()

