import streamlit as st
import pydeck as pdk
from pydeck.data_utils import lnglat_to_meters

def display_map(location):
    """
    Function to display a map for a given location.

    Args:
        location (str): The name of the location.
    """
    # Set up initial map view
    view_state = pdk.ViewState(
        latitude=0,
        longitude=0,
        zoom=1,
        pitch=0
    )

    # Create a scatter plot layer with a single point for the given location
    layer = pdk.Layer(
        "ScatterplotLayer",
        data=[[0, 0]],
        get_position="[lon, lat]",
        get_radius=100,
        get_fill_color=[255, 0, 0],
        pickable=True
    )

    # Set the map style
    map_style = pdk.map_styles.LIGHT

    # Geocode the location
    geocoded_location = pdk.data_utils.geocode(location)
    if geocoded_location:
        latitude = geocoded_location[0]["latitude"]
        longitude = geocoded_location[0]["longitude"]
        view_state.latitude = latitude
        view_state.longitude = longitude

        # Convert coordinates to meters
        x, y = lnglat_to_meters(longitude, latitude)
        layer.data = [[x, y]]

    # Add a dark purple gradient to the map background
    deck_template = """
    const mapCanvas = document.getElementsByClassName("deckgl-overlay")[0].children[0];
    mapCanvas.style.background = "linear-gradient(180deg, #1e003e 0%, #311f4d 100%)";
    """
    custom_layer = pdk.Deck(
        layers=[layer],
        initial_view_state=view_state,
        map_style=map_style,
        js_extensions=[{"type": "custom", "value": deck_template}]
    )

    # Display the map using Streamlit
    st.pydeck_chart(custom_layer)
