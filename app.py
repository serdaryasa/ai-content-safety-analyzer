import streamlit as st
import pandas as pd
import plotly.express as px
from src.analyzer import ContentSafetyAnalyzer

# Sayfa Ayarları
st.set_page_config(page_title="AI Content Safety Analyzer", page_icon="🛡️", layout="wide")
analyzer = ContentSafetyAnalyzer()

st.title("🛡️ AI-Powered Web Content Safety Analyzer")
st.markdown("Bu platform, girilen metinlerin yapay zeka (LLM) tarafından üretilip üretilmediğini ve içerik güvenliğini gelişmiş metriklerle analiz eder.")

st.divider()

# Arayüz Düzeni (Sol kolon girdi, Sağ kolon sonuçlar)
col1, col2 = st.columns([1.2, 1])

with col1:
    st.subheader("📝 Analiz Edilecek Metin")
    user_input = st.text_area("Metni buraya yapıştırın:", height=300, placeholder="Analiz etmek istediğiniz makale, ödev veya log metnini buraya girin...")
    
    analyze_btn = st.button("Güvenlik Analizini Başlat 🚀", use_container_width=True)

with col2:
    st.subheader("📊 Analiz Raporu ve Sonuçlar")
    
    if analyze_btn and user_input:
        with st.spinner("Yapay zeka modelleri metni inceliyor..."):
            results = analyzer.analyze_text(user_input)
            
            if results["status"] == "success":
                # Risk Durumu Kartı
                if results["color"] == "red":
                    st.error(f"**Karar:** {results['verdict']}")
                elif results["color"] == "orange":
                    st.warning(f"**Karar:** {results['verdict']}")
                else:
                    st.success(f"**Karar:** {results['verdict']}")
                
                st.divider()
                
                # Grafik Gösterimi
                data = pd.DataFrame({
                    "Kaynak": ["Yapay Zeka (AI)", "İnsan (Human)"],
                    "Olasılık (%)": [results["ai_prob"], results["human_prob"]]
                })
                fig = px.pie(data, values="Olasılık (%)", names="Kaynak", color="Kaynak",
                             color_discrete_map={"Yapay Zeka (AI)": "#ef553b", "İnsan (Human)": "#00cc96"},
                             hole=0.4)
                fig.update_layout(margin=dict(t=20, b=20, l=20, r=20), height=250)
                st.plotly_chart(fig, use_container_width=True)
                
                # Metrik Tablosu
                st.markdown("#### 📐 Detaylı Metrikler")
                for key, val in results["metrics"].items():
                    st.metric(label=key, value=val)
            else:
                st.error(results["message"])
    else:
        st.info("Analiz sonuçlarını görmek için sol tarafa metin girip butona basın.")