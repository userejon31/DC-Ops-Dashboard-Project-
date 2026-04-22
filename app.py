import streamlit as st


st.set_page_config(
    page_title="DC-Ops Analytics Platform",
    page_icon="DC",
    layout="wide",
    initial_sidebar_state="expanded",
)


def inject_global_styles() -> None:
    st.markdown(
        """
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;800&family=JetBrains+Mono:wght@400;600&display=swap');

            :root {
                --primary: #00d4ff;
                --secondary: #ff006e;
                --accent: #ffbe0b;
                --dark-bg: #0a0e27;
                --card-bg: #1a1f3a;
                --text-primary: #e8e9f3;
                --text-secondary: #a8aac5;
                --success: #06d6a0;
                --warning: #ef476f;
            }

            .stApp {
                background: linear-gradient(135deg, var(--dark-bg) 0%, #0f1535 50%, #0a0e27 100%);
                color: var(--text-primary);
                font-family: 'Inter', sans-serif;
            }

            h1, h2, h3, h4 {
                font-family: 'Inter', sans-serif;
                color: var(--primary);
                font-weight: 700;
            }

            h1 { font-size: 2.5rem; letter-spacing: -1px; }
            h2 { font-size: 1.8rem; letter-spacing: -0.5px; }
            h3 { font-size: 1.3rem; }

            div[data-testid="stMetricValue"] {
                color: var(--accent);
                font-size: 2rem;
                font-weight: 800;
            }

            div[data-testid="stMetricLabel"] {
                color: var(--text-secondary);
                font-size: 0.85rem;
                font-weight: 600;
            }

            section[data-testid="stSidebar"] {
                background: linear-gradient(180deg, #0d1122 0%, #0f1535 100%);
                border-right: 2px solid rgba(0, 212, 255, 0.15);
            }

            .dc-card {
                background: linear-gradient(135deg, rgba(26, 31, 58, 0.8) 0%, rgba(15, 21, 53, 0.8) 100%);
                border-left: 4px solid var(--primary);
                border-radius: 8px;
                padding: 1.5rem;
                margin-bottom: 1rem;
                backdrop-filter: blur(10px);
                box-shadow: 0 4px 20px rgba(0, 212, 255, 0.1);
            }

            .metric-box {
                background: rgba(26, 31, 58, 0.6);
                border: 1px solid rgba(0, 212, 255, 0.2);
                border-radius: 8px;
                padding: 1rem;
                margin: 0.5rem 0;
            }

            .stButton > button {
                background: linear-gradient(90deg, var(--primary) 0%, #00b8cc 100%);
                color: var(--dark-bg);
                border: none;
                border-radius: 6px;
                font-weight: 600;
                padding: 0.7rem 1.5rem;
            }

            .stButton > button:hover {
                background: linear-gradient(90deg, #00e5ff 0%, #00d4ff 100%);
            }

            .info-box {
                background: rgba(6, 214, 160, 0.1);
                border-left: 4px solid var(--success);
                padding: 1rem;
                border-radius: 6px;
                margin: 1rem 0;
            }

            .warning-box {
                background: rgba(255, 0, 110, 0.1);
                border-left: 4px solid var(--secondary);
                padding: 1rem;
                border-radius: 6px;
                margin: 1rem 0;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )


inject_global_styles()

st.title("DC-Ops Analytics Platform")
st.caption("Intelligent Data Center Operations & Market Intelligence | Units 3 & 4 Analysis")

col1, col2, col3 = st.columns([1, 1.2, 1])

with col1:
    st.markdown(
        """
        <div class="dc-card">
            <h3>Platform Purpose</h3>
            <p>
                Advanced analytics for Units 3 (Operations) and Unit 4 (Market Intelligence).
                Combines real-time monitoring with strategic market insights for data center decision-making.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col2:
    st.markdown(
        """
        <div class="dc-card">
            <h3>Five Core Pages</h3>
            <p>
                <strong>Operations:</strong> SLA + incidents<br>
                <strong>Energy:</strong> PUE efficiency analysis<br>
                <strong>Security:</strong> Compliance frameworks<br>
                <strong>Market:</strong> Mexico DC landscape<br>
                <strong>Tech:</strong> Emerging solutions
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col3:
    st.markdown(
        """
        <div class="dc-card">
            <h3>Analysis Features</h3>
            <p>
                Real data from IDC, Statista, AWS, Google Cloud,
                Gartner, GitHub, and Gov.mx sources. Regional
                capacity modeling and trend projections.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.divider()

st.markdown(
    """
    <div class="info-box">
        <strong>Data Quality:</strong> All metrics sourced from publicly verifiable reports (2024-2025).
        Latest Mexico data center market analysis integrated. Navigate using the sidebar.
    </div>
    """,
    unsafe_allow_html=True,
)
