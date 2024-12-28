#Importar as bibliotecas streamlit, pandas e plotly:
import streamlit as st
import pandas as pd
import plotly.express as px

#Para deixar as configurações padrão e não mudar:
st.set_page_config(layout="wide")

#Abrir os arquivos cvs no diretório:
df_review = pd.read_csv("data/customer reviews.csv")
df_top100_books = pd.read_csv("data/Top-100 Trending Books.csv")

# Criação do Preço Max e Min (coluna book price):
price_max = df_top100_books["book price"].max()
price_min = df_top100_books["book price"].min()

#Criação de Variavel(Prince Range) do Preço Min/Max e Slider(filtro) / sitebar(ao lado do site)
max_price = st.sidebar.slider("Price Range", price_min, price_max)

#Criação de Filtro:
df_books = df_top100_books[df_top100_books["book price"] <= max_price]

#Chama a Tabela:
st.title("Dashboard Livros Mais Vendidos Amazon")
st.subheader("Elaborado por: Carlos Vollrath")
df_books


#Criar a variavel fig e chamar o parametro bar(coluna) e px(metodo plotly), chama def_books que é a variavel dos preços max e min, passa a coluna [ano da publicação com parametro valor e counts()
fig = px.bar(df_books["year of publication"].value_counts())

# Criar a variavel fig2 e chamar o parametro histogram(histograma), chamar entre () df_books que é a variavel de preços e a coluna "book price"
fig2 = px.histogram(df_books["book price"])

#Ajustar a coluna:
col1,col2 = st.columns(2)

#Printar na tela, col1 e col2 é passado pelo parametro st(streamlit) e o metodo columns(aquidentro é 2)
#Usar o plotly_chart que é o metodo para plotagem na tela
col1.plotly_chart(fig)
col2.plotly_chart(fig2)

