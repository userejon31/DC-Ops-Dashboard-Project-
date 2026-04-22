import streamlit as st

from utils.data_loader import compliance_checklist


st.title("03 | Security & Compliance")
st.caption("Unit 3: TIA-942, ISO 27001 controls, and physical protection practices")

df = compliance_checklist()

st.subheader("Compliance Checklist")
st.dataframe(df, use_container_width=True, hide_index=True)

status_filter = st.multiselect(
    "Filter by status",
    options=sorted(df["Status"].unique()),
    default=sorted(df["Status"].unique()),
)

filtered = df[df["Status"].isin(status_filter)]
st.subheader("Filtered Controls")
st.table(filtered)

pending = (df["Status"] == "Pending").sum()
st.metric("Pending Controls", pending)

st.markdown("### Security Notes")
st.markdown(
    """
- Maintain strict visitor escort and digital logs.
- Perform semiannual disaster recovery rehearsals.
- Enforce segmentation between OT and corporate IT zones.
- Review badge and biometric policies every quarter.
"""
)
