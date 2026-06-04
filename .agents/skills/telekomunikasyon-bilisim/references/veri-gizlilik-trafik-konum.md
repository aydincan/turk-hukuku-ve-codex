# Elektronik Haberleşmede Veri, Gizlilik ve Ticari İleti

## Görev
Telekom/internet faaliyetinde kişisel veri, trafik-konum verisi ve haberleşmenin gizliliği yükümlülüklerini 5809 m.51, KVKK (6698) ve ticari ileti rejimi (6563) çerçevesinde denetlemek; uyum veya ihlal sorumluluğunu belirlemek.

## Soğuk başlangıç (intake)
1. İşlenen veri türü: abone kimlik, trafik, konum, içerik/haberleşme verisi mi?
2. İşleme amacı (faturalama, pazarlama, güvenlik, yasal talep) ve dayanağı nedir?
3. Ticari elektronik ileti gönderiliyor mu; İYS kaydı ve rıza var mı?
4. Bir veri ihlali, talep (ilgili kişi/adli/idari) veya Kurul incelemesi var mı?

## Denetim şeması
1. **Çerçeve kesişimi**: 5809 m.51 — kişisel veri ve gizlilik; trafik/konum verisinin sınırlı amaçla işlenmesi ve anonimleştirme/silme. KVKK genel rejimi (6698 m.4-6 işleme şartları, m.5-6 hukuki sebepler) birlikte uygulanır. Ara sonuç: işleme dayanağı geçerli mi.
2. **Trafik ve konum verisi**: Faturalama ve hizmet dışında işleme için kural olarak abone/kullanıcı rızası; sürenin sonunda silme/anonimleştirme. Konum verisi katma değerli hizmette ek rıza gerektirir.
3. **Haberleşmenin gizliliği**: Anayasa m.22 ve 5809 — içeriğe erişim ancak hâkim kararı/yasal yetkiyle; yetkisiz dinleme/kayıt TCK m.132-138 ve m.243-245 ile yarışabilir.
4. **Ticari elektronik ileti**: 6563 — önceden onay (İYS kaydı), ileti içeriği ve red (ICODE/abonelikten çıkma) hakkı; onaysız ileti idari para cezası doğurur. KVKK pazarlama rızasıyla birlikte değerlendirilir.
5. **İhlal ve bildirim**: Veri ihlalinde KVKK m.12 bildirim (Kurul ve ilgili kişi); 5809 kapsamında BTK bildirim yükümlülükleri ayrıca işler. Yasal talepte (adli/idari) yetki ve ölçülülük denetlenir.

İspat açısından rıza kayıtları, İYS onayı, log ve silme/anonimleştirme süreçleri belirleyicidir.

## Çıktı modülleri
- Veri işleme uyum/boşluk notu (dayanak/süre/rıza).
- İhlal bildirimi veya ilgili kişi başvurusu yanıt taslağı.
- Ticari ileti ve İYS uyum kontrol listesi.
