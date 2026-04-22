import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime

st.title("06 | Strategic Analysis & Trends")
st.caption("Comparative regional analysis, market forecasts, and strategic recommendations")

# Load data
try:
    market_df = pd.read_csv("data/market_overview.csv")
except FileNotFoundError:
    st.error("Market data file not found. Please ensure data/market_overview.csv exists.")
    st.stop()

try:
    model_df = pd.read_csv("data/deployment_models.csv")
except FileNotFoundError:
    model_df = pd.DataFrame()

st.subheader("Regional Growth Analysis")

# Create growth comparison chart
fig_growth = go.Figure()

fig_growth.add_trace(go.Bar(
    x=market_df["Region"],
    y=market_df["Growth YoY %"],
    marker=dict(
        color=market_df["Growth YoY %"],
        colorscale="Turbo",
        showscale=True,
        colorbar=dict(title="Growth %")
    ),
    text=market_df["Growth YoY %"],
    textposition="outside"
))

fig_growth.update_layout(
    title="YoY Growth Rate by Region (2024-2026)",
    xaxis_title="Region",
    yaxis_title="Growth YoY %",
    template="plotly_dark",
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    height=400
)

st.plotly_chart(fig_growth, use_container_width=True)

# Regional insights
col1, col2 = st.columns(2)

with col1:
    st.markdown("### Fastest Growing Regions")
    top_growth = market_df.nlargest(3, "Growth YoY %")[["Region", "Growth YoY %", "Notes"]]
    for idx, row in top_growth.iterrows():
        st.markdown(f"**{row['Region']}** — {row['Growth YoY %']}% YoY  \n*{row['Notes']}*")

with col2:
    st.markdown("### Largest Capacity Markets")
    top_cap = market_df.nlargest(3, "Capacity MW (2026)")[["Region", "Capacity MW (2026)"]]
    for idx, row in top_cap.iterrows():
        st.metric(row["Region"], f"{row['Capacity MW (2026)']} MW")

st.divider()

st.subheader("Market Concentration Analysis")

# Market share pie
fig_share = go.Figure(
    go.Pie(
        labels=market_df["Region"],
        values=market_df["Capacity MW (2026)"],
        hole=0.4,
        marker=dict(colors=["#00d4ff", "#ff006e", "#ffbe0b", "#06d6a0", "#8338ec"])
    )
)

fig_share.update_layout(
    title="Data Center Capacity Distribution by Region (2026)",
    template="plotly_dark",
    paper_bgcolor="rgba(0,0,0,0)",
    height=450
)

st.plotly_chart(fig_share, use_container_width=True)

# Market concentration metrics
total_capacity = market_df["Capacity MW (2026)"].sum()
top_2_capacity = market_df.nlargest(2, "Capacity MW (2026)")["Capacity MW (2026)"].sum()
top_2_share = (top_2_capacity / total_capacity) * 100

col1, col2, col3 = st.columns(3)
col1.metric("Total Market Capacity", f"{total_capacity} MW")
col2.metric("Top 2 Regions Share", f"{top_2_share:.1f}%")
col3.metric("Number of Regions", len(market_df))

st.divider()

st.subheader("2024-2030 Capacity Forecast")

# Forecast projection
forecast_years = pd.DataFrame({
    "Year": [2024, 2025, 2026, 2027, 2028, 2029, 2030],
    "Projected Capacity (MW)": [850, 920, 1068, 1220, 1380, 1550, 1720],
    "CAGR": [8.2, 8.5, 16.1, 14.2, 13.1, 12.3, 11.0]
})

fig_forecast = go.Figure()

fig_forecast.add_trace(go.Scatter(
    x=forecast_years["Year"],
    y=forecast_years["Projected Capacity (MW)"],
    mode="lines+markers+text",
    name="Projected Capacity",
    line=dict(color="#00d4ff", width=4),
    marker=dict(size=10, symbol="diamond"),
    text=forecast_years["Projected Capacity (MW)"],
    textposition="top center",
    fill="tozeroy",
    fillcolor="rgba(0, 212, 255, 0.1)"
))

fig_forecast.update_layout(
    title="Mexico Data Center Market Capacity Forecast (2024-2030)",
    xaxis_title="Year",
    yaxis_title="Total Capacity (MW)",
    template="plotly_dark",
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    height=450,
    hovermode="x unified"
)

st.plotly_chart(fig_forecast, use_container_width=True)

st.markdown("""
**Key Insights:**
- **CAGR 2024-2026:** 12.2% — Market expanding significantly
- **Projected 2030:** 1,720 MW (61% growth from 2026)
- **Primary Drivers:** Nearshoring, cloud adoption, government digitalization
""")

st.divider()

st.subheader("Deployment Model Evolution")

if not model_df.empty:
    col1, col2 = st.columns([1.2, 1])
    
    with col1:
        fig_models = go.Figure(
            go.Bar(
                x=model_df["Model"],
                y=model_df["Adoption %"],
                marker=dict(color=["#00d4ff", "#ff006e", "#ffbe0b", "#06d6a0"]),
                text=model_df["Adoption %"],
                textposition="outside"
            )
        )
        fig_models.update_layout(
            title="Current Deployment Model Distribution (2026)",
            template="plotly_dark",
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            height=400
        )
        st.plotly_chart(fig_models, use_container_width=True)
    
    with col2:
        st.markdown("### Model Trends")
        st.markdown("""
        **Growing:**
        - Hyperscale (+8% by 2030)
        - Edge Micro-DC (+6%)
        
        **Declining:**
        - On-Premises (-4%)
        - Colocation (-2%)
        
        **Implication:** Market shifting to cloud-native + edge architectures
        """)

st.divider()

st.subheader("Strategic Recommendations")

recommendations = pd.DataFrame({
    "Priority": ["HIGH", "HIGH", "MEDIUM", "MEDIUM", "LOW"],
    "Initiative": [
        "Accelerate hyperscale partnerships",
        "Invest in renewable energy infrastructure",
        "Develop edge computing capabilities",
        "Modernize compliance monitoring",
        "Explore H2 backup technologies"
    ],
    "Timeline": ["2026-2027", "2026-2028", "2027-2029", "2026 (ongoing)", "2029-2030"],
    "Impact": ["Growth acceleration", "Cost reduction + sustainability", "Market differentiation", "Risk mitigation", "Long-term resilience"]
})

st.dataframe(recommendations, use_container_width=True, hide_index=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    #### Market Opportunity
    - **Queretaro + Mexico City** = 56% of capacity
    - **Average growth 17.2%** exceeds global DC average (7%)
    - **Edge segment** = highest growth opportunity
    """)

with col2:
    st.markdown("""
    #### Key Risks
    - Heavy concentration in 2 regions
    - Energy infrastructure constraints
    - Regulatory compliance complexity
    - Competition from hyperscalers
    """)

st.info(f"Analysis updated: {datetime.now().strftime('%Y-%m-%d %H:%M UTC')}")
