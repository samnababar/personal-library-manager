import streamlit as st
import pandas as pd

# Initialize the library data
if 'library' not in st.session_state:
    st.session_state.library = pd.DataFrame(columns=['Title', 'Author', 'Year', 'Genre'])

st.title("Library Manager")

# Add a New Book
st.header("Add a New Book")
title = st.text_input("Title")
author = st.text_input("Author")
year = st.number_input("Year", min_value=1800, max_value=2100)
genre = st.text_input("Genre")

if st.button("Add Book"):
    new_book = pd.DataFrame([[title, author, year, genre]], columns=['Title', 'Author', 'Year', 'Genre'])
    st.session_state.library = pd.concat([st.session_state.library, new_book], ignore_index=True)
    st.success("Book added successfully!")

# Display the Library
st.header("Library")
st.dataframe(st.session_state.library)

# Update a Book
st.header("Update a Book")
if not st.session_state.library.empty:
    update_index = st.number_input("Enter the index of the book to update", min_value=0, max_value=len(st.session_state.library)-1)
    new_title = st.text_input("New Title")
    new_author = st.text_input("New Author")
    new_year = st.number_input("New Year", min_value=1800, max_value=2100)
    new_genre = st.text_input("New Genre")

    if st.button("Update Book"):
        if update_index >= 0 and update_index < len(st.session_state.library):
            st.session_state.library.at[update_index, 'Title'] = new_title
            st.session_state.library.at[update_index, 'Author'] = new_author
            st.session_state.library.at[update_index, 'Year'] = new_year
            st.session_state.library.at[update_index, 'Genre'] = new_genre
            st.success("Book updated successfully!")
        else:
            st.error("Invalid index!")
else:
    st.info("No books available to update.")

# Delete a Book
st.header("Delete a Book")
if not st.session_state.library.empty:
    delete_index = st.number_input("Enter the index of the book to delete", min_value=0, max_value=len(st.session_state.library)-1)

    if st.button("Delete Book"):
        if delete_index >= 0 and delete_index < len(st.session_state.library):
            st.session_state.library = st.session_state.library.drop(delete_index).reset_index(drop=True)
            st.success("Book deleted successfully!")
        else:
            st.error("Invalid index!")
else:
    st.info("No books available to delete.")

# Search for a Book
st.header("Search for a Book")
search_term = st.text_input("Enter search term (Title, Author, or Genre)")

if search_term:
    search_results = st.session_state.library[
        st.session_state.library.apply(lambda row: row.astype(str).str.contains(search_term, case=False).any(), axis=1)
    ]
    st.dataframe(search_results)
else:
    st.info("Enter a search term to find books.")