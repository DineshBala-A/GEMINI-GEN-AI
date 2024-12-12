from dotenv import load_dotenv
from PIL import Image
import streamlit as st
import os
import google.generativeai as genai
load_dotenv()

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

model=genai.GenerativeModel('gemini-pro')

def get_gemini_responsive(input_text,image):
    if(input_text !=""):
        response=model.generate_content([input_text,image])
    else:
        response= model.generate_content([image])
    return response.text

st.set_page_config(page_title='Pro-Vision Analysis')
st.header('Gemini-Pro--Vision Application')
input_text=st.text_input('input:',key='input')


uploaded_file=st.file_uploader('choose an image...',type=['jpeg','jpg','png'])
image=''
if uploaded_file is not None:
    image=Image.open(uploaded_file)
    st.image(image,caption='uploaded image..',use_column_width=True)
submit=st.button('all about image')
if submit:
    response=get_gemini_responsive(input,image)
    st.subheader('the response is')
    st.write(response)



# from dotenv import load_dotenv
# from PIL import Image
# import streamlit as st
# import os
# import google.generativeai as genai

# load_dotenv()

# genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

# model = genai.GenerativeModel('gemini-pro')

# def get_gemini_responsive(input_text, image):
#     if input_text:
#         response = model.generate_content([input_text, image])
#     else:
#         response = model.generate_content([image])
#     return response.text

# st.set_page_config(page_title='Pro-Vision Analysis')
# st.header('Gemini-Pro--Vision Application')

# input_text = st.text_input('Input:')
# uploaded_file = st.file_uploader('Choose an image...', type=['jpeg', 'jpg', 'png'])
# image = ''

# if uploaded_file is not None:
#     image = Image.open(uploaded_file)
#     st.image(image, caption='Uploaded image...', use_column_width=True)

# submit = st.button('All about image')

# if submit:
#     response = get_gemini_responsive(input_text, image)
#     st.subheader('The response is')
#     st.write(response)
