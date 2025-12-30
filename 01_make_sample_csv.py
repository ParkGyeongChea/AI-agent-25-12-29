import pandas as pd

rows = [
    {"id": 1, "title": "AI 기술 동향", "category": "IT", "views": "1200", "content": "AI 기술이 빠르게 발전하고 있다.", "published_at": "2025-11-01"},
    {"id": 2, "title": "데이터 분석 입문", "category": "IT", "views": "850", "content": "데이터 분석은 의사결정에 활용된다.", "published_at": "2025-11-02"},
    {"id": 3, "title": "미디어와 AI", "category": "Media", "views": "640", "content": "미디어 산업에서 AI 활용이 증가하고 있다.", "published_at": "2025-11-02"},
    {"id": 4, "title": "스포츠 하이라이트", "category": "Sports", "views": "1500", "content": "경기 요약과 주요 장면을 정리한다.", "published_at": "2025-11-03"},
    {"id": 5, "title": "경제 전망", "category": "Economy", "views": "980", "content": "금리와 물가의 상호작용을 점검한다.", "published_at": "2025-11-03"},
    {"id": 6, "title": "AI 윤리 쟁점", "category": "IT", "views": "", "content": "저작권과 책임 소재가 중요하다.", "published_at": "2025-11-04"},
    {"id": 7, "title": "지역 문화 행사", "category": "Culture", "views": "410", "content": "지역 축제와 공연 정보를 제공한다.", "published_at": "2025-11-04"},
    {"id": 8, "title": "오늘의 날씨", "category": "Life", "views": "730", "content": "기온과 강수 확률을 안내한다.", "published_at": "2025-11-05"},
    {"id": 9, "title": "데이터 시각화 팁", "category": "IT", "views": "1020", "content": "그래프 선택 기준을 정리한다.", "published_at": "2025-11-05"},
    {"id": 10, "title": "연예 뉴스", "category": "Entertainment", "views": "2100", "content": "신작 공개와 인터뷰를 다룬다.", "published_at": "2025-11-06"},
    {"id": 11, "title": "AI 기술 동향", "category": "IT", "views": "1200", "content": "동일 제목 중복 사례를 포함한다.", "published_at": "2025-11-06"},
    {"id": 12, "title": "국제 이슈 브리핑", "category": "World", "views": "870", "content": "주요 국제 현안을 요약한다.", "published_at": "2025-11-07"},
]

df = pd.DataFrame(rows)
df.to_csv("news_sample_plus.csv", index=False, encoding="utf-8-sig")
print("news_sample_plus.csv 생성 완료입니다.")
