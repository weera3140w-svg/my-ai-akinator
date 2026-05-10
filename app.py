import streamlit as st
import google.generativeai as genai

# ตั้งค่า API
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

model = genai.GenerativeModel("gemini-2.0-flash")

st.set_page_config(page_title="Thai Akinator")

st.title("🎮 เกม AI ทายสิ่งที่คุณคิด")

category = st.selectbox(
    "เลือกหมวด",
    ["ตัวละคร", "หนัง", "สิ่งของ"]
)

real = st.radio(
    "มีอยู่จริงไหม?",
    ["มีจริง", "ไม่มีจริง"]
)

desc = st.text_area(
    "อธิบายสิ่งที่คุณคิด"
)

if st.button("ให้ AI เดา"):

    prompt = f"""
    ผู้เล่นกำลังคิดถึงอะไรบางอย่าง

    หมวด: {category}
    สถานะ: {real}

    คำอธิบาย:
    {desc}

    ให้ตอบสั้นๆแบบนี้:

    ชื่อ: ...
    ประเภท: ...

    ตัวอย่าง:
    ชื่อ: เบิร์ด ธงไชย
    ประเภท: นักร้อง
    """

    response = model.generate_content(prompt)

    st.success(response.text)
