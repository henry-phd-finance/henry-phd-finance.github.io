## Summary

- 공학·제조 맥락의 품질·공정 데이터를 운영 가능한 ML/AI 분석 시스템으로 연결하는 Data Scientist
- 삼성전자 DX부문 Machine Learning 엔지니어 / CL3 Staff Engineer. TV 공정 잠재 불량, miniLED BLU, 사용자 단말 센서 품질 로그, eCommerce risk 분석 경험
- Principal Data Scientist(Data Science Level 4 최고 인증), AI Specialist, 사내 A2 등급 발명/특허 3건, 경력 입사 전문성 면접관 20회 이상

## Core Skills

- Programming / Tools: Python, SQL, BigQuery, PyQt, Streamlit, Django, Docker, Jupyter, Superset, Git/GitHub
- ML / Statistics: XGBoost, Prophet/SARIMAX, 회귀분석, curve fitting, 통계적 유의성 검증, threshold 설계
- Data / AI: Data mart, JSON log parsing, table/column description, Question-SQL pair, LLM knowledge, Ontology/RDF/지식 그래프
- Domains: 제조·공정 품질, 제품·디바이스 품질 로그(DQA), 광학 시뮬레이션, eCommerce risk, 수요예측, 구매 분석

## Experience

### Samsung Electronics, DX Division | 2018.09 - 현재

Machine Learning 엔지니어 / CL3 Staff Engineer

- 2018.09 - 2020.12: TV사업부(VD) 개발팀 AI·Big Data Lab. TV 제조·품질·개발 데이터 분석, 공정 잠재 불량 예측, BLU 광학 시뮬레이션, 서비스 자재 수요예측
- 2021.01 - 2025.10: Big Data 센터 분석그룹. 시장규모 예측, 구매 원가 분석, 데이터 추출·분석 서비스(DCS) dashboard/mart, Smart Charging, eStore fraud, SKU impact simulation
- 2025.11 - 현재: Big Data 센터 Gen AI 개발그룹. 사용자 단말 센서 품질 로그(DQA) Data Agent, 지식 시스템/Ontology/지식 그래프, AI Specialist 과제

## Selected Projects

### 사용자 단말 센서 품질 로그(DQA) Data Agent / AI-ready Data 구축 | 2026 - 현재

- 스마트폰 사용자 단말에서 수집되는 30여개 component의 부품·센서 품질 로그 대상. spec 명세서와 실제 인입 데이터의 gap, key별 의미·단위·전처리 차이를 정리
- mart table, LLM용 table/column description, domain knowledge, Question-SQL pair, 검증 query를 설계해 AI가 로그 의미를 해석하고 SQL을 생성·검증할 수 있는 기반 구축
- 하드웨어 개발자가 자연어로 배터리 온도 구간, error log 발생 비율 등 품질 로그 분석을 수행하도록 지원. Agent 실행 파이프라인은 별도 개발부서 담당, 본인은 data/knowledge preparation과 사용 부서 key 의미 검증 담당

### TV 공정 단계 잠재 불량 예측 | 2018.11 - 2020.10

- CS 단계 이전의 공정 직후 잠재 불량 조기 스크리닝. 공정 검계측 데이터와 전세계 CS 불량·수리 이력을 serial number 기반으로 연결
- 데이터 매핑·전처리, 의미 단위 학습 데이터 구성, 초기 모델링 코드, 평가 metric 직접 구현. 희소 불량과 시기별 기본 불량률 변화를 고려한 lift 지표 제안
- Aging test 가능 물량과 라인 병목을 고려한 threshold 협의. 예측 근거 feature와 유사 과거 데이터 경향 제공, 적용 기간 중 관련 불량률 절반 수준 감소

### BLU Simulator 개발 및 검증 | 2020 - 2021

- miniLED BLU(패널 후면 Back Light Unit) 개발의 실물 패널 반복 제작·육안 평가 부담. 대상 화질 문제는 블루밍, 블록단차, uniformity
- 70여 가지 광분포 curve fitting, 광원-패널 간격별 parameter 회귀, 광원 중첩 로직 검증, 소벨 필터 기반 블록단차 지표 구현
- PyQt Windows 프로그램 배포. 실물-시뮬레이션 유사도 평균 90% 이상, 개발기간 절반 수준 단축, 재료비 70% 이상 절감

### Galaxy Smart Charging / Principal Data Scientist 인증 과제 | 2023

- 고속 충전 옵션이 수면 중 장시간 충전 상황에서도 유지되어 리튬이온 배터리 수명 관점의 비효율 발생. 충전 시작/종료 시점, 배터리 잔량, 앱 사용 로그 활용
- 디바이스별 최근 로그로 개별 수면 패턴을 파악하고, 장시간 충전 구간에서는 배터리 보호를 위해 완속 충전으로 전환하는 로직 선행 개발
- 실제 Android 코드, 설정 앱 UI, 충전 제어 로직 반영은 협업 부서 담당. 선행 개발 방향은 Galaxy Smart Charging 제품 옵션 반영으로 연결

### eStore / Trade-in Fraud Detection | 2025.07 - 2026.03

- Samsung.com eStore trade-in incentive 악용 주문의 구매 시점 탐지. order/customer/discount/chargeback 데이터 기반 fraud risk 판단
- order·customer·discount·chargeback feature 발굴, XGBoost 분류 모델 학습, 주 1회 재학습, probability distribution drift 기반 threshold 조정 설계
- 탐지 물량 제어 및 담당자 검토 dashboard 설계. 미국 판매법인(SEA) 이관 및 2026년 3월 운영 적용, 운영 precision 70%

### Additional Selected Work

- 서비스 자재 / TV 패널 수요예측: 판매·서비스 수요 패턴 기반 유사자재 매핑, trend/총량 분리 예측. BM 오차율 29.6%에서 19.1%로 개선한 시스템화 T/F 기여
- VCC Simulator: 수백만 단위 자재코드의 유사자재 단가·사양 비교용 Python/PyQt 프로그램, Python 기반 Excel 자동화 데이터 확보 프로그램 개발. 분석 시간 121분에서 11분으로 단축
- 데이터 추출·분석 서비스(DCS) Dashboard / Data Mart: 2년치 DCS SQL 약 2,000건의 CTE 구조와 반복 패턴 분석. BigQuery/Superset/Jinja dashboard query format 및 약 30개 mart table 설계
- 지식 시스템 / Ontology / 지식 그래프 PoC: 상용 LLM이 알 수 없는 사내 용어·데이터 활용 지식을 OKF 기반 Markdown/LLM Wiki에서 Ontology/RDF/지식 그래프로 구조화. 상충 definition, 오래된 문서, 모호한 질의 mapping, 데이터값-지식 규칙 불일치 탐지 예시 구현

## Certification / Recognition

- Principal Data Scientist: 삼성전자 DX부문 Data Science Level 4 최고 인증. 2023년 1년 과정 수행, 2024년 1월 인증. 인증 과제는 위 Galaxy Smart Charging이며, 2026년 6월 기준 DX부문 인증자 9명
- AI Specialist: 인재개발원 주관 사내 AI 전문가 Level 3 자격. DQA error signal과 연관 후보 key를 전기·전자·물리 지식, DQA spec, 통계 검증으로 추적하는 Expert-like Thinking Agent PoC 단독 구현
- 발명/특허: 사내 A2 등급 발명/특허 3건. 공정 잠재 불량 예측, BLU 광분포 시뮬레이션, 서비스 자재 수요예측 및 자재수급 이상감지
- Internal leadership: 경력 입사 실무진 전문성 면접관 20회 이상. Django/Docker/Jupyter 기반 사내 Data Science 학습 플랫폼 직접 개발·운영. 일 평균 약 50명, 시험 직전 일 100명 수준 방문

## Education / Research

- KAIST 경영공학부, Ph.D. in Finance / 금융공학 | 2018.08
- KAIST, 수학과 / 산업공학과 복수전공 | 3년 조기졸업
- 한국과학영재학교
- 박사학위논문: `Essays on investor herding behavior and stock market`
- 학회 발표: APAD 2017, AsianFA 2017에서 `The Disagreement with Herding, Market Bubble, and Excess Volatility` 직접 발표
