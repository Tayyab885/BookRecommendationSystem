import streamlit as st
import pickle
import numpy as np

pt = pickle.load(open('pt.pkl','rb'))
books = pickle.load(open('books.pkl','rb'))
similarity_score = pickle.load(open('similarity_score.pkl','rb'))

st.set_page_config(
    page_title="Home",
    page_icon="book",
    )
st.title("Book Recommender System 📚")
st.subheader("Popularity Based Recommendations 📈")
st.sidebar.success("Please select the Page")

def recommend(book_name):
    #fetching index
    index = np.where(pt.index==book_name)[0][0]
    similar_items = sorted(list(enumerate(similarity_score[index])),key=lambda x: x[1],reverse=True)[1:4]
    data = []
    for i in similar_items:
        item = []
        #print(i[0]) # It will return the index of similar books
        #print(pt.index[i[0]]) # it will return the names of similar books
        temp_df = books[books['Book-Title'] == pt.index[i[0]]]
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))
        
        data.append(item)
    return data



input = st.text_input(label='Enter Book Name:',placeholder='Please enter name of a book..')
button = st.button(label="Submit")

col1, col2, col3 = st.columns(3)
if button:
    result = recommend(input)
    book_name1 = result[0][0]
    author1 = result[0][1]
    image1 = result[0][2]
    caption1 = f"Name:{book_name1} | Author:{author1}"
    col1.image(image1,width=200,caption=caption1)
    
    book_name2 = result[1][0]
    author2 = result[1][1]
    image2 = result[1][2]
    caption2 = f"Name:{book_name2} | Author:{author2}"
    col2.image(image2,width=200,caption=caption2)
    
    book_name3 = result[2][0]
    author3 = result[2][1]
    image3 = result[2][2]
    caption3 = f"Name:{book_name3} | Author:{author3}"
    col3.image(image3,width=200,caption=caption3)