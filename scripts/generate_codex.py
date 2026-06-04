#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Codex ve Türk Hukuku — depo üreteci.

Aynı `scripts/catalog.json` + `scripts/content.json` (paylaşılan kaynak) üzerinden
OpenAI Codex 'Agent Skills' formatını üretir:

  .agents/skills/<alan>/SKILL.md          -> alan başına bir skill (özet + yönlendirme)
  .agents/skills/<alan>/references/*.md    -> o alanın ~12 alt-konusu (denetim şemaları)
  AGENTS.md                                -> kök: metodoloji + kaynak hijyeni (hep yüklü)
  README.md, SKILLS.md

Codex skill'leri `.agents/skills/` (repo), `~/.agents/skills/` (kullanıcı) veya
`/etc/codex/skills` altından tarar. Her SKILL.md frontmatter'da name + description ister.
"""
import json
import os
import shutil

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CATALOG = os.path.join(ROOT, "scripts", "catalog.json")
CONTENT = os.path.join(ROOT, "scripts", "content.json")
SKILLS_DIR = os.path.join(ROOT, ".agents", "skills")

cat = json.load(open(CATALOG, encoding="utf-8"))
content = json.load(open(CONTENT, encoding="utf-8"))
_p = cat["pazar"]
gruplar = cat["gruplar"]
eklentiler = cat["eklentiler"]

# Codex'e özgü pazar değerleri (kaynak pazar alanları ezilir; sahip/lisans/ithaf paylaşılır)
PAZAR = {
    "baslik": "Codex ve Türk Hukuku",
    "sahip": _p["sahip"],
    "lisans": _p["lisans"],
    "ithaf": _p["ithaf"],
    "homepage": "https://github.com/aydincan/codex-ve-turk-hukuku",
    "kurulum_yolu": "aydincan/codex-ve-turk-hukuku",
    "aciklama": ("Codex ve Türk Hukuku — OpenAI Codex için Türk hukuku Agent Skills "
                 "koleksiyonu. Her hukuk alanı bir skill; metodoloji, atıf hijyeni, sözleşme, "
                 "dava ve mütalaa iş akışları. Katı kaynak hijyeni: içtihat yalnızca "
                 "mahkeme + daire + esas/karar no + tarih + doğrulanabilir kaynakla; "
                 "uydurma karar numarası yok."),
}


def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def skill_aciklama(e):
    kw = ", ".join(e.get("anahtar", [])[:8])
    return (f"{e['aciklama']} Bu beceriyi {e['baslik']} alanındaki sorular, olaylar ve "
            f"belgeler için kullan ({kw}). Alan dışı konularda tetiklenme.").replace('"', "'")


def build_skill_md(e, beceriler, referans_var):
    slug = e["slug"]
    kanunlar = ", ".join(e.get("kanunlar", [])) or "ilgili mevzuat"
    konu_satir = "\n".join(
        f"| {b['ad']} | [`references/{b['slug']}.md`](references/{b['slug']}.md) | {b['aciklama']} |"
        for b in beceriler
    )
    metod = ("\n- Alanın metodolojisi ve kaynak notu: "
             "[`references/_metodoloji.md`](references/_metodoloji.md)") if referans_var else ""
    return f"""---
name: {slug}
description: "{skill_aciklama(e)}"
---

# {e['baslik']}

{e['aciklama']}

**Başat mevzuat:** {kanunlar}

## Çalışma akışı

1. **Süre/aciliyet taraması:** Hak düşürücü süre, zamanaşımı, tebligat, duruşma, itiraz
   süresi var mı? Varsa önce onu sabitle.
2. **Olayı sabitle:** Çekişmesiz/çekişmeli olgular ve eksikler; en çok bir gezelim soru.
3. **Alt-konuya in:** Aşağıdaki tablodan ilgili konuyu seç ve `references/<konu>.md`
   dosyasını oku; oradaki denetim şemasını uygula.
4. **Altlama ve sonuç:** Olay → norm → altlama → gerekçeli sonuç; somut sonraki adım.

## Alt-konular

| Konu | Referans | Ne zaman? |
|---|---|---|{("\n" + konu_satir) if konu_satir else ""}{metod}

## Kaynak kuralı (özet)

İçtihat yalnızca doğrulanmış künyeyle (mahkeme + daire + esas/karar no + tarih +
doğrulanabilir kaynak); **model hafızasından karar numarası üretme**; emin olunmayan künye
`[doğrulanacak]`. Mevzuat madde/fıkra ile. `turk-hukuku-mevzuat-mcp` /
`turk-hukuku-ictihat-mcp` araçları kuruluysa metni hafızadan değil onlardan çek
(`madde_getir`, `ictihat_ara`, `karar_getir`). Ayrıntılı kural kökteki `AGENTS.md`'dedir.

---

*Deneysel; hukuki danışmanlık değildir. Çıktılar yürürlükteki mevzuat ve doğrulanmış
içtihatla teyit edilmelidir. Bkz. `SORUMLULUK-REDDI.md`.*
"""


def build_reference(b):
    return f"{b['govde_md'].strip()}\n"


def build_metodoloji_ref(e, referans_md):
    return f"{referans_md.strip()}\n"


def build_agents_md():
    return f"""# AGENTS.md — Codex ve Türk Hukuku

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
- MCP araçları varsa resmî metni onlardan çek. `turk-hukuku-mevzuat-mcp` kuruluysa
  kanun/madde metnini hafızadan değil `madde_getir` / `kanun_metni_getir` / `mevzuat_ara`
  ile getir; `turk-hukuku-ictihat-mcp` kuruluysa kararları `ictihat_ara` / `karar_getir`
  ile bulup künyeyi (mahkeme, esas/karar no, tarih) aynen aktar. Bu araçlar mevcutsa
  doğrulamada önce onları kullan; yoksa yukarıdaki künye kuralları aynen geçerlidir.

## Sınırlar

Bu skill'ler avukatlık/hukuki danışmanlık yerine geçmez; nihai sorumluluk yetkili
hukukçudadır. Belgelerle/net beyanla desteklenmeyen vakıalar olgu gibi değerlendirilmez.
Ayrıntı: `SORUMLULUK-REDDI.md`.

## İthaf

{PAZAR['ithaf']}
"""


def build_readme(skill_count, topic_count):
    kurulum = PAZAR["kurulum_yolu"]
    bloklar = []
    for gk, gad in gruplar.items():
        ge = [e for e in eklentiler if e["grup"] == gk]
        if not ge:
            continue
        satir = "\n".join(f"| `{e['slug']}` | {e['baslik']} | {e['aciklama']} |" for e in ge)
        bloklar.append(f"### {gad}\n\n| Skill | Başlık | Açıklama |\n|---|---|---|\n{satir}\n")
    katalog = "\n".join(bloklar)
    return f"""# {PAZAR['baslik']}

> **{PAZAR['baslik']}** — OpenAI **Codex** için Türk hukuku **Agent Skills** koleksiyonu.
> Her hukuk alanı bir skill; metodoloji, atıf hijyeni, sözleşme, dava ve mütalaa iş akışları.

{PAZAR['aciklama']}

**{skill_count} skill · {topic_count} alt-konu (references) · {PAZAR['lisans']}**

**Yazar:** {PAZAR['sahip']}

> *{PAZAR['ithaf']}*

---

## ⚠️ Önce bunu okuyun

Bu proje **hukuki danışmanlık değildir** ve denenmiş bir ürün değil; teknik bir oyun
alanıdır. Çıktılar **yürürlükteki mevzuat ve doğrulanmış güncel içtihatla** teyit
edilmelidir. Ayrıntı: [`SORUMLULUK-REDDI.md`](./SORUMLULUK-REDDI.md).

## Kurulum (OpenAI Codex)

Codex skill'leri şu konumlardan tarar: `.agents/skills/` (repo), `~/.agents/skills/`
(kullanıcı), `/etc/codex/skills` (sistem).

**Repo içinde kullanım:** Depoyu klonlayıp Codex'i bu klasörde çalıştırın; skill'ler
`.agents/skills/` altından otomatik bulunur.

```bash
git clone https://github.com/{kurulum}.git
cd codex-ve-turk-hukuku
codex
```

**Her yerde kullanım (kullanıcı kapsamı):** Skill'leri kişisel dizine kopyalayın:

```bash
mkdir -p ~/.agents/skills
cp -R .agents/skills/* ~/.agents/skills/
```

Codex içinde `/skills` ile listeleyin, `$` ile bir skill'i çağırın ya da görev
açıklamanız bir skill'in tanımıyla eşleştiğinde Codex onu kendiliğinden seçer.
Bir skill'i kapatmak için `~/.codex/config.toml`:

```toml
[[skills.config]]
path = "/path/to/.agents/skills/<alan>/SKILL.md"
enabled = false
```

Ayrıntı için [`KURULUM.md`](./KURULUM.md).

## Nasıl çalışır?

1. Kökteki [`AGENTS.md`](./AGENTS.md) her oturumda yüklenir — yöntem + **kaynak hijyeni**.
2. Olayınızı anlatın ya da belgeyi verin; Codex uygun alan-skill'ini seçer.
3. Skill sizi alt-konuya (`references/<konu>.md`) yönlendirir; oradaki denetim şeması uygulanır.
4. Çıktı: gerekçeli mütalaa, dilekçe/sözleşme taslağı, kontrol listesi veya analiz.

## Kaynak hijyeni (omurga)

İçtihat asla model hafızasından zikredilmez; her karar mahkeme + daire + **esas/karar no** +
tarih + doğrulanabilir kaynakla verilir; emin olunmayan künye `[doğrulanacak]`. (Bkz. `AGENTS.md`.)

## Skill kataloğu

{katalog}

## Lisans

**{PAZAR['lisans']}** — [`LICENSE-APACHE`](./LICENSE-APACHE), [`LICENSE-MIT`](./LICENSE-MIT),
[`NOTICE`](./NOTICE).

> "Codex" ve "OpenAI" OpenAI'nin markalarıdır; bu proje OpenAI ile resmî olarak ilişkili değildir.
"""


def build_skills_index(topic_map):
    lines = ["# Skill Dizini (SKILLS.md)\n",
             "Her alan bir skill'dir; alt-konular o skill'in `references/` klasöründedir.\n"]
    for gk, gad in gruplar.items():
        ge = [e for e in eklentiler if e["grup"] == gk]
        if not ge:
            continue
        lines.append(f"\n## {gad}\n")
        for e in ge:
            lines.append(f"\n### `{e['slug']}` — {e['baslik']}\n")
            for b in topic_map[e["slug"]]:
                lines.append(f"- `references/{b['slug']}.md` — {b['ad']}")
    return "\n".join(lines) + "\n"


def main():
    shutil.rmtree(SKILLS_DIR, ignore_errors=True)
    skill_count = 0
    topic_count = 0
    topic_map = {}
    for e in eklentiler:
        slug = e["slug"]
        c = content.get(slug, {}) or {}
        beceriler = c.get("beceriler") or []
        topic_map[slug] = beceriler
        base = os.path.join(SKILLS_DIR, slug)
        referans_md = c.get("referans_md", "")
        write(os.path.join(base, "SKILL.md"),
              build_skill_md(e, beceriler, bool(referans_md)))
        if referans_md:
            write(os.path.join(base, "references", "_metodoloji.md"),
                  build_metodoloji_ref(e, referans_md))
        for b in beceriler:
            write(os.path.join(base, "references", f"{b['slug']}.md"), build_reference(b))
            topic_count += 1
        skill_count += 1

    write(os.path.join(ROOT, "AGENTS.md"), build_agents_md())
    write(os.path.join(ROOT, "README.md"), build_readme(skill_count, topic_count))
    write(os.path.join(ROOT, "SKILLS.md"), build_skills_index(topic_map))
    print(f"Üretildi: {skill_count} skill, {topic_count} alt-konu (references).")


if __name__ == "__main__":
    main()
