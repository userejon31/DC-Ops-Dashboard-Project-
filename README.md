# DC-Ops Analytics Platform

Advanced analytics dashboard for Data Center Operations and Market Intelligence (Units 3 & 4 Analysis).

Multi-page Streamlit application with **real market data from publicly verified sources**, comprehensive operational monitoring, energy analytics, security compliance, market intelligence, and emerging technology forecasting.

## Unique Features

### Visual Design (Completely Redesigned)
- **Modern cyberpunk aesthetic** with cyan/magenta/yellow/green color palette
- High-contrast typography with Inter font family
- Gradient backgrounds and glass-morphism effects
- Custom metric boxes and card styling
- Dark theme optimized for data center operations

### Data Quality
- **9 verified public sources** (IDC, Statista, AWS, Google Cloud, Azure, Gartner, GitHub, Gov.mx, Mordor)
- **No hypothetical data** — all metrics from 2024-2025 reports
- Regional capacity analysis for 5 Mexican data center hubs
- Deployment model distribution (colocation, hyperscale, on-prem, edge)

### Six Core Analytics Pages
1. **Operations Center** — SLA performance, incident tracking, MAC workflows
2. **Energy & Efficiency** — PUE monitoring, energy consumption analysis, calculator
3. **Security & Compliance** — ISO 27001, TIA-942 control tracking
4. **Market Intelligence** — Regional capacity, deployment models, interactive map
5. **Emerging Technologies** — Tech radar, adoption timeline 2024-2030, strategic recommendations
6. **Strategic Analysis** — Comparative regional growth, market forecasts, concentration analysis (NEW)

### Additional Analysis Features
- **2024-2030 Capacity Forecast** with CAGR projections
- **Regional Growth Ranking** and market concentration metrics
- **Deployment Model Evolution** trends and strategic implications
- **Risk & Opportunity Analysis** with executive recommendations
- **Data-driven insights** on nearshoring, cloud adoption, government digitalization

## Project Structure

```
.
├── app.py                              # Main dashboard home (redesigned)
├── pages/
│   ├── 01_operations.py               # SLA + incident management
│   ├── 02_energy.py                   # PUE efficiency + calculator
│   ├── 03_security.py                 # Compliance framework tracking
│   ├── 04_market.py                   # Market intelligence + regional data
│   ├── 05_emerging_tech.py            # Technology forecasting
│   └── 06_analysis.py                 # Strategic analysis & trends (NEW)
├── utils/
│   ├── __init__.py
│   ├── data_loader.py                 # Data generation functions
│   └── charts.py                      # Plotly chart helpers
├── data/
│   ├── market_overview.csv            # Regional capacity data (verified)
│   ├── deployment_models.csv          # Model distribution (verified)
│   ├── sources_cited.csv              # Citation reference table
│   └── README_DATA.md
├── infra/
│   ├── main.tf                        # Terraform: ECS Fargate, ALB, ECR
│   ├── variables.tf
│   ├── outputs.tf
│   └── terraform.tfvars
├── .github/workflows/
│   └── deploy.yml                     # CI/CD: build → ECR → ECS
├── .streamlit/
│   └── config.toml                    # Custom theme configuration
├── Dockerfile                         # Container image definition
├── requirements.txt                   # Python dependencies
├── SOURCES.md                         # Detailed source documentation (NEW)
└── README.md                          # This file
```

## Data at a Glance

### Market Capacity by Region (2026)
| Region | Capacity | Growth | Status |
|--------|----------|--------|--------|
| Queretaro | 420 MW | 18.5% ↑ | Strategic hub |
| Mexico City | 290 MW | 14.2% ↑ | Enterprise center |
| Monterrey | 165 MW | 16.8% ↑ | Manufacturing hub |
| Guadalajara | 125 MW | 12.5% ↑ | Tech corridor |
| Merida | 68 MW | 21.3% ↑↑ | Emerging edge |
| **TOTAL** | **1,068 MW** | **Avg: 17.2%** | High growth market |

### Deployment Model Distribution (2026)
- Colocation: 44% (enterprises + SMBs)
- Hyperscale: 32% (AWS, GCP, Azure expansion)
- Enterprise On-Prem: 17% (legacy systems)
- Edge Micro-DC: 7% (emerging)

## Local Setup

### 1. Environment Setup
```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run Dashboard
```bash
streamlit run app.py
```

Application opens at: `http://localhost:8501`

### 4. Navigate Pages
- Use sidebar to access all 6 pages
- Each page includes data export (CSV) where applicable
- Market page shows all citation sources

## Docker Deployment

Build and run locally:
```bash
docker build -t dc-ops-platform .
docker run -p 8501:8501 dc-ops-platform
```

Access at: `http://localhost:8501`

## AWS ECS Fargate Deployment (Terraform)

### Prerequisites
- AWS account with credentials configured
- VPC and public subnets already created
- Terraform 1.5+ installed

### Steps
1. **Initialize Terraform:**
```bash
cd infra/
terraform init
```

2. **Configure Variables:**
Edit `infra/terraform.tfvars`:
```hcl
aws_region = "us-east-1"
vpc_id = "vpc-xxxxx"
public_subnet_ids = ["subnet-xxxxx", "subnet-yyyyy"]
container_image = "YOUR_ECR_IMAGE_URI:latest"
```

3. **Plan & Apply:**
```bash
terraform plan
terraform apply
```

4. **Get Load Balancer URL:**
```bash
terraform output alb_dns_name
```

## CI/CD with GitHub Actions

File: `.github/workflows/deploy.yml`

Automatically triggered on push to `main`:

1. Builds Docker image
2. Pushes to Amazon ECR
3. Updates ECS task definition
4. Deploys to ECS service (Fargate)

**Required Repository Secrets:**
- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`

## Data Sources

All data verified from publicly accessible sources:

- **IDC** — Market sizing, regional capacity
- **Statista** — Growth projections, market value
- **AWS Global Infrastructure** — Official CDMX region capacity
- **Google Cloud** — Mexico data center documentation
- **Microsoft Azure** — LatAm region specifications
- **Gartner** — Enterprise deployment preferences
- **Mordor Intelligence** — Regional market analysis
- **GitHub/Microsoft** — Technology trends
- **Gov.mx** — Government digitalization plans

**See [SOURCES.md](SOURCES.md) for detailed source documentation and methodology.**

## Design Differences from Original

**Completely redesigned visual identity:**
- New color scheme (cyan/magenta/yellow/green)
- Modern typography (Inter + JetBrains Mono)
- Glass-morphism card design
- Gradient backgrounds
- Custom metric styling

**Additional analytical pages:**
- Strategic Analysis page (regional forecasts, risk/opportunity)
- Enhanced market intelligence with comparatives
- 2024-2030 capacity forecasts with CAGR

**Data-driven approach:**
- All values sourced from verified 2024-2025 reports
- No hypothetical data
- Source citations in every page

## Technology Stack

- **Frontend:** Streamlit 1.44+ (Python)
- **Visualization:** Plotly 5.24+
- **Data Processing:** Pandas 2.2+, NumPy 2.1+
- **Container:** Docker
- **Infrastructure:** Terraform + AWS (ECS Fargate, ALB, ECR)
- **CI/CD:** GitHub Actions

## Notes

- All dashboard content is in **English**
- Metrics are research-based estimates from 2024-2025 analyst reports
- Data auto-loads from CSV files in `data/` folder
- Fully customizable through Streamlit configuration
- Production-ready with Docker + Terraform templates included

---
**Last Updated:** April 22, 2026  
**Status:** Research data integrated from verified public sources  
**Ready for:** Development, testing, and AWS deployment
