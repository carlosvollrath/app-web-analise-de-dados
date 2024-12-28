#Importar as bibliotecas streamlit, pandas e plotly:
import streamlit as st
import pandas  as pd

#Para deixar as configurações padrão e não mudar:
st.set_page_config(layout="wide")


#Abrir os arquivos cvs no diretório:
df_reviews = pd.read_csv("data/customer reviews.csv")
df_top100_books = pd.read_csv("data/Top-100 Trending Books.csv")


# Variavel guarda onde pega os unicos textos
books = df_top100_books["book title"].unique()

#Caixa de seleção ao lado:
book = st.sidebar.selectbox("Books", books)


#Filtro ao lado:
df_book = df_top100_books[df_top100_books["book title" ]== book]
df_reviews_f = df_reviews[df_reviews["book name"] == book]



#Uma função de um valor sozinho utilizando o iloc(variavel por valiavel / coluna): |Aqui serve para iterar as caixas de texto superior|
book_title= df_book["book title"].iloc[0]
book_genre= df_book["genre"].iloc[0]
book_price = f"${df_book['book price'].iloc[0]}"
book_rating = df_book['rating'].iloc[0]
book_year= df_book['year of publication'].iloc[0]
book_author = df_book['author'].iloc[0]


#Caixas de Texto Superior:
st.title(book_title)
st.subheader(book_genre)
st.subheader(book_author)
col1,col2,col3 = st.columns(3)
col1.metric("Price", book_price)
col2.metric("Rating", book_rating)
col3.metric("Year of Publication", book_year)

#Divisor de Tela:
st.divider()


#Aqui é um laço de repetição para iterar as mensagens:
for row in df_reviews.values:
    massage = st.chat_message(f"{row[4]}")
    massage.write(f"**{row[2]}**")
    massage.write(f"{row[5]}")

df_reviews_f





