# Yanlış ve Yanıltıcı Atıf Önleme

## Görev
Görünüşte düzgün ama içerik olarak yanlış atıfları — yanlış madde, mülga hüküm, çarpıtılmış ilke, alakasız emsal — tespit edip düzeltmek; metnin dayanaklarını gerçekten taşır hâle getirmek.

## Soğuk başlangıç (intake)
- Atfedilen madde, ileri sürülen kuralı gerçekten içeriyor mu?
- Hüküm güncel mi, yoksa değişmiş/mülga mı?
- Atfedilen kararın ilkesi, metinde söylendiği gibi mi?
- Emsal kararın vakıası eldeki olaya benziyor mu?

## Denetim şeması
1. **Madde-içerik eşleştirme** — Her mevzuat atfı açılır; maddenin gerçek metni ileri sürülen kuralı içeriyor mu kontrol edilir. Sık hata: doğru kanun, yanlış madde; veya doğru madde, yanlış fıkra/bent.
2. **Yürürlük kontrolü** — Mülga/değişik hükme dayanılmış mı (mevzuat.gov.tr güncel metin)? Eski-yeni kanun karışıklığı (örn. eski BK/yeni TBK madde numaraları) ayıklanır.
3. **İlke çarpıtması** — Kararın kurduğu ilke ile metindeki ifade örtüşüyor mu? İstisna kural gibi, obiter ratio gibi sunulmuş olabilir; düzeltilir.
4. **Emsal uygunsuzluğu** — Atfedilen kararın vakıası farklıysa (farklı sözleşme tipi, farklı taraf sıfatı) emsal değildir; benzerlik kararın amacı bakımından test edilir.
5. **Yollama hatası** — Madde başka hükme yolluyor ama atıf yollanan yere değil, yollayan maddeye yapılmışsa; asıl uygulanacak hükme düzeltilir.
6. **Düzeltme ve gerekçe** — Her hata için doğru atıf + neden yanlış olduğu kısaca yazılır; doğrulanamayan kısım `[doğrulanacak]` bırakılır.

## Çıktı modülleri
- Hatalı atıf → doğru atıf düzeltme tablosu.
- Yürürlük/madde uyumsuzluğu listesi.
- İlke çarpıtması / emsal uygunsuzluğu notları.
- Düzeltilmiş dayanak listesi + işaretler.
