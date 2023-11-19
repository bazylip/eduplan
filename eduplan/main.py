import streamlit as st
from data_loader import load_data

data = load_data()

st.sidebar.header("Eduplan - Kutno")
selected_school = st.sidebar.selectbox("Wybierz szkołę", data["Szkoła"].unique())
selected_school_full_name = data[data["Szkoła"] == selected_school][
    "Nazwa szkoły / placówki"
].iloc[0]

st.title(selected_school_full_name)

subvention_tab, details_tab, data_tab = st.tabs(["Subwencje", "Szczegóły", "Dane"])


with data_tab:
    st.header(f"Dane dla szkoły: {selected_school}")
    school_data = data[data["Szkoła"] == selected_school]
    st.table(school_data.transpose())


with subvention_tab:
    for subvention_columns, title in [
        ([f"P{i}" for i in range(1, 73)], "Liczba uczniów"),
        ([f"P{i}_subwencja_total" for i in range(1, 73)], "Kwoty"),
    ]:
        st.header(title)

        subvention_values = school_data[subvention_columns].astype(float)

        non_zero_subventions = school_data[subvention_columns].transpose()
        non_zero_subventions.columns = ["Kwota"]
        non_zero_subventions = non_zero_subventions[non_zero_subventions["Kwota"] != 0]

        non_zero_subventions = non_zero_subventions.reset_index()
        non_zero_subventions = non_zero_subventions.rename(columns={"index": "Rodzaj"})

        non_zero_subventions["Rodzaj"] = (
            non_zero_subventions["Rodzaj"].str.split("_").str[0]
        )

        st.bar_chart(non_zero_subventions.set_index("Rodzaj"))


with details_tab:
    subvention_per_student = school_data["subwencja_per_uczeń"].values[0]
    supplement_total = school_data["dopłata_total"].values[0]
    supplement_per_student = school_data["dopłata_per_uczeń"].values[0]
    supplement_per_stanin = school_data["dopłata_per_stanin"].values[0]

    st.header("Szczegóły")

    st.markdown(
        f"""
    | Opis            | Wartość |
    |------------------------|-------|
    | Subwencja per uczeń    | {subvention_per_student:,.2f} zł |
    | Łączna subwencja       | {supplement_total:,.2f} zł |
    | Dopłata per uczeń      | {supplement_per_student:,.2f} zł |
    | Dopłata per stanin     | {supplement_per_stanin:,.2f} zł |
    """
    )
