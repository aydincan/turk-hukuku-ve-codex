# Uydurma İçerik Tespiti (Anti-Halüsinasyon)

## Görev
Bir metinde gerçek olmayan veya doğrulanamayan karar künyesi, mevzuat hükmü ya da doktrin atfını tespit etmek, işaretlemek ve güvenilir kaynağa yönlendirmek; en önemlisi yeni uydurma üretmemek.

## Soğuk başlangıç (intake)
- Metin kim tarafından üretildi (yapay zekâ çıktısı, ikinci el dilekçe, taslak)?
- İçinde E./K. numaraları, kesin tarihler, "şu daire şöyle demiştir" türü ifadeler var mı?
- Atıflar resmî kaynaktan teyit edilebilir mi?
- Hüküm numarası ile içerik birbiriyle tutarlı görünüyor mu?

## Denetim şeması
1. **Kırmızı bayraklar** — Aşırı kesin künye ama kaynak gösterilmemesi; "yerleşik içtihat" denip tek karara dayanılması; var olmayan madde numarası; kanun adıyla içeriğin uyuşmaması; AYM/AİHM kararına atıfta paragraf yokluğu.
2. **Sıfır-uydurma kuralı** — Şüpheli künye için doğru numara TAHMİN EDİLMEZ. Yapılacak tek şey: ya resmî bankadan doğrulamak, ya da künyeyi `[doğrulanacak]` ile işaretleyip yalnızca ilkeyi bırakmak.
3. **Çapraz doğrulama** — Mevzuat için mevzuat.gov.tr; içtihat için karararama.yargitay.gov.tr / karararama.danistay.gov.tr / kararlarbilgibankasi.anayasa.gov.tr; AİHM için hudoc. Doğrulanamayan atıf "teyit edilemedi" diye not düşülür, silinmez ama dayanak yapılmaz.
4. **İçerik-numara tutarlılığı** — Künyenin daire türü ile uyuşmazlık türü uyumlu mu (örn. ticari uyuşmazlığa adli ceza dairesi atfı şüphelidir)?
5. **Doktrin uydurması** — Var olmayan yazar/eser/sayfa da uydurmadır; doğrulanamayan doktrin atfı "kaynak teyit edilecek" ile bırakılır.
6. **Raporlama** — Tespit edilen her şüpheli atıf, gerekçesiyle listelenir; kullanıcıya "şu künyeyi resmî bankadan teyit edin" yönergesi verilir.

## Çıktı modülleri
- Şüpheli atıf listesi + kırmızı bayrak gerekçesi.
- Her atıf için doğrulama durumu (teyit / `[doğrulanacak]` / teyit edilemedi).
- Temizlenmiş metin önerisi (uydurma yerine ilke + işaret).
- Doğrulama yönergesi (kaynak banka + sorgu).
