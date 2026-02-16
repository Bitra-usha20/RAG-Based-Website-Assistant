import streamlit as st
from rag import process_urls,generate_answer  #this is user defined module for RAG functions
st.title("RAG BASED WEBSITE ASSISTANT")
url1=st.sidebar.text_input("Enter the URL of the website")
url2=st.sidebar.text_input("Enter the second URL of the website")
url3=st.sidebar.text_input("Enter the third URL of the website")
# placeholder is temporary varaibe to hold st.empty()
placeholder=st.empty()
process_url_button=st.sidebar.button("process")
if process_url_button:
    urls=[url for url in (url1,url2,url3) if url!=" "]
    # if url are not present alert message sent
    if len(urls)==0:
        placeholder.text("Please Enter Atleast one url")
    else:
        # processurl divide the data into chunks
        for status in process_urls(urls):
            placeholder.text(status)
query=placeholder.text_input("Question")
if query:
    # get answer from the processed chunks 
    try:
        answer,sources=generate_answer(query)
        st.header("Answer")
        st.write(answer)
        if sources:
            st.header("sources")
            for source in sources.split("\n"):
                st.write(source)
    except RuntimeError as e:
        st.error(f"please click the url first process it: {e}")
   

    