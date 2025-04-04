import streamlit as st
import folium
from folium.plugins import Fullscreen
from streamlit_folium import st_folium


# Función para crear el mapa
def create_map(latitude, longitude, zoom_start=15, add_marker=False):
    mapa = folium.Map(location=[latitude, longitude], zoom_start=zoom_start)

    # Agregar el marcador si es necesario
    if add_marker:
        folium.Marker([latitude, longitude], popup="¡Aquí estás!", icon=folium.Icon(color="blue")).add_to(mapa)

    # Añadir el complemento de pantalla completa
    Fullscreen(position="topright", title="Pantalla completa", titleCancel="Cancelar pantalla completa", ).add_to(mapa)

    folium.plugins.Fullscreen(
        position="topright",
        title="Expand me",
        title_cancel="Exit me",
        force_separate_button=True,
    ).add_to(m)
    return mapa


# Función para renderizar el mapa
def render_map(mapa):
    # Generar una clave única para el mapa
    map_key = f"mapa_{st.session_state['latitude']}_{st.session_state['longitude']}"

    # Renderizar el mapa con st_folium
    st_folium(mapa, width=1000, height=500, key=map_key)


# Configuración de latitud y longitud (pueden provenir de un formulario o entrada de usuario)
st.session_state['latitude'] = 40.416609  # Latitud de ejemplo (Madrid)
st.session_state['longitude'] = -3.702556  # Longitud de ejemplo (Madrid)

# Crear y renderizar el mapa
mapa = create_map(st.session_state['latitude'], st.session_state['longitude'])
render_map(mapa)
