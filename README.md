# AI-Powered Web Content Safety Analyzer

Bu proje, web tabanlı metinlerin veya içeriklerin yapay zeka (LLM/ChatGPT vb.) tarafından mı üretildiğini yoksa insan eliyle mi yazıldığını gelişmiş doğal dil işleme (NLP) metrikleri kullanarak analiz eden, modern arayüze sahip bir içerik güvenliği platformudur.

##  Özellikler (Features)
*   **Görsel Web Arayüzü:** Streamlit entegrasyonu sayesinde kullanıcı dostu ve hızlı tarayıcı deneyimi.
*   **Gelişmiş Metrik Analizi:** Kelime çeşitliliği (Lexical Diversity), AI kalıp kelime (buzzword) yoğunluğu ve cümle uzunluğu stabilitesi ölçümü.
*   **İnteraktif Grafik Dağılımı:** Plotly destekli pasta grafiği (Pie Chart) ile yapay zeka/insan oranını görselleştirme.
*   **Risk Derecelendirmesi:** Analiz sonucuna göre yeşil (düşük), turuncu (orta) ve kırmızı (yüksek) risk uyarı dinamikleri.

##  Klasör Yapısı (Project Structure)
*   `src/analyzer.py`: Kelime çeşitliliği, cümle varyansı ve risk skorlama algoritmalarını barındıran analiz motoru.
*   `app.py`: Streamlit ile tasarlanmış, grafik ve metrik kartlarını içeren web arayüz dosyası.
*   `requirements.txt`: Projenin çalışması için gerekli kütüphanelerin listesi.

##  Kurulum ve Çalıştırma (Installation)
1. Gerekli kütüphaneleri bilgisayarınıza yükleyin:
   ```bash
   pip install -r requirements.txt
2. Web uygulamasını yerel sunucuda başlatın:
   ```bash
   streamlit run app.py