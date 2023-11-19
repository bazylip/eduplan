import pandas as pd
import streamlit as st

from eduplan.config import EduplanConfig


@st.cache_data
def load_data():
    config = EduplanConfig()
    data = pd.read_csv(config.data_filepath, delimiter=",")
    cols_to_convert = [
        "subwencja_total",
        "dopłata_total",
        "subwencja_per_uczeń",
        "dopłata_per_uczeń",
        "dopłata_per_stanin",
    ]
    for col in cols_to_convert:
        data[col] = data[col].str.replace(",", ".").astype(float)
    subvention_columns = [f"P{i}" for i in range(1, 73)]
    for col in subvention_columns:
        data[col] = data[col].astype(str).str.replace(",", ".").astype(float)
    return data


data = load_data()
