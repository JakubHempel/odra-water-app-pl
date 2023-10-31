import streamlit as st
from sentinel_imagery import get_disaster_images
from show_map import disaster_map
from visualizationparams import get_vis_params


@st.cache_data
def get_vis_params_cache():
    return get_vis_params()


@st.cache_data
def get_disaster_layers_cache():
    return get_disaster_images()


st.set_page_config(layout="wide")

cities = ["Ostrava", "Wrocław", "Frankfurt", "Szczecin"]
indexes = ["NDWI", "NDVI", "NDSI", "SABI", "CGI", "CDOM", "DOC", "Cya", "Turb"]
coords = {
    "Wrocław": [17.036, 51.111, 11],
    "Szczecin": [14.605, 53.439, 11],
    "Frankfurt": [14.496, 52.329, 11],
    "Ostrava": [18.248, 49.812, 11],
}

if not "city" in st.session_state:
    st.session_state["city"] = None

if not "index" in st.session_state:
    st.session_state["index"] = None

if not "zoom" in st.session_state:
    st.session_state["zoom"] = None

if not "layer" in st.session_state:
    st.session_state["layer"] = None

if not "disaster" in st.session_state:
    st.session_state["disaster"] = None

col1, col2 = st.columns([2, 5], gap="large")

with col1:
    st.session_state["index"] = st.selectbox(
        "Choose index",
        ("NDWI", "NDVI", "NDSI", "SABI", "CGI", "CDOM", "DOC", "Cya", "Turb"),
        index=None,
    )

    st.header("\n")

    st.session_state["disaster"] = st.radio(
        "Choose the layer you want to see",
        ["Before disaster", "During disaster", "After disaster"],
        captions=["2022-07-20", "2022-07-31", "2022-08-25"],
        index=None,
    )

with col1:
    st.header("\n")
    st.session_state["city"] = st.selectbox(
        "Choose city to zoom map view",
        ("Ostrava", "Wrocław", "Frankfurt", "Szczecin"),
        index=None,
    )

if st.session_state.disaster and st.session_state.index is not None:
    st.session_state["layer"] = get_disaster_layers_cache()[st.session_state.disaster]
    colormap = get_vis_params_cache()[st.session_state.index]

if st.session_state.city is not None:
    st.session_state["zoom"] = coords[st.session_state.city]

with col2:
    if st.session_state.index and st.session_state.layer is not None:
        disaster_map(
            st.session_state.layer,
            st.session_state.index,
            st.session_state.city,
            colormap,
            st.session_state.zoom,
        )
