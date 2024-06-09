import streamlit as st
import pandas as pd
import pydeck as pdk

st.set_page_config(layout='wide', initial_sidebar_state='expanded')

# Load data
df = pd.read_csv('synthetic_trashbin_data_eskisehir.csv')
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Sidebar
st.sidebar.header('Dashboard')
bin_options = ['TOTAL'] + list(df['bin_id'].unique())
selected_bin_id = st.sidebar.selectbox('Select Bin ID', bin_options)

# Main
st.title('Eskişehir Trash Bin Monitoring Dashboard')

# Map
st.subheader('Map of Bin Locations')

if selected_bin_id == 'TOTAL':
    filtered_data = df
else:
    filtered_data = df[df['bin_id'] == selected_bin_id]

# Create the map
midpoint = (filtered_data['latitude'].mean(), filtered_data['longitude'].mean())
layer = pdk.Layer(
    "ScatterplotLayer",
    data=filtered_data,
    get_position="[longitude, latitude]",
    get_fill_color="[fill_level * 2, 100, 150]",
    get_radius=100,  # Reduced radius for smaller visual representation
    pickable=True,
)

tooltip = {
    "html": """
    <b>Bin ID:</b> {bin_id} <br/>
    <b>Fill Level:</b> {fill_level}% <br/>
    <b>Expected Full:</b> {expected_full} minutes <br/>
    <b>Cardboard:</b> {cardboard}% <br/>
    <b>Glass:</b> {glass}% <br/>
    <b>Metal:</b> {metal}% <br/>
    <b>Paper:</b> {paper}% <br/>
    <b>Plastic:</b> {plastic}% <br/>
    <b>Trash:</b> {trash}% <br/>
    """,
    "style": {
        "backgroundColor": "steelblue",
        "color": "white",
        "fontSize": "12px",
        "padding": "5px",
    },
}

view_state = pdk.ViewState(
    latitude=midpoint[0],
    longitude=midpoint[1],
    zoom=13,  # Adjusted zoom level for better view
    pitch=50,
)

r = pdk.Deck(
    layers=[layer],
    initial_view_state=view_state,
    tooltip=tooltip,
)

st.pydeck_chart(r)

# Display bin details in a table
st.subheader(f"Details for {selected_bin_id}")

# Display the dataframe as a table
st.dataframe(
    filtered_data[
        [
            "bin_id",
            "latitude",
            "longitude",
            "fill_level",
            "expected_full",
            "cardboard",
            "glass",
            "metal",
            "paper",
            "plastic",
            "trash",
        ]
    ]
)
