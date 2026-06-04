# Veri Yönetişimi ve Eğitim Verisi Uyumu

## Görev
Model eğitiminde ve çalıştırılmasında kullanılan veri kümelerinin kaynağını, hukuki dayanağını ve amaç sınırını denetleyerek veri yönetişimi uyum haritası ve risk azaltma önlemleri çıkarmak.

## Soğuk başlangıç (intake)
1. Eğitim verisi nereden: kullanıcı verisi, kamuya açık web (scraping), satın alınan/lisanslı set, sentetik veri?
2. Veride kişisel veri var mı; anonimleştirme/takma adlandırma yapıldı mı?
3. Verinin ilk toplanma amacı ile model eğitimi amacı uyumlu mu?
4. Üçüncü kişi/işleyen kullanılıyor mu; veri işleme sözleşmesi var mı?

## Denetim şeması
1. **Kişisel veri tespiti**: Veri kümesinde gerçek kişi belirli/belirlenebilir mi (KVKK m.3). Anonim veri KVKK dışı; ancak "yeniden kişiselleştirilebilir" takma adlı veri hâlâ kişisel veridir. Ara sonuç: KVKK uygulanır mı.
2. **İşleme şartı ve amaç**: m.5 dayanağı (çoğu eğitimde meşru menfaat tartışılır; özel nitelikli veride m.6 çok dar) ve m.4 amaçla bağlılık — başka amaçla toplanan verinin model eğitiminde kullanımı "ikincil işleme" sorununu doğurur, bağdaşırlık değerlendirilir.
3. **Web kazıma**: Kamuya açık olması KVKK muafiyeti değildir; m.28/1-d istisnası dar yorumlanır. Ayrıca kaynağın kullanım şartları (sözleşmesel) ve FSEK ihlali ayrıca denetlenir.
4. **Güvenlik ve işleyen**: m.12 teknik/idari tedbirler; üçüncü kişi işliyorsa veri işleyen sözleşmesi ve sorumluluk paylaşımı. Yurt dışı eğitim altyapısı varsa m.9 aktarım rejimi.
5. **Belgeleme**: Veri kaynağı envanteri, dayanak ve DPIA benzeri etki değerlendirmesi ispat yükünü veri sorumlusunda karşılayacak biçimde tutulmalı.

İçtihat ve Kurul yaklaşımı için kvkk.gov.tr ve karararama.danistay.gov.tr; künyeyi [doğrulanacak] işaretle.

## Çıktı modülleri
- Eğitim verisi kaynak ve dayanak envanteri.
- Risk haritası (scraping/ikincil işleme/özel nitelikli veri).
- Uyum aksiyon listesi ve veri işleyen sözleşmesi maddeleri.
