# AGENTS.md — Codex ve Türk Hukuku

Bu depo, **OpenAI Codex için Türk hukuku Agent Skills** koleksiyonudur. `.agents/skills/`
altında her hukuk alanı bir skill'dir (özet + yönlendirme); alanın alt-konuları o skill'in
`references/` klasöründedir. Bu dosya (AGENTS.md) **her oturumda yüklü** kalır ve aşağıdaki
yöntem ile **kaynak hijyeni** kurallarını tüm skill'ler için bağlar.

## Kim için

Avukat, hukuk müşaviri, hâkim/savcı adayı, akademisyen ve hukuk öğrencisi. Türk hukukunun
kendi sistematiğine göre (özel/kamu hukuku, suç genel teorisi, dava şartları) düzenlenmiştir.

## Çalışma yöntemi (her görevde)

1. **Önce süre/aciliyet:** Hak düşürücü süre, zamanaşımı, tebligat, itiraz/dava süresi.
2. **Olayı sabitle:** Çekişmesiz/çekişmeli olgular, eksikler. Gerekiyorsa tek somut soru.
3. **Doğru alana yönel:** İlgili `.agents/skills/<alan>` skill'ini ve uygun
   `references/<konu>.md` dosyasını kullan.
4. **Altlama (subsumption):** Olay → norm → şartların somut olaya uygulanması → ara sonuç.
5. **Gerekçeli sonuç:** Risk haritası ve somut sonraki adım; sorumlu kişi ve süre.

## Kaynak hijyeni (DEĞİŞMEZ — tüm skill'ler için)

- **İçtihat asla model hafızasından zikredilmez.** Her karar; mahkeme (Yargıtay / Danıştay /
  Anayasa Mahkemesi / BAM / BİM), daire, **esas ve karar numarası**, tarih ve doğrulanabilir
  kaynak ile verilir (`karararama.yargitay.gov.tr`, `karararama.danistay.gov.tr`,
  `kararlarbilgibankasi.anayasa.gov.tr`, `mevzuat.gov.tr`, UYAP Emsal).
  **Esas/karar numarası ÜRETME.** Emin olunmayan künye `[doğrulanacak]` işaretlenir.
- **Mevzuat** madde/fıkra/bent ile gösterilir (ör. "TBK m.49/1", "HMK m.114/1-ç").
- **Doktrin** yalnızca kullanıcı kaynağı veya lisanslı erişimle; yazar-eser-baskı-sayfa ile.
- Varsayımlar açıkça "varsayım" diye işaretlenir; sahte kesinlik üretilmez.
- MCP sunucuları kuruluysa resmî metni onlardan çek. `turk-hukuku-mevzuat-mcp` kanun ve
  madde metnini mevzuat.gov.tr'den, `turk-hukuku-ictihat-mcp` kararları Yargıtay/BAM
  (UYAP Emsal), Danıştay ve AYM (bireysel başvuru, norm denetimi) bankalarından canlı
  getirir; hangi aracın ne zaman kullanılacağı araçların kendi açıklamalarındadır. Bu
  sunucular varsa doğrulamada önce onları kullan ve dönen künyeyi aynen aktar; yoksa
  yukarıdaki künye kuralları aynen geçerlidir.

## Sınırlar

Bu skill'ler avukatlık/hukuki danışmanlık yerine geçmez; nihai sorumluluk yetkili
hukukçudadır. Belgelerle/net beyanla desteklenmeyen vakıalar olgu gibi değerlendirilmez.
Ayrıntı: `SORUMLULUK-REDDI.md`.

## İthaf

Bu çalışma, ömrünü Türk yargısına adamış babam Hâkim Vahit Polatkan'ın ebedi anısına ithaf edilmiştir.
