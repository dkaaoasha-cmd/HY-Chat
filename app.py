import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import random
import time
import calendar
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
    user_profile = {
        "student_id": "2022067365",
        "name": "박성동",
        "major": "기계공학과",
        "grade": 4,
        "semester": 1,
        "gpa": 3.54,
        "income_level": 1,
        "interest_career": "데이터 사이언티스트",
        "completed_credits": 105,
        "skills": {
            "프로그래밍": 70,
            "데이터분석": 83,
            "의사소통": 72,
            "문제해결": 35,
            "팀워크": 88,
            "영어능력": 65,
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
            "deadline": (datetime.now() + timedelta(days=5)).strftime("%Y-%m-%d"),
            "description": "직전 학기 성적 우수자에게 지급되는 장학금입니다.",
            "link": "https://sc.hanyang.ac.kr/home",
            "eligibility": ["직전 학기 평점 4.0 이상", "재학생 (휴학생 제외)", "성적 장학금 중복 수혜 불가", "학기당 15학점 이상 이수자"]
        },
        {
            "name": "한양 희망 장학금",
            "type": "소득연계",
            "amount": "등록금 70%",
            "requirements": {"min_gpa": 2.5, "max_income": 4},
            "deadline": (datetime.now() + timedelta(days=12)).strftime("%Y-%m-%d"),
            "description": "저소득층 학생을 위한 교내 장학금입니다.",
            "link": "https://sc.hanyang.ac.kr/home",
            "eligibility": ["소득분위 4분위 이하", "직전 학기 평점 2.5 이상", "재학생 (신입생 제외)", "국가장학금 신청 완료자"]
        },
        {
            "name": "국가근로장학금",
            "type": "근로",
            "amount": "시간당 11,150원",
            "requirements": {"min_gpa": 2.0, "max_income": 8},
            "deadline": (datetime.now() + timedelta(days=8)).strftime("%Y-%m-%d"),
            "description": "교내외 근로를 통해 지급받는 장학금입니다.",
            "link": "https://www.kosaf.go.kr",
            "eligibility": ["소득분위 8분위 이하", "직전 학기 평점 2.0 이상 (경고 1회 허용)", "대한민국 국적 소지자", "한국장학재단 국가근로장학금 신청자"]
        },
        {
            "name": "국가장학금 I유형",
            "type": "소득연계",
            "amount": "최대 570만원",
            "requirements": {"min_gpa": 2.0, "max_income": 8},
            "deadline": (datetime.now() + timedelta(days=3)).strftime("%Y-%m-%d"),
            "description": "소득분위에 따라 차등 지급되는 국가장학금입니다.",
            "link": "https://www.kosaf.go.kr",
            "eligibility": ["대한민국 국적 소지자", "소득분위 8분위 이하", "직전 학기 평점 2.0 이상", "한국장학재단 신청 필수"]
        },
        {
            "name": "이공계 국가장학금",
            "type": "특별",
            "amount": "등록금 전액 + 생활비",
            "requirements": {"min_gpa": 3.5, "max_income": 6, "major_type": "이공계"},
            "deadline": (datetime.now() + timedelta(days=18)).strftime("%Y-%m-%d"),
            "description": "이공계 전공 우수 학생을 위한 국가 장학금입니다.",
            "link": "https://www.kosaf.go.kr",
            "eligibility": ["이공계 전공자 (자연과학, 공학 계열)", "소득분위 6분위 이하", "직전 학기 평점 3.5 이상", "졸업 후 의무복무 기간 동의자"]
        },
        {
            "name": "한양 봉사장학금",
            "type": "특별",
            "amount": "100만원",
            "requirements": {"min_gpa": 2.5, "max_income": 10},
            "deadline": (datetime.now() + timedelta(days=10)).strftime("%Y-%m-%d"),
            "description": "봉사활동 우수자에게 지급되는 장학금입니다.",
            "link": "https://sc.hanyang.ac.kr/home",
            "eligibility": ["봉사활동 80시간 이상", "직전 학기 평점 2.5 이상", "재학생", "봉사활동 확인서 제출"]
        },
        {
            "name": "외부장학금 (삼성꿈장학)",
            "type": "외부",
            "amount": "등록금 전액",
            "requirements": {"min_gpa": 3.5, "max_income": 3},
            "deadline": (datetime.now() + timedelta(days=20)).strftime("%Y-%m-%d"),
            "description": "삼성에서 지원하는 저소득층 우수 학생 장학금입니다.",
            "link": "https://www.samsungfoundation.org",
            "eligibility": ["소득분위 3분위 이하", "직전 학기 평점 3.5 이상", "4학기 이상 재학생", "리더십 역량 보유자"]
        },
        {
            "name": "외국어우수장학금",
            "type": "성적",
            "amount": "200만원",
            "requirements": {"min_gpa": 3.0, "max_income": 10},
            "deadline": (datetime.now() + timedelta(days=15)).strftime("%Y-%m-%d"),
            "description": "TOEIC 900점 이상 또는 동등 수준의 외국어 능력 보유자",
            "link": "https://sc.hanyang.ac.kr/home",
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
    
    responses = [
        {
            "keywords": ["수강신청", "수강 신청", "수강신청기간", "수강신청 기간", "수강신청 언제"],
            "answer": "2024-1학기 수강신청은 2월 19일(월)부터 2월 23일(금)까지입니다. 수강신청 전 희망과목을 미리 장바구니에 담아두시고, 본인의 수강신청 시간을 확인하세요. 학년별로 시간이 다르며, 4학년이 가장 먼저 시작합니다.",
            "link": "https://portal.hanyang.ac.kr",
            "regulation": "학칙 제42조 (수강신청)"
        },
        {
            "keywords": ["장바구니", "예비수강", "희망과목"],
            "answer": "장바구니(예비수강신청)는 수강신청 1주일 전부터 이용 가능합니다. 장바구니에 담은 과목은 수강신청 시 빠르게 신청할 수 있어 경쟁 과목 수강에 유리합니다. 최대 24학점까지 담을 수 있습니다.",
            "link": "https://portal.hanyang.ac.kr",
            "regulation": "학칙 제42조 (수강신청)"
        },
        {
            "keywords": ["수강정정", "수강 정정", "정정기간", "정정 기간"],
            "answer": "수강 정정 기간은 개강 후 1주일간 진행됩니다. 수강신청과 동일하게 포털시스템에서 과목을 추가하거나 삭제할 수 있습니다. 정정 기간에는 수강 인원 제한이 완화되어 여석이 있는 과목에 추가 신청이 가능합니다.",
            "link": "https://portal.hanyang.ac.kr",
            "regulation": "학칙 제43조 (수강정정)"
        },
        {
            "keywords": ["수강취소", "수강 취소", "w학점", "취소기간"],
            "answer": "수강 취소는 학기 중 8주차~10주차에 가능합니다. 취소된 과목은 성적표에 'W'로 표기되며, 학기당 최대 3학점까지 취소 가능합니다. 졸업학기 학생은 취소가 제한될 수 있습니다.",
            "link": "https://portal.hanyang.ac.kr",
            "regulation": "학칙 제44조 (수강취소)"
        },
        {
            "keywords": ["재수강", "재 수강", "f학점", "성적갱신"],
            "answer": "재수강은 C+ 이하 성적(D+, D0, F 포함)을 받은 과목에 대해 가능합니다. 재수강 시 기존 성적은 삭제되고 새 성적으로 대체됩니다. 단, 재수강 최고 성적은 A0이며, 동일 과목은 최대 2회까지 재수강 가능합니다.",
            "link": "https://portal.hanyang.ac.kr",
            "regulation": "학칙 제45조 (재수강)"
        },
        {
            "keywords": ["학점", "몇학점", "최대학점", "학점제한", "이수학점"],
            "answer": "한 학기 최대 이수학점은 19학점이며, 직전 학기 평점 3.5 이상인 경우 22학점까지 신청 가능합니다(초과학점). 최소 이수학점은 12학점입니다. 졸업학기는 12학점 미만도 가능합니다.",
            "link": "https://portal.hanyang.ac.kr",
            "regulation": "학칙 제41조 (이수학점)"
        },
        {
            "keywords": ["성적", "학점계산", "평점", "gpa", "성적확인", "성적조회"],
            "answer": "성적은 매 학기 종강 후 2주 내에 포털시스템에서 확인 가능합니다. 평점은 4.5만점 기준이며, A+(4.5), A0(4.0), B+(3.5), B0(3.0), C+(2.5), C0(2.0), D+(1.5), D0(1.0), F(0)입니다. 성적이의신청은 성적 발표 후 3일 이내 가능합니다.",
            "link": "https://portal.hanyang.ac.kr",
            "regulation": "학칙 제48조 (성적평가)"
        },
        {
            "keywords": ["출석", "출결", "결석", "지각", "출석인정"],
            "answer": "수업 결석은 전체 수업시수의 1/4 이상 시 해당 과목 F 처리됩니다. 공결(공적 결석)은 학교 행사, 취업면접, 질병 등의 사유로 인정되며, 증빙서류를 학과에 제출해야 합니다. 지각 3회는 결석 1회로 처리됩니다.",
            "link": "https://portal.hanyang.ac.kr",
            "regulation": "학칙 제46조 (출결관리)"
        },
        {
            "keywords": ["휴학", "휴학신청", "휴학 신청", "휴학기간"],
            "answer": "휴학 신청은 포털시스템에서 가능합니다. 일반휴학(1년), 군휴학(복무기간), 임신·출산·육아휴학(최대 2년) 등이 있습니다. 등록금 납부 전에 신청해야 하며, 휴학은 통산 4년(8학기)까지 가능합니다.",
            "link": "https://www.hanyang.ac.kr/web/www/leave",
            "regulation": "학칙 제31조 (휴학)"
        },
        {
            "keywords": ["복학", "복학신청", "복학 신청", "복학절차"],
            "answer": "복학은 휴학 종료 예정 학기 시작 전 포털시스템에서 신청합니다. 군휴학자는 전역 후 1년 이내 복학해야 합니다. 복학 시 기존 학년/학과가 유지되며, 복학 신청 기간은 학사일정에서 확인하세요.",
            "link": "https://www.hanyang.ac.kr/web/www/return",
            "regulation": "학칙 제32조 (복학)"
        },
        {
            "keywords": ["자퇴", "자퇴신청", "자퇴 신청", "학교그만"],
            "answer": "자퇴는 포털시스템에서 신청 가능합니다. 자퇴 신청 시 보호자 동의서가 필요하며, 등록금 납부 전 자퇴 시 등록금이 반환됩니다. 자퇴 후 재입학은 별도 심사를 통해 가능합니다.",
            "link": "https://www.hanyang.ac.kr",
            "regulation": "학칙 제33조 (자퇴)"
        },
        {
            "keywords": ["제적", "제적사유", "미등록"],
            "answer": "제적 사유: ① 등록금 미납 ② 수업연한 초과(8년) ③ 징계(퇴학) ④ 학사경고 3회 연속 등이 있습니다. 제적 시 학적이 말소되며, 재입학 신청을 통해 복귀할 수 있습니다.",
            "link": "https://www.hanyang.ac.kr",
            "regulation": "학칙 제35조 (제적)"
        },
        {
            "keywords": ["전과", "전과신청", "전과 신청", "학과변경", "과변경"],
            "answer": "전과는 2학년 이상, 평점 3.0 이상, 35학점 이상 취득자가 신청 가능합니다. 매 학기 초 신청 기간이 공지되며, 전과 정원의 20% 내에서 선발합니다. 동일 계열 전과는 비교적 수월하나, 타 계열은 경쟁이 있습니다.",
            "link": "https://www.hanyang.ac.kr/web/www/change_major",
            "regulation": "학칙 제28조 (전과)"
        },
        {
            "keywords": ["복수전공", "복수 전공", "이중전공", "복전"],
            "answer": "복수전공은 주전공 36학점 이상 취득 후 신청 가능합니다. 복수전공 학과에서 전공필수 포함 36학점 이상 이수해야 하며, 졸업 시 두 개의 학위가 병기됩니다. 신청은 매 학기 초 포털에서 가능합니다.",
            "link": "https://www.hanyang.ac.kr/web/www/double_major",
            "regulation": "학칙 제25조 (복수전공)"
        },
        {
            "keywords": ["부전공", "부 전공"],
            "answer": "부전공은 주전공 36학점 이상 취득 후 신청 가능합니다. 부전공 학과에서 21학점 이상 이수해야 하며, 졸업증명서에 부전공이 표기됩니다. 복수전공보다 학점 부담이 적어 추천됩니다.",
            "link": "https://www.hanyang.ac.kr/web/www/minor",
            "regulation": "학칙 제26조 (부전공)"
        },
        {
            "keywords": ["연계전공", "융합전공", "학제간"],
            "answer": "연계전공은 2개 이상 학과가 공동으로 운영하는 전공입니다. 36학점 이수 시 별도 학위로 인정되며, 4차 산업혁명 관련 융합전공이 인기입니다. 신청은 매 학기 포털에서 가능합니다.",
            "link": "https://www.hanyang.ac.kr",
            "regulation": "학칙 제27조 (연계전공)"
        },
        {
            "keywords": ["졸업", "졸업요건", "졸업 요건", "졸업조건"],
            "answer": "졸업 요건: ① 130학점 이상 취득 ② 전공필수/선택 이수 ③ 교양필수 이수 ④ 영어졸업인증 ⑤ 졸업논문/시험 ⑥ 사회봉사 이수(2010학번 이후). 학과별 세부 요건이 다르니 교육과정표를 확인하세요.",
            "link": "https://www.hanyang.ac.kr/web/www/graduation",
            "regulation": "학칙 제55조 (졸업요건)"
        },
        {
            "keywords": ["영어졸업", "영어인증", "토익", "토플", "텝스", "어학인증"],
            "answer": "영어졸업인증 기준: TOEIC 700점, TOEFL iBT 71점, TEPS(New) 327점, IELTS 5.5 이상. 영어강의 12학점 이수로 대체 가능하며, 교환학생 1학기 이상도 인정됩니다. 입학년도에 따라 기준이 다를 수 있습니다.",
            "link": "https://www.hanyang.ac.kr/web/www/english_cert",
            "regulation": "졸업인증규정 제3조"
        },
        {
            "keywords": ["졸업논문", "졸업시험", "캡스톤", "졸업프로젝트"],
            "answer": "졸업논문/시험은 학과별로 다릅니다. 공학계열은 주로 캡스톤디자인으로 대체하고, 인문/사회계열은 논문 또는 졸업시험을 실시합니다. 졸업학기 전에 학과 사무실에서 요건을 확인하세요.",
            "link": "https://www.hanyang.ac.kr/web/www/thesis",
            "regulation": "학칙 제56조 (졸업논문)"
        },
        {
            "keywords": ["조기졸업", "조기 졸업", "빨리졸업"],
            "answer": "조기졸업 조건: 평점 4.0 이상, 130학점 이상, 모든 졸업요건 충족, 6학기 이상 등록. 7학기 또는 6학기 졸업이 가능하며, 졸업 예정 학기 초에 학과에 신청합니다.",
            "link": "https://www.hanyang.ac.kr/web/www/early_graduation",
            "regulation": "학칙 제57조 (조기졸업)"
        },
        {
            "keywords": ["기숙사", "생활관", "기숙사신청", "기숙사 신청"],
            "answer": "기숙사(생활관) 신청은 매 학기 초 기숙사 홈페이지(dorm.hanyang.ac.kr)에서 진행됩니다. 선발 기준: 거리점수 40% + 성적 30% + 소득분위 30%. 합격 여부는 홈페이지에서 확인 가능합니다.",
            "link": "https://dorm.hanyang.ac.kr",
            "regulation": "기숙사 운영규정 제5조"
        },
        {
            "keywords": ["기숙사비", "기숙사 비용", "생활관비"],
            "answer": "2024년 기숙사비: 2인실 약 150~180만원/학기, 4인실 약 100~130만원/학기 (식비 별도). 식권은 월 15만원 내외입니다. 정확한 금액은 기숙사 홈페이지 공지를 확인하세요.",
            "link": "https://dorm.hanyang.ac.kr",
            "regulation": "기숙사 운영규정 제12조"
        },
        {
            "keywords": ["기숙사규정", "기숙사 규정", "통금", "벌점"],
            "answer": "기숙사 주요 규정: ① 24시 통금 ② 외부인 출입 금지 ③ 음주/흡연 금지 ④ 취사 금지 ⑤ 소음 규제. 규정 위반 시 벌점 부과되며, 15점 초과 시 퇴사 조치됩니다.",
            "link": "https://dorm.hanyang.ac.kr",
            "regulation": "기숙사 생활규정"
        },
        {
            "keywords": ["등록금", "등록금납부", "등록금 납부", "학비"],
            "answer": "등록금은 매 학기 초 가상계좌로 고지되며, 납부 기간 내 은행 이체, 신용카드, 창구 납부 가능합니다. 2024년 공학계열 약 480만원, 인문/사회 약 400만원 수준입니다. 미납 시 미등록 처리됩니다.",
            "link": "https://finance.hanyang.ac.kr",
            "regulation": "학칙 제17조 (등록금)"
        },
        {
            "keywords": ["분납", "등록금분납", "등록금 분납", "할부"],
            "answer": "등록금 분할납부(2~4회)가 가능합니다. 납부 기간 전 포털에서 분납 신청 후, 각 회차 기한 내 납부하면 됩니다. 추가 수수료는 없습니다. 분납 신청 후 취소는 불가합니다.",
            "link": "https://finance.hanyang.ac.kr",
            "regulation": "등록금규정 제8조"
        },
        {
            "keywords": ["장학금", "장학금종류", "교내장학"],
            "answer": "교내장학금 종류: ① 한양브레인(성적) ② 한양희망(소득연계) ③ 국가근로장학금 ④ 봉사장학금 ⑤ 외국어우수장학금 ⑥ 리더십장학금 등. 매 학기 포털에서 신청하며, 성적/소득 조건이 다릅니다.",
            "link": "https://sc.hanyang.ac.kr/home",
            "regulation": "장학규정 제5조"
        },
        {
            "keywords": ["국가장학금", "한국장학재단", "kosaf"],
            "answer": "국가장학금은 한국장학재단(kosaf.go.kr)에서 신청합니다. I유형(소득연계)은 8구간 이하, II유형(대학연계)은 학교별 기준으로 지원됩니다. 신청 기간: 학기 시작 2개월 전~1개월 전. 1구간 최대 학기당 285만원 지원.",
            "link": "https://www.kosaf.go.kr",
            "regulation": "국가장학금 운영규정"
        },
        {
            "keywords": ["근로장학", "근로장학금", "교내근로"],
            "answer": "국가근로장학금은 한국장학재단에서 신청하며, 교내근로(시급 11,150원)와 교외근로가 있습니다. 소득 8분위 이하, 성적 2.0 이상이 조건입니다. 학기 중 주 20시간, 방학 중 주 40시간 이내 근무 가능합니다.",
            "link": "https://www.kosaf.go.kr",
            "regulation": "국가근로장학금 운영지침"
        },
        {
            "keywords": ["학사경고", "학사 경고", "경고", "유급"],
            "answer": "학사경고: 학기 평점 1.75 미만 시 부과됩니다. 3회 연속 경고 시 제적 사유가 됩니다. 학사경고 학생은 다음 학기 19학점 초과 신청이 제한되며, 학습상담이 권장됩니다.",
            "link": "https://www.hanyang.ac.kr",
            "regulation": "학칙 제53조 (학사경고)"
        },
        {
            "keywords": ["교양", "교양필수", "핵심교양", "기초교양"],
            "answer": "교양 이수 체계: ① 기초교양(글쓰기, 영어 등 필수) ② 핵심교양(5개 영역 중 3개 이상) ③ 일반교양. 입학년도별 교육과정이 다르니 본인 학번의 교육과정표를 확인하세요. 최소 35학점 이상 이수해야 합니다.",
            "link": "https://www.hanyang.ac.kr/web/www/liberal_arts",
            "regulation": "교양교육과정 운영규정"
        },
        {
            "keywords": ["전공필수", "전공선택", "전공학점", "전공과목"],
            "answer": "전공 이수: 전공필수(학과 지정 필수과목) + 전공선택으로 구성됩니다. 단일전공 시 최소 60학점, 복수전공 시 36학점씩 이수해야 합니다. 전공필수 미이수 시 졸업 불가합니다.",
            "link": "https://www.hanyang.ac.kr",
            "regulation": "학칙 제40조 (전공이수)"
        },
        {
            "keywords": ["포털", "hyu 포털", "portal", "학생포털"],
            "answer": "한양대학교 포털(portal.hanyang.ac.kr)에서 수강신청, 성적조회, 증명서 발급, 휴복학 신청 등 대부분의 학사업무를 처리할 수 있습니다. 초기 비밀번호는 생년월일 6자리이며, 로그인 후 변경하세요.",
            "link": "https://portal.hanyang.ac.kr",
            "regulation": "정보시스템 운영규정"
        },
        {
            "keywords": ["증명서", "재학증명", "성적증명", "졸업증명", "발급"],
            "answer": "증명서 발급: ① 포털 온라인 발급 ② 무인발급기(도서관, 학생회관) ③ 학과 사무실. 영문증명서도 발급 가능하며, 일부는 수수료(500~1,000원)가 부과됩니다. 졸업생은 총동창회관에서도 발급 가능합니다.",
            "link": "https://portal.hanyang.ac.kr",
            "regulation": "학사운영규정 제15조"
        },
        {
            "keywords": ["도서관", "중앙도서관", "열람실", "도서대출"],
            "answer": "백남학술정보관(중앙도서관)은 평일 08:00~22:00, 주말 09:00~18:00 운영됩니다. 도서 대출은 학부생 10권/2주, 대학원생 20권/4주입니다. 열람실 좌석은 모바일앱으로 예약 가능합니다.",
            "link": "https://lib.hanyang.ac.kr",
            "regulation": "도서관 운영규정"
        },
        {
            "keywords": ["학생증", "id카드", "모바일학생증"],
            "answer": "학생증은 입학 시 자동 발급되며, 분실 시 학생지원팀에서 재발급(수수료 5,000원) 받을 수 있습니다. 모바일학생증은 한양대 앱에서 발급 가능하며, 도서관/기숙사 출입에 사용됩니다.",
            "link": "https://www.hanyang.ac.kr",
            "regulation": "학생증 발급규정"
        },
        {
            "keywords": ["학식", "학생식당", "식당", "기숙사 식당", "밥"],
            "answer": "학생식당은 학생회관, 기숙사, 각 단과대 건물에 위치합니다. 가격은 3,500~6,000원 수준이며, 포털에서 주간 메뉴를 확인할 수 있습니다. 기숙사 식권은 별도 구매합니다.",
            "link": "https://www.hanyang.ac.kr",
            "regulation": "복지시설 운영규정"
        },
        {
            "keywords": ["상담", "심리상담", "학생상담", "고민"],
            "answer": "학생상담센터에서 심리상담, 진로상담, 학습상담을 무료로 제공합니다. 예약은 전화(02-2220-1191) 또는 온라인으로 가능합니다. 개인상담, 집단상담, 심리검사 등 다양한 프로그램이 있습니다.",
            "link": "https://counsel.hanyang.ac.kr",
            "regulation": "학생상담센터 운영규정"
        },
        {
            "keywords": ["취업", "취업지원", "경력개발", "진로"],
            "answer": "경력개발센터에서 취업상담, 이력서 첨삭, 모의면접, 취업특강 등을 지원합니다. 채용정보는 HY-CDP 시스템에서 확인 가능하며, 기업설명회/채용박람회도 연중 개최됩니다.",
            "link": "https://career.hanyang.ac.kr",
            "regulation": "경력개발센터 운영규정"
        },
        {
            "keywords": ["교환학생", "해외교류", "유학", "교환"],
            "answer": "교환학생 프로그램은 국제협력처에서 운영합니다. 지원 자격: 2학년 이상, 평점 2.5~3.0 이상(학교별 상이), 어학성적 보유. 모집은 매년 3월(2학기 파견)과 9월(1학기 파견)에 진행됩니다.",
            "link": "https://www.hanyangoia.com",
            "regulation": "국제교류 규정"
        },
        {
            "keywords": ["동아리", "학회", "소모임"],
            "answer": "중앙동아리(총학생회 소속)와 단과대 동아리가 있습니다. 동아리 가입은 학기 초 동아리박람회 또는 각 동아리 SNS를 통해 가능합니다. 활동비 지원을 받으려면 정식 등록이 필요합니다.",
            "link": "https://www.hanyang.ac.kr",
            "regulation": "학생자치활동 규정"
        },
        {
            "keywords": ["군대", "군입대", "군휴학", "병역"],
            "answer": "군휴학은 입영통지서 수령 후 포털에서 신청합니다. 군복무 기간 동안 자동 휴학 처리되며, 전역 후 1년 이내 복학해야 합니다. 학점은행제를 통해 군 복무 중에도 학점 취득이 가능합니다.",
            "link": "https://www.hanyang.ac.kr",
            "regulation": "학칙 제31조 (휴학)"
        },
        {
            "keywords": ["계절학기", "여름학기", "겨울학기", "방학수업"],
            "answer": "계절학기(하계/동계)는 방학 중 4~5주간 진행됩니다. 최대 6학점까지 수강 가능하며, 별도 등록금(학점당 약 8만원)이 부과됩니다. 수강신청은 학기 종료 전 포털에서 진행합니다.",
            "link": "https://portal.hanyang.ac.kr",
            "regulation": "계절학기 운영규정"
        },
        {
            "keywords": ["학점교류", "타대학", "국내교류", "학점인정"],
            "answer": "국내 대학 간 학점교류로 타 대학 과목 수강이 가능합니다. 학기당 6학점 이내이며, 협정 대학(서울권 주요 대학) 과목 중 선택합니다. 신청은 수강신청 기간에 포털에서 진행합니다.",
            "link": "https://www.hanyang.ac.kr",
            "regulation": "학점교류 규정"
        },
        {
            "keywords": ["사회봉사", "봉사활동", "봉사학점"],
            "answer": "2010학번 이후 학생은 '사회봉사' 교과목(1학점, 32시간)을 필수로 이수해야 합니다. 한양봉사단, 교내봉사, 외부기관 봉사 등으로 시간을 채울 수 있으며, 1365 또는 VMS에서 봉사시간을 인정받습니다.",
            "link": "https://www.hanyang.ac.kr",
            "regulation": "사회봉사 운영지침"
        },
        {
            "keywords": ["셔틀버스", "통학버스", "셔틀", "버스"],
            "answer": "교내 셔틀버스는 정문-공대-기숙사 노선이 운행됩니다. 또한 지하철 왕십리역, 한양대역에서 도보 10분 거리입니다. 통학버스 시간표는 포털 공지사항에서 확인하세요.",
            "link": "https://www.hanyang.ac.kr",
            "regulation": "교통편의시설 운영규정"
        },
        {
            "keywords": ["건물", "강의실", "캠퍼스맵", "위치"],
            "answer": "한양대학교 서울캠퍼스는 성동구 왕십리에 위치합니다. 주요 건물: 백남학술정보관(도서관), 한양종합기술연구원(HIT), 신본관, 경영관 등. 캠퍼스맵은 학교 홈페이지에서 확인 가능합니다.",
            "link": "https://www.hanyang.ac.kr",
            "regulation": "시설관리규정"
        },
        {
            "keywords": ["와이파이", "wifi", "인터넷", "네트워크"],
            "answer": "교내 Wi-Fi는 'HYU' 또는 'eduroam'을 사용합니다. 포털 아이디/비밀번호로 로그인하며, 전 건물에서 이용 가능합니다. 접속 문제 시 정보통신처(02-2220-0114)로 문의하세요.",
            "link": "https://www.hanyang.ac.kr",
            "regulation": "정보통신시설 운영규정"
        },
        {
            "keywords": ["프린터", "출력", "복사", "스캔"],
            "answer": "도서관 각 층에 복합기(프린터/복사/스캔)가 있습니다. 출력비용: 흑백 50원, 컬러 200원/장. 학생증 또는 현금으로 결제하며, 일부 컴퓨터실에서는 무료 출력이 가능합니다.",
            "link": "https://lib.hanyang.ac.kr",
            "regulation": "도서관 시설이용규정"
        },
        {
            "keywords": ["장애학생", "장애", "편의시설", "특수교육"],
            "answer": "장애학생지원센터에서 학습지원(대필, 속기, 점자), 이동지원, 보조공학기기 대여 등을 제공합니다. 장애학생 특별전형 입학자와 장애인등록증 소지자가 대상입니다.",
            "link": "https://disability.hanyang.ac.kr",
            "regulation": "장애학생지원규정"
        },
        {
            "keywords": ["등록금환불", "환불", "반환"],
            "answer": "등록금 환불: 개강 전 100%, 1/4 경과 전 75%, 2/4 경과 전 50%, 3/4 경과 전 25%, 이후 0%. 휴학/자퇴 시 해당 기간에 따라 환불됩니다. 재무팀(02-2220-0044)으로 문의하세요.",
            "link": "https://finance.hanyang.ac.kr",
            "regulation": "등록금규정 제15조"
        }
    ]
    
    for item in responses:
        for keyword in item["keywords"]:
            if keyword in question_lower:
                return {
                    "answer": item["answer"],
                    "link": item["link"],
                    "regulation": item["regulation"]
                }
    
    return {
        "answer": f"'{question}'에 대한 정확한 정보를 찾지 못했습니다. 아래 카테고리에서 키워드를 선택하시거나, 더 구체적인 단어로 질문해 주세요.\n\n💡 **자주 묻는 질문 예시:**\n• 수강신청 기간이 언제야?\n• 휴학 신청 어떻게 해?\n• 졸업 요건이 뭐야?\n• 장학금 종류 알려줘\n• 기숙사 신청 방법\n• 복수전공 조건이 뭐야?\n• 학점 몇 학점까지 들을 수 있어?\n• 도서관 몇 시까지 해?",
        "link": "https://www.hanyang.ac.kr",
        "regulation": "한양대학교 학칙"
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
    if not st.session_state.get("data_generated", False):
        user_profile, academic_notices, scholarships, career_requirements = generate_dummy_data()
        st.session_state.user_profile = user_profile
        st.session_state.academic_notices = academic_notices
        st.session_state.scholarships = scholarships
        st.session_state.career_requirements = career_requirements
        st.session_state.data_generated = True
    
    with st.sidebar:
        st.markdown("### 🎓 한양챗 (HY-Chat)")
        st.markdown("---")
        
        profile = st.session_state.user_profile
        
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #0E4A84 0%, #1a6fc4 100%); border-radius: 12px; overflow: hidden; box-shadow: 0 4px 15px rgba(14, 74, 132, 0.3); margin-bottom: 15px;">
            <div style="padding: 18px; text-align: center; border-bottom: 1px solid rgba(255,255,255,0.2);">
                <div style="width: 70px; height: 70px; background: white; border-radius: 50%; margin: 0 auto 12px; display: flex; align-items: center; justify-content: center; font-size: 34px;">👤</div>
                <h3 style="color: white; margin: 0; font-size: 22px; font-weight: bold;">{profile['name']}</h3>
                <p style="color: rgba(255,255,255,0.9); margin: 8px 0 0 0; font-size: 16px;">{profile['major']}</p>
            </div>
            <div style="padding: 15px;">
                <div style="background: white; border-radius: 10px; padding: 14px; margin-bottom: 10px;">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
                        <span style="color: #666; font-size: 15px;">🔢 학번</span>
                        <span style="color: #0E4A84; font-weight: bold; font-size: 16px;">{profile['student_id']}</span>
                    </div>
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
                        <span style="color: #666; font-size: 15px;">📅 학년</span>
                        <span style="color: #0E4A84; font-weight: bold; font-size: 16px;">{profile['grade']}학년 {profile['semester']}학기</span>
                    </div>
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <span style="color: #666; font-size: 15px;">📊 학점</span>
                        <span style="color: #0E4A84; font-weight: bold; font-size: 16px;">{profile['gpa']}/4.5</span>
                    </div>
                </div>
                <div style="background: rgba(255,255,255,0.15); border-radius: 10px; padding: 14px;">
                    <p style="color: rgba(255,255,255,0.8); font-size: 14px; margin: 0 0 6px 0;">🎯 관심 직무</p>
                    <p style="color: white; font-weight: bold; margin: 0; font-size: 17px;">{profile['interest_career']}</p>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

def render_chatbot():
    st.markdown("### 💬 AI 학사 챗봇")
    st.markdown("학사 관련 궁금한 점을 질문해 주세요! 아래 키워드를 선택하거나 직접 입력할 수 있습니다.")
    
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "selected_category" not in st.session_state:
        st.session_state.selected_category = None
    
    chatbot_categories = {
        "📝 수강신청": {
            "icon": "📝",
            "subcategories": {
                "수강신청 기간": "수강신청 기간이 언제인가요?",
                "수강신청 방법": "수강신청은 어떻게 하나요?",
                "수강 정정": "수강 정정 기간과 방법이 궁금해요",
                "수강 취소": "수강 취소는 어떻게 하나요?",
                "재수강 규정": "재수강 규정이 어떻게 되나요?"
            }
        },
        "🏠 기숙사": {
            "icon": "🏠",
            "subcategories": {
                "기숙사 신청": "기숙사 신청 방법을 알려주세요",
                "기숙사 비용": "기숙사 비용이 얼마인가요?",
                "입퇴사 일정": "기숙사 입퇴사 일정이 궁금해요",
                "기숙사 규정": "기숙사 생활 규정을 알려주세요",
                "호실 배정": "기숙사 호실 배정은 어떻게 되나요?"
            }
        },
        "📋 학사 행정": {
            "icon": "📋",
            "subcategories": {
                "휴학 신청": "휴학은 어떻게 신청하나요?",
                "복학 신청": "복학 절차가 어떻게 되나요?",
                "전과 신청": "전과 신청 방법을 알려주세요",
                "복수전공": "복수전공 신청 조건이 뭔가요?",
                "학적 증명서": "학적 증명서 발급 방법이 궁금해요"
            }
        },
        "🎓 졸업": {
            "icon": "🎓",
            "subcategories": {
                "졸업 요건": "졸업 요건이 어떻게 되나요?",
                "졸업 학점": "졸업에 필요한 학점이 몇 학점인가요?",
                "영어 졸업인증": "영어 졸업인증 기준이 뭔가요?",
                "졸업 논문": "졸업 논문/시험은 어떻게 되나요?",
                "조기 졸업": "조기 졸업 조건이 뭔가요?"
            }
        },
        "💰 등록금·장학": {
            "icon": "💰",
            "subcategories": {
                "등록금 납부": "등록금 납부 방법을 알려주세요",
                "등록금 분납": "등록금 분할 납부가 가능한가요?",
                "장학금 종류": "어떤 장학금이 있나요?",
                "장학금 신청": "장학금 신청은 어떻게 하나요?",
                "국가장학금": "국가장학금 신청 방법이 궁금해요"
            }
        }
    }
    
    detailed_responses = {
        "수강신청 기간": {
            "answer": "2024-1학기 수강신청은 2월 19일(월)부터 2월 23일(금)까지입니다. 학년별로 수강신청 시간이 다르니 포털에서 본인의 수강신청 시간을 꼭 확인하세요. 수강신청 전 장바구니에 희망 과목을 미리 담아두시기 바랍니다.",
            "link": "https://portal.hanyang.ac.kr",
            "regulation": "학칙 제42조 (수강신청)"
        },
        "수강신청 방법": {
            "answer": "수강신청은 한양대학교 포털시스템(portal.hanyang.ac.kr)에서 진행됩니다. 1) 포털 로그인 → 2) 학사행정 → 3) 수강신청 → 4) 과목 검색 및 신청 순서로 진행하세요. 수강신청 전 장바구니 기능을 활용하여 미리 과목을 담아두면 편리합니다.",
            "link": "https://portal.hanyang.ac.kr",
            "regulation": "학칙 제42조 (수강신청)"
        },
        "수강 정정": {
            "answer": "수강 정정 기간은 개강 후 1주일간 진행됩니다. 수강신청과 동일하게 포털시스템에서 과목을 추가하거나 삭제할 수 있습니다. 정정 기간에는 수강 인원 제한이 완화되어 여석이 있는 과목에 추가 신청이 가능합니다.",
            "link": "https://portal.hanyang.ac.kr",
            "regulation": "학칙 제43조 (수강정정)"
        },
        "수강 취소": {
            "answer": "수강 취소는 학기 중 일정 기간 내에 가능합니다. 취소된 과목은 성적표에 'W'로 표기되며, 학기당 취소 가능 학점 제한이 있습니다. 수강 취소 기간은 학사일정에서 확인하세요.",
            "link": "https://portal.hanyang.ac.kr",
            "regulation": "학칙 제44조 (수강취소)"
        },
        "재수강 규정": {
            "answer": "재수강은 C+ 이하 성적을 받은 과목에 대해 가능합니다. 재수강 시 기존 성적은 삭제되고 새 성적으로 대체됩니다. 단, 재수강으로 받을 수 있는 최고 성적은 A0입니다. 동일 과목은 최대 2회까지 재수강 가능합니다.",
            "link": "https://www.hanyang.ac.kr/web/www/re-enrollment",
            "regulation": "학칙 제45조 (재수강)"
        },
        "기숙사 신청": {
            "answer": "기숙사 신청은 매 학기 초 한양대학교 기숙사 홈페이지에서 진행됩니다. 신청 기간 내에 온라인으로 신청하며, 성적, 거리, 소득분위 등을 종합하여 선발합니다. 합격 여부는 기숙사 홈페이지에서 확인 가능합니다.",
            "link": "https://dorm.hanyang.ac.kr",
            "regulation": "기숙사 운영규정 제5조"
        },
        "기숙사 비용": {
            "answer": "기숙사비는 기숙사 유형(2인실, 4인실 등)과 식사 포함 여부에 따라 다릅니다. 2024년 기준 2인실 약 150만원~180만원(학기), 4인실 약 100만원~130만원(학기) 수준입니다. 정확한 금액은 기숙사 홈페이지에서 확인하세요.",
            "link": "https://dorm.hanyang.ac.kr",
            "regulation": "기숙사 운영규정 제12조"
        },
        "입퇴사 일정": {
            "answer": "입사일은 개강 2~3일 전, 퇴사일은 종강 후 2~3일 이내입니다. 정확한 일정은 매 학기 기숙사 공지사항에서 확인하세요. 조기 퇴사나 방학 중 잔류는 별도 신청이 필요합니다.",
            "link": "https://dorm.hanyang.ac.kr",
            "regulation": "기숙사 운영규정 제8조"
        },
        "기숙사 규정": {
            "answer": "기숙사 주요 규정: 1) 통금시간 준수 (24시) 2) 외부인 출입 금지 3) 음주/흡연 금지 4) 취사 금지 (지정 장소 제외) 5) 소음 규제 등이 있습니다. 규정 위반 시 벌점이 부과되며, 누적 시 퇴사 조치될 수 있습니다.",
            "link": "https://dorm.hanyang.ac.kr",
            "regulation": "기숙사 생활규정"
        },
        "호실 배정": {
            "answer": "호실 배정은 기숙사 선발 후 무작위 또는 선착순으로 진행됩니다. 룸메이트 신청 기능을 통해 원하는 친구와 같은 방을 사용할 수도 있습니다. 배정 결과는 기숙사 홈페이지에서 확인 가능합니다.",
            "link": "https://dorm.hanyang.ac.kr",
            "regulation": "기숙사 운영규정 제7조"
        },
        "휴학 신청": {
            "answer": "휴학 신청은 한양대학교 포털시스템(portal.hanyang.ac.kr)에서 가능합니다. 일반휴학, 군휴학, 임신·출산 휴학 등이 있으며, 등록금 납부 전에 신청해야 합니다. 휴학 기간은 1년 단위이며, 최대 4년까지 가능합니다.",
            "link": "https://www.hanyang.ac.kr/web/www/leave",
            "regulation": "학칙 제31조 (휴학)"
        },
        "복학 신청": {
            "answer": "복학은 휴학 기간 종료 전 포털시스템에서 신청합니다. 군휴학의 경우 전역 후 복학 신청하며, 복학 시 소속 학과와 학년이 유지됩니다. 복학 신청 기간은 학사일정을 확인하세요.",
            "link": "https://www.hanyang.ac.kr/web/www/return",
            "regulation": "학칙 제32조 (복학)"
        },
        "전과 신청": {
            "answer": "전과는 2학년 이상, 평점 3.0 이상인 학생만 신청 가능합니다. 매 학기 초에 신청 기간이 공지되며, 전과 정원 및 세부 조건은 학과별로 다릅니다. 전과 신청서와 성적증명서를 제출해야 합니다.",
            "link": "https://www.hanyang.ac.kr/web/www/change_major",
            "regulation": "학칙 제28조 (전과)"
        },
        "복수전공": {
            "answer": "복수전공은 주전공 36학점 이상 취득 후 신청 가능합니다. 복수전공 이수를 위해서는 해당 전공의 필수과목을 포함하여 36학점 이상을 이수해야 합니다. 신청 기간은 매 학기 학사일정에서 확인하세요.",
            "link": "https://www.hanyang.ac.kr/web/www/double_major",
            "regulation": "학칙 제25조 (복수전공)"
        },
        "학적 증명서": {
            "answer": "학적 증명서(재학증명서, 성적증명서 등)는 포털시스템 또는 무인발급기에서 발급 가능합니다. 영문 증명서도 발급 가능하며, 일부 증명서는 수수료가 발생할 수 있습니다.",
            "link": "https://portal.hanyang.ac.kr",
            "regulation": "학사운영규정 제15조"
        },
        "졸업 요건": {
            "answer": "졸업을 위해서는 ① 130학점 이상 취득 ② 전공필수 과목 이수 ③ 교양필수 과목 이수 ④ 영어졸업인증 ⑤ 졸업논문/시험이 필요합니다. 세부 요건은 학과별로 다를 수 있으니 학과 사무실에 문의하세요.",
            "link": "https://www.hanyang.ac.kr/web/www/graduation",
            "regulation": "학칙 제55조 (졸업요건)"
        },
        "졸업 학점": {
            "answer": "졸업에 필요한 최소 학점은 130학점입니다. 전공 최소 이수학점, 교양 최소 이수학점 등 세부 요건이 있으며, 복수전공/부전공 시 추가 학점이 필요합니다. 자세한 내용은 학과 교육과정을 확인하세요.",
            "link": "https://www.hanyang.ac.kr/web/www/graduation",
            "regulation": "학칙 제55조 (졸업요건)"
        },
        "영어 졸업인증": {
            "answer": "영어 졸업인증 기준: TOEIC 700점 이상, TOEFL iBT 71점 이상, TEPS 556점 이상 등입니다. 영어 강의 일정 학점 이수로도 대체 가능합니다. 인증 기준은 입학년도에 따라 다를 수 있으니 확인이 필요합니다.",
            "link": "https://www.hanyang.ac.kr/web/www/english_cert",
            "regulation": "졸업인증규정 제3조"
        },
        "졸업 논문": {
            "answer": "졸업논문 또는 졸업시험은 학과별로 운영 방식이 다릅니다. 일부 학과는 논문 제출, 일부 학과는 졸업시험, 일부 학과는 캡스톤 프로젝트로 대체합니다. 본인 학과의 졸업 요건을 확인하세요.",
            "link": "https://www.hanyang.ac.kr/web/www/thesis",
            "regulation": "학칙 제56조 (졸업논문)"
        },
        "조기 졸업": {
            "answer": "조기 졸업은 평점 4.0 이상, 130학점 이상 취득, 모든 졸업 요건 충족 시 신청 가능합니다. 최소 6학기 이상 등록해야 하며, 조기 졸업 신청은 졸업 예정 학기 초에 학과에 신청합니다.",
            "link": "https://www.hanyang.ac.kr/web/www/early_graduation",
            "regulation": "학칙 제57조 (조기졸업)"
        },
        "등록금 납부": {
            "answer": "등록금 납부는 매 학기 초 고지서 발송 후 지정된 기간 내에 납부해야 합니다. 가상계좌 이체, 신용카드, 은행 창구 납부 등이 가능합니다. 납부 기한을 놓치면 미등록 처리될 수 있으니 주의하세요.",
            "link": "https://finance.hanyang.ac.kr",
            "regulation": "학칙 제17조 (등록금)"
        },
        "등록금 분납": {
            "answer": "등록금 분할 납부(분납)는 2~4회 분할이 가능합니다. 분납 신청은 등록금 납부 기간 전에 포털시스템에서 신청해야 합니다. 분납 시 추가 수수료는 없으나, 각 회차 납부 기한을 준수해야 합니다.",
            "link": "https://finance.hanyang.ac.kr",
            "regulation": "등록금규정 제8조"
        },
        "장학금 종류": {
            "answer": "한양대학교는 성적장학금(한양브레인), 소득연계장학금(한양희망), 근로장학금, 외국어우수장학금, 봉사장학금 등 다양한 교내장학금과 국가장학금, 외부장학금을 제공합니다. 자세한 내용은 장학안내 페이지에서 확인하세요.",
            "link": "https://sc.hanyang.ac.kr/home",
            "regulation": "장학규정 제5조"
        },
        "장학금 신청": {
            "answer": "장학금 신청은 매 학기 초 포털시스템 또는 장학안내 홈페이지에서 가능합니다. 장학금 종류별로 신청 기간과 방법이 다르니 공지사항을 확인하세요. 국가장학금은 한국장학재단(kosaf.go.kr)에서 별도 신청해야 합니다.",
            "link": "https://sc.hanyang.ac.kr/home",
            "regulation": "장학규정 제10조"
        },
        "국가장학금": {
            "answer": "국가장학금은 한국장학재단(kosaf.go.kr)에서 신청합니다. 소득분위에 따라 지원 금액이 달라지며, 1~3구간은 학기당 최대 285만원까지 지원됩니다. 신청 기간은 매 학기 시작 전 약 2개월간입니다.",
            "link": "https://www.kosaf.go.kr",
            "regulation": "국가장학금 운영규정"
        }
    }
    
    st.markdown("---")
    st.markdown("##### 🔍 키워드로 빠르게 찾기")
    
    st.markdown("""
    <style>
    div[data-testid="column"] > div > div > div > button {
        font-size: 12px !important;
        padding: 0.3rem 0.5rem !important;
        white-space: nowrap !important;
    }
    </style>
    """, unsafe_allow_html=True)
    
    cols = st.columns(5, gap="small")
    for idx, (category, data) in enumerate(chatbot_categories.items()):
        with cols[idx]:
            if st.button(category, key=f"cat_{idx}", use_container_width=True):
                st.session_state.selected_category = category
                st.session_state.selected_subcategory = None
                st.rerun()
    
    if st.session_state.selected_category:
        category = st.session_state.selected_category
        st.markdown(f"##### {category} 관련 질문")
        
        subcats = chatbot_categories[category]["subcategories"]
        sub_cols = st.columns(len(subcats))
        
        for idx, (subcat_name, subcat_query) in enumerate(subcats.items()):
            with sub_cols[idx]:
                if st.button(subcat_name, key=f"sub_{idx}"):
                    st.session_state.messages.append({"role": "user", "content": subcat_query})
                    response = detailed_responses.get(subcat_name, get_chatbot_response(subcat_query, []))
                    st.session_state.messages.append({
                        "role": "assistant",
                        "content": response["answer"],
                        "metadata": {"link": response["link"], "regulation": response["regulation"]}
                    })
                    st.session_state.selected_category = None
                    st.rerun()
        
        if st.button("← 카테고리 다시 선택", key="back_btn"):
            st.session_state.selected_category = None
            st.rerun()
    
    st.markdown("---")
    
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
    
    if prompt := st.chat_input("직접 질문을 입력하세요 (예: 수강신청 기간이 언제야?)"):
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
        <p style="margin: 10px 0 0 0;">학점: {profile['gpa']}/4.5 | 전공: {profile['major']}</p>
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
    
    st.markdown("### 📅 장학금 신청 일정 캘린더")
    st.markdown("장학금 신청 마감일을 한눈에 확인하세요!")
    
    today = datetime.now()
    
    scholarship_types = {
        "성적": {"color": "#0E4A84", "icon": "🏆"},
        "소득연계": {"color": "#28a745", "icon": "💰"},
        "근로": {"color": "#ffc107", "icon": "👷"},
        "외부": {"color": "#17a2b8", "icon": "🌐"},
        "특별": {"color": "#dc3545", "icon": "⭐"}
    }
    
    if "scholarship_cal_year" not in st.session_state:
        st.session_state.scholarship_cal_year = today.year
    if "scholarship_cal_month" not in st.session_state:
        st.session_state.scholarship_cal_month = today.month
    
    nav_col1, nav_col2, nav_col3 = st.columns([1, 2, 1])
    with nav_col1:
        if st.button("◀ 이전 달", key="sch_prev"):
            if st.session_state.scholarship_cal_month == 1:
                st.session_state.scholarship_cal_month = 12
                st.session_state.scholarship_cal_year -= 1
            else:
                st.session_state.scholarship_cal_month -= 1
            st.rerun()
    with nav_col2:
        st.markdown(f"<h4 style='text-align: center;'>{st.session_state.scholarship_cal_year}년 {st.session_state.scholarship_cal_month}월</h4>", unsafe_allow_html=True)
    with nav_col3:
        if st.button("다음 달 ▶", key="sch_next"):
            if st.session_state.scholarship_cal_month == 12:
                st.session_state.scholarship_cal_month = 1
                st.session_state.scholarship_cal_year += 1
            else:
                st.session_state.scholarship_cal_month += 1
            st.rerun()
    
    if st.button("📍 오늘로 이동", key="sch_today"):
        st.session_state.scholarship_cal_year = today.year
        st.session_state.scholarship_cal_month = today.month
        st.rerun()
    
    st.markdown("""
    <style>
    .sch-cal-grid {
        display: grid;
        grid-template-columns: repeat(7, 1fr);
        gap: 1px;
        background-color: #e0e0e0;
        border: 1px solid #e0e0e0;
        border-radius: 8px;
        overflow: hidden;
    }
    .sch-cal-header {
        background-color: #0E4A84;
        color: white;
        padding: 10px;
        text-align: center;
        font-weight: bold;
    }
    .sch-cal-header-sat { background-color: #0066cc; }
    .sch-cal-header-sun { background-color: #dc3545; }
    .sch-cal-day {
        background-color: #fff;
        min-height: 90px;
        padding: 5px;
        vertical-align: top;
    }
    .sch-cal-day-empty { background-color: #f5f5f5; }
    .sch-cal-day-today { background-color: #e3f2fd; border: 2px solid #0E4A84; }
    .sch-cal-day-num {
        font-weight: bold;
        font-size: 14px;
        margin-bottom: 3px;
    }
    .sch-cal-day-num-today { color: #0E4A84; }
    .sch-cal-event {
        font-size: 10px;
        padding: 2px 4px;
        margin: 1px 0;
        color: white;
        border-radius: 3px;
        overflow: hidden;
        text-overflow: ellipsis;
        white-space: nowrap;
        display: block;
    }
    .sch-cal-more {
        font-size: 9px;
        color: #666;
        padding: 1px 2px;
    }
    </style>
    """, unsafe_allow_html=True)
    
    weekdays = ["월", "화", "수", "목", "금", "토", "일"]
    
    cal_module = calendar.Calendar(firstweekday=0)
    month_days = cal_module.monthdayscalendar(st.session_state.scholarship_cal_year, st.session_state.scholarship_cal_month)
    
    header_html = ""
    for i, day_name in enumerate(weekdays):
        header_class = "sch-cal-header"
        if i == 5:
            header_class += " sch-cal-header-sat"
        elif i == 6:
            header_class += " sch-cal-header-sun"
        header_html += f"<div class='{header_class}'>{day_name}</div>"
    
    scholarships_by_deadline = {}
    for sch in scholarship_matches:
        deadline = sch["deadline"]
        if deadline not in scholarships_by_deadline:
            scholarships_by_deadline[deadline] = []
        scholarships_by_deadline[deadline].append(sch)
    
    all_weeks_html = header_html
    
    for week in month_days:
        for i, day in enumerate(week):
            if day == 0:
                all_weeks_html += "<div class='sch-cal-day sch-cal-day-empty'></div>"
            else:
                date_str = f"{st.session_state.scholarship_cal_year}-{st.session_state.scholarship_cal_month:02d}-{day:02d}"
                date_obj = datetime(st.session_state.scholarship_cal_year, st.session_state.scholarship_cal_month, day)
                is_today = (date_obj.date() == today.date())
                
                day_class = "sch-cal-day sch-cal-day-today" if is_today else "sch-cal-day"
                num_class = "sch-cal-day-num sch-cal-day-num-today" if is_today else "sch-cal-day-num"
                today_marker = " 🔴" if is_today else ""
                
                day_scholarships = scholarships_by_deadline.get(date_str, [])
                
                events_html = ""
                for sch in day_scholarships[:3]:
                    sch_type = sch.get("type", "성적")
                    color = scholarship_types.get(sch_type, {}).get("color", "#666")
                    icon = scholarship_types.get(sch_type, {}).get("icon", "📌")
                    name_short = sch["name"][:10] + "..." if len(sch["name"]) > 10 else sch["name"]
                    events_html += f"<div class='sch-cal-event' style='background-color: {color};'>{icon} {name_short}</div>"
                
                if len(day_scholarships) > 3:
                    events_html += f"<div class='sch-cal-more'>+{len(day_scholarships) - 3}개 더</div>"
                
                all_weeks_html += f"<div class='{day_class}'><div class='{num_class}'>{day}{today_marker}</div>{events_html}</div>"
    
    st.markdown(f"<div class='sch-cal-grid'>{all_weeks_html}</div>", unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("##### 🎨 범례")
    legend_cols = st.columns(5)
    for idx, (type_name, type_info) in enumerate(scholarship_types.items()):
        with legend_cols[idx]:
            st.markdown(f"<span style='background-color: {type_info['color']}; color: white; padding: 3px 8px; border-radius: 3px;'>{type_info['icon']} {type_name}</span>", unsafe_allow_html=True)

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
        
        st.markdown("---")
        st.markdown("### 📅 공모전 · 인턴 · 대외활동 일정 캘린더")
        st.markdown("진로 관련 활동의 접수 기간을 한눈에 확인하세요!")
        
        career_activities = generate_career_activities(selected_career)
        
        activity_sites = {
            "링커리어": "https://linkareer.com",
            "위비티": "https://www.wevity.com",
            "캠퍼스픽": "https://www.campuspick.com",
            "슥삭": "https://www.ssgsag.kr",
            "자소설닷컴": "https://jasoseol.com/intern"
        }
        
        st.markdown("##### 🔗 실시간 정보 확인하기")
        site_cols = st.columns(5)
        for idx, (site_name, site_url) in enumerate(activity_sites.items()):
            with site_cols[idx]:
                st.markdown(f"[{site_name}]({site_url})")
        
        st.markdown("---")
        
        activity_filter = st.multiselect(
            "활동 유형 필터",
            ["공모전", "인턴십", "대외활동", "서포터즈", "해커톤"],
            default=["공모전", "인턴십", "대외활동", "서포터즈", "해커톤"]
        )
        
        filtered_activities = [a for a in career_activities if a["type"] in activity_filter]
        filtered_activities.sort(key=lambda x: x["end_date"])
        
        today = datetime.now()
        
        type_colors = {
            "공모전": "#0E4A84",
            "인턴십": "#28a745",
            "대외활동": "#ffc107",
            "서포터즈": "#17a2b8",
            "해커톤": "#dc3545"
        }
        
        type_icons = {
            "공모전": "🏆",
            "인턴십": "💼",
            "대외활동": "🌟",
            "서포터즈": "📣",
            "해커톤": "💻"
        }
        
        if "calendar_year" not in st.session_state:
            st.session_state.calendar_year = today.year
        if "calendar_month" not in st.session_state:
            st.session_state.calendar_month = today.month
        
        nav_col1, nav_col2, nav_col3 = st.columns([1, 2, 1])
        with nav_col1:
            if st.button("◀ 이전 달"):
                if st.session_state.calendar_month == 1:
                    st.session_state.calendar_month = 12
                    st.session_state.calendar_year -= 1
                else:
                    st.session_state.calendar_month -= 1
                st.rerun()
        with nav_col2:
            st.markdown(f"<h4 style='text-align: center;'>{st.session_state.calendar_year}년 {st.session_state.calendar_month}월</h4>", unsafe_allow_html=True)
        with nav_col3:
            if st.button("다음 달 ▶"):
                if st.session_state.calendar_month == 12:
                    st.session_state.calendar_month = 1
                    st.session_state.calendar_year += 1
                else:
                    st.session_state.calendar_month += 1
                st.rerun()
        
        if st.button("📍 오늘로 이동"):
            st.session_state.calendar_year = today.year
            st.session_state.calendar_month = today.month
            st.rerun()
        
        st.markdown("""
        <style>
        .cal-grid {
            display: grid;
            grid-template-columns: repeat(7, 1fr);
            gap: 1px;
            background-color: #e0e0e0;
            border: 1px solid #e0e0e0;
            border-radius: 8px;
            overflow: hidden;
        }
        .cal-header {
            background-color: #0E4A84;
            color: white;
            padding: 10px;
            text-align: center;
            font-weight: bold;
        }
        .cal-header-sat { background-color: #0066cc; }
        .cal-header-sun { background-color: #dc3545; }
        .cal-day {
            background-color: #fff;
            min-height: 90px;
            padding: 5px;
            vertical-align: top;
        }
        .cal-day-empty { background-color: #f5f5f5; }
        .cal-day-today { background-color: #e3f2fd; border: 2px solid #0E4A84; }
        .cal-day-num {
            font-weight: bold;
            font-size: 14px;
            margin-bottom: 3px;
        }
        .cal-day-num-today { color: #0E4A84; }
        .cal-event-bar {
            font-size: 10px;
            padding: 2px 4px;
            margin: 1px 0;
            color: white;
            overflow: hidden;
            text-overflow: ellipsis;
            white-space: nowrap;
            display: block;
        }
        .cal-event-start {
            border-radius: 4px 0 0 4px;
            margin-right: -5px;
        }
        .cal-event-middle {
            border-radius: 0;
            margin-left: -5px;
            margin-right: -5px;
        }
        .cal-event-end {
            border-radius: 0 4px 4px 0;
            margin-left: -5px;
        }
        .cal-event-single {
            border-radius: 4px;
        }
        .cal-more {
            font-size: 9px;
            color: #666;
            padding: 1px 2px;
        }
        </style>
        """, unsafe_allow_html=True)
        
        weekdays = ["월", "화", "수", "목", "금", "토", "일"]
        
        cal_module = calendar.Calendar(firstweekday=0)
        month_days = cal_module.monthdayscalendar(st.session_state.calendar_year, st.session_state.calendar_month)
        
        header_html = ""
        for i, day_name in enumerate(weekdays):
            header_class = "cal-header"
            if i == 5:
                header_class += " cal-header-sat"
            elif i == 6:
                header_class += " cal-header-sun"
            header_html += f"<div class='{header_class}'>{day_name}</div>"
        
        def get_week_dates(week, year, month):
            dates = []
            for day in week:
                if day == 0:
                    dates.append(None)
                else:
                    dates.append(datetime(year, month, day))
            return dates
        
        def get_events_for_week(week_dates, activities):
            week_events = []
            for act in activities:
                start = datetime.strptime(act["start_date"], "%Y-%m-%d")
                end = datetime.strptime(act["end_date"], "%Y-%m-%d")
                
                week_start_idx = None
                week_end_idx = None
                
                for idx, date in enumerate(week_dates):
                    if date is None:
                        continue
                    if start <= date <= end:
                        if week_start_idx is None:
                            week_start_idx = idx
                        week_end_idx = idx
                
                if week_start_idx is not None:
                    is_event_start = week_dates[week_start_idx] and week_dates[week_start_idx].date() == start.date()
                    is_event_end = week_dates[week_end_idx] and week_dates[week_end_idx].date() == end.date()
                    week_events.append({
                        "activity": act,
                        "start_idx": week_start_idx,
                        "end_idx": week_end_idx,
                        "is_event_start": is_event_start,
                        "is_event_end": is_event_end
                    })
            return week_events
        
        all_weeks_html = header_html
        
        for week in month_days:
            week_dates = get_week_dates(week, st.session_state.calendar_year, st.session_state.calendar_month)
            week_events = get_events_for_week(week_dates, filtered_activities)
            
            events_by_day = {i: [] for i in range(7)}
            for evt in week_events:
                for idx in range(evt["start_idx"], evt["end_idx"] + 1):
                    events_by_day[idx].append(evt)
            
            for i, day in enumerate(week):
                if day == 0:
                    all_weeks_html += "<div class='cal-day cal-day-empty'></div>"
                else:
                    date_obj = week_dates[i]
                    is_today = (date_obj and date_obj.date() == today.date())
                    
                    day_class = "cal-day cal-day-today" if is_today else "cal-day"
                    num_class = "cal-day-num cal-day-num-today" if is_today else "cal-day-num"
                    today_marker = " 🔴" if is_today else ""
                    
                    events_html = ""
                    shown_events = set()
                    event_count = 0
                    
                    for evt in events_by_day[i]:
                        if event_count >= 3:
                            break
                        act = evt["activity"]
                        act_id = act["name"]
                        
                        if evt["start_idx"] == i:
                            event_count += 1
                            shown_events.add(act_id)
                            
                            color = type_colors.get(act["type"], "#666")
                            icon = type_icons.get(act["type"], "📌")
                            span = evt["end_idx"] - evt["start_idx"] + 1
                            
                            if span == 1:
                                bar_class = "cal-event-bar cal-event-single"
                            elif evt["is_event_start"] and evt["is_event_end"]:
                                bar_class = "cal-event-bar cal-event-single"
                            elif evt["is_event_start"]:
                                bar_class = "cal-event-bar cal-event-start"
                            else:
                                bar_class = "cal-event-bar cal-event-start"
                            
                            name_short = act["name"][:12] + "..." if len(act["name"]) > 12 else act["name"]
                            events_html += f"<div class='{bar_class}' style='background-color: {color};'>{icon} {name_short}</div>"
                        elif act_id not in shown_events:
                            event_count += 1
                            color = type_colors.get(act["type"], "#666")
                            
                            if evt["end_idx"] == i and evt["is_event_end"]:
                                bar_class = "cal-event-bar cal-event-end"
                            elif evt["end_idx"] == i:
                                bar_class = "cal-event-bar cal-event-end"
                            else:
                                bar_class = "cal-event-bar cal-event-middle"
                            
                            events_html += f"<div class='{bar_class}' style='background-color: {color};'>&nbsp;</div>"
                    
                    remaining = len(events_by_day[i]) - event_count
                    if remaining > 0:
                        events_html += f"<div class='cal-more'>+{remaining}개 더</div>"
                    
                    all_weeks_html += f"<div class='{day_class}'><div class='{num_class}'>{day}{today_marker}</div>{events_html}</div>"
        
        st.markdown(f"<div class='cal-grid'>{all_weeks_html}</div>", unsafe_allow_html=True)
        
        st.markdown("---")
        st.markdown("##### 🎨 범례")
        legend_cols = st.columns(5)
        for idx, (type_name, color) in enumerate(type_colors.items()):
            with legend_cols[idx]:
                icon = type_icons.get(type_name, "📌")
                st.markdown(f"<span style='background-color: {color}; color: white; padding: 3px 8px; border-radius: 3px;'>{icon} {type_name}</span>", unsafe_allow_html=True)
        
        st.markdown("##### 📋 활동 상세 목록")
        
        for activity in filtered_activities:
            end = datetime.strptime(activity["end_date"], "%Y-%m-%d")
            days_until_deadline = (end - today).days
            
            if days_until_deadline < 0:
                status_badge = "🔴 마감"
                status_color = "#dc3545"
            elif days_until_deadline <= 3:
                status_badge = f"🔥 D-{days_until_deadline} 마감임박!"
                status_color = "#dc3545"
            elif days_until_deadline <= 7:
                status_badge = f"⚠️ D-{days_until_deadline}"
                status_color = "#ffc107"
            else:
                status_badge = f"✅ D-{days_until_deadline}"
                status_color = "#28a745"
            
            with st.expander(f"{activity['type']} | {activity['name']} ({status_badge})"):
                col1, col2 = st.columns(2)
                with col1:
                    st.markdown(f"**주최:** {activity['host']}")
                    st.markdown(f"**접수 기간:** {activity['start_date']} ~ {activity['end_date']}")
                    st.markdown(f"**대상:** {activity['target']}")
                with col2:
                    st.markdown(f"**혜택:** {activity['benefit']}")
                    st.markdown(f"**관련 분야:** {activity['field']}")
                    if activity.get("link"):
                        st.markdown(f"🔗 [상세정보 보기]({activity['link']})")

def generate_career_activities(career):
    today = datetime.now()
    
    base_activities = [
        {
            "name": "2024 대학생 창업 아이디어 공모전",
            "type": "공모전",
            "start_date": (today - timedelta(days=10)).strftime("%Y-%m-%d"),
            "end_date": (today + timedelta(days=20)).strftime("%Y-%m-%d"),
            "host": "중소벤처기업부",
            "target": "대학생/대학원생",
            "benefit": "총 상금 3,000만원",
            "field": "창업/아이디어",
            "link": "https://linkareer.com"
        },
        {
            "name": "삼성전자 동계 인턴십",
            "type": "인턴십",
            "start_date": (today - timedelta(days=5)).strftime("%Y-%m-%d"),
            "end_date": (today + timedelta(days=15)).strftime("%Y-%m-%d"),
            "host": "삼성전자",
            "target": "대학교 3학년 이상",
            "benefit": "정규직 전환 기회",
            "field": "IT/전자",
            "link": "https://www.samsungcareers.com"
        },
        {
            "name": "현대자동차 대학생 서포터즈",
            "type": "서포터즈",
            "start_date": (today + timedelta(days=5)).strftime("%Y-%m-%d"),
            "end_date": (today + timedelta(days=30)).strftime("%Y-%m-%d"),
            "host": "현대자동차",
            "target": "대학생",
            "benefit": "활동비 + 수료증",
            "field": "마케팅/홍보",
            "link": "https://linkareer.com"
        },
        {
            "name": "2024 데이터 분석 경진대회",
            "type": "공모전",
            "start_date": (today - timedelta(days=3)).strftime("%Y-%m-%d"),
            "end_date": (today + timedelta(days=25)).strftime("%Y-%m-%d"),
            "host": "한국데이터산업진흥원",
            "target": "대학생/일반인",
            "benefit": "총 상금 5,000만원",
            "field": "데이터분석/AI",
            "link": "https://www.wevity.com"
        },
        {
            "name": "네이버 테크 인턴십",
            "type": "인턴십",
            "start_date": (today + timedelta(days=10)).strftime("%Y-%m-%d"),
            "end_date": (today + timedelta(days=40)).strftime("%Y-%m-%d"),
            "host": "네이버",
            "target": "컴퓨터공학 전공",
            "benefit": "인턴 급여 + 정규직 전환",
            "field": "IT/개발",
            "link": "https://recruit.navercorp.com"
        },
        {
            "name": "글로벌 마케팅 공모전",
            "type": "공모전",
            "start_date": (today - timedelta(days=15)).strftime("%Y-%m-%d"),
            "end_date": (today + timedelta(days=5)).strftime("%Y-%m-%d"),
            "host": "한국마케팅협회",
            "target": "대학생",
            "benefit": "상금 + 인턴 기회",
            "field": "마케팅/광고",
            "link": "https://www.wevity.com"
        },
        {
            "name": "카카오 해커톤 2024",
            "type": "해커톤",
            "start_date": (today + timedelta(days=15)).strftime("%Y-%m-%d"),
            "end_date": (today + timedelta(days=45)).strftime("%Y-%m-%d"),
            "host": "카카오",
            "target": "개발자/대학생",
            "benefit": "상금 + 채용 우대",
            "field": "IT/개발",
            "link": "https://www.campuspick.com"
        },
        {
            "name": "ESG 대학생 아이디어 공모전",
            "type": "공모전",
            "start_date": (today + timedelta(days=3)).strftime("%Y-%m-%d"),
            "end_date": (today + timedelta(days=35)).strftime("%Y-%m-%d"),
            "host": "환경부",
            "target": "대학생",
            "benefit": "총 상금 2,000만원",
            "field": "환경/ESG",
            "link": "https://linkareer.com"
        },
        {
            "name": "LG 대학생 마케팅 서포터즈",
            "type": "서포터즈",
            "start_date": (today - timedelta(days=7)).strftime("%Y-%m-%d"),
            "end_date": (today + timedelta(days=7)).strftime("%Y-%m-%d"),
            "host": "LG전자",
            "target": "대학생 2-4학년",
            "benefit": "활동비 + LG제품 제공",
            "field": "마케팅/홍보",
            "link": "https://www.ssgsag.kr"
        },
        {
            "name": "금융권 체험형 인턴십",
            "type": "인턴십",
            "start_date": (today + timedelta(days=20)).strftime("%Y-%m-%d"),
            "end_date": (today + timedelta(days=50)).strftime("%Y-%m-%d"),
            "host": "KB국민은행",
            "target": "경영/경제 전공",
            "benefit": "인턴 급여 + 멘토링",
            "field": "금융/경영",
            "link": "https://jasoseol.com/intern"
        },
        {
            "name": "청년 창업 지원 프로그램",
            "type": "대외활동",
            "start_date": (today - timedelta(days=2)).strftime("%Y-%m-%d"),
            "end_date": (today + timedelta(days=28)).strftime("%Y-%m-%d"),
            "host": "창업진흥원",
            "target": "만 39세 이하 청년",
            "benefit": "창업 자금 + 멘토링",
            "field": "창업",
            "link": "https://www.k-startup.go.kr"
        },
        {
            "name": "글로벌 인재 양성 프로그램",
            "type": "대외활동",
            "start_date": (today + timedelta(days=8)).strftime("%Y-%m-%d"),
            "end_date": (today + timedelta(days=38)).strftime("%Y-%m-%d"),
            "host": "KOTRA",
            "target": "대학생/대학원생",
            "benefit": "해외연수 + 수료증",
            "field": "글로벌/무역",
            "link": "https://linkareer.com"
        }
    ]
    
    career_specific = {
        "소프트웨어 개발자": ["IT/개발", "IT/전자", "데이터분석/AI"],
        "데이터 사이언티스트": ["데이터분석/AI", "IT/개발"],
        "금융 애널리스트": ["금융/경영", "데이터분석/AI"],
        "건축가": ["창업/아이디어", "환경/ESG"],
        "연구원": ["데이터분석/AI", "환경/ESG"],
        "컨설턴트": ["금융/경영", "마케팅/광고", "글로벌/무역"],
        "의사": ["환경/ESG", "창업"],
        "마케터": ["마케팅/광고", "마케팅/홍보"]
    }
    
    relevant_fields = career_specific.get(career, [])
    
    prioritized = []
    others = []
    for activity in base_activities:
        if activity["field"] in relevant_fields:
            prioritized.append(activity)
        else:
            others.append(activity)
    
    return prioritized + others

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
