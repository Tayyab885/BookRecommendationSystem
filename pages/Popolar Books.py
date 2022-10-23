import streamlit as st
import pickle


popular_df = pickle.load(open('popular.pkl','rb'))

st.set_page_config(
    page_title="Popular Books",
    page_icon="book",
    )
st.title("Book Recommender System 📚")
st.subheader("Top Popular Books 📈")

book_name = list(popular_df['Book-Title'].values)
author = list(popular_df['Book-Author'].values)
image = list(popular_df['Image-URL-M'].values)
votes = list(popular_df['Number of Ratings'].values)
ratings = list(popular_df['Average of Ratings'].values)

no_of_books = st.number_input(label='Enter how many top books:',max_value=len(book_name))
submit = st.button("Submit")
col1, col2, col3 = st.columns(3)
i = 0
if submit and no_of_books >0:
    while i<no_of_books:
        caption = f"Name:{book_name[i]}|Author:{author[i]}|Rating:{round(ratings[i],4)}"
        col1.image(image[i],width=200,caption=caption)
        # col1.caption(f"Name:{book_name[i]}")
        # col1.caption(f"Author:{author[i]}")
        # col1.caption(f"No of Ratings:{votes[i]}")
        # col1.caption(f"Rating:{ratings[i]}")
        # col1.write(f"Name:{book_name[i]}\nAuthor:{author[i]}\nNo of Ratings:{votes[i]}\nRating:{ratings[i]}")
        i+=1
        caption = f"Name:{book_name[i]}|Author:{author[i]}|Rating:{round(ratings[i],4)}"
        col2.image(image[i],width=200,caption=caption)    
        i+=1
        caption = f"Name:{book_name[i]}|Author:{author[i]}|Rating:{round(ratings[i],4)}"
        col3.image(image[i], width=200,caption=caption)
        i+=1
else:
    st.warning("Please Enter No. of Books")
