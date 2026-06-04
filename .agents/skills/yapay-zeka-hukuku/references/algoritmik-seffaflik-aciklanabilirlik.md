# Algoritmik Şeffaflık ve Açıklanabilirlik

## Görev
Bir yapay zekâ sisteminin işleyişi ve ürettiği karar hakkında açıklama yükümlülüğünün kapsamını belirlemek; ilgili kişinin bilgi hakkı ile geliştiricinin ticari sır/fikri mülkiyet menfaatini dengeleyerek uygun şeffaflık seviyesini tasarlamak.

## Soğuk başlangıç (intake)
1. Talep eden kim: ilgili kişi, Kurul/denetçi, sözleşmenin karşı tarafı, mahkeme?
2. Ne isteniyor: kararın gerekçesi, kullanılan veri kategorileri, modelin mantığı, kaynak kod?
3. Sistemde aydınlatma metni ve karar gerekçesi loglanıyor mu?
4. Ticari sır/lisans kısıtı veya üçüncü kişi modeli (kapalı API) var mı?

## Denetim şeması
1. **Yükümlülüğün kaynağı**: KVKK m.10 aydınlatma (işlemenin amacı, otomatik karar varlığı), m.11 bilgi talep hakkı ve m.13 başvuru. Bu, kaynak kodun teslimini değil, kararın mantığı ve sonuçları konusunda anlamlı bilgiyi gerektirir. Ara sonuç: talep edilen şeffaflık seviyesi.
2. **Kapsam sınırı**: Şeffaflık, ticari sır ve fikri mülkiyetle (FSEK/SMK, TTK haksız rekabet) sınırlanır; ancak bu sınır bilgi hakkını tamamen bertaraf edemez — "anlamlı açıklama" verilmelidir. Denge ölçülülükle kurulur.
3. **Yargısal talepte**: HMK m.219-220 belgelerin ibrazı ve bilirkişi incelemesi yoluyla teknik açıklama sağlanabilir; mahkeme önünde ticari sır tedbirleriyle inceleme istenebilir.
4. **Kamu kararında**: İdarenin otomatik işleminde gerekçe yükümlülüğü ve İYUK kapsamında bilgi edinme/savunma hakları; gerekçesiz idari işlem sakatlık sebebi.
5. **Belgeleme**: Karar gerekçesinin ve model versiyonunun loglanması, sonradan açıklanabilirliği ve ispatı sağlar.

Kurul rehberleri için kvkk.gov.tr; yargı uygulaması için karararama portalları, künye [doğrulanacak].

## Çıktı modülleri
- Şeffaflık seviyesi matrisi (talep eden / verilecek bilgi / sınır).
- Açıklama metni taslağı (ticari sır korunarak).
- Logging/açıklanabilirlik öneri listesi.
