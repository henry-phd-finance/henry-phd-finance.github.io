## Summary

- 삼성전자 DX부문 Machine Learning 엔지니어 / CL3 Staff Engineer. 제조 품질, 제품 품질, DQA telemetry, eCommerce risk, 구매·자재 데이터 분석
- 문제 정의, 데이터 연결, 모델·지표·시뮬레이터 개발, threshold·dashboard·현업 적용까지 End-to-End 수행
- Principal Data Scientist(Data Science Level 4 최고 인증), AI Specialist, A2 등급 발명 3건, 경력 입사 전문성 면접관 20회 이상

## Core Skills

- Programming / Tools: Python, SQL, BigQuery, PyQt, Streamlit, Django, Docker, Jupyter, Superset, Git/GitHub
- ML / Statistics: XGBoost, Prophet/SARIMAX, 회귀분석, curve fitting, 통계적 유의성 검증, threshold 설계
- Data / AI: Data mart, JSON log parsing, AI-ready data, Question-SQL pair, LLM knowledge, Ontology/RDF/지식 그래프
- Domains: 제조 품질, 제품·디바이스 품질, DQA telemetry, 광학 시뮬레이션, eCommerce risk, 수요예측, 구매 분석

## Experience

### Samsung Electronics, DX Division | 2018.09 - 현재

Machine Learning 엔지니어 / CL3 Staff Engineer

- 2018.09 - 2020.12: VD사업부 개발팀 AI·Big Data Lab. TV 제조·품질·개발 데이터 분석, 공정 잠재 불량 예측, BLU 광학 시뮬레이션, 서비스 자재 수요예측
- 2021.01 - 2025.10: Big Data 센터 분석그룹. 시장규모 예측, 구매 원가 분석, DCS dashboard/mart, Smart Charging, eStore fraud, SKU impact simulation
- 2025.11 - 현재: Big Data 센터 Gen AI 개발그룹. DQA Data Agent, 지식 시스템/Ontology/지식 그래프, AI Specialist 과제

## Selected Projects

### DQA Data Agent / AI-ready Data 구축 | 2026 - 현재

- 스마트폰 30여개 component의 DQA 부품·센서 로그 대상. spec 명세서와 실제 인입 데이터의 gap, key별 의미·단위·전처리 차이로 하드웨어 개발자의 직접 분석 난이도 높음
- spec-actual gap 분석, key별 의미·단위·전처리·범위 정의, mart table, LLM용 table/column description, domain knowledge, Question-SQL pair, 검증 query 구축
- 하드웨어 개발자의 자연어 기반 DQA 분석 지원. Agent harness는 별도 개발부서 담당, 본인 담당 범위는 data/knowledge preparation, 사용 부서와 key 의미 검증, 답변 품질 개선

### eStore / Trade-in Fraud Detection | 2025.07 - 2026.03

- Samsung.com eStore trade-in incentive 악용 주문의 구매 시점 탐지. order/customer/discount/chargeback 데이터 기반 fraud risk 판단
- order·customer·discount·chargeback feature 발굴, XGBoost 분류 모델 학습, 주 1회 재학습, probability distribution drift 기반 threshold 조정 설계
- positive 물량 제어 및 담당자 검토 dashboard 설계. SEA 이관 및 2026년 3월 운영 적용, 운영 precision 70%

### BLU Simulator 개발 및 검증 | 2020 - 2021

- miniLED BLU 개발의 실물 패널 반복 제작·육안 평가 부담. 대상 화질 문제는 블루밍, 블록단차, uniformity
- 70여 가지 광분포 curve fitting, 광원-패널 간격별 parameter 회귀, 광원 중첩 로직 검증, 소벨 필터 기반 블록단차 지표 구현
- PyQt Windows 프로그램 배포. 실물-시뮬레이션 유사도 평균 90% 이상, 개발기간 절반 수준 단축, 재료비 70% 이상 절감

### TV 공정 단계 잠재 불량 예측 | 2018.11 - 2020.10

- CS 단계 이전의 공정 직후 잠재 불량 조기 탐지. 공정 검계측 데이터와 전세계 CS 불량·수리 이력의 serial number 기반 연결
- 데이터 매핑·전처리, 의미 단위 학습 데이터 구성, 초기 모델링 코드, 평가 metric 직접 구현. 희소 불량과 시기별 기본 불량률 변화를 고려한 lift 지표 제안
- Aging test 가능 물량과 라인 병목을 고려한 threshold 협의. 예측 근거 feature와 유사 과거 데이터 경향 제공, 적용 기간 중 관련 불량률 절반 수준 감소

### 지식 시스템 / Ontology / 지식 그래프 PoC | 2026 - 현재

- 상용 LLM이 알 수 없는 사내 용어, 시스템 사용법, 데이터 활용 지식, 부서별 convention. 임직원 질의에 필요한 사내 맥락의 구조화 필요
- OKF 기반 Markdown/LLM Wiki 지식의 Ontology/RDF/지식 그래프 관리 PoC. Entity/relation 추출 기준, RDF 변환 규칙, 기본 지식 그래프 설계
- 상충 definition, 오래된 문서, 모호한 질의 mapping, 실제 데이터값과 지식 규칙의 불일치 탐지 예시 구현. 도메인 담당자용 guide/Agent/Skill 구조로 확장 중

### Additional Selected Work

- 서비스 자재 / TV 패널 수요예측: 판매·서비스 수요 패턴 기반 유사자재 매핑, trend/총량 분리 예측. BM 오차율 29.6%에서 19.1%로 개선한 시스템화 T/F 기여
- VCC Simulator: 수백만 단위 자재코드의 유사자재 단가·사양 비교용 Python/PyQt 프로그램, Python 기반 Excel 자동화 데이터 확보 프로그램 개발. 분석 시간 121분에서 11분으로 단축
- DCS Dashboard / Data Mart: 2년치 DCS SQL 약 2,000건의 CTE 구조와 반복 패턴 분석. BigQuery/Superset/Jinja dashboard query format 및 약 30개 mart table 설계

## Certification / Recognition

- Principal Data Scientist: 삼성전자 DX부문 Data Science Level 4 최고 인증. 2023년 1년 과정에서 디바이스별 앱 사용/충전 로그 기반 수면 패턴 파악, 장시간 충전 구간 완속 충전 전환 Galaxy Smart Charging 로직 선행 개발. 제품 옵션 반영으로 연결. 2026년 6월 기준 DX부문 인증자 9명
- AI Specialist: 인재개발원 주관 사내 AI 전문가 Level 3 자격. DQA error signal과 연관 후보 key를 전기·전자·물리 지식, DQA spec, 통계 검증으로 추적하는 Expert-like Thinking Agent PoC 단독 구현
- 발명/특허: A2 등급 발명 3건. 공정 잠재 불량 예측, BLU 광분포 시뮬레이션, 서비스 자재 수요예측 및 자재수급 이상감지
- Internal leadership: 경력 입사 실무진 전문성 면접관 20회 이상. Django/Docker/Jupyter 기반 사내 Data Science 학습 플랫폼 직접 개발·운영. 일 평균 약 50명, 시험 직전 일 100명 수준 방문

## Education / Research

- KAIST 경영공학부, Ph.D. in Finance / 금융공학 | 2018.08
- KAIST, 수학과 / 산업공학과 복수전공 | 3년 조기졸업
- 한국과학영재학교
- 박사학위논문: `Essays on investor herding behavior and stock market`
- 학회 발표: APAD 2017, AsianFA 2017에서 `The Disagreement with Herding, Market Bubble, and Excess Volatility` 직접 발표
