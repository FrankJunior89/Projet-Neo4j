from Utils import load_credentials
from Database import Database
import streamlit as st


credentials = load_credentials('.gitignore/credentials.json')

URL = credentials['url']
USER = credentials['user']
PASSWORD = credentials['password']

st.header("OUR DATABASE")

database = Database(URL,USER,PASSWORD)

st.write("Number of nodes")

st.write(database.number_nodes())

st.write("Number of relationships")

st.write(database.number_relationships())

st.write("List of nodes")

st.write(database.nodes())