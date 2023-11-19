import streamlit as st

from eduplan.data_loader import load_data

data = load_data()

# Sidebar - School selection
school_list = data["Nazwa szkoły / placówki"].unique()
selected_school = st.sidebar.selectbox("Wybierz Szkołę", school_list)

# Filter data
school_data = data[data["Nazwa szkoły / placówki"] == selected_school]

# Display data table
st.write("Dane dla szkoły", selected_school)
st.dataframe(school_data)

# Extracting subvention and supplement data for the pie chart
subvention_total = school_data["subwencja_total"].values[0]
supplement_total = school_data["dopłata_total"].values[0]
subvention_per_student = school_data["subwencja_per_uczeń"].values[0]
supplement_per_student = school_data["dopłata_per_uczeń"].values[0]
supplement_per_stanin = school_data["dopłata_per_stanin"].values[0]

# Pie chart
subvention_columns = [f"P{i}" for i in range(1, 73)]
# subvention_values = school_data[subvention_columns].values.flatten().tolist()

# Bar chart
subvention_values = school_data[subvention_columns].astype(float)

# Generate the bar chart using Streamlit's built-in function
bar_chart_data = school_data[subvention_columns].transpose().reset_index()
bar_chart_data.columns = ["Subvention Type", "Amount"]  # Rename columns for clarity

# Filter out rows where the Amount is not zero
bar_chart_data = bar_chart_data[bar_chart_data["Amount"] != 0]

# Plot the bar chart with non-zero values
st.bar_chart(bar_chart_data.set_index("Subvention Type"))


# Displaying additional details
st.write(f"Subwencja per Uczeń: {subvention_per_student}")
st.write(f"Dopłata Total: {supplement_total}")
st.write(f"Dopłata per Uczeń: {supplement_per_student}")
st.write(f"Dopłata per Stanin: {supplement_per_stanin}")
