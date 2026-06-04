# Taraf ve Vekil Tablosu

## Görev
Dosyadaki tüm tarafları, sıfatlarını, vekillerini ve tebligat bilgilerini tek tabloda toplayıp husumet, taraf teşkili ve tebligat hatalarını görünür kılmak.

## Soğuk başlangıç (intake)
- Kaç taraf var ve sıfatları ne (davacı, davalı, fer'î müdahil, ihbar olunan)?
- Her tarafın vekili belli mi, vekâletname dosyada mı?
- Tebligat adresleri ve KEP/MERSIS bilgileri mevcut mu?
- Ceza dosyası ise şüpheli/sanık, müşteki/katılan, mağdur ayrımı yapıldı mı?

## Denetim şeması
1. Sıfat kolonu: HMK'da davacı-davalı; çok taraflılıkta ihtiyari/zorunlu dava arkadaşlığı (HMK m.57-59) var mı denetle. Zorunlu dava arkadaşlığında taraf teşkili eksikse dava şartı sorunu doğar (HMK m.114), eksik listesine yaz.
2. Vekil kolonu: her taraf için vekil adı, baro-sicil, vekâletname tarihi. Vekâletname yoksa veya kapsamı dar ise (özel yetki gerektiren işlemler için) işaretle.
3. Tebligat kolonu: adres, tüzel kişilerde MERSIS/KEP. Tebligat Kanunu (7201) gereği usulsüz tebligat riskini not et; tebligatın geçerliliği süreleri etkiler.
4. Müdahil/üçüncü kişi: fer'î müdahale (HMK m.66), davanın ihbarı (HMK m.61) varsa ayrı satır.
5. Ara sonuç: taraf teşkili tamam mı, husumet doğru tarafa mı yöneltilmiş, hangi tebligat eksik — kontrol listesi olarak çıkar. Adres ve sıfatlar yalnızca evraktan alınır.

## Çıktı modülleri
- Taraf-sıfat-vekil-adres-tebligat kolonlu Excel tablosu.
- Eksik vekâletname / eksik taraf teşkili uyarı listesi.
- Tebligat riski notları.
