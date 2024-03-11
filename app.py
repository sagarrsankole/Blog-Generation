import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import ctransformers

## function to get llama model
def getLlamaresponse(blog_style,input_text,no_words):
  
    ##llama2 model
    llm=ctransformers.CTransformers(model='C:\\Users\\Sagar\\Documents\\Sagar\\Guvi\\PROJECT\\Models\\llama-2-7b-chat.ggmlv3.q8_0.bin',
                      model_type='llama',
                      config={'max_new_tokens':256,
                              'temperature':0.01})

    ## propmt template
    template= """
            write a blog for {blog_style} job profile for topic {input_text} 
            within {no_words} words.
                                    """
    prompt=PromptTemplate(input_variables=["blog_style","input_text","no_words"],
                         template=template)
    
## generate the response from llama2 model
    response = llm(prompt.format(blog_style=blog_style,input_text=input_text,no_words=no_words))
    print(response)
    return response


st.set_page_config(page_title="Blog Generation",
                   layout="centered",
                   initial_sidebar_state='collapsed')


st.header("Generate my blog")

input_text=st.text_input("Enter the blog topic")

## creating two more fields

col1,col2=st.columns([5,5])

with col1:
    no_words=st.text_input('No of words')
with col2:
    blog_style=st.selectbox('writing the blog for',('Researchers','Data Scientist','Common man'),index=0)

submit=st.button("Generate")
## final response
if submit:
    st.write(getLlamaresponse(blog_style,input_text,no_words))

