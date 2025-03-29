import streamlit as st
import json
import os

DATA_FILE = "data.json"

# ✅ JSON 데이터 로드 (캐싱 적용하여 속도 최적화)
@st.cache_data
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    return []

# ✅ JSON 데이터 저장
def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

# ✅ 처음 한 번만 JSON 데이터 로드
DATA = load_data()

# 🎨 Streamlit 웹 UI 만들기
st.title("💖 좋아할 가능성 분석기")

# 🔽 사용자 입력
name1 = st.text_input("첫 번째 사람의 이름")
name2 = st.text_input("두 번째 사람의 이름")

if st.button("🔍 분석하기"):
    st.subheader(f"📌 '{name1}'과(와) '{name2}'의 좋아할 가능성: 75%")
    
    # 데이터 저장 후 JSON 업데이트
    DATA.append({"name1": name1, "name2": name2})
    save_data(DATA)
    st.success("✅ 데이터가 저장되었습니다!")

