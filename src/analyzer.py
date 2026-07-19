import re
import numpy as np

class ContentSafetyAnalyzer:
    def __init__(self):
        # Yapay zeka metinlerinde sık rastlanan kalıplar ve kelime çeşitliliği analizi için basit metrikler
        self.ai_buzzwords = ["kesinlikle", "önemlidir", "dikkate değer", "özetlemek gerekirse", "bu doğrultuda", "perspektif"]
        
    def analyze_text(self, text):
        if not text or len(text.strip()) < 10:
            return {"status": "error", "message": "Analiz için çok kısa metin."}
            
        words = text.lower().split()
        word_count = len(words)
        unique_words = len(set(words))
        
        # Kelime çeşitliliği (Lexical Diversity) - Yapay zeka genellikle daha tekdüze yazar
        diversity_score = unique_words / word_count if word_count > 0 else 0
        
        # Yapay zeka kelimelerinin yoğunluğu
        buzzword_count = sum(1 for word in words if word in self.ai_buzzwords)
        buzzword_ratio = buzzword_count / word_count if word_count > 0 else 0
        
        # Ortalama cümle uzunluğu stabilitesi (AI genellikle çok düzenli ve benzer uzunlukta cümleler kurar)
        sentences = re.split(r'[.!?]+', text)
        sentences = [s.strip() for s in sentences if s.strip()]
        sentence_lengths = [len(s.split()) for s in sentences]
        
        sentence_variance = np.var(sentence_lengths) if len(sentence_lengths) > 1 else 0
        
        # Basit bir skorlama algoritması (Olasılık hesabı)
        ai_probability = 50 # Baz puan
        
        if diversity_score < 0.6:
            ai_probability += 15
        else:
            ai_probability -= 10
            
        if buzzword_ratio > 0.05:
            ai_probability += 20
            
        if sentence_variance < 5 and len(sentences) > 2:
            ai_probability += 15 # Çok düzenli cümle uzunlukları yapay zekaya işaret eder
            
        # Sınırları belirle
        ai_probability = max(5, min(95, ai_probability))
        human_probability = 100 - ai_probability
        
        # Risk değerlendirmesi
        if ai_probability > 75:
            verdict = "YÜKSEK RİSK: Muhtemelen Yapay Zeka Tarafından Üretilmiş"
            color = "red"
        elif ai_probability > 45:
            verdict = "ORTA RİSK: Şüpheli İçerik / Karma Yapı"
            color = "orange"
        else:
            verdict = "DÜŞÜK RİSK: Muhtemelen İnsan Tarafından Yazılmış"
            color = "green"
            
        return {
            "status": "success",
            "ai_prob": ai_probability,
            "human_prob": human_probability,
            "verdict": verdict,
            "color": color,
            "metrics": {
                "Toplam Kelime": word_count,
                "Benzersiz Kelime Oranı": f"%{int(diversity_score * 100)}",
                "Cümle Sayısı": len(sentences)
            }
        }