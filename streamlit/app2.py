import streamlit as st

def main():
    st.title("Mapbox Mini-Map")

    st.markdown(
        """
        <html>
        <head>
            <title>Mapbox API Example</title>
            <script src="https://api.mapbox.com/mapbox-gl-js/v2.3.1/mapbox-gl.js"></script>
            <link href="https://api.mapbox.com/mapbox-gl-js/v2.3.1/mapbox-gl.css" rel="stylesheet" />
            <style>
                #map {
                    height: 400px;
                    width: 100%;
                }
            </style>
        </head>
        <body>
            <div id="map"></div>
            <script>
                mapboxgl.accessToken = 'pk.eyJ1IjoiZ2dteGlwIiwiYSI6ImNsajlzOThoaTE3OWkza3Mxbjd4bXZudngifQ.rTd0T90eJsUPDy7TFPmxbQ';

                const map = new mapboxgl.Map({
                    container: 'map',
                    style: 'mapbox://styles/mapbox/streets-v11',
                    center: [78.0421, 27.1751],
                    zoom: 15
                });

                const marker = new mapboxgl.Marker()
                    .setLngLat([78.0421, 27.1751])
                    .addTo(map);

                function openMapbox() {
                    const latitude = 27.1751;
                    const longitude = 78.0421;
                    const url = `https://www.mapbox.com/maps/@${latitude},${longitude},15z`;
                    window.open(url);
                }
            </script>
            <button onclick="openMapbox()">Open in Mapbox</button>
        </body>
        </html>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
