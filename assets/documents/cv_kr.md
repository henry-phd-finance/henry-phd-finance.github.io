## Professional Summary

- 삼성전자 DX부문에서 제조, 제품, 고객, 구매, 리스크, 지식 시스템 데이터를 다뤄온 Data Scientist입니다. 문제 정의, 데이터 연결, 모델/지표/시뮬레이터 개발, 현업 적용과 운영 셋업까지 수행한 경험을 보유하고 있습니다.
- 공정 검계측 데이터, DQA 부품/센서 로그, 광분포 이미지, 주문/chargeback 로그, 구매/자재 데이터처럼 과학·공학·운영 맥락이 강한 데이터를 다뤄왔습니다. 단순 분석 보고서보다 현업이 반복적으로 쓸 수 있는 모델, mart, dashboard, simulator, Agent용 지식 기반으로 남기는 방식에 강점이 있습니다.
- 삼성전자 DX부문 Data Science Level 4 최고 인증인 Principal Data Scientist를 취득했으며, 인증 과제에서는 Galaxy Smart Charging 로직을 선행 개발해 제품 옵션 반영으로 이어졌습니다. AI Specialist 자격, A2 등급 발명 3건, 경력 입사 전문성 면접관 20회 이상, 사내 Data Science 학습 플랫폼 개발·운영 경험도 보유하고 있습니다.

## Core Skills

- Programming / Tools: Python, SQL, BigQuery, PyQt, Streamlit, Django, Docker, Jupyter, Superset, Git/GitHub
- ML / Statistics: Supervised Learning, XGBoost, Time-series Forecasting, Prophet/SARIMAX, Regression, Curve Fitting, Statistical Significance Testing, Thresholding
- Data / AI: Data Mart Design, JSON Log Parsing, AI-ready Data, Question-SQL Pair, LLM Knowledge Preparation, Agent Pipeline PoC, Ontology/RDF/Knowledge Graph, SPARQL
- Domains: Manufacturing Quality, Product/Device Quality, DQA Telemetry, Optical Simulation, eCommerce Risk, Demand Forecasting, Procurement Analytics

## Professional Experience

### Samsung Electronics, DX Division

- 기간: 2018.09.01 ~ 현재
- 공식 직무: Machine Learning 엔지니어
- 직급: CL3 / Staff Engineer
- 주요 업무: 제조/제품/고객/구매/리스크/지식 시스템 데이터 분석, 모델링, 시뮬레이션, AI-ready data 구축

경력 흐름:

- 2018.09 ~ 2020.12 | VD사업부 개발팀 AI·Big Data Lab: TV 공정 잠재 불량 예측, miniLED BLU 시뮬레이션, 서비스 자재 수요예측 등 제조·품질·개발 데이터 분석 수행
- 2021.01 ~ 2025.10 | Big Data 센터 분석그룹: 시장규모 예측, 구매 원가 분석, DCS dashboard/mart, Smart Charging, eStore fraud, SKU impact simulation 수행
- 2025.11 ~ 현재 | Big Data 센터 Gen AI 개발그룹: DQA Data Agent, 지식 시스템/Ontology/지식 그래프, AI Specialist 과제 수행

경력 참고:

- 2024.04 ~ 2024.11: 육아휴직

## Selected Projects

### DQA Data Agent / AI-ready Data 구축

- 기간: 2026년 현재 진행 중
- 데이터/도메인: 사용자 스마트폰 기기에서 측정되어 서버로 인입되는 DQA 부품/센서 계측 로그. 디바이스 quality 파악, 다음 라인업 spec 결정, 불량 디바이스 log 분석 등에 활용되는 데이터.
- 문제: DQA raw 데이터는 JSON 문자열 형태로 하루 수십억~수백억 row가 쌓이고, key별 의미·단위·전처리·정상 범위가 하드웨어 도메인 지식에 강하게 의존합니다. Spec 명세서와 실제 인입 데이터 사이에도 gap이 있어 하드웨어 개발자가 SQL 없이 직접 분석하기 어려웠습니다.
- 역할: spec 명세서와 실제 인입 데이터 gap 분석, key별 단위/의미/전처리/범위 정의, mart table 설계/생성, LLM용 table/column description 작성, prompt 주입용 domain knowledge 작성, Question-SQL pair 작성, SQL 검증용 기준 query 작성, 사용자 질문 유형 정의, Agent 답변 품질 test/개선, client 부서와 key 의미 검증을 수행했습니다.
- 역할 경계: SQL 생성/검증/실행/해석 Agent harness와 pipeline은 다른 개발부서가 담당했습니다. 본인은 Agent가 DQA 데이터를 정확히 읽고 분석할 수 있도록 만드는 data/knowledge preparation과 품질 개선을 담당했습니다.
- 적용/성과: Power Solution/Audio 영역 성과를 인정받아 30여개 component 전체로 확대 진행 중입니다. 정식 운영 후 사용자 문의에 따른 수정/A/S를 수행했고, 하드웨어 개발자가 자연어로 배터리 온도 구간 비중, 평균 온도, error log 발생률 등을 질의하고 SQL 결과와 해석을 받을 수 있게 했습니다.

### 지식 시스템 / Ontology / 지식 그래프 PoC

- 기간: 2026년 현재 진행 중
- 도메인: Knowledge System, LLM Wiki, Ontology, RDF, 지식 그래프, AI-ready enterprise knowledge
- 문제: ChatGPT, Gemini, Claude 같은 상용 LLM은 사내 용어, 시스템 사용법, 데이터 활용 지식, 부서별 convention을 기본적으로 알지 못합니다. 임직원이 매번 사내 맥락을 직접 prompt에 넣지 않아도 되도록, 사내 지식을 LLM이 활용 가능한 형태로 정리하고 관리하는 체계가 필요했습니다.
- 접근: Google OKF(Open Knowledge Format) 기반 Markdown/LLM Wiki를 참고해 사내 지식을 구조화하고, 이를 Ontology/RDF/지식 그래프로 승격해 지식 간 관계, 상충 definition, 오래된 문서, 모호한 질의 mapping, 실제 데이터값과 지식 규칙의 불일치 등을 관리하는 방향으로 PoC를 수행했습니다.
- 역할: Ontology 설계 PoC, RDF 변환 규칙 설계, entity/relation 추출 기준 설계, 기본 지식 그래프 구축, outdated/상충/모호/불일치 지식 탐지 PoC, PoC 코드 구현, 샘플 Ontology와 지식 그래프 구축, 아키텍처 문서 작성, demo 및 내부 발표를 수행했습니다.
- 역할 경계: LLM Wiki schema 자체 설계는 담당하지 않았습니다. Ontology와 entity/relation 기준은 현재 default를 만들고 있으나, 궁극적으로는 도메인 담당자가 수정·운영할 수 있도록 guide/Agent/Skill을 만드는 방향입니다. Knowledge lineage와 Agent Builder 연계는 아직 기획/초기 단계입니다.

### eStore / Trade-in Reseller Fraud Detection

- 기간: 2025.07 ~ 2025.12 개발/이관, 2026.03부터 SEA 운영 적용
- 도메인: eCommerce risk, trade-in incentive abuse, fraud detection, human-in-the-loop operations
- 문제: Samsung.com eStore는 Galaxy 구매 시 기존 기기 제출을 전제로 trade-in incentive를 즉시 할인으로 제공합니다. 그러나 일부 주문은 기기를 제출하지 않고 chargeback 회수도 실패해 손실이 발생했습니다. Trade-in 기기 도착 후 payback하는 구조는 현실적으로 어려워, 구매 시점에 fraud 가능성이 높은 주문을 탐지해 주문 담당자가 double-check/취소할 수 있게 하는 것이 목표였습니다.
- 데이터: order id, customer id, 구매 물품, 구매 방식, 제품 수령 방식, 배송지 주소, 과거 구매이력, 할인 방식, 적용 쿠폰/할인, 제출 예정 trade-in 구형 모델, chargeback 시도 로그 및 성공 여부.
- 모델링: 기기 미제출 및 chargeback 회수 실패 여부를 label로 정의하고 XGBoost classifier를 개발했습니다. 제출 예정 구형 모델, 제품 수령 방식, 적용 할인, 고객 과거 주문 등 order/customer/discount/chargeback feature를 발굴했습니다.
- 운영 설계: 주 1회 자동 재학습, probability distribution drift 기반 threshold 조정, positive 물량 제어, 탐지 건수 급증 시 break 조건을 설계했습니다. Positive 주문은 주요 feature, 전체 feature 값, 고객 과거 주문을 dashboard로 제공해 주문 담당자가 최종 판단하도록 했습니다.
- 검증/성과: 일부 주문에만 모델을 적용하고 미적용군의 사후 fraud 여부를 활용하는 A/B test 유사 방식으로 precision을 확인했습니다. 운영 precision 70%를 달성했고, SEA에 이관되어 2026년 3월부터 운영 중입니다.
- 본인 역할: EDA, feature 발굴, 모델 학습, threshold 설계, dashboard 제공 정보 정의 등 데이터/모델링 전반을 단독 수행했습니다.

### Galaxy Smart Charging / Principal Data Scientist 인증 과제

- 기간: 2023년 1년 과정 수행, 2024년 1월 Principal Data Scientist 인증
- 맥락: 삼성전자 DX부문 Data Science Level 4는 1년 동안 직접 과제를 발굴·정의·해결하고 현업 반영 및 임원 발표를 통과해야 하는 최고 레벨 인증 과정입니다.
- 문제: Galaxy 스마트폰에서 고속 충전 옵션이 켜져 있으면 사용자가 잠자는 장시간 충전 상황에서도 고속 충전이 유지되어, 리튬이온 배터리 수명 관점에서 비효율이 발생했습니다.
- 데이터: 충전 시작/종료 시점, 충전 시작/종료 배터리 잔량, 앱 사용 로그.
- 접근: 별도 복잡한 ML 모델보다 앱 사용 시간 기반 heatmap 분석을 활용했습니다. 디바이스별 최근 로그를 기반으로 액티브 사용량이 낮아지는 시간대가 반복되는지 확인해 개별 수면 패턴을 파악하고, 장시간 충전 구간에서는 배터리 보호를 위해 완속 충전으로 전환하는 로직을 설계했습니다.
- 역할: 문제 정의, 데이터 분석, 수면 시간대 파악 로직 개발, 완속 충전 전환 로직 선행 개발, 사용자 안내/빠른 고속 충전 전환 UX 방향 제안을 수행했습니다.
- 적용/역할 경계: 실제 Android 코드, 설정 앱 UI, 충전 제어 로직 반영과 제품 테스트는 협업 부서가 수행했습니다. 본인이 선행 개발한 방향은 Smart Charging 제품 옵션에 반영되었습니다.

### DCS Dashboard / Data Mart

- 기간: 2023.01 ~ 2023.12
- 도메인: Data Consulting Service, SQL workflow, dashboard, data mart
- 문제: 전사 여러 조직에서 데이터 추출/분석 요청이 들어왔고, 이를 대응할 분석가는 제한적이었습니다. 요청 중에는 반복되는 패턴이 많았지만 기존에는 분석가가 기존 SQL을 복사해 일부 조건을 수정하거나 새로 작성하는 방식으로 처리했습니다.
- 접근: 최근 2년치 DCS SQL 약 2,000건의 CTE 구조와 반복 패턴을 분석해, 정형화 가능한 요청 유형을 dashboard GUI 기반으로 처리할 수 있는 SQL/template 구조를 설계했습니다.
- 구현: BigQuery/Superset/Jinja template 기반 dashboard query format, 약 30개 mart table, 1개 dashboard/3개 tab/약 10개 chart를 설계했습니다. Chart는 dimension 선택이 가능하도록 설계해 다양한 dimension 조합에 대응했습니다.
- 추가 산출물: 터미널에서 동작하는 Python query parser, Streamlit 검색 web module, GitHub 기반 SQL review workflow를 만들었습니다. DCS 1건 완료 후 SQL을 GitHub으로 가져와 parsing하고 Mermaid diagram을 생성해 commit/review assign하는 흐름을 정립했습니다.
- 성과: Big Data센터 분석가들이 정형 요청을 dashboard GUI로 처리하고, 더 복잡한 DCS 요청에 집중할 수 있게 했습니다. 공통 SQL format과 template으로 결과물 품질과 SQL 구조의 일관성을 높였습니다.

### BLU Simulator 개발 및 검증

- 기간: 2020 ~ 2021
- 도메인: TV miniLED 백라이트 개발, BLU(Back Light Unit) 광학 시뮬레이션
- 문제: miniLED 백라이트 도입 초기에는 블루밍, 블록단차, uniformity 등 화질 문제를 실물 패널 반복 제작과 육안 평가로 검토해야 했고, 검토 케이스가 많아 개발 비용과 시간이 크게 소요되었습니다.
- 데이터/방법: 협업부서가 촬영한 70여 가지 단일 광원 광분포를 parametric curve로 fitting하고, 광원과 패널 간격에 따라 curve parameter가 어떻게 변하는지 선형회귀분석으로 확인했습니다. 제한된 측정값만으로 다양한 간격의 광분포를 생성하고, 두 개 이상의 인접 광원에서 발생하는 광분포 중첩이 덧셈 연산으로 계산 가능함을 검증했습니다.
- 지표 설계: uniformity 정량지표와 소벨 필터 기반 블록단차 지표를 개발했습니다. 광원 실장 오차로 인해 일부 영역의 화질지표가 나빠지는 문제를 반영하기 위해 단일 지표가 아니라 여러 화질지표를 함께 고려했습니다.
- 구현/배포: Python으로 구현한 뒤 PyQt/PyInstaller로 Windows GUI 프로그램을 제작·배포했습니다. 사용자는 선행패널개발그룹이며, 입력값은 광원 분포, 광원-패널 간격 범위, 최소 간격, 광원 구동 제약사항 등입니다. 출력은 세로 간격, 가로 간격, 광원-패널 간격을 포함한 설계 옵션 후보입니다.
- 성과: 실물 패널 촬영 이미지와 시뮬레이션 밝기 map을 0~100 normalize한 뒤 픽셀별 밝기 오차율 평균으로 비교했을 때 유사도 평균 90% 이상을 달성했습니다. miniLED 방식 전체 라인업 개발 프로세스에 적용되었고, 개발기간은 4개월에서 2개월 수준으로 단축, 재료비는 70% 이상 절감되었습니다.

### TV 공정 단계 잠재 불량 예측

- 기간: 2018.11 ~ 2020.10
- 도메인: TV 제품 제조 공정 품질
- 문제: CS 단계에서 시장불량을 대응하기 전에, 공정 직후 잠재 불량을 조기 탐지하자는 리더십 공감대에서 출발했습니다.
- 데이터/문제 정의: 공정 검계측 데이터와 전세계 서비스센터의 CS 데이터(불량, 수리 이력)가 serial number 기준으로 연결될 수 있음을 확인하고, 공정 완료 시점의 검계측 데이터로 향후 불량 발생 가능성을 예측하는 지도학습 문제로 정의했습니다.
- 역할: 데이터 매핑 및 전처리, 의미 단위로 학습 데이터를 묶는 구조 설계, 모델링 초기 코드, 초기 평가 metric 코드를 직접 구현했습니다. 희소 불량과 시기별 기본 불량률 변화를 고려해 랜덤 샘플 대비 precision 개선 배율인 lift 지표를 제안했습니다.
- 운영 셋업: Positive로 예측된 세트는 aging test를 우선 진행해야 했으므로, false positive가 과도하면 라인 병목이 발생할 수 있었습니다. 현업과 협의해 aging test 가능 물량과 탐지 효과 사이의 균형을 맞추는 threshold를 설정했습니다. 또한 어떤 feature 때문에 불량 가능성이 높게 나왔는지, 유사한 과거 데이터가 어떤 경향을 보였는지 설명하는 정보의 전달 방식을 협의했습니다.
- 성과: 적용 기간 중 관련 불량률은 절반 수준으로 낮아졌습니다.

### 서비스 자재 / TV 패널 수요예측

- 기간: 2018.10 ~ 2020.09
- 도메인: TV 서비스 패널, Last Time Buy, 장기 수요예측, 자재수급 이상감지
- 문제: TV 패널은 모델/연식별 구조가 달라 호환이 어렵고, 단종 시점에 서비스용 패널을 미리 확보해야 합니다. 적게 확보하면 신형 TV 교환/환불 등 비용이 발생하고, 많이 확보하면 과불용 재고 매각/폐기 비용이 발생합니다.
- 데이터: 과거 패널별/시점별 판매수량, 서비스 교체 수량, CS 이력, 자재 마스터, 제조/생산/재고 정보 등을 활용했습니다.
- 접근: 판매 패턴과 서비스 수량 패턴이 유사한 자재를 매핑했습니다. 스펙 기준이 아니라 판매 trend와 서비스 trend의 모양 기준으로 유사자재를 정의했습니다. Prophet 기반 trend 예측, 전체 수량 별도 예측, 월별 trend normalize, Savitzky-Golay smoothing을 활용했습니다.
- 역할: 문제 정의, 데이터 전처리, 유사자재 매핑 로직 구현, 전체 수량과 월별 trend를 분리 예측해 정확도를 판별하는 아이디어를 제안했습니다. 2020년 시스템화 단계에서는 개발자에게 역할을 위임하고 주로 관리/매니징을 수행했습니다.
- 성과: BM 오차율 29.6% 대비 최종 19.1%를 달성해 목표 오차율 20%를 초과 달성했습니다. 현업 시스템 적용 및 특허 출원으로 연결되었습니다.

### VCC Simulator / Data 활용 원가절감 분석 기능 고도화

- 기간: 2022년
- 도메인: 구매 원가, 유사자재 분석, 내부 구매 데이터 확보, 업무 자동화
- 문제: 수백만 단위 자재코드에 대해 유사한 사양의 자재를 비교하고 원가절감 아이디어를 발굴해야 했지만, 내부 구매 데이터의 정식 I/F가 불가능해 분석 데이터 확보 자체가 과제의 병목이었습니다.
- 구현: Python/PyQt 기반 VCC Simulator와 Python 기반 Excel 자동화 데이터 확보 프로그램을 별도로 구현했습니다. 데이터 확보는 RPA 프로그램으로 한 사람이 수행해 공유하고, 다수 사용자는 확보된 데이터를 기반으로 VCC Simulator를 활용하는 구조였습니다.
- 기능: 유사자재 사양 및 단가 비교, 가격 trend, 물류, BOM 등 데이터 연계 분석, 조건 customizing, report download, interactive 시각화를 지원했습니다.
- 사용자/이관: 생산기술연구소에서 사용했습니다. 로컬 프로그램으로 사용 후 유용성을 인정받아 웹 개발로 전환되었고, 본인 로직과 코드를 웹 구현용으로 이관했습니다.
- 성과: 기존 분석 업무시간을 121분에서 11분으로 줄여 91% 단축했습니다.

### 시장규모 / 스마트폰 판매량 시계열 예측

- 기간: 2021.02 ~ 2021.11
- 도메인: 스마트폰 시장규모 예측, market share 대응, time-series forecasting
- 문제: 경쟁사를 포함한 전체 스마트폰 판매량을 국가/가격대별로 예측해 market share 하락에 선제 대응할 필요가 있었습니다. 외부 시장 데이터는 약 2개월 latency가 있어, 월말 예측 시점 기준 최근 2개월과 향후 3개월, 총 5개월 값을 예측해야 했습니다.
- 데이터: GFK의 국가/가격대별 스마트폰 판매량, 자사 sell-out 데이터, 국가별 event, 거시경제 지표, 제조사별 출시 정보, Google mobility report 등을 활용했습니다.
- 방법: 국가/가격대 segment별 계절성, 이벤트 영향, 거시경제 변수, 자사 sell-out과의 관계를 파악하고, Prophet/SARIMAX/ensemble을 검토했습니다. Backtesting 환경을 구축해 시계열 모델, 주기, 외부변수 영향도를 dynamic하게 검증했습니다.
- 역할/성과: 모델링 전 과정을 단독 수행했습니다. 47개국 미래구간 예측 정확도 89.4%를 달성했고, 기존 모델 74.7% 대비 개선되었습니다. 결과는 MX 경영혁신그룹 내 관련 부서에 이관되어 국가별 시장규모 분기 성장률 예측 참고자료로 활용되었습니다.

### 파생 SKU Business Impact Simulation

- 기간: 2025.01 ~ 2025.06
- 도메인: Business analytics, SKU portfolio, revenue/profit simulation, PyQt PoC
- 문제: 소비자 관점의 제품 spec은 동일하지만 내부 model code가 다른 파생 SKU가 많아지면 관리 복잡도와 비용이 증가하고, 동일 제품인데 SKU별 할인/가격 정책 적용이 달라져 가격 정책 실행력이 낮아질 수 있습니다.
- 데이터: 3개 법인의 2024년 SKU/채널별 판매량, 매출, 영업이익, 순이익, 가격, promotion, SKU별 제품 spec 데이터를 활용했습니다.
- 접근/구현: 동일 spec 대체 SKU가 존재하는 경우에만 제거를 검토하고, 제거 SKU의 수요가 같은 spec의 잔존 SKU로 일부 흡수된다고 보고 가격 차이에 따른 수요 탄력성을 반영했습니다. Spec 중복 SKU 목록, 가격 탄력성, 잔존 SKU 후보, SKU 제외 시 손익/판매량 변화 결과를 제공하는 PyQt 기반 Windows Program PoC를 개발했습니다.
- 역할/상태: `SKU를 줄여라`라는 미션을 받아 문제 정의, 데이터 확보, 전처리, 가격 탄력성 분석, 시뮬레이션 로직 개발/검증, PyQt 프로그램화까지 단독 수행했습니다. 데이터 추가 확보 실패로 운영 적용까지 가지 못했고, PoC/feasibility 검토로 정리합니다.

## Education

| 구분 | 학교 | 전공/내용 | 비고 |
| --- | --- | --- | --- |
| 박사 | KAIST 경영공학부 | Finance / 금융공학 | 2018년 8월 졸업, 석박사통합과정, 지도교수 변석준, 공동지도교수 강장구 |
| 학사 | KAIST | 수학과, 산업공학과 복수전공 | 3년 조기졸업 |
| 고등학교 | 한국과학영재학교 | 과학영재학교 | 전국 유일 영재학교 시절 입학 |

## Research / Conference

- 박사학위논문: `Essays on investor herding behavior and stock market`, KAIST 경영공학부, 2018년. 주식시장에서 투자자 군집행동이 가격·변동성·행동 전파에 미치는 영향을 다룬 두 편의 essay로 구성.
- APAD 2017: `The Disagreement with Herding, Market Bubble, and Excess Volatility` 직접 발표. Analyst EPS forecast에서 관측되는 disagreement와 consensus-following behavior를 하나의 모형에서 다룸. 모형 유도, simulation, 보조 실증분석, 발표자료 작성을 단독 수행.
- AsianFA 2017: `The Disagreement with Herding, Market Bubble, and Excess Volatility` 직접 발표. Herding parameter가 disagreement 모형의 price·return volatility 해석을 어떻게 바꾸는지 설명.
- StockTwits 기반 cognitive network 연구: 약 3,100만 건 게시글과 약 15만 명 사용자 활동을 활용해 stock-user bipartite network를 stock-stock cognitive network로 변환. Disagreement, overconfidence, pessimism 등이 cognitive distance가 가까운 종목으로 전파되는지 portfolio sorting과 clustered regression으로 검증. 데이터 수집과 cashtag parsing은 직접 수행 범위가 아니며, network 구성, regression, 발표자료 작성을 수행.
## Patents / Inventions

| 발명명칭 | 등급 | 기여도 | 연결 프로젝트 | 비고 |
| --- | --- | --- | --- | --- |
| 다중모델 최적화 기반의 실시간 데이터특성 변화에 적응적인 잠재 불량 예측 시스템 | A2 | 10% | TV 공정 단계 잠재 불량 예측 | 특허 문서 작성 기여는 작으므로 과제 수행 역할 중심으로 설명 |
| 광프로파일을 이용한 화면표시장치의 광분포 시뮬레이션 방법 및 화질 최적 광학옵션 탐색 시스템 | A2 | 25% | BLU Simulator | 과제 주도성이 높아 상세 CV 핵심 발명으로 사용 가능 |
| 자재군집화기반 서비스자재 수요예측 및 실시간 자재수급 이상감지 시스템 및 그 방법 | A2 | 30% | 서비스 자재 수요예측 | 출원, LTB 이후 수요예측 및 자재수급 이상감지 구조 |

## Certification / Recognition

- Principal Data Scientist: 삼성전자 DX부문 Data Science Level 4 최고 인증. 2023년 1년 과정 수행, 2024년 1월 인증. 2026년 6월 기준 DX부문 인증자 9명. 인증 과제는 Galaxy Smart Charging 선행 개발이며 제품 옵션 반영으로 이어졌습니다.
- AI Specialist: 인재개발원 주관 사내 AI 전문가 Level 3 자격. 2025.10부터 3개월 과정 진행 후 취득. 취득 과제는 DQA error signal과 연관 후보 key를 전기/전자/물리 지식, DQA spec, 통계 검증으로 추적하는 Expert-like Thinking Agent PoC입니다.
- 상위 고과: 육아휴직 기간을 제외한 평가 대상 연도마다 상위 평가
- 경력 입사 전문성 면접관: 사내 면접관 교육 이수 후 경력 입사 실무진 전문성 면접관 20회 이상 수행. 지원자의 경력 PT를 바탕으로 과제 맥락, 본인 기여, 실행 과정을 검토하고 scoring 수행.
- Data Science Level 3 시험문제 검수: 2022.01 ~ 2023.12 중 간헐 지원. 문제 요구사항 명확성, 오류 여부, 난이도, 출제 범위 적절성 검토.

## Internal Leadership / Teaching

- Data Science 학습 플랫폼 개발·운영: 2025.04 ~ 현재. Django/Docker/Jupyter 기반 사내 Data Science 학습 플랫폼을 직접 개발·운영. 평소 일 평균 약 50명, 시험 직전 일 100명 수준 방문. 플랫폼 공유 공로로 Center 단위 Award를 수상하고 전사 임직원 포털에 운영자로 소개되었습니다.
- 분석가 문화 개선 TF: 2023년 전체. 5인 TF에서 Big Data센터 분석가 그룹 전체를 대상으로 Git 기반 SQL/code review 문화를 확산했습니다. 로컬 텍스트 파일 중심으로 흩어지던 SQL 산출물을 Git 기반 지식 자산으로 관리하고 서로 리뷰하는 프로세스를 마련하기 위해 가이드, 모범 샘플, 세미나, Q&A 채널을 운영했습니다.
