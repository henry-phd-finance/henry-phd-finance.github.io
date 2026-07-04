## Summary

- Machine Learning Engineer / CL3 Staff Engineer at Samsung Electronics DX Division, with experience across manufacturing quality, device quality telemetry, eCommerce risk, procurement analytics, and AI-ready enterprise knowledge.
- Strong in framing ambiguous business and engineering problems as data problems, connecting fragmented data sources, building models/metrics/simulators, and turning analysis into reusable tools, dashboards, thresholds, and operating workflows.
- Principal Data Scientist, the highest internal Data Science Level 4 certification in Samsung Electronics DX Division; AI Specialist; contributor to three A2-grade inventions; and technical interviewer for experienced-hire data science roles.

## Core Skills

- Programming / Tools: Python, SQL, BigQuery, PyQt, Streamlit, Django, Docker, Jupyter, Superset, Git/GitHub
- ML / Statistics: XGBoost, Prophet/SARIMAX, regression, curve fitting, statistical significance testing, threshold design
- Data / AI: Data mart design, JSON log parsing, AI-ready data, Question-SQL pairs, LLM knowledge preparation, Ontology/RDF/Knowledge Graph
- Domains: Manufacturing quality, device quality telemetry, optical simulation, eCommerce risk, demand forecasting, procurement analytics

## Experience

### Samsung Electronics, DX Division | 2018.09 - Present

Machine Learning Engineer / CL3 Staff Engineer

- 2018.09 - 2020.12: AI & Big Data Lab, Visual Display Business. Worked on TV manufacturing quality, process defect prediction, BLU optical simulation, and service parts demand forecasting.
- 2021.01 - 2025.10: Analytics Group, Big Data Center. Worked on market-size forecasting, procurement cost analytics, DCS dashboard/mart, Smart Charging, eStore fraud detection, and SKU impact simulation.
- 2025.11 - Present: Gen AI Development Group, Big Data Center. Working on DQA Data Agent, enterprise knowledge systems, Ontology/Knowledge Graph PoC, and AI Specialist projects.

## Selected Projects

### DQA Data Agent / AI-ready Data | 2026 - Present

- Prepared AI-ready data for DQA component and sensor logs across 30+ smartphone components by analyzing gaps between specifications and actual incoming data, then defining key-level meanings, units, preprocessing rules, and valid ranges.
- Built mart tables, LLM-oriented table/column descriptions, domain knowledge, Question-SQL pairs, and validation queries so hardware engineers can ask natural-language questions about battery temperature ranges, average temperatures, and error-log occurrence rates without writing SQL. The Agent harness was owned by a separate development team; my scope was data/knowledge preparation and answer-quality improvement.

### eStore / Trade-in Fraud Detection | 2025.07 - 2026.03

- Developed an XGBoost classification model to detect Samsung.com eStore trade-in incentive abuse at order time, using order, customer, discount, trade-in, and chargeback data.
- Designed weekly retraining, probability-distribution-drift-based threshold adjustment, and a human review dashboard for risk operators. The model was transferred to SEA and has been in operation since March 2026, achieving 70% operational precision.

### BLU Simulator Development and Validation | 2020 - 2021

- Reframed miniLED BLU quality issues such as blooming, block mura, and uniformity from repeated physical-panel builds and visual inspection into an optical simulation and metric-design problem.
- Implemented curve fitting for 70+ light distribution profiles, parameter regression by source-panel distance, light-overlap validation, and a Sobel-filter-based block mura metric, then delivered a PyQt Windows application. The simulator achieved 90%+ average similarity against physical-panel images, reduced development time by about half, and cut material cost by more than 70%.

### Early-stage TV Process Defect Prediction | 2018.11 - 2020.10

- Connected process inspection data with global service-center defect and repair history by serial number, framing the problem as early-stage latent defect prediction immediately after manufacturing.
- Implemented data mapping, preprocessing, initial modeling code, and evaluation metrics; proposed a lift metric to account for sparse defects and time-varying base rates; and coordinated thresholds with manufacturing teams based on aging-test capacity and line bottlenecks. Related defect rates dropped to roughly half during the application period.

### Enterprise Knowledge System / Ontology / Knowledge Graph PoC | 2026 - Present

- Working on a PoC to manage internal terminology, system usage knowledge, data conventions, and tacit domain rules as OKF-based Markdown/LLM Wiki knowledge elevated into Ontology/RDF/Knowledge Graph structures.
- Designed entity/relation extraction criteria, RDF conversion rules, and baseline knowledge graphs; implemented examples for detecting conflicting definitions, stale documents, ambiguous query-to-knowledge mappings, and mismatches between knowledge rules and actual data values. The design is being extended toward guides, agents, and skills that domain owners can operate.

### Additional Selected Work

- Service parts / TV panel demand forecasting: Contributed to a systemization task force that improved benchmark error from 29.6% to 19.1% by mapping similar parts through sales/service-demand patterns and separating trend from total-volume forecasting.
- VCC Simulator: Built a Python/PyQt application for comparing specifications and unit prices across millions of material codes, plus a Python-based Excel automation tool for data acquisition; reduced analysis time from 121 minutes to 11 minutes.
- DCS Dashboard / Data Mart: Analyzed CTE structures and recurring patterns from about 2,000 DCS SQL queries over two years, then designed a BigQuery/Superset/Jinja dashboard query format and about 30 mart tables.

## Certification / Recognition

- Principal Data Scientist: Highest internal Data Science Level 4 certification in Samsung Electronics DX Division. During the 2023 one-year program, developed a Galaxy Smart Charging logic that identifies individual sleep patterns from device usage/charging logs and switches long charging windows to slow charging for battery protection. The direction was later connected to a product option; as of June 2026, there are 9 certified Principal Data Scientists in the DX Division.
- AI Specialist: Internal AI expert Level 3 certification led by Samsung's HR development organization. Independently built an Expert-like Thinking Agent PoC that traces DQA error signals to candidate keys using electrical/electronic/physics knowledge, DQA specifications, and statistical validation.
- Inventions / Patents: Contributor to three A2-grade inventions: process latent defect prediction, BLU light-distribution simulation, and service parts demand forecasting with inventory anomaly detection.
- Internal leadership: Served as a technical interviewer for 20+ experienced-hire interviews. Built and operated an internal Data Science learning platform using Django, Docker, and Jupyter, reaching about 50 daily visitors on average and about 100 daily visitors near certification exams.

## Education / Research

- KAIST, Ph.D. in Finance / Financial Engineering | 2018.08
- KAIST, B.S. in Mathematics and Industrial Engineering | early graduation in 3 years
- Korea Science Academy
- Dissertation: `Essays on investor herding behavior and stock market`
- Conference presentations: Presented `The Disagreement with Herding, Market Bubble, and Excess Volatility` at APAD 2017 and AsianFA 2017
