# Kurulum (OpenAI Codex)

**Codex ve Türk Hukuku**, OpenAI **Codex** için bir **Agent Skills** koleksiyonudur. Her
hukuk alanı `.agents/skills/<alan>/SKILL.md` altında bir skill'dir; alt-konular o skill'in
`references/` klasöründedir. Kökteki `AGENTS.md` her oturumda yüklenir.

> Önce [`SORUMLULUK-REDDI.md`](./SORUMLULUK-REDDI.md) dosyasını okuyun. İçerik **hukuki
> danışmanlık değildir** ve doğrulanmadan kullanılmamalıdır.

## Codex skill'leri nereden tarar?

| Kapsam | Yol |
|---|---|
| Repo | `.agents/skills/` (geçerli klasör veya repo kökü) |
| Kullanıcı | `~/.agents/skills/` |
| Sistem | `/etc/codex/skills` |

## A) Repo içinde kullanım (en kolay)

```bash
git clone https://github.com/aydincan/turk-hukuku-ve-codex.git
cd turk-hukuku-ve-codex
codex
```

Codex bu klasörde çalışınca skill'ler `.agents/skills/` altından otomatik bulunur.
`AGENTS.md` de kök dizinden yüklenir.

## B) Her yerde kullanım (kullanıcı kapsamı)

Skill'leri kişisel dizine kopyalayın; böylece her repoda kullanılabilir:

```bash
mkdir -p ~/.agents/skills
cp -R .agents/skills/* ~/.agents/skills/
```

## Kullanım

- `/skills` ile yüklü skill'leri listeleyin.
- `$` yazıp bir skill'i adıyla çağırın (ör. `$vergi-davalari`).
- Ya da görevinizi anlatın; açıklamanız bir skill'in tanımıyla eşleşince Codex onu
  kendiliğinden seçer.

Bir skill'i silmeden kapatmak için `~/.codex/config.toml`:

```toml
[[skills.config]]
path = "/abs/path/.agents/skills/<alan>/SKILL.md"
enabled = false
```

> Değişiklikten sonra Codex'i yeniden başlatın.

## Depoyu yeniden üretmek / genişletmek

Tüm skill'ler `scripts/catalog.json` (omurga) ve `scripts/content.json` (hukuki gövde)
dosyalarından üretilir:

```bash
python3 scripts/generate_codex.py
```

- Yeni bir alan eklemek için `scripts/catalog.json` → `eklentiler` dizisine girdi ekleyin.
- Alt-konu gövdeleri `scripts/content.json` içindedir.
- Üretici `.agents/skills/`'i sıfırdan yazar (idempotent); üretilen dosyaları elle
  düzenlemeyin.

## Gereksinimler

- Skill'leri kullanmak için: **OpenAI Codex** (CLI veya IDE).
- Depoyu yeniden üretmek için: **Python 3** (ek bağımlılık yoktur).
