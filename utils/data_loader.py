from __future__ import annotations

from datetime import datetime

import numpy as np
import pandas as pd


SEED = 42


def _rng() -> np.random.Generator:
    return np.random.default_rng(SEED)


def operations_metrics() -> dict:
    return {
        "sla_target": 99.95,
        "sla_actual": 99.982,
        "open_incidents": 4,
        "critical_incidents": 1,
        "mean_resolution_minutes": 36,
    }


def operations_incidents() -> pd.DataFrame:
    data = [
        ["INC-2041", "Power", "Major", "Resolved", "14 min"],
        ["INC-2049", "Cooling", "Minor", "Resolved", "23 min"],
        ["INC-2057", "Network", "Critical", "In Progress", "48 min"],
        ["INC-2063", "Security", "Major", "Monitoring", "59 min"],
    ]
    return pd.DataFrame(
        data,
        columns=["Incident ID", "Domain", "Severity", "Status", "Duration"],
    )


def mac_processes() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "Type": ["Move", "Add", "Change", "Change", "Add", "Move"],
            "Owner": [
                "Infrastructure",
                "Security",
                "Network",
                "Facilities",
                "Cloud Ops",
                "Infrastructure",
            ],
            "Ticket": ["MAC-98", "MAC-99", "MAC-100", "MAC-101", "MAC-102", "MAC-103"],
            "Window": ["02:00", "03:30", "04:00", "22:00", "01:00", "05:00"],
            "Risk": ["Low", "Medium", "High", "Medium", "Low", "Medium"],
        }
    )


def monthly_pue() -> pd.DataFrame:
    months = pd.date_range("2025-01-01", periods=12, freq="MS")
    base = np.linspace(1.62, 1.41, 12)
    noise = _rng().normal(0, 0.015, 12)
    values = np.round(base + noise, 3)
    return pd.DataFrame({"Month": months, "PUE": values})


def energy_consumption() -> pd.DataFrame:
    months = pd.date_range("2025-01-01", periods=12, freq="MS")
    it_load = np.round(np.linspace(3250, 3890, 12) + _rng().normal(0, 45, 12), 0)
    facility = np.round(it_load * np.linspace(1.58, 1.42, 12), 0)
    return pd.DataFrame(
        {
            "Month": months,
            "IT Load (MWh)": it_load,
            "Facility Total (MWh)": facility,
        }
    )


def compliance_checklist() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "Control": [
                "Access logging retention (90 days)",
                "Dual-factor badge + biometric",
                "CCTV retention policy",
                "Visitor escort protocol",
                "Disaster recovery test (semiannual)",
                "Network segmentation review",
            ],
            "Framework": ["ISO 27001", "TIA-942", "TIA-942", "ISO 27001", "ISO 27001", "ISO 27001"],
            "Status": ["Compliant", "Compliant", "Pending", "Compliant", "Pending", "Compliant"],
            "Owner": ["SecOps", "Physical Security", "Facilities", "SecOps", "Infra Ops", "NetOps"],
        }
    )


def market_overview() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "Region": ["Queretaro", "Mexico City", "Monterrey", "Guadalajara", "Merida"],
            "Capacity MW (2026)": [390, 270, 145, 110, 60],
            "Growth YoY %": [22.0, 16.3, 18.4, 14.2, 24.1],
            "Latitude": [20.5888, 19.4326, 25.6866, 20.6597, 20.9674],
            "Longitude": [-100.3899, -99.1332, -100.3161, -103.3496, -89.5926],
        }
    )


def deployment_models() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "Model": ["Colocation", "Hyperscale", "Enterprise On-Prem", "Edge Micro-DC"],
            "Adoption %": [43, 31, 17, 9],
        }
    )


def tech_radar() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "Technology": [
                "Liquid Cooling",
                "AI Ops for Predictive Maintenance",
                "Hydrogen Backup Systems",
                "DCIM + Digital Twin",
                "Small Modular Reactors Readiness",
            ],
            "Impact": [9.4, 8.8, 7.1, 8.2, 6.6],
            "Adoption": [6.7, 7.4, 3.1, 5.9, 1.8],
            "Horizon": ["2026", "2025", "2029", "2027", "2030"],
        }
    )


def adoption_timeline() -> pd.DataFrame:
    years = np.arange(2024, 2031)
    return pd.DataFrame(
        {
            "Year": years,
            "Advanced Cooling": [8, 11, 18, 30, 43, 55, 63],
            "AI Operations": [5, 13, 22, 38, 49, 58, 67],
            "Renewable Integration": [17, 23, 31, 37, 44, 51, 59],
        }
    )


def generated_at() -> str:
    return datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
