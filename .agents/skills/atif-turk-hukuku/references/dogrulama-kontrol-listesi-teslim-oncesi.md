# Teslim Öncesi Atıf Doğrulama Kontrol Listesi

## Görev
Bir hukuki metin teslim edilmeden önce, içindeki tüm atıfları sistematik bir kontrol listesinden geçirerek hatalı, güncelliğini yitirmiş veya doğrulanmamış hiçbir dayanağın kalmadığından emin olmak.

## Soğuk başlangıç (intake)
- Belge türü ve muhatabı kim (mahkeme, müvekkil, karşı taraf)?
- Metinde kaç mevzuat, kaç içtihat, kaç doktrin atfı var?
- Hangileri teyit edildi, hangileri hâlâ `[doğrulanacak]`?
- Son değişiklikten sonra yeni eklenen atıf var mı?

## Denetim şeması
1. **Envanter** — Metindeki tüm atıflar listelenir: mevzuat (madde/fıkra/bent), içtihat (künye), doktrin (yazar-sayfa). Her biri için "teyit kaynağı" sütunu açılır.
2. **Mevzuat denetimi** — Her madde mevzuat.gov.tr'den açılır; numara, fıkra, bent ve yürürlük durumu (güncel/değişik/mülga) doğrulanır; zaman bakımından uygulama sorunu yoksa işaretlenir.
3. **İçtihat denetimi** — Her künye resmî bankadan teyit edilir; teyit edilemeyen künye `[doğrulanacak]` ile bırakılır veya çıkarılır — **asla tahmin numarasıyla tamamlanmaz.** İBK/AYM bağlayıcılığı doğru sunulmuş mu kontrol edilir.
4. **Doktrin denetimi** — Yazar-eser-sayfa doğrulanır; doğrulanamayan atıf "kaynak teyit edilecek" notuyla bırakılır.
5. **Tutarlılık ve dürüstlük** — Aleyhe yerleşik içtihat gizlenmemiş; tek karar "yerleşik" diye sunulmamış; doktrin kural gibi gösterilmemiş; kesinlik derecesi dürüstçe yansıtılmış mı?
6. **İşaret taraması** — Metinde kalan tüm `[doğrulanacak]` / `[doldurulacak]` işaretleri raporlanır; bilerek bırakılanlar dışında işaretsiz uydurma kalmadığı teyit edilir.

## Çıktı modülleri
- Atıf envanter tablosu (tür / dayanak / teyit durumu).
- Mevzuat ve içtihat doğrulama sonucu (geçti/düzeltildi/`[doğrulanacak]`).
- Dürüstlük/tutarlılık denetimi notu.
- Kalan işaret listesi ve teslim hazırlık özeti.
