## Summary

- Data Scientist focused on connecting engineering and manufacturing data to operational ML/AI systems for quality and process decisions.
- Machine Learning Engineer / CL3 Staff Engineer at Samsung Electronics DX Division, with experience in TV process defect prediction, miniLED Back Light Unit (BLU) simulation, device quality sensor logs, and eCommerce risk.
- Strong in framing ambiguous business and engineering problems as data problems, connecting fragmented data sources, building models/metrics/simulators, and turning analysis into reusable tools, dashboards, thresholds, and operating workflows.
- Principal Data Scientist (Samsung DX Division's top internal Data Science Level 4 certification), AI Specialist, contributor to three A2-grade internal invention/patent disclosures, and technical interviewer for experienced-hire data science roles.

## Core Skills

- Programming / Tools: Python, SQL, BigQuery, PyQt, Streamlit, Django, Docker, Jupyter, Superset, Git/GitHub
- ML / Statistics: XGBoost, Prophet/SARIMAX, regression, curve fitting, statistical significance testing, threshold design
- Data / AI: Data mart design, JSON log parsing, table/column descriptions, Question-SQL pairs, LLM knowledge preparation, Ontology/RDF/Knowledge Graph
- Domains: Manufacturing quality, device quality telemetry, optical simulation, eCommerce risk, demand forecasting, procurement analytics

## Experience

### Samsung Electronics, DX Division | 2018.09 - Present

Machine Learning Engineer / CL3 Staff Engineer

- 2018.09 - 2020.12: AI & Big Data Lab, Visual Display (TV) Business. Worked on TV manufacturing quality, process defect prediction, Back Light Unit (BLU) optical simulation, and service parts demand forecasting.
- 2021.01 - 2025.10: Analytics Group, Big Data Center. Worked on market-size forecasting, procurement cost analytics, internal Data Consulting Service (DCS) dashboard/mart, Smart Charging, eStore fraud detection, and SKU impact simulation.
- 2025.11 - Present: Gen AI Development Group, Big Data Center. Working on Data Agent for device quality sensor logs (DQA), enterprise knowledge systems, Ontology/Knowledge Graph PoC, and AI Specialist projects.

## Selected Projects

### Device Quality Sensor Log (DQA) Data Agent / AI-ready Data | 2026 - Present

- Prepared AI-ready data for component and sensor quality logs collected from user smartphones across 30+ components by analyzing specification-to-actual gaps and defining key-level meanings, units, preprocessing rules, and valid ranges.
- Built mart tables, LLM-oriented table/column descriptions, domain knowledge, Question-SQL pairs, and validation queries so AI can interpret log semantics and generate/validate SQL.
- Enabled hardware engineers to analyze battery-temperature ranges, error-log occurrence rates, and other quality signals in natural language. Another team owned the agent execution pipeline; my scope was data/knowledge preparation, key-meaning validation with client teams, and answer-quality improvement.

### Early-stage TV Process Defect Prediction | 2018.11 - 2020.10

- Connected process inspection data with global service-center defect and repair history by serial number, framing the problem as early-stage latent defect screening immediately after manufacturing.
- Implemented data mapping, preprocessing, initial modeling code, and evaluation metrics; proposed a lift metric to account for sparse defects and time-varying base rates.
- Coordinated thresholds with manufacturing teams based on aging-test capacity and line bottlenecks, and provided predicted drivers and similar historical cases. Related defect rates dropped to roughly half during the application period.

### BLU Simulator Development and Validation | 2020 - 2021

- Reframed miniLED Back Light Unit (BLU) quality issues such as blooming, block mura, and uniformity from repeated physical-panel builds and visual inspection into an optical simulation and metric-design problem.
- Implemented curve fitting for 70+ light-distribution curves, parameter regression by source-panel distance, light-overlap validation, and a Sobel-filter-based block mura metric.
- Delivered a PyQt Windows application. The simulator achieved 90%+ average similarity to physical-panel images, reduced development time by about half, and cut material cost by more than 70%.

### Galaxy Smart Charging / Principal Data Scientist Certification Project | 2023

- Addressed battery-life inefficiency caused by fast charging continuing during long overnight charging windows, using charging start/end times, battery levels, and app-usage logs.
- Developed logic to infer individual sleep windows from recent device-level logs and switch long charging sessions to battery-protective slow charging.
- Partner teams owned Android implementation, Settings UI, charging-control integration, and product testing. My upstream logic contributed to a Galaxy Smart Charging product option.

### eStore / Trade-in Fraud Detection | 2025.07 - 2026.03

- Developed an XGBoost classification model to detect Samsung.com eStore trade-in incentive abuse at order time, using order, customer, discount, trade-in, and chargeback data.
- Designed weekly retraining, probability-distribution-drift-based threshold adjustment, and a human review dashboard for risk operators. The model was transferred to the U.S. sales subsidiary (SEA) and has been in operation since March 2026, achieving 70% operational precision.

### Additional Selected Work

- Service parts / TV panel demand forecasting: Contributed to a systemization task force that improved benchmark error from 29.6% to 19.1% by mapping similar parts through sales/service-demand patterns and separating trend from total-volume forecasting.
- VCC Simulator: Built a Python/PyQt application for comparing specifications and unit prices across millions of material codes, plus a Python-based Excel automation tool for data acquisition; reduced analysis time from 121 minutes to 11 minutes.
- Data Consulting Service (DCS) Dashboard / Data Mart: Analyzed CTE structures and recurring patterns from about 2,000 SQL queries over two years, then designed a BigQuery/Superset/Jinja dashboard query format and about 30 mart tables.
- Enterprise Knowledge System / Ontology / Knowledge Graph PoC: Structured internal terminology and data-usage knowledge that commercial LLMs cannot know into OKF-based Markdown/LLM Wiki, Ontology/RDF, and Knowledge Graph formats; implemented examples for conflicting definitions, stale documents, ambiguous query mappings, and mismatches between data values and knowledge rules.

## Certification / Recognition

- Principal Data Scientist: Samsung DX Division's top internal Data Science Level 4 certification. Completed the 2023 one-year program and was certified in January 2024; the certification project was the Galaxy Smart Charging work listed above. As of June 2026, there are 9 certified Principal Data Scientists in the DX Division.
- AI Specialist: Internal AI expert Level 3 certification led by Samsung's HR development organization. Independently built an Expert-like Thinking Agent PoC that traces DQA error signals to candidate keys using electrical/electronic/physics knowledge, DQA specifications, and statistical validation.
- Inventions / Patents: Contributor to three A2-grade internal invention/patent disclosures: process latent defect prediction, BLU light-distribution simulation, and service parts demand forecasting with inventory anomaly detection.
- Internal leadership: Served as a technical interviewer for 20+ experienced-hire interviews. Built and operated an internal Data Science learning platform using Django, Docker, and Jupyter, reaching about 50 daily visitors on average and about 100 daily visitors near certification exams.

## Education / Research

- KAIST, Ph.D. in Finance / Financial Engineering | 2018.08
- KAIST, B.S. in Mathematics and Industrial Engineering | early graduation in 3 years
- Korea Science Academy
- Dissertation: `Essays on investor herding behavior and stock market`
- Conference presentations: Presented `The Disagreement with Herding, Market Bubble, and Excess Volatility` at APAD 2017 and AsianFA 2017
