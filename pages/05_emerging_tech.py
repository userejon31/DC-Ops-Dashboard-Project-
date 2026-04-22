import streamlit as st

from utils.charts import grouped_bar, scatter_radar
from utils.data_loader import adoption_timeline, tech_radar


st.title("05 | Emerging Technologies")
st.caption("Unit 4: technology radar, adoption timeline 2024-2030, and strategic recommendations")

radar_df = tech_radar()
timeline_df = adoption_timeline()

st.plotly_chart(
    scatter_radar(
        radar_df,
        "Adoption",
        "Impact",
        "Horizon",
        "Technology Radar: Adoption vs Strategic Impact",
    ),
    use_container_width=True,
)

st.plotly_chart(
    grouped_bar(
        timeline_df,
        "Year",
        ["Advanced Cooling", "AI Operations", "Renewable Integration"],
        "Adoption Timeline (Index) 2024-2030",
    ),
    use_container_width=True,
)

st.subheader("Strategic Recommendations")
st.markdown(
    """
1. Prioritize AI Ops in 2026 to reduce incident response time and improve uptime.
2. Scale liquid cooling pilots in high-density halls before the 2027 capacity wave.
3. Expand renewable sourcing contracts to protect long-term energy costs.
4. Start feasibility reviews for alternative backup technologies by 2028.
"""
)
