import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import random
import time
from datetime import datetime, timedelta

st.set_page_config(
    page_title="한양챗 (HY-Chat)",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #0E4A84;
        text-align: center;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #666;
        text-align: center;
        margin-bottom: 2rem;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 24px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        background-color: #f0f4f8;
        border-radius: 8px 8px 0 0;
        padding: 10px 24px;
        font-weight: 600;
    }
    .stTabs [aria-selected="true"] {
        background-color: #0E4A84;
        color: white;
    }
    .scholarship-card {
        background: linear-gradient(135deg, #0E4A84 0%, #1a6fc4 100%);
        border-radius: 12px;
        padding: 20px;
        color: white;
        margin-bottom: 15px;
    }
    .info-card {
        background: #f8f9fa;
        border-left: 4px solid #0E4A84;
        padding: 15px;
        border-radius: 0 8px 8px 0;
        margin: 10px 0;
    }
    .metric-box {
        background: white;
        border: 1px solid #e0e0e0;
        border-radius: 10px;
        padding: 15px;
        text-align: center;
    }
    .timeline-item {
        border-left: 3px solid #0E4A84;
        padding-left: 20px;
        margin-left: 10px;
        padding-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

def generate_dummy_data():
    majors = ["컴퓨터소프트웨어학부", "전자공학부", "경영학과", "건축학과", "화학공학과", "기계공학과", "의예과", "국어국문학과"]
    careers = ["소프트웨어 개발자", "데이터 사이언티스트", "금융 애널리스트", "건축가", "연구원", "컨설턴트", "의사", "마케터"]
    
    user_profile = {
        "student_id": f"2022{random.randint(10000, 99999)}",
        "name": random.choice(["김한양", "이서울", "박성동", "최안산", "정에리카"]),
        "major": random.choice(majors),
        "grade": random.randint(1, 4),
        "semester": random.randint(1, 2),
        "gpa": round(random.uniform(2.5, 4.5), 2),
        "income_level": random.randint(1, 10),
        "interest_career": random.choice(careers),
        "completed_credits": random.randint(30, 130),
        "skills": {
            "프로그래밍": random.randint(30, 100),
            "데이터분석": random.randint(30, 100),
            "의사소통": random.randint(30, 100),
            "문제해결": random.randint(30, 100),
            "팀워크": random.randint(30, 100),
            "영어능력": random.randint(30, 100),
        }
    }
    
    academic_notices = [
        {
            "title": "2024-1학기 수강신청 안내",
            "content": "수강신청 기간: 2024년 2월 19일(월) ~ 2월 23일(금)",
            "date": "2024-02-01",
            "link": "https://www.hanyang.ac.kr/web/www/notice_academic",
            "regulation": "학칙 제42조"
        },
        {
            "title": "휴학 신청 안내",
            "content": "휴학 신청은 포털시스템에서 가능하며, 등록금 납부 전 신청해야 합니다.",
            "date": "2024-01-15",
            "link": "https://www.hanyang.ac.kr/web/www/leave",
            "regulation": "학칙 제31조"
        },
        {
            "title": "졸업요건 안내",
            "content": "졸업을 위해서는 130학점 이상 취득, 전공필수 이수, 영어졸업인증이 필요합니다.",
            "date": "2024-01-10",
            "link": "https://www.hanyang.ac.kr/web/www/graduation",
            "regulation": "학칙 제55조"
        },
        {
            "title": "전과 신청 안내",
            "content": "전과는 2학년 이상, 평점 3.0 이상인 학생만 신청 가능합니다.",
            "date": "2024-01-05",
            "link": "https://www.hanyang.ac.kr/web/www/change_major",
            "regulation": "학칙 제28조"
        },
        {
            "title": "복수전공/부전공 신청",
            "content": "복수전공은 주전공 36학점 이상 취득 후 신청 가능합니다.",
            "date": "2023-12-20",
            "link": "https://www.hanyang.ac.kr/web/www/double_major",
            "regulation": "학칙 제25조"
        }
    ]
    
    scholarships = [
        {
            "name": "한양 성적우수 장학금",
            "type": "성적",
            "amount": "등록금 100%",
            "requirements": {"min_gpa": 4.0, "max_income": 10},
            "deadline": (datetime.now() + timedelta(days=30)).strftime("%Y-%m-%d"),
            "description": "직전 학기 성적 우수자에게 지급되는 장학금입니다.",
            "link": "https://www.hanyang.ac.kr/web/www/scholarship",
            "eligibility": ["직전 학기 평점 4.0 이상", "재학생 (휴학생 제외)", "성적 장학금 중복 수혜 불가", "학기당 15학점 이상 이수자"]
        },
        {
            "name": "한양 희망 장학금",
            "type": "소득연계",
            "amount": "등록금 70%",
            "requirements": {"min_gpa": 2.5, "max_income": 4},
            "deadline": (datetime.now() + timedelta(days=45)).strftime("%Y-%m-%d"),
            "description": "저소득층 학생을 위한 교내 장학금입니다.",
            "link": "https://www.hanyang.ac.kr/web/www/scholarship",
            "eligibility": ["소득분위 4분위 이하", "직전 학기 평점 2.5 이상", "재학생 (신입생 제외)", "국가장학금 신청 완료자"]
        },
        {
            "name": "국가근로장학금",
            "type": "근로",
            "amount": "시간당 11,150원",
            "requirements": {"min_gpa": 2.0, "max_income": 8},
            "deadline": (datetime.now() + timedelta(days=20)).strftime("%Y-%m-%d"),
            "description": "교내외 근로를 통해 지급받는 장학금입니다.",
            "link": "https://www.kosaf.go.kr",
            "eligibility": ["소득분위 8분위 이하", "직전 학기 평점 2.0 이상 (경고 1회 허용)", "대한민국 국적 소지자", "한국장학재단 국가근로장학금 신청자"]
        },
        {
            "name": "이공계 국가장학금",
            "type": "국가",
            "amount": "등록금 전액 + 생활비",
            "requirements": {"min_gpa": 3.5, "max_income": 6, "major_type": "이공계"},
            "deadline": (datetime.now() + timedelta(days=60)).strftime("%Y-%m-%d"),
            "description": "이공계 전공 우수 학생을 위한 국가 장학금입니다.",
            "link": "https://www.kosaf.go.kr",
            "eligibility": ["이공계 전공자 (자연과학, 공학 계열)", "소득분위 6분위 이하", "직전 학기 평점 3.5 이상", "졸업 후 의무복무 기간 동의자"]
        },
        {
            "name": "외국어우수장학금",
            "type": "특기",
            "amount": "200만원",
            "requirements": {"min_gpa": 3.0, "max_income": 10},
            "deadline": (datetime.now() + timedelta(days=35)).strftime("%Y-%m-%d"),
            "description": "TOEIC 900점 이상 또는 동등 수준의 외국어 능력 보유자",
            "link": "https://www.hanyang.ac.kr/web/www/scholarship",
            "eligibility": ["TOEIC 900점 이상 또는 TOEFL iBT 100점 이상", "직전 학기 평점 3.0 이상", "어학성적 유효기간 내 제출", "재학생 (휴학생 제외)"]
        }
    ]
    
    career_requirements = {
        "소프트웨어 개발자": {
            "skills": {"프로그래밍": 90, "데이터분석": 70, "의사소통": 60, "문제해결": 85, "팀워크": 75, "영어능력": 65},
            "courses": [
                {"name": "자료구조론", "code": "CSE2010", "credits": 3, "department": "컴퓨터소프트웨어학부", "description": "프로그래밍에 필요한 자료구조(배열, 연결리스트, 스택, 큐, 트리, 그래프 등)의 개념과 구현을 학습합니다."},
                {"name": "알고리즘", "code": "CSE3080", "credits": 3, "department": "컴퓨터소프트웨어학부", "description": "정렬, 탐색, 그래프 알고리즘, 동적 프로그래밍 등 효율적인 문제 해결 알고리즘을 다룹니다."},
                {"name": "소프트웨어공학", "code": "CSE4006", "credits": 3, "department": "컴퓨터소프트웨어학부", "description": "소프트웨어 개발 생명주기, 요구사항 분석, 설계 패턴, 테스팅 등 체계적인 개발 방법론을 학습합니다."},
                {"name": "데이터베이스시스템", "code": "CSE3030", "credits": 3, "department": "컴퓨터소프트웨어학부", "description": "관계형 데이터베이스 설계, SQL, 트랜잭션 처리, 데이터 모델링 등을 다룹니다."},
                {"name": "웹프로그래밍", "code": "CSE4004", "credits": 3, "department": "컴퓨터소프트웨어학부", "description": "HTML, CSS, JavaScript, 서버사이드 프로그래밍 등 웹 애플리케이션 개발 기술을 학습합니다."},
            ],
            "activities": ["오픈소스 기여", "해커톤 참가", "개발 동아리", "산업체 인턴십"],
        },
        "데이터 사이언티스트": {
            "skills": {"프로그래밍": 80, "데이터분석": 95, "의사소통": 65, "문제해결": 85, "팀워크": 70, "영어능력": 75},
            "courses": [
                {"name": "확률및통계", "code": "MAT3100", "credits": 3, "department": "수학과", "description": "확률론의 기초, 확률분포, 통계적 추론, 가설검정 등 데이터 분석의 수학적 기초를 학습합니다."},
                {"name": "기계학습", "code": "CSE4007", "credits": 3, "department": "컴퓨터소프트웨어학부", "description": "지도학습, 비지도학습, 신경망, 딥러닝 등 기계학습 알고리즘의 원리와 응용을 다룹니다."},
                {"name": "데이터마이닝", "code": "CSE4009", "credits": 3, "department": "컴퓨터소프트웨어학부", "description": "대용량 데이터에서 유용한 패턴을 발견하는 기법(군집화, 연관규칙, 분류 등)을 학습합니다."},
                {"name": "빅데이터분석", "code": "CSE4015", "credits": 3, "department": "컴퓨터소프트웨어학부", "description": "Hadoop, Spark 등 빅데이터 처리 프레임워크와 대규모 데이터 분석 기법을 다룹니다."},
                {"name": "인공지능", "code": "CSE3050", "credits": 3, "department": "컴퓨터소프트웨어학부", "description": "탐색, 지식표현, 추론, 자연어처리 등 인공지능의 핵심 개념과 기술을 학습합니다."},
            ],
            "activities": ["캐글 대회", "데이터 분석 프로젝트", "연구실 인턴", "논문 작성"],
        },
        "금융 애널리스트": {
            "skills": {"프로그래밍": 60, "데이터분석": 85, "의사소통": 80, "문제해결": 75, "팀워크": 70, "영어능력": 85},
            "courses": [
                {"name": "재무관리", "code": "BUS3001", "credits": 3, "department": "경영학부", "description": "기업의 자금조달, 투자결정, 자본구조, 배당정책 등 재무의사결정의 기초를 학습합니다."},
                {"name": "투자론", "code": "BUS3010", "credits": 3, "department": "경영학부", "description": "주식, 채권, 파생상품 등 금융자산의 가치평가와 포트폴리오 이론을 다룹니다."},
                {"name": "금융공학", "code": "BUS4020", "credits": 3, "department": "경영학부", "description": "파생상품 가격결정, 리스크 관리, 수치해석적 방법론 등 금융공학의 핵심 개념을 학습합니다."},
                {"name": "경제학원론", "code": "ECO1001", "credits": 3, "department": "경제금융학부", "description": "미시경제학과 거시경제학의 기본 원리, 시장경제의 작동원리를 이해합니다."},
                {"name": "회계원리", "code": "BUS1002", "credits": 3, "department": "경영학부", "description": "재무제표 작성과 분석, 회계순환과정, 기업 회계의 기초를 학습합니다."},
            ],
            "activities": ["금융 공모전", "투자 동아리", "CFA 준비", "증권사 인턴"],
        },
        "건축가": {
            "skills": {"프로그래밍": 40, "데이터분석": 50, "의사소통": 80, "문제해결": 85, "팀워크": 90, "영어능력": 60},
            "courses": [
                {"name": "건축설계스튜디오", "code": "ARC2001", "credits": 6, "department": "건축학부", "description": "건축 설계의 기본 개념과 방법론을 실습을 통해 학습하며, 창의적 공간 구성 능력을 배양합니다."},
                {"name": "구조역학", "code": "ARC2010", "credits": 3, "department": "건축학부", "description": "건축물의 하중과 응력 분석, 구조 시스템의 역학적 원리를 이해합니다."},
                {"name": "건축환경", "code": "ARC3005", "credits": 3, "department": "건축학부", "description": "열환경, 빛환경, 음환경 등 건축물의 물리적 환경 조절 원리를 학습합니다."},
                {"name": "도시계획론", "code": "ARC3020", "credits": 3, "department": "건축학부", "description": "도시의 형성과 발전, 토지이용계획, 도시설계의 기본 원리를 다룹니다."},
                {"name": "건축CAD", "code": "ARC1005", "credits": 3, "department": "건축학부", "description": "AutoCAD, Revit 등 건축 설계 소프트웨어를 활용한 도면 작성 및 3D 모델링을 학습합니다."},
            ],
            "activities": ["설계 공모전", "건축 전시회", "설계사무소 인턴십", "해외 건축 탐방"],
        },
        "연구원": {
            "skills": {"프로그래밍": 70, "데이터분석": 80, "의사소통": 65, "문제해결": 90, "팀워크": 60, "영어능력": 85},
            "courses": [
                {"name": "연구방법론", "code": "GEN4001", "credits": 3, "department": "교양학부", "description": "과학적 연구의 설계, 자료수집 방법, 연구윤리 등 학술 연구의 기초를 학습합니다."},
                {"name": "논문작성법", "code": "GEN4002", "credits": 2, "department": "교양학부", "description": "학술 논문의 구조, 학술적 글쓰기, 인용 방법 등을 체계적으로 배웁니다."},
                {"name": "고급통계학", "code": "MAT4010", "credits": 3, "department": "수학과", "description": "회귀분석, 분산분석, 다변량분석 등 고급 통계기법을 학습합니다."},
                {"name": "실험설계", "code": "IND3010", "credits": 3, "department": "산업공학과", "description": "실험의 계획, 수행, 분석 방법론을 학습하고 실제 실험에 적용합니다."},
                {"name": "캡스톤디자인", "code": "ENG4001", "credits": 3, "department": "공과대학", "description": "전공 지식을 종합하여 실제 문제를 해결하는 프로젝트 수행 능력을 배양합니다."},
            ],
            "activities": ["학부연구생", "논문 발표", "학회 참가", "연구 프로젝트"],
        },
        "컨설턴트": {
            "skills": {"프로그래밍": 50, "데이터분석": 75, "의사소통": 95, "문제해결": 90, "팀워크": 85, "영어능력": 80},
            "courses": [
                {"name": "경영전략", "code": "BUS4001", "credits": 3, "department": "경영학부", "description": "기업의 경쟁우위 확보를 위한 전략 수립과 실행, 산업분석 방법론을 학습합니다."},
                {"name": "조직행동론", "code": "BUS2005", "credits": 3, "department": "경영학부", "description": "조직 내 개인과 집단의 행동, 리더십, 조직문화, 동기부여 이론을 다룹니다."},
                {"name": "마케팅원론", "code": "BUS2001", "credits": 3, "department": "경영학부", "description": "마케팅의 기본 개념, 소비자 행동, 마케팅 믹스 전략을 학습합니다."},
                {"name": "경영정보시스템", "code": "BUS3015", "credits": 3, "department": "경영학부", "description": "기업의 정보시스템 활용, 디지털 전환, IT 기반 경영혁신을 다룹니다."},
                {"name": "프로젝트관리", "code": "IND3020", "credits": 3, "department": "산업공학과", "description": "프로젝트 계획, 일정관리, 리스크관리, 팀 관리 등 PM 역량을 배양합니다."},
            ],
            "activities": ["케이스 스터디", "컨설팅 공모전", "컨설팅펌 인턴십", "프레젠테이션 대회"],
        },
        "의사": {
            "skills": {"프로그래밍": 30, "데이터분석": 60, "의사소통": 90, "문제해결": 95, "팀워크": 85, "영어능력": 75},
            "courses": [
                {"name": "해부학", "code": "MED1001", "credits": 4, "department": "의학과", "description": "인체의 구조와 형태, 각 기관계의 해부학적 특성을 학습합니다."},
                {"name": "생리학", "code": "MED1002", "credits": 4, "department": "의학과", "description": "인체 각 기관의 기능과 작동 원리, 항상성 유지 메커니즘을 이해합니다."},
                {"name": "약리학", "code": "MED2001", "credits": 3, "department": "의학과", "description": "약물의 작용 기전, 약동학, 약력학 및 임상 적용을 학습합니다."},
                {"name": "병리학", "code": "MED2002", "credits": 4, "department": "의학과", "description": "질병의 원인, 발생기전, 형태학적 변화를 연구하여 진단의 기초를 학습합니다."},
                {"name": "임상실습", "code": "MED4001", "credits": 6, "department": "의학과", "description": "병원 각 과에서 실제 환자를 대상으로 진료 참관 및 실습을 수행합니다."},
            ],
            "activities": ["병원 봉사", "의료 봉사단", "기초의학 연구 참여", "학술 동아리"],
        },
        "마케터": {
            "skills": {"프로그래밍": 45, "데이터분석": 70, "의사소통": 90, "문제해결": 75, "팀워크": 85, "영어능력": 70},
            "courses": [
                {"name": "마케팅원론", "code": "BUS2001", "credits": 3, "department": "경영학부", "description": "마케팅의 기본 개념, STP 전략, 4P 믹스 등 마케팅 관리의 기초를 학습합니다."},
                {"name": "소비자행동론", "code": "BUS3002", "credits": 3, "department": "경영학부", "description": "소비자 의사결정 과정, 심리적 요인, 구매행동 분석을 다룹니다."},
                {"name": "디지털마케팅", "code": "BUS4010", "credits": 3, "department": "경영학부", "description": "온라인 광고, SNS 마케팅, SEO, 데이터 기반 마케팅 전략을 학습합니다."},
                {"name": "브랜드관리", "code": "BUS4015", "credits": 3, "department": "경영학부", "description": "브랜드 자산 구축, 브랜드 전략, 브랜드 확장 및 리뉴얼을 다룹니다."},
                {"name": "광고론", "code": "BUS3005", "credits": 3, "department": "경영학부", "description": "광고의 기획, 제작, 매체 전략, 효과 측정 등 광고 커뮤니케이션을 학습합니다."},
            ],
            "activities": ["마케팅 공모전", "브랜드사 인턴십", "SNS 채널 운영", "시장조사 프로젝트"],
        }
    }
    
    return user_profile, academic_notices, scholarships, career_requirements

def get_chatbot_response(question, notices):
    question_lower = question.lower()
    
    responses = {
        "수강신청": {
            "answer": "2024-1학기 수강신청은 2월 19일(월)부터 2월 23일(금)까지입니다. 수강신청 전 희망과목을 미리 장바구니에 담아두시고, 본인의 수강신청 시간을 확인하세요.",
            "link": "https://www.hanyang.ac.kr/web/www/notice_academic",
            "regulation": "학칙 제42조 (수강신청)"
        },
        "휴학": {
            "answer": "휴학 신청은 한양대학교 포털시스템(portal.hanyang.ac.kr)에서 가능합니다. 일반휴학, 군휴학, 임신·출산 휴학 등이 있으며, 등록금 납부 전에 신청해야 합니다. 휴학 기간은 1년 단위이며, 최대 4년까지 가능합니다.",
            "link": "https://www.hanyang.ac.kr/web/www/leave",
            "regulation": "학칙 제31조 (휴학)"
        },
        "졸업": {
            "answer": "졸업을 위해서는 ① 130학점 이상 취득 ② 전공필수 과목 이수 ③ 교양필수 과목 이수 ④ 영어졸업인증 ⑤ 졸업논문/시험이 필요합니다. 세부 요건은 학과별로 다를 수 있으니 학과 사무실에 문의하세요.",
            "link": "https://www.hanyang.ac.kr/web/www/graduation",
            "regulation": "학칙 제55조 (졸업요건)"
        },
        "전과": {
            "answer": "전과는 2학년 이상, 평점 3.0 이상인 학생만 신청 가능합니다. 매 학기 초에 신청 기간이 공지되며, 전과 정원 및 세부 조건은 학과별로 다릅니다.",
            "link": "https://www.hanyang.ac.kr/web/www/change_major",
            "regulation": "학칙 제28조 (전과)"
        },
        "복수전공": {
            "answer": "복수전공은 주전공 36학점 이상 취득 후 신청 가능합니다. 복수전공 이수를 위해서는 해당 전공의 필수과목을 포함하여 36학점 이상을 이수해야 합니다.",
            "link": "https://www.hanyang.ac.kr/web/www/double_major",
            "regulation": "학칙 제25조 (복수전공)"
        },
        "장학금": {
            "answer": "한양대학교는 성적장학금, 소득연계장학금, 근로장학금 등 다양한 장학금을 제공합니다. 장학금 신청은 매 학기 초 포털시스템에서 가능하며, 자격 요건은 장학금 종류별로 다릅니다.",
            "link": "https://www.hanyang.ac.kr/web/www/scholarship",
            "regulation": "장학규정 제5조 (장학금 종류)"
        },
        "등록금": {
            "answer": "등록금 납부는 매 학기 초 고지서 발송 후 지정된 기간 내에 납부해야 합니다. 분할납부도 가능하며, 등록금 관련 문의는 재무팀(02-2220-0044)으로 연락하세요.",
            "link": "https://www.hanyang.ac.kr/web/www/tuition",
            "regulation": "학칙 제17조 (등록금)"
        }
    }
    
    for keyword, response in responses.items():
        if keyword in question_lower:
            return response
    
    return {
        "answer": f"'{question}'에 대한 정확한 정보를 찾지 못했습니다. 더 구체적인 키워드로 질문해 주시거나, 아래 학사 관련 주요 키워드를 참고해 주세요: 수강신청, 휴학, 졸업, 전과, 복수전공, 장학금, 등록금",
        "link": "https://www.hanyang.ac.kr/web/www/notice_academic",
        "regulation": "학칙 전체보기"
    }

def calculate_scholarship_match(scholarship, user_profile):
    score = 100
    
    if user_profile["gpa"] < scholarship["requirements"]["min_gpa"]:
        gap = scholarship["requirements"]["min_gpa"] - user_profile["gpa"]
        score -= min(40, gap * 20)
    
    if user_profile["income_level"] > scholarship["requirements"]["max_income"]:
        gap = user_profile["income_level"] - scholarship["requirements"]["max_income"]
        score -= min(30, gap * 5)
    
    if "major_type" in scholarship["requirements"]:
        engineering_majors = ["컴퓨터소프트웨어학부", "전자공학부", "화학공학과", "기계공학과"]
        if scholarship["requirements"]["major_type"] == "이공계" and user_profile["major"] not in engineering_majors:
            score -= 50
    
    return max(0, min(100, int(score)))

def render_sidebar():
    with st.sidebar:
        st.markdown("### 🎓 한양챗 (HY-Chat)")
        st.markdown("---")
        
        if st.button("🔄 더미 데이터 생성", width="stretch", type="primary"):
            user_profile, academic_notices, scholarships, career_requirements = generate_dummy_data()
            st.session_state.user_profile = user_profile
            st.session_state.academic_notices = academic_notices
            st.session_state.scholarships = scholarships
            st.session_state.career_requirements = career_requirements
            st.session_state.data_generated = True
            st.rerun()
        
        st.markdown("---")
        
        if st.session_state.get("data_generated", False):
            st.markdown("### 📋 사용자 정보")
            profile = st.session_state.user_profile
            
            st.markdown(f"""
            <div style="background: #f0f4f8; padding: 15px; border-radius: 10px; margin-bottom: 10px;">
                <p style="margin: 5px 0;"><strong>👤 이름:</strong> {profile['name']}</p>
                <p style="margin: 5px 0;"><strong>🔢 학번:</strong> {profile['student_id']}</p>
                <p style="margin: 5px 0;"><strong>📚 전공:</strong> {profile['major']}</p>
                <p style="margin: 5px 0;"><strong>📅 학년:</strong> {profile['grade']}학년 {profile['semester']}학기</p>
                <p style="margin: 5px 0;"><strong>📊 학점:</strong> {profile['gpa']}/4.5</p>
                <p style="margin: 5px 0;"><strong>💰 소득분위:</strong> {profile['income_level']}분위</p>
                <p style="margin: 5px 0;"><strong>🎯 관심직무:</strong> {profile['interest_career']}</p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.info("👆 '더미 데이터 생성' 버튼을 클릭하여 시작하세요!")

def render_chatbot():
    st.markdown("### 💬 AI 학사 챗봇")
    st.markdown("학사 관련 궁금한 점을 질문해 주세요!")
    
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
            if message["role"] == "assistant" and "metadata" in message:
                col1, col2 = st.columns(2)
                with col1:
                    st.markdown(f"""
                    <div class="info-card">
                        <strong>📎 출처 링크</strong><br>
                        <a href="{message['metadata']['link']}" target="_blank">{message['metadata']['link']}</a>
                    </div>
                    """, unsafe_allow_html=True)
                with col2:
                    st.markdown(f"""
                    <div class="info-card">
                        <strong>📖 관련 규정</strong><br>
                        {message['metadata']['regulation']}
                    </div>
                    """, unsafe_allow_html=True)
    
    if prompt := st.chat_input("예: 수강신청 기간이 언제야?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        with st.chat_message("user"):
            st.markdown(prompt)
        
        with st.chat_message("assistant"):
            with st.spinner("답변을 생성하고 있습니다..."):
                time.sleep(1)
                
                notices = st.session_state.get("academic_notices", [])
                response = get_chatbot_response(prompt, notices)
                
                st.markdown(response["answer"])
                
                col1, col2 = st.columns(2)
                with col1:
                    st.markdown(f"""
                    <div class="info-card">
                        <strong>📎 출처 링크</strong><br>
                        <a href="{response['link']}" target="_blank">{response['link']}</a>
                    </div>
                    """, unsafe_allow_html=True)
                with col2:
                    st.markdown(f"""
                    <div class="info-card">
                        <strong>📖 관련 규정</strong><br>
                        {response['regulation']}
                    </div>
                    """, unsafe_allow_html=True)
        
        st.session_state.messages.append({
            "role": "assistant", 
            "content": response["answer"],
            "metadata": {"link": response["link"], "regulation": response["regulation"]}
        })

def render_scholarship_matcher():
    st.markdown("### 🎁 맞춤형 장학금 추천")
    
    if not st.session_state.get("data_generated", False):
        st.warning("⚠️ 사이드바에서 '더미 데이터 생성' 버튼을 클릭해 주세요!")
        return
    
    profile = st.session_state.user_profile
    scholarships = st.session_state.scholarships
    
    st.markdown(f"""
    <div style="background: linear-gradient(135deg, #0E4A84 0%, #1a6fc4 100%); padding: 20px; border-radius: 12px; color: white; margin-bottom: 20px;">
        <h4 style="margin: 0;">👤 {profile['name']}님의 프로필 기반 추천</h4>
        <p style="margin: 10px 0 0 0;">학점: {profile['gpa']}/4.5 | 소득분위: {profile['income_level']}분위 | 전공: {profile['major']}</p>
    </div>
    """, unsafe_allow_html=True)
    
    with st.spinner("장학금을 분석하고 있습니다..."):
        time.sleep(0.5)
    
    scholarship_matches = []
    for scholarship in scholarships:
        match_score = calculate_scholarship_match(scholarship, profile)
        scholarship_matches.append({**scholarship, "match_score": match_score})
    
    scholarship_matches.sort(key=lambda x: x["match_score"], reverse=True)
    
    for i, scholarship in enumerate(scholarship_matches):
        with st.container():
            col1, col2 = st.columns([3, 1])
            
            with col1:
                st.markdown(f"#### {scholarship['name']}")
                st.markdown(f"**유형:** {scholarship['type']} | **지급액:** {scholarship['amount']}")
                
                match_color = "#28a745" if scholarship["match_score"] >= 70 else "#ffc107" if scholarship["match_score"] >= 40 else "#dc3545"
                st.markdown(f"**매칭 점수:**")
                st.progress(scholarship["match_score"] / 100)
                st.markdown(f"<span style='color: {match_color}; font-weight: bold;'>{scholarship['match_score']}%</span>", unsafe_allow_html=True)
            
            with col2:
                with st.expander("📋 상세보기"):
                    st.markdown(f"**설명:** {scholarship['description']}")
                    st.markdown(f"**신청 기한:** {scholarship['deadline']}")
                    st.markdown(f"**최소 학점:** {scholarship['requirements']['min_gpa']}")
                    st.markdown(f"**소득분위 제한:** {scholarship['requirements']['max_income']}분위 이하")
                    st.markdown("---")
                    st.markdown("**📝 신청 자격조건:**")
                    for req in scholarship.get('eligibility', []):
                        st.markdown(f"• {req}")
                    if scholarship.get('link'):
                        st.markdown("---")
                        st.markdown(f"🔗 [장학금 신청 바로가기]({scholarship['link']})")
            
            st.markdown("---")

def render_career_roadmap():
    st.markdown("### 🗺️ 전공 진로 로드맵")
    
    if not st.session_state.get("data_generated", False):
        st.warning("⚠️ 사이드바에서 '더미 데이터 생성' 버튼을 클릭해 주세요!")
        return
    
    profile = st.session_state.user_profile
    career_requirements = st.session_state.career_requirements
    
    careers = list(career_requirements.keys())
    selected_career = st.selectbox(
        "희망 진로를 선택하세요:",
        careers,
        index=careers.index(profile["interest_career"]) if profile["interest_career"] in careers else 0
    )
    
    if selected_career:
        with st.spinner("진로 분석 중..."):
            time.sleep(0.5)
        
        required_skills = career_requirements[selected_career]["skills"]
        user_skills = profile["skills"]
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.markdown("#### 📊 역량 비교 분석")
            
            categories = list(required_skills.keys())
            
            fig = go.Figure()
            
            fig.add_trace(go.Scatterpolar(
                r=[required_skills[cat] for cat in categories],
                theta=categories,
                fill='toself',
                name='필수 역량',
                line_color='#0E4A84',
                fillcolor='rgba(14, 74, 132, 0.3)'
            ))
            
            fig.add_trace(go.Scatterpolar(
                r=[user_skills[cat] for cat in categories],
                theta=categories,
                fill='toself',
                name='보유 역량',
                line_color='#28a745',
                fillcolor='rgba(40, 167, 69, 0.3)'
            ))
            
            fig.update_layout(
                polar=dict(
                    radialaxis=dict(
                        visible=True,
                        range=[0, 100]
                    )
                ),
                showlegend=True,
                legend=dict(x=0.5, y=-0.1, xanchor='center', orientation='h'),
                height=400,
                margin=dict(l=80, r=80, t=40, b=80)
            )
            
            st.plotly_chart(fig, width="stretch")
        
        with col2:
            st.markdown("#### 📈 역량 격차 분석")
            
            skill_improvement_guide = {
                "프로그래밍": {
                    "reason": "코딩 실습 및 프로젝트 경험 부족",
                    "solution": "알고리즘 문제 풀이(백준, 프로그래머스), 개인 프로젝트 진행, 오픈소스 기여 활동 추천"
                },
                "데이터분석": {
                    "reason": "통계 및 데이터 처리 도구 활용 경험 부족",
                    "solution": "Python(Pandas, NumPy) 학습, 캐글 대회 참가, 데이터 분석 관련 수업 이수 권장"
                },
                "의사소통": {
                    "reason": "발표 및 협업 경험 부족",
                    "solution": "팀 프로젝트 적극 참여, 발표 동아리 활동, 스터디 그룹 리더 경험 쌓기 추천"
                },
                "문제해결": {
                    "reason": "복잡한 문제 분석 및 해결 경험 부족",
                    "solution": "공모전 참가, 캡스톤 디자인 프로젝트, 케이스 스터디 연습 권장"
                },
                "팀워크": {
                    "reason": "팀 기반 협업 프로젝트 경험 부족",
                    "solution": "학과 동아리 활동, 그룹 프로젝트 참여, 학생회/봉사단체 활동 추천"
                },
                "영어능력": {
                    "reason": "영어 사용 환경 노출 부족",
                    "solution": "영어 원서 읽기, 영어 강의 수강, TOEIC/TOEFL 준비, 교환학생 프로그램 고려"
                }
            }
            
            gaps = []
            for skill in categories:
                gap = required_skills[skill] - user_skills[skill]
                gaps.append({"skill": skill, "gap": gap, "required": required_skills[skill], "current": user_skills[skill]})
            
            gaps.sort(key=lambda x: x["gap"], reverse=True)
            
            for gap_info in gaps:
                if gap_info["gap"] > 0:
                    with st.expander(f"⚠️ {gap_info['skill']}: 현재 {gap_info['current']}% → 목표 {gap_info['required']}% (부족: {gap_info['gap']}%)"):
                        st.progress(gap_info["current"] / 100)
                        guide = skill_improvement_guide.get(gap_info['skill'], {})
                        st.markdown(f"**📌 부족한 이유:** {guide.get('reason', '관련 경험 부족')}")
                        st.markdown(f"**💡 개선 방법:** {guide.get('solution', '관련 활동 참여 권장')}")
                else:
                    st.markdown(f"✅ **{gap_info['skill']}**: 목표 달성! ({gap_info['current']}%)")
                    st.progress(gap_info["current"] / 100)
        
        st.markdown("---")
        st.markdown("#### 🎯 맞춤형 성장 로드맵")
        
        courses = career_requirements[selected_career]["courses"]
        activities = career_requirements[selected_career]["activities"]
        
        timeline_data = []
        semesters = ["현재", "다음 학기", "1년 후", "2년 후", "졸업 전"]
        
        for i, (course, activity) in enumerate(zip(courses, activities)):
            course_name = course["name"] if isinstance(course, dict) else course
            timeline_data.append({
                "time": semesters[i] if i < len(semesters) else f"{i+1}단계",
                "course": course_name,
                "activity": activity
            })
        
        fig_timeline = go.Figure()
        
        for i, item in enumerate(timeline_data):
            fig_timeline.add_trace(go.Scatter(
                x=[i],
                y=[0],
                mode='markers+text',
                marker=dict(size=30, color='#0E4A84'),
                text=[item["time"]],
                textposition="top center",
                name=item["time"],
                hoverinfo='text',
                hovertext=f"📚 {item['course']}<br>🎯 {item['activity']}"
            ))
        
        fig_timeline.add_trace(go.Scatter(
            x=list(range(len(timeline_data))),
            y=[0] * len(timeline_data),
            mode='lines',
            line=dict(color='#0E4A84', width=3),
            showlegend=False
        ))
        
        fig_timeline.update_layout(
            showlegend=False,
            height=150,
            margin=dict(l=20, r=20, t=50, b=20),
            xaxis=dict(showticklabels=False, showgrid=False, zeroline=False),
            yaxis=dict(showticklabels=False, showgrid=False, zeroline=False, range=[-0.5, 1])
        )
        
        st.plotly_chart(fig_timeline, width="stretch")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("##### 📚 추천 과목 (한양대학교 개설 과목)")
            for i, course in enumerate(courses, 1):
                if isinstance(course, dict):
                    with st.expander(f"{i}. {course['name']} ({course['credits']}학점)"):
                        st.markdown(f"**과목코드:** {course['code']}")
                        st.markdown(f"**개설학과:** {course['department']}")
                        st.markdown(f"**학점:** {course['credits']}학점")
                        st.markdown(f"**과목설명:** {course['description']}")
                else:
                    st.markdown(f"""
                    <div style="background: #f0f4f8; padding: 10px; border-radius: 8px; margin: 5px 0; border-left: 4px solid #0E4A84;">
                        <strong>{i}. {course}</strong>
                    </div>
                    """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("##### 🎯 추천 대외활동")
            for i, activity in enumerate(activities, 1):
                st.markdown(f"""
                <div style="background: #e8f5e9; padding: 10px; border-radius: 8px; margin: 5px 0; border-left: 4px solid #28a745;">
                    <strong>{i}. {activity}</strong>
                </div>
                """, unsafe_allow_html=True)
        
        total_credits = sum(c["credits"] for c in courses if isinstance(c, dict))
        st.markdown("---")
        st.info(f"💡 **추천 근거**: {profile['name']}님의 현재 역량과 {selected_career} 직무의 필수 역량을 비교 분석한 결과입니다. 위 추천 과목은 총 {total_credits}학점이며, 부족한 역량을 중심으로 한양대학교 개설 과목과 대외활동을 제안드립니다.")

def main():
    st.markdown('<h1 class="main-header">🎓 한양챗 (HY-Chat)</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">한양대학교 학생을 위한 AI 맞춤형 비서 서비스</p>', unsafe_allow_html=True)
    
    render_sidebar()
    
    tab1, tab2, tab3 = st.tabs(["💬 AI 학사 챗봇", "🎁 장학금 추천", "🗺️ 진로 로드맵"])
    
    with tab1:
        render_chatbot()
    
    with tab2:
        render_scholarship_matcher()
    
    with tab3:
        render_career_roadmap()

if __name__ == "__main__":
    main()
