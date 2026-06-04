# Telekom-Bilişimde Süreler ve Zamanaşımı

## Görev
Bir telekom/internet dosyasındaki tüm süreleri tek tabloda toplamak; hak düşürücü süre, dava/itiraz süresi ve zamanaşımını ayırarak süre kaçırma riskini ortadan kaldırmak.

## Soğuk başlangıç (intake)
1. Hangi işlem/olay için süre soruluyor (BTK işlemi, içerik kararı, başvuru yanıtı, alacak, ceza)?
2. Başlangıç tarihi nedir (tebliğ, öğrenme, başvuru, ihlal)?
3. Süreyi durduran/keser bir başvuru/işlem yapıldı mı?
4. Olay tarihindeki yürürlük hali hangisi (5651 ve BTK mevzuatı sık değişir)?

## Denetim şeması
1. **İdari dava süresi**: BTK işlemlerine karşı İYUK m.7 — kural 60 gün; özel kanunda farklı süre varsa o uygulanır. İdari başvuru (İYUK m.11) süreyi durdurur; ret/zımni retle yeniden işler.
2. **5651 içerik süreleri**: Erişim engelleme/içerik çıkarma kararına karşı CMK m.268 itiraz süresi; m.9'da hâkimin karar verme süresi (24 saat) ve kararın yerine getirilme süresi (kural 4 saat); m.9/A'da BTK'nın 4 saat içinde sonuçlandırma rejimi izlenir.
3. **Sosyal ağ başvuru süreleri**: İçerik kaldırma başvurularını yanıtlama süresi (kural 48 saat) ve şeffaflık raporu dönemleri; kaçırılan yanıt yaptırım doğurur, durmaz.
4. **İdari para cezası zamanaşımı**: 5809/5651 özel hükmü öncelikli; genel kabahat rejiminde 5326 s.K. soruşturma/yerine getirme zamanaşımı tamamlayıcıdır.
5. **Sözleşmesel/tüketici zamanaşımı**: Abonelik alacaklarında TBK m.147 (bazı periyodik edimlerde 5 yıl) ve genel m.146 (10 yıl); tüketici işleminde 6502 özel süreleri; haksız fiilde TBK m.72. Faiz ve fatura alacaklarında tür ayrımı yapılır.

Tüm süreler başlangıç tarihi + dayanak madde + hak düşürücü/zamanaşımı ayrımı ile yazılır; tereddütte en kısa süreye göre hareket edilir.

## Çıktı modülleri
- Konsolide süre takvimi tablosu (olay/dayanak/son gün).
- Durma-kesilme notları.
- Kritik süre uyarı listesi (özellikle kısa içerik ve itiraz süreleri).
