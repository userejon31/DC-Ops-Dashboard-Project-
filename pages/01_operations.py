import streamlit as st

from utils.data_loader import generated_at, mac_processes, operations_incidents, operations_metrics


st.title("01 | Operations Center")
st.caption("Unit 3: Administration, SLA performance, incidents, and MAC workflows")

metrics = operations_metrics()
col1, col2, col3, col4 = st.columns(4)
col1.metric("SLA Target", f"{metrics['sla_target']}%")
col2.metric("SLA Actual", f"{metrics['sla_actual']}%", "+0.03%")
col3.metric("Open Incidents", metrics["open_incidents"])
col4.metric("Critical", metrics["critical_incidents"])

st.subheader("Incident Log")
inc = operations_incidents()
st.dataframe(inc, use_container_width=True, hide_index=True)

st.download_button(
    label="Download incident log (CSV)",
    data=inc.to_csv(index=False),
    file_name="incident_log.csv",
    mime="text/csv",
)

st.subheader("MAC Process Planning")
st.dataframe(mac_processes(), use_container_width=True, hide_index=True)

st.info(f"Dataset generated: {generated_at()}")
