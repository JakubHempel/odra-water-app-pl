import streamlit as st
st.set_page_config(layout="wide", page_title="Wykresy 📈 | OdrApp 💦")

import plotly.graph_objects as go
from stats import get_images_stats, get_adv_stats
from typing import Final


@st.cache_data
def get_stats_cache():
    return get_images_stats()


@st.cache_data
def get_monthly_stats_cache():
    return get_adv_stats()["monthly_stats"]


@st.cache_data
def get_yearly_stats_cache():
    return get_adv_stats()["yearly_stats"]


@st.cache_data
def get_period_stats_cache():
    return get_adv_stats()["period_stats"]


@st.cache_data
def get_disaster_stats_cache():
    return get_adv_stats()["disaster_stats"]

st.subheader("Analiza wyników wskaźników dot. jakości wody")
st.title("\n")

index_names = [
    "NDWI",
    "NDVI",
    "NDSI",
    "SABI",
    "CGI",
    "CDOM",
    "DOC",
    "Cyanobacteria",
    "Turbidity",
]
buttons_name = [
    "💦 NDWI",
    "💦 NDVI",
    "💦 NDSI",
    "🦠 SABI",
    "🦠 CGI",
    "🦠 CDOM",
    "🦠 DOC",
    "🦠 Cyanobacteria",
    "🦠 Turbidity"
]
months = ["Kwiecień", "Maj", "Czerwiec", "Lipiec", "Sierpień", "Wrzesień", "Październik"]
years = ["2018", "2019", "2020", "2021", "2022", "2023"]

if not "index" in st.session_state:
    st.session_state["index"] = "NDWI"

# Create a layout with 9 columns
columns = st.columns(9)

hover_template = "Wartość: %{y:.2f}<extra></extra>"

with st.container():
    for i, index_name in enumerate(index_names):
        if columns[i].button(buttons_name[i], help=f"{index_name} wykresy"):
            st.session_state["index"] = index_name
            with st.container():
                tab1, tab2, tab3, tab4 = st.tabs(
                    ["📆 Roczne", "📆 Miesięczne", "📆 Okresowy", "☣️ Z katastrofy"]
                )
                with tab1:
                    st.cache_data.clear()
                    st.subheader(f"{st.session_state.index} roczne wykresy")
                    rows = st.columns(3)
                    for i, year in enumerate(years):
                        with rows[i % 3]:
                            yearly_data = get_yearly_stats_cache()[
                                st.session_state.index
                            ][year]
                            fig = go.Figure()
                            fig.add_trace(
                                go.Scatter(
                                    x=yearly_data.index,
                                    y=yearly_data["Value"],
                                    mode="lines+markers",
                                    name=year,
                                    line=dict(color="#A6CEE3", width=2),
                                    marker=dict(
                                        color="#A6CEE3",
                                        line=dict(color="black", width=1),
                                    ),
                                    hovertemplate=hover_template,
                                )
                            )
                            fig.update_layout(
                                title=f"{year}",
                                yaxis_title="Wartość",
                                height=450,
                                width=510,
                            )
                            st.plotly_chart(fig)
                with tab2:
                    st.cache_data.clear()
                    st.subheader(f"{st.session_state.index} miesięczne wykresy")
                    rows = st.columns(3)
                    for i, month in enumerate(months):
                        with rows[i % 3]:
                            monthly_data = get_monthly_stats_cache()[
                                st.session_state.index
                            ][month]
                            fig = go.Figure()
                            fig.add_trace(
                                go.Scatter(
                                    x=monthly_data.index,
                                    y=monthly_data["Value"],
                                    mode="lines+markers",
                                    name=month,
                                    line=dict(color="#BBBBA9", width=2),
                                    marker=dict(
                                        color="#BBBBA9",
                                        line=dict(color="black", width=1),
                                    ),
                                    hovertemplate=hover_template,
                                )
                            )
                            fig.update_layout(
                                title=f"{month}",
                                yaxis_title="Wartość",
                                height=450,
                                width=510,
                            )
                            st.plotly_chart(fig)
                with tab3:
                    st.cache_data.clear()
                    periods_data = get_period_stats_cache()[st.session_state.index]
                    fig = go.Figure()
                    # Plot mean_df_am
                    trace1 = go.Scatter(
                        x=periods_data["spring"].index,
                        y=periods_data["spring"]["Mean"],
                        name="Kwiecień-Maj",
                        mode="lines+markers",
                        line=dict(color="#B6D79A", width=2),
                        marker=dict(color="#B6D79A", line=dict(color="black", width=1)),
                        hovertemplate=hover_template,
                    )
                    # Plot mean_df_ja
                    trace2 = go.Scatter(
                        x=periods_data["summer"].index,
                        y=periods_data["summer"]["Mean"],
                        name="Czerwiec-Sierpień",
                        mode="lines+markers",
                        line=dict(color="#FFB0B0", width=2),
                        marker=dict(
                            color="#FFB0B0", line=dict(color="black", width=1)
                        ),
                        hovertemplate=hover_template,
                    )

                    # Plot mean_df_so
                    trace3 = go.Scatter(
                        x=periods_data["autumn"].index,
                        y=periods_data["autumn"]["Mean"],
                        name="Wrzesień-Październik",
                        mode="lines+markers",
                        line=dict(color="#B0B0FF", width=2),
                        marker=dict(color="#B0B0FF", line=dict(color="black", width=1)),
                        hovertemplate=hover_template,
                    )

                    # Add all traces to the plot
                    fig.add_trace(trace1)
                    fig.add_trace(trace2)
                    fig.add_trace(trace3)

                    fig.update_layout(
                        title=f"{st.session_state.index} - średnie wartości z 3 grup miesięcy",
                        title_font=dict(family="Tahoma", size=20),
                        showlegend=True,
                        yaxis_title="Wartość",
                        height=600,
                        width=800,
                    )

                    with st.container():
                        col1, col2, col3, col4 = st.columns((4, 1, 1, 1))
                        with col1:
                            st.plotly_chart(fig)
                        with col2:
                            st.header("\n")
                            st.write("Kwiecień-Maj")
                            st.write(periods_data["spring"])
                        with col3:
                            st.header("\n")
                            st.write("Czerwiec-Sierpień")
                            st.write(periods_data["summer"])
                        with col4:
                            st.header("\n")
                            st.write("Wrzesień-Październik")
                            st.write(periods_data["autumn"])
                with tab4:
                    st.cache_data.clear()
                    disaster_data = get_disaster_stats_cache()[st.session_state.index]
                    fig = go.Figure()
                    trace = go.Scatter(
                        x=disaster_data["Month"],
                        y=disaster_data["2022"],
                        mode="lines+markers",
                        name="2022",
                        line=dict(color="#BF96FE", width=2),
                        marker=dict(color="#BF96FE", line=dict(color="black", width=1)),
                        hovertemplate=hover_template,
                    )

                    fig.add_trace(trace)

                    fig.update_layout(
                        yaxis_title="Wartość",
                        title=f"{st.session_state.index} - średnia wartość - katastrofa ekologiczna na Odrze w 2022 r.",
                        title_font=dict(family="Tahoma", size=20),
                        height=600,
                        width=800,
                    )

                    with st.container():
                        col1, col2 = st.columns((4, 2))
                        with col1:
                            st.plotly_chart(fig)
                        with col2:
                            st.header("\n")
                            st.write("Wartości z katastrofy")
                            st.write(disaster_data)
