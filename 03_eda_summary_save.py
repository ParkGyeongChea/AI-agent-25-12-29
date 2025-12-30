import pandas as pd

df = pd.read_csv("news_sample_plus.csv", encoding="utf-8-sig")

# 1) 기본 점검
print("shape:", df.shape)
print(df.head(3))
print(df.dtypes)

# 2) 타입 정리: views를 숫자로 변환하고 결측은 0으로 처리
df["views"] = pd.to_numeric(df["views"], errors="coerce").fillna(0).astype(int)

# 3) 날짜 파싱: published_at을 datetime으로 변환
df["published_at"] = pd.to_datetime(df["published_at"], errors="coerce")

# 4) 중복 처리 예시: 동일 title이 여러 번이면 title 기준으로 첫 행만 유지하는 방식
# 실제 업무에서는 id 기준, (title+published_at) 기준 등 정책을 명시해야 합니다.
df_dedup = df.drop_duplicates(subset=["title"], keep="first").copy()

# 5) 파생 변수 예시: 제목 길이, 본문 길이
df_dedup["title_len"] = df_dedup["title"].astype(str).str.len()
df_dedup["content_len"] = df_dedup["content"].astype(str).str.len()

# 6) 카테고리 집계: 합계/평균/건수
by_cat = (
    df_dedup.groupby("category", as_index=False)
    .agg(대출아님_조회수합계=("views", "sum"), 평균조회수=("views", "mean"), 기사수=("id", "count"))
    .sort_values("대출아님_조회수합계", ascending=False)
)

# 7) 상위 10개 기사(중복 제거 후 views 기준)
top10 = df_dedup.sort_values("views", ascending=False).head(10)[
    ["id", "title", "category", "views", "published_at"]
]

# 8) 저장
df_dedup.to_csv("news_clean.csv", index=False, encoding="utf-8-sig")
by_cat.to_csv("news_by_category.csv", index=False, encoding="utf-8-sig")
top10.to_csv("news_top10.csv", index=False, encoding="utf-8-sig")

print("정제 데이터:", "news_clean.csv")
print("카테고리 집계:", "news_by_category.csv")
print("상위 10개:", "news_top10.csv")
print(by_cat.head(10))
print(top10)
