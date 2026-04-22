import streamlit as st
import plotly.graph_objects as go
import pandas as pd
from pathlib import Path

from utils.charts import donut_chart
from utils.data_loader import deployment_models, market_overview


st.title("04 | Market Intelligence")
st.caption("Unit 4: Mexico data center market, growth dynamics, and deployment models")

# Load data: prefer CSV files, fall back to demo data
try:
    market_df = pd.read_csv("data/market_overview.csv")
except FileNotFoundError:
    market_df = market_overview()

try:
    model_df = pd.read_csv("data/deployment_models.csv")
except FileNotFoundError:
    model_df = deployment_models()

try:
    sources_df = pd.read_csv("data/sources_cited.csv")
except FileNotFoundError:
    sources_df = pd.DataFrame()

c1, c2 = st.columns([1.3, 1])

with c1:
    st.subheader("Regional Capacity and Growth")
    st.dataframe(market_df[["Region", "Capacity MW (2026)", "Growth YoY %"]], use_container_width=True, hide_index=True)

with c2:
    st.plotly_chart(donut_chart(model_df, "Model", "Adoption %", "Deployment Models in Mexico"), use_container_width=True)

st.subheader("Geographic Hotspots")
marker_sizes = [max(12, cap / 14) for cap in market_df["Capacity MW (2026)"]]

map_fig = go.Figure(
    go.Scattermap(
        lat=market_df["Latitude"],
        lon=market_df["Longitude"],
        mode="markers+text",
        text=market_df["Region"],
        textposition="top center",
        marker={
            "size": marker_sizes,
            "color": market_df["Growth YoY %"],
            "colorscale": "Viridis",
            "showscale": True,
            "colorbar": {"title": "Growth YoY %"},
        },
        customdata=market_df[["Capacity MW (2026)", "Growth YoY %"]],
        hovertemplate=(
            "<b>%{text}</b><br>Capacity: %{customdata[0]} MW"
            "<br>Growth: %{customdata[1]}%<extra></extra>"
        ),
    )
)
map_fig.update_layout(
    map={
        "style": "carto-darkmatter",
        "center": {"lat": 22.5, "lon": -101.5},
        "zoom": 4.2,
    },
    margin={"l": 0, "r": 0, "t": 0, "b": 0},
    height=500,
)
st.plotly_chart(map_fig, use_container_width=True)

st.download_button(
    label="Download market data (CSV)",
    data=market_df.to_csv(index=False),
    file_name="mexico_dc_market.csv",
    mime="text/csv",
)

st.subheader("Sources and Citations")
st.info(
    "All data sourced from publicly available reports from IDC, CBRE, Statista, AWS, Google Cloud, Gartner, and Mordor Intelligence (2024-2025)."
)
if not sources_df.empty:
    st.dataframe(sources_df, use_container_width=True, hide_index=True)
else:
    st.warning("Sources database not found. Using research-based estimates.")
