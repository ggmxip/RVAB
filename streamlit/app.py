import streamlit as st

import streamlit as st

# Set the Streamlit page configuration
st.set_page_config(
    page_title="Map Display",
    page_icon="🗺️",
    layout="wide"
)

# Title
st.title("Welcome Tourist")

# Text Input
user_input = st.text_input("Enter your name", "Your name here")

# Display user input
st.write("Hello, " + user_input + "!")

st.markdown(
    """
    <style>
    .stTextInput > div > div > input {
        width: 100%;
    }
    .stButton button {
        width: 100%;
    }
    </style>
    """,
    unsafe_allow_html=True
)

                                            # import streamlit as st
                                            # import pandas as pd
                                            # import pydeck as pdk

                                            # # Load data
                                            # data_url = "https://raw.githubusercontent.com/visgl/deck.gl-data/master/website/bart-stations.json"
                                            # data = pd.read_json(data_url)

                                            # # Set up initial map view
                                            # view_state = pdk.ViewState(
                                            #     latitude=37.7749,
                                            #     longitude=-122.4194,
                                            #     zoom=11,
                                            #     pitch=50
                                            # )

                                            # # Create a scatter plot layer
                                            # layer = pdk.Layer(
                                            #     "ScatterplotLayer",
                                            #     data,
                                            #     pickable=True,
                                            #     opacity=0.8,
                                            #     stroked=True,
                                            #     filled=True,
                                            #     radius_scale=6,
                                            #     radius_min_pixels=1,
                                            #     radius_max_pixels=100,
                                            #     line_width_min_pixels=1,
                                            #     get_position="[lon, lat]",
                                            #     get_radius="size",
                                            #     get_fill_color=[255, 140, 0],
                                            #     get_line_color=[0, 0, 0],
                                            # )

                                            # # Set the map style
                                            # map_style = pdk.map_styles.LIGHT

                                            # # Render the map
                                            # r = pdk.Deck(
                                            #     layers=[layer],
                                            #     initial_view_state=view_state,
                                            #     map_style=map_style
                                            # )

                                            # # Display the map using Streamlit
                                            # st.pydeck_chart(r)


import streamlit as st
import pydeck as pdk

# Set up initial map view for Taj Mahal
view_state = pdk.ViewState(
    latitude=27.1751,
    longitude=78.0421,
    zoom=14,
    pitch=50
)

# Create a scatter plot layer with a single point for Taj Mahal
layer = pdk.Layer(
    "ScatterplotLayer",
    data=[[78.0421, 27.1751]],
    get_position="[lon, lat]",
    get_radius=100,
    get_fill_color=[255, 0, 0],
    pickable=True
)

# Set the map style
map_style = pdk.map_styles.LIGHT

# Render the map
r = pdk.Deck(
    layers=[layer],
    initial_view_state=view_state,
    map_style=map_style
)

# Display the map using Streamlit
st.pydeck_chart(r)

# --------------------------------------------------------------

from map_display import display_map
import streamlit as st

# Set the Streamlit page configuration
st.set_page_config(
    page_title="Map Display",
    page_icon="🗺️",
    layout="wide"
)

# Get the location input from the user
location = st.text_input("Enter a location:")

# Display the map for the given location
if location:
    display_map(location)

