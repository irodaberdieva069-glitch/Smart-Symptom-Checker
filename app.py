import streamlit as st
import google.generativeai as genai

# Sahifa sozlamalari
st.set_page_config(page_title="Smart-Symptom Checker", page_icon="🩺")

st.title("🩺 Smart-Symptom Checker")
st.write("Salomingizni kiriting, men esa tibbiy ma'lumotlarga tayanib tahlil qilaman.")

# API Key (o'z kalitingni kirit)
api_key = st.text_input("Gemini API kalitingizni kiriting:", type="password")

if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-pro')

    # Foydalanuvchi inputi
    symptoms = st.text_area("Qanday alomatlar bor? (masalan: bosh og'rig'i, isitma, holsizlik)")
    duration = st.slider("Alomatlar necha kundan beri davom etmoqda?", 0, 14, 1)

    if st.button("Tahlil qilish"):
        if symptoms:
            prompt = f"""
            Sen tibbiy yordamchi AI emassan, sen faqat umumiy ma'lumot beruvchi tahlilchisan.
            Foydalanuvchi alomatlari: {symptoms}. Davomiyligi: {duration} kun.
            Quyidagi formatda javob ber:
            1. Ehtimoliy umumiy holat (tashxis qo'yma!).
            2. Triage darajasi (Yashil/Sariq/Qizil).
            3. Umumiy maslahat (shifokorga borish kerakmi yoki yo'q).
            Eslatma: Har doim 'Bu shifokor ko'rigini o'rnini bosmaydi' deb yozib qo'y.
            """
            
            response = model.generate_content(prompt)
            st.markdown("### Tahlil natijasi:")
            st.write(response.text)
        else:
            st.warning("Iltimos, alomatlarni yozing.")
else:
    st.info("Iltimos, davom etish uchun API kalitni kiriting.")
