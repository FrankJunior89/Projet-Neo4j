import numpy as np
import streamlit as st
import pandas as pd
import folium
from Utils import load_credentials , Departements
import plotly.express as px


option = st.sidebar.multiselect(
    "Selectionnez une Departement:",
    Departements
)



