import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Smart-Symptom Checker", page_icon="🩺")

# Secrets-dan kalitni yuklash
try:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-pro')
except Exception as e:
    st.error("API kalit topilmadi. Iltimos, Secrets sozlamalarini tekshiring.")
    st.stop()

st.title("🩺 Smart-Symptom Checker")
symptoms = st.text_area("Qanday alomatlar bor?")

if st.button("Tahlil qilish") and symptoms:
    with st.spinner("AI tahlil qilmoqda..."):
        try:
            prompt = f"Foydalanuvchi alomatlari: {symptoms}. Tibbiy maslahat ber (tashxis qo'yma)."
            response = model.generate_content(prompt)
            st.write(response.text)
        except Exception as e:
            st.error(f"Xatolik yuz berdi: {e}")
