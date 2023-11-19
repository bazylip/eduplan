import streamlit as st
from data_loader import load_data

# Set page config
# st.set_page_config(layout="wide", page_title="EDUplan")

# Load data
data = load_data()

# Sidebar for filtering
# Sidebar for filtering
st.sidebar.header("Search & Filter")
# Text input for search
search_query = st.sidebar.text_input("Search by School Name")
# Filter the school list based on the search query
filtered_school_list = [
    school
    for school in data["Nazwa szkoły / placówki"].unique()
    if search_query.lower() in school.lower()
]
# SelectBox for filtered results
selected_school = st.sidebar.selectbox("Select a School", filtered_school_list)
# Main layout
st.title(selected_school)

# Use tabs for organization
subvention_tab, details_tab, data_tab = st.tabs(["Subwencje", "Szczegóły", "Dane"])


with data_tab:
    # Overview information
    st.header(f"Dane dla szkoły: {selected_school}")
    school_data = data[data["Nazwa szkoły / placówki"] == selected_school]
    st.table(school_data.transpose())


with subvention_tab:
    # Financial details
    st.header("Struktura subwencji")
    subvention_columns = [f"P{i}" for i in range(1, 73)]

    # Assuming 'subvention_columns' is a list of column names for subvention values
    subvention_values = school_data[subvention_columns].astype(float)

    # Filter out rows where the amount is not zero and set index
    non_zero_subventions = school_data[subvention_columns].transpose()
    non_zero_subventions.columns = ["Kwota"]
    non_zero_subventions = non_zero_subventions[non_zero_subventions["Kwota"] != 0]

    # Display bar chart
    st.bar_chart(non_zero_subventions)

with details_tab:
    # Additional details and metrics
    subvention_per_student = school_data["subwencja_per_uczeń"].values[0]
    supplement_total = school_data["dopłata_total"].values[0]
    supplement_per_student = school_data["dopłata_per_uczeń"].values[0]
    supplement_per_stanin = school_data["dopłata_per_stanin"].values[0]

    # Streamlit app
    st.header("Szczegóły")

    # Custom formatting using Markdown
    st.markdown(
        f"""
    | Opis            | Wartość |
    |------------------------|-------|
    | Subwencja per uczeń    | {subvention_per_student} |
    | Łączna subwencja       | {supplement_total} |
    | Dopłata per uczeń      | {supplement_per_student} |
    | Dopłata per stanin     | {supplement_per_stanin} |
    """
    )

# Footer or additional information
# st.sidebar.markdown("### Additional Resources")
# st.sidebar.write("Include links to resources, guides, or contact info here.")

# Feedback loop (could be a form or just a button with a mailto link)
# st.sidebar.markdown("### Feedback")
# st.sidebar.write("Click below to provide feedback on the dashboard.")
# st.sidebar.button("Provide Feedback")

# Ensure caching is used for data loading and processing to improve performance
