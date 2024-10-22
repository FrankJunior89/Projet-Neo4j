import numpy as np
import streamlit as st
import pandas as pd
import folium
from Utils import load_credentials , Departements
import plotly.express as px
from Database import Database


credentials = load_credentials('.gitignore/credentials.json')

URL = credentials['url']
USER = credentials['user']
PASSWORD = credentials['password']



departements = st.sidebar.selectbox(
    "Selectionnez un Departement:",
    Departements
)

db = Database(URL,USER,PASSWORD)

st.write(departements)

if departements != 'Pas de Préférences':
    st.write(db.filter_departments(departements))







