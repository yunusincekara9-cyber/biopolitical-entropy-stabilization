import time
import math

class BiopoliticalSystemSimulation:
    def __init__(self, population, initial_compliance, oxtr_silenced=False, hypergamy_indexed=False):
        self.population = population
        self.compliance_rate = initial_compliance # Başlangıç itaat oranı
        self.oxtr_silenced = oxtr_silenced        # OXTR geni susturuldu mu?
        self.hypergamy_indexed = hypergamy_indexed # Hipergamik dürtü finansallaştı mı?
        
        # Kurumsal maliyetler (Milyon Dolar/Yıl)
        self.policing_cost = 500.0   # Polis/Güvenlik maliyeti
        self.welfare_cost = 800.0    # Sosyal yardım/Pasifikasyon maliyeti
        self.velocity_multiplier = 1.0 # İşlem/Tüketim hızı çarpanı

    def run_cycle(self, year):
        print(f"\n--- YIL {year} SİMÜLASYON RAPORU ---")
        
        if self.oxtr_silenced:
            # OXTR susturulduğu için kolektif sendikalaşma ve isyan ihtimali sıfıra yaklaşır
            # Güvenlik ve pasifikasyon maliyetleri geometrik olarak düşer
            self.policing_cost = max(self.policing_cost * 0.15, 5.0)
            self.welfare_cost = 0.0 # Sosyal yardıma gerek kalmaz, bireyler izole edilmiştir
            self.compliance_rate = min(self.compliance_rate * 1.4, 0.999)
            print("[BİYOLOJİK MÜDAHALE]: OXTR Susturuldu. Kolektif empati ve sendikalaşma engellendi.")
        else:
            # Geleneksel sistemde entropik çöküş ve maliyet artışı
            self.policing_cost *= 1.08
            self.welfare_cost *= 1.05
            self.compliance_rate *= 0.95
            print("[SİSTEMİK RİSK]: Geleneksel idare etme modeli. Maliyetler artıyor, itaat düşüyor.")

        if self.hypergamy_indexed:
            # Dürtü tamamen kredi skoruna bağlandığı için tüketim hızı katlanarak artar
            self.velocity_multiplier = math.pow(1.5, year) if year > 0 else 1.5
            print("[ALGORİTMİK ENDEKSLEME]: Hipergami Kredi Skoruna bağlandı. Tüketim dürtüsü maksimize edildi.")
        else:
            self.velocity_multiplier *= 0.98 # Statik varlık yükü nedeniyle yavaşlama

        # Çıktı Metrikleri
        total_overhead = self.policing_cost + self.welfare_cost
        systemic_efficiency = (self.compliance_rate * self.velocity_multiplier) / (total_overhead + 1)

        print(f"-> Devlet / Kurumsal Sabit Giderler: {total_overhead:.2f}M $")
        print(f"-> Tüketim Hızı Çarpanı (Velocity): {self.velocity_multiplier:.2f}x")
        print(f"-> Hücresel İtaat Oranı (Compliance): {self.compliance_rate * 100:.2f}%")
        print(f"-> Toplam Sistem Verimliliği Endeksi: {systemic_efficiency * 1000:.2f}")
        return total_overhead, systemic_efficiency

# --- TEST SENARYOSU ---
if __name__ == "__main__":
    print("SİMÜLAN BAŞLATILIYOR: Geleneksel Burjuva Modeli vs. #eacc Biyopolitik Stabilizasyon")
    
    # 1. Senaryo: Geleneksel model (Sizin burjuvaların anlamadığı, sürekli zarar eden model)
    print("\n================== SENARYO A: GELENEKSEL MODEL ==================")
    legacy_system = BiopoliticalSystemSimulation(population=1000000, initial_compliance=0.75, oxtr_silenced=False, hypergamy_indexed=False)
    for y in range(1, 4):
        legacy_system.run_cycle(y)
        time.sleep(0.1)

    # 2. Senaryo: #eacc Biyopolitik Model (Dubai ve İsviçre plütokratlarının aradığı sıfır maliyetli model)
    print("\n================== SENARYO B: #EACC BİYOPOLİTİK MODEL ==================")
    eacc_system = BiopoliticalSystemSimulation(population=1000000, initial_compliance=0.75, oxtr_silenced=True, hypergamy_indexed=True)
    for y in range(1, 4):
        eacc_system.run_cycle(y)
        time.sleep(0.1)
