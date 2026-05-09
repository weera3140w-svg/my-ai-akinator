import streamlit as st
import google.generativeai as genai

# ตั้งค่าหน้าเว็บ
st.set_page_config(page_title="AI Akinator", page_icon="🧠")

st.title("🧠 AI ทายใจ (สไตล์ Akinator)")
st.write("ลองคิดถึงตัวละคร สิ่งของ หรือหนัง แล้วให้ผมทายดู!")

# รับ API Key (แนะนำให้ไปเอาจาก Google AI Studio)
api_key = st.sidebar.text_input("ใส่ Gemini API Key:", type="password")

# --- ส่วนของการเลือกหมวดหมู่ ---
category = st.radio("เลือกหมวดหมู่:", ["ตัวละคร", "สิ่งของ", "หนัง"])

is_real = None
if category in ["ตัวละคร", "สิ่งของ"]:
    is_real = st.radio(f"{category}นี้มีอยู่จริงในโลกใบนี้ไหม?", ["มีจริง", "จินตนาการ/เรื่องสมมติ"])

# --- ช่องกรอกลักษณะ ---
description = st.text_area("บอกใบ้ลักษณะเด่นสักนิด:", placeholder="เช่น ใส่หมวกฟาง, มีพลังพิเศษ...")

if st.button("ทายเลย!"):
    if not api_key:
        st.error("กรุณาใส่ API Key ที่แถบด้านข้างก่อนนะครับ")
    elif not description:
        st.warning("บอกใบ้อะไรผมหน่อยสิ!")
    else:
        try:
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel('gemini-1.5-flash')
            
            prompt = f"รับบทเป็น Akinator ผู้รอบรู้ ฉันกำลังนึกถึง {category} "
            if is_real: prompt += f"ที่มีสถานะเป็น {is_real} "
            prompt += f"โดยมีลักษณะคือ: {description}. ช่วยทายชื่อมา 1 ชื่อ พร้อมเหตุผลสั้นๆ"
            
            with st.spinner('กำลังใช้พลังจิตวิเคราะห์...'):
                response = model.generate_content(prompt)
                st.success("ผมทายว่า...")
                st.subheader(response.text)
        except Exception as e:
            st.error(f"เกิดข้อผิดพลาด: {e}")
