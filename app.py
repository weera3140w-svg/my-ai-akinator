import streamlit as st
import google.generativeai as genai

# โหลด API KEY
genai.configure(
    api_key=st.secrets["GEMINI_API_KEY"]
)

# ใช้ model ที่เสถียร
model = genai.GenerativeModel(
    "gemini-2.0-flash"
)

st.title("🎮 Thai Akinator")

category = st.selectbox(
    "เลือกหมวด",
    ["ตัวละคร", "หนัง", "สิ่งของ"]
)

real = st.radio(
    "มีจริงไหม?",
    ["มีจริง", "ไม่มีจริง"]
)

desc = st.text_area(
    "อธิบายสิ่งที่คุณคิด"
)

if st.button("ให้ AI เดา"):

    if desc.strip() == "":
        st.warning("กรุณาพิมพ์คำอธิบาย")
    else:

        prompt = f"""
        ผู้เล่นกำลังคิดถึงอะไรบางอย่าง

        หมวด: {category}
        สถานะ: {real}

        คำอธิบาย:
        {desc}

        ให้ตอบสั้นๆแบบนี้เท่านั้น

        ชื่อ: ...
        ประเภท: ...
        """

        try:
            response = model.generate_content(prompt)

            st.success(response.text)

        except Exception as e:
            st.error("AI มีปัญหา กรุณาลองใหม่")
            st.code(str(e))
