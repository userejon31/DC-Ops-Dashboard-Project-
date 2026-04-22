import streamlit as st

from utils.charts import grouped_bar, line_chart
from utils.data_loader import energy_consumption, monthly_pue


st.title("02 | Energy & Efficiency")
st.caption("Unit 3: PUE monitoring, electricity profile, and optimization scenarios")

pue_df = monthly_pue()
energy_df = energy_consumption()

left, right = st.columns([1.2, 1])

with left:
    st.plotly_chart(line_chart(pue_df, "Month", "PUE", "Monthly PUE Trend"), use_container_width=True)

with right:
    st.markdown("### PUE Calculator")
    facility = st.number_input("Facility Energy (kWh)", min_value=1.0, value=1450000.0, step=10000.0)
    it_load = st.number_input("IT Equipment Energy (kWh)", min_value=1.0, value=980000.0, step=10000.0)
    pue = facility / it_load
    st.metric("Calculated PUE", f"{pue:.3f}")
    if pue <= 1.4:
        st.success("Excellent efficiency profile.")
    elif pue <= 1.6:
        st.warning("Acceptable, with room for optimization.")
    else:
        st.error("High overhead detected. Consider cooling and airflow improvements.")

st.plotly_chart(
    grouped_bar(
        energy_df,
        "Month",
        ["IT Load (MWh)", "Facility Total (MWh)"],
        "Facility vs IT Energy Consumption",
    ),
    use_container_width=True,
)
