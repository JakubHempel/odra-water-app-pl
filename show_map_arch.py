import ee
import streamlit as st
import geemap.foliumap as geemap
import gee_data as gd
from visualizationparams import get_vis_params


@st.cache_data
def get_vis_params_cache():
    return get_vis_params()


def show_map(cache_image, index_name, vis_param):
    image = cache_image
    layer_name = image.get("system:index").getInfo()

    Map = geemap.Map(layer_ctrl=True, basemap="Esri.WorldGrayCanvas")
    Map.addLayer(image.select(index_name), vis_param, f"{index_name} - {layer_name}")
    Map.add_colorbar(vis_param, label=f"{index_name} Index")
    Map.setCenter(17.036, 51.111, 11)
    Map.to_streamlit(height=850)


def disaster_map(cache_image_col, index_name, city, vis_param, zoom):
    cities = ["Wrocław", "Szczecin", "Frankfurt", "Ostrava"]
    Map = geemap.Map(basemap="Esri.WorldGrayCanvas")

    boundries_style = {
        "color": "#CD5C5C",
        "width": 1.5,
        "lineType": "solid",
        "fillColor": "96969612",
    }
    points_style = {
        "color": "000000a8",
        "pointSize": 4,
        "pointShape": "diamond",
        "width": 0.7,
        "lineType": "solid",
        "fillColor": "#FFFF99",
    }
    river_style = {
        "color": "#4682B4",
        "fillColor": "#E0FFFF",
        "width": 0.2,
        "lineType": "solid",
    }

    Map.addLayer(gd.odra.style(**river_style), {}, "Odra")

    image_collection_list = cache_image_col.toList(4)

    for city in cities:
        for index in range(0, 4):
            image = ee.Image(image_collection_list.get(index))
            date_acquired = image.get("DATE_ACQUIRED").getInfo()
            Map.addLayer(
                image.select(index_name),
                vis_param,
                f"{index_name} - {city} - {date_acquired}",
            )

    for city, layer in gd.city_boundaries.items():
        Map.addLayer(layer.style(**boundries_style), {}, city)

    for city, points in gd.pois.items():
        Map.addLayer(points.style(**points_style), {}, f"Punkty pomiarowe - {city}")

    Map.add_colorbar(vis_param, label=f"{index_name} Index")

    # Map.setCenter(*zoom)
    Map.to_streamlit(height=850)
