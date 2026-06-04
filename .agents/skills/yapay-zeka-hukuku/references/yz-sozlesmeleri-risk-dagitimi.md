# Yapay Zekâ Sözleşmeleri ve Sözleşmesel Risk Dağıtımı

## Görev
Yapay zekâ geliştirme/lisans/SaaS/API sözleşmelerinde tarafların risk, veri, fikri mülkiyet ve sorumluluk dengesini TBK çerçevesinde tasarlamak veya incelemek; eksik, asimetrik veya geçersiz şartları tespit edip redline önermek.

## Soğuk başlangıç (intake)
1. Sözleşme tipi: model geliştirme/eser, lisans, API/SaaS abonelik, entegrasyon/danışmanlık?
2. Müvekkil hangi taraf: sağlayıcı mı, kullanan/alıcı mı?
3. Eğitim/girdi/çıktı verisi kime ait, modeli iyileştirmede kullanılıyor mu?
4. Çıktı üzerinde fikri hak kime; ticari sır ve KVKK boyutu var mı?

## Denetim şeması
1. **Konu ve tip tayini**: Eser/geliştirme ağırlıklıysa TBK eser sözleşmesi (m.470 vd.) ve ayıba karşı tekeffül; sürekli hizmet/lisans ise hizmet/atipik sözleşme. Ara sonuç: hangi tip ve emredici hükümler.
2. **Veri ve KVKK maddeleri**: Girdi verisinin model eğitiminde kullanımı için açık yetki; veri işleyen sıfatı doğuyorsa KVKK m.12 uyumlu veri işleme sözleşmesi ve m.9 aktarım taahhütleri. Eksikse uyum açığı.
3. **Fikri mülkiyet**: Çıktı ve modelin hak sahipliği, lisans kapsamı, üçüncü kişi açık kaynak/lisans uyumu (FSEK/SMK). "Çıktı üzerinde hak garanti edilemez" gerçeğini sözleşmeye yansıt.
4. **Performans ve sorumluluk**: SLA, doğruluk/halüsinasyon riskine ilişkin garanti sınırları; sorumluluk sınırlaması maddeleri TBK m.115 (ağır kusur/kasıtta geçersizlik) ve genel işlem koşulu denetimi (m.20-25) süzgecinden geçirilir.
5. **Tazminat/rücu**: Üçüncü kişi taleplerinde tazmin (indemnity), veri ihlali ve fikri hak ihlali için tahsis; cezai şart ve fesih.

Emredici hüküm ve tüketici işlemi varsa 6502 TKHK ek denetimi. İçtihat künyesini [doğrulanacak] işaretle.

## Çıktı modülleri
- Risk maddesi haritası (veri/IP/sorumluluk/SLA).
- Redline ve alternatif lafız önerileri.
- Müzakere notu ve risk skoru.
