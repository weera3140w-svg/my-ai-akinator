import streamlit as st
import google.generativeai as genai

# 1. ตั้งค่าหน้าเว็บ
st.set_page_config(page_title="AI Akinator", page_icon="🧠")

st.title("🧠 AI ทายใจ (สไตล์ Akinator)")
st.write("ลองคิดถึงตัวละคร สิ่งของ หรือหนัง แล้วให้ผมทายดู!")

# 2. รับ API Key จากแถบด้านข้าง
api_key = st.sidebar.text_input("ใส่ Gemini API Key:", type="password")

# 3. ส่วนของการเลือกหมวดหมู่
category = st.radio("เลือกหมวดหมู่:", ["ตัวละคร", "สิ่งของ", "หนัง"])

is_real = "ไม่ระบุ"
if category in ["ตัวละคร", "สิ่งของ"]:
    is_real = st.radio(f"{category}นี้มีอยู่จริงในโลกใบนี้ไหม?", ["มีจริง", "จินตนาการ/เรื่องสมมติ"])

# 4. ช่องกรอกลักษณะ
description = st.text_area("บอกใบ้ลักษณะเด่นสักนิด:", placeholder="เช่น ใส่หมวกฟาง, มีพลังพิเศษ...")

# 5. ปุ่มกดทาย
if st.button("ทายเลย!"):
    if not api_key:
        st.error("กรุณาใส่ API Key ที่แถบด้านข้างก่อนนะครับ")
    elif not description:
        st.warning("บอกใบ้อะไรผมหน่อยสิ!")
    else:
        try:
            # ตั้งค่า AI
            genai.configure(api_key=api_key)
            
            # ใช้รุ่นที่เสถียรที่สุด
            model = genai.GenerativeModel('gemini-1.5-flash')
            
            # สร้างคำถามให้ AI
            prompt = f"คุณคือ Akinator ผู้รอบรู้ ฉันกำลังนึกถึง {category} ที่เป็นแบบ {is_real} มีลักษณะคือ: {description}. ช่วยทายชื่อมา 1 ชื่อ พร้อมเหตุผลสั้นๆ"
            
            with st.spinner('กำลังใช้พลังจิตวิเคราะห์...'):
                response = model.generate_content(prompt)
                st.success("ผมทายว่า...")
                st.subheader(response.text)
        except Exception as e:
            st.error(f"เกิดข้อผิดพลาด: {e}")
