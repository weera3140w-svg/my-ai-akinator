import streamlit as st
import google.generativeai as genai

# โหลด API KEY จาก Streamlit Secrets
genai.configure(
    api_key=st.secrets["GEMINI_API_KEY"]
)

# ใช้ Gemini
model = genai.GenerativeModel(
    "gemini-2.0-flash"
)

# ตั้งค่าหน้าเว็บ
st.set_page_config(
    page_title="Thai Akinator",
    page_icon="🎮"
)

# หัวเว็บ
st.title("🎮 Thai Akinator")
st.write("ให้ AI เดาสิ่งที่คุณกำลังคิด")

# เลือกหมวด
category = st.selectbox(
    "เลือกหมวด",
    ["ตัวละคร", "หนัง", "สิ่งของ"]
)

# มีจริงไหม
real = st.radio(
    "สิ่งนี้มีอยู่จริงไหม?",
    ["มีจริง", "ไม่มีจริง"]
)

# ช่องพิมพ์คำอธิบาย
desc = st.text_area(
    "อธิบายสิ่งที่คุณคิด",
    placeholder="เช่น เป็นผู้ชาย ร้องเพลง ดังในไทย..."
)

# ปุ่มเดา
if st.button("🎯 ให้ AI เดา"):

    # กันข้อความว่าง
    if desc.strip() == "":
        st.warning("กรุณาพิมพ์คำอธิบายก่อน")
    
    else:

        # Prompt ส่งให้ AI
        prompt = f"""
        คุณคือ AI เกมทายสิ่งของแบบ Akinator

        ผู้เล่นกำลังคิดถึงบางอย่าง

        หมวด: {category}
        สถานะ: {real}

        คำอธิบาย:
        {desc}

        ให้ตอบสั้นๆแบบนี้เท่านั้น

        🎯 ชื่อ: ...
        📌 ประเภท: ...

        ตัวอย่าง:
        🎯 ชื่อ: เบิร์ด ธงไชย
        📌 ประเภท: นักร้อง
        """

        try:

            # ให้ AI เดา
            response = model.generate_content(prompt)

            # แสดงผล
            st.success(response.text)

        except Exception as e:

            st.error("AI มีปัญหา กรุณาลองใหม่อีกครั้ง")
            st.code(str(e))
