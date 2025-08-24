import streamlit as st
import time

# Modern koyu tema ve kutu stilleri
st.markdown("""
    <style>
        body, .stApp {
            background-color: #181a20;
            color: #eaeaea;
        }
        .input-box {
            background: #23272f;
            border-radius: 12px;
            padding: 18px 18px 8px 18px;
            margin-bottom: 18px;
            box-shadow: 0 0 10px #0002;
        }
        label, .stRadio label, .stSlider label, .stNumberInput label {
            color: #eaeaea !important;
            font-weight: bold;
            font-size: 1.08em;
        }
        .result-box {
            background: linear-gradient(135deg, #23272f 80%, #2d323c 100%);
            border-radius: 18px;
            padding: 32px;
            margin-top: 32px;
            text-align: center;
            font-size: 1.5em;
            color: #fff;
            border: 2px solid #3a3f4b;
            box-shadow: 0 0 24px #0006;
        }
        .stButton>button {
            background-color: #00c896 !important;
            color: #fff !important;
            border-radius: 8px !important;
            font-weight: bold;
            font-size: 1.1em;
            padding: 0.5em 2em;
            margin-top: 10px;
        }
        .stButton>button:hover {
            background-color: #009e74 !important;
            color: #fff !important;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='color:#fff;text-align:center;'>💰 Yatırım Hesaplama Aracı</h1>", unsafe_allow_html=True)

st.markdown("""
<div style="background:#23272f;padding:15px 20px;border-radius:12px;margin-bottom:24px;text-align:center;">
    <span style="color:#eaeaea;">Bu araç ile birikimlerinizi ve beklenen kazancınızı kolayca hesaplayabilirsiniz.</span>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

def turkce_format(sayi):
    return f"{sayi:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

with col1:
    st.markdown('<div class="input-box">', unsafe_allow_html=True)
    mevcut_birikim = st.number_input("Mevcut birikiminiz (TL)", min_value=0.0, value=0.0, step=100.0, key="mevcut")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="input-box">', unsafe_allow_html=True)
    birikim_sikligi = st.radio("Birikim sıklığı", options=["Haftalık", "Aylık", "Yıllık"], horizontal=True, key="siklik")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="input-box">', unsafe_allow_html=True)
    yatirim_miktari = st.number_input(f"{birikim_sikligi} yatırım miktarı (TL)", min_value=0.0, value=0.0, step=100.0, key="yatirim")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="input-box">', unsafe_allow_html=True)
    beklenen_kar_yuzdesi = st.slider("Beklenen yıllık kar yüzdesi (%)", min_value=0, max_value=100, value=10, step=1, key="kar")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="input-box">', unsafe_allow_html=True)
    gorulecek_sure = st.number_input("Kaç ay sonrasını görmek istersiniz?", min_value=1, value=12, step=1, key="sure")
    st.markdown('</div>', unsafe_allow_html=True)

if birikim_sikligi == "Haftalık":
    periyot_sayisi = gorulecek_sure * 4
    kar_orani = beklenen_kar_yuzdesi / 52 / 100
elif birikim_sikligi == "Aylık":
    periyot_sayisi = gorulecek_sure
    kar_orani = beklenen_kar_yuzdesi / 12 / 100
else:  # Yıllık
    periyot_sayisi = gorulecek_sure / 12
    kar_orani = beklenen_kar_yuzdesi / 100

toplam_yatirim = yatirim_miktari * periyot_sayisi
toplam_birikim = mevcut_birikim
for _ in range(int(periyot_sayisi)):
    toplam_birikim = (toplam_birikim + yatirim_miktari) * (1 + kar_orani)

kazanc = toplam_birikim - mevcut_birikim - toplam_yatirim

if st.button("Hesapla"):
    with st.spinner("Kazancınız hesaplanıyor..."):
        for i in range(10):
            st.markdown(
                f"<div style='text-align:center;font-size:{1.5 + i*0.2}em;'>💸</div>",
                unsafe_allow_html=True
            )
            time.sleep(0.07)
        st.markdown("")  # Animasyon sonrası boşluk bırak
    st.markdown(
        f"""
        <div class="result-box">
            <span style="font-size:2em;">🎉</span><br>
            <b>{gorulecek_sure} ay sonraki birikiminiz:</b> <span style="color:#00ffae;">{turkce_format(toplam_birikim)} TL</span><br>
            <b>Toplam yatırdığınız para:</b> <span style="color:#00e0ff;">{turkce_format(toplam_yatirim)} TL</span><br>
            <b>Kazancınız:</b> <span style="color:#ffe066;">{turkce_format(kazanc)} TL</span>
        </div>
        """,
        unsafe_allow_html=True
    )  
###########################################################################################
#              cd C:\Users\Bartu\Desktop\Python Bartu
 #ÇALIŞTIRMAK İÇİN# to cmd
#              streamlit run "Yatırım Hesap.py"
###########################################################################################

