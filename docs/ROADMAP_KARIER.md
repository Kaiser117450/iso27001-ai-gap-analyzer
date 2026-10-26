# Roadmap Karier: AI Engineer + Keamanan Informasi (ISO 27001)

Disusun 26 Oktober 2026 untuk Akmal Habib Marzuki. Harga dan syarat sertifikasi berubah, jadi cek situs resminya sebelum mendaftar.

## Fakta penting dulu

1. **ISO 27001 adalah sertifikasi untuk organisasi, bukan untuk orang.** Yang bisa Anda raih sebagai individu adalah sertifikat profesional seperti **ISO/IEC 27001 Lead Implementer** atau **Lead Auditor** (penyelenggara: PECB, BSI, TÜV, IRCA). Anda lulus lewat ujian, bukan lewat proyek GitHub.
2. **Cara tercepat punya cerita "ISO 27001" yang kuat** adalah memimpin persiapan ISMS di tempat kerja Anda sekarang (grup F&B), dengan repo ini sebagai alatnya. Pengalaman nyata ini lebih berharga di CV daripada sertifikat saja.
3. **Tidak ada gaji dollar yang datang otomatis tanpa kerja.** Penghasilan USD datang dari klien atau perusahaan remote yang membayar hasil kerja Anda. Tawaran "gaji otomatis" hampir selalu penipuan.

## Rencana 12 bulan

| Bulan | Target | Bukti yang dihasilkan |
|---|---|---|
| 1 | Push repo ini ke GitHub; aktifkan MFA (passkey) di GitHub, Google, Anthropic; arsipkan repo yang merusak citra (lihat bawah) | Repo publik dengan CI hijau |
| 1–3 | Isi self-assessment nyata untuk perusahaan (simpan **privat**), tutup 5 gap risiko tertinggi: MFA, akun admin bersama, sharing password via WhatsApp, backup yang belum pernah diuji, data member (UU PDP) | Laporan sebelum/sesudah (versi anonim untuk portofolio) |
| 2–4 | Belajar + ujian **ISO/IEC 27001 Lead Implementer** | Sertifikat |
| 3–6 | Proyek AI kedua: misalnya pemeriksa kebijakan keamanan berbasis Claude atau triase log login Supabase | Repo + tulisan blog di akmlab.vercel.app |
| 4–8 | Sertifikat dasar keamanan (mis. ISC2 CC atau CompTIA Security+) dan satu sertifikat cloud/AI | Sertifikat |
| 6–12 | Mulai dibayar USD: proyek freelance (Upwork, Contra), kerja remote (LinkedIn "Remote", Wellfound), atau program bug bounty **resmi** (HackerOne, Bugcrowd) hanya pada target yang mengizinkan | Klien/kontrak pertama |

## Bersihkan profil GitHub sebelum mengajukan apa pun

- **Arsipkan atau hapus fork `Teardroidv4_api` ("Botnet API").** Untuk program keamanan defensif dan perekrut, repo botnet di profil adalah tanda bahaya.
- **Repo `pentes` / tulisan "school data-leak exposure":** pastikan tidak memuat data pribadi siapa pun, dan jelaskan bahwa temuan sudah dilaporkan ke pihak sekolah (responsible disclosure). Kalau belum dilaporkan, laporkan dulu.
- Beri deskripsi dan README pada repo utama (`pnl-system`, `ABSENKOK`, `enakko-stock-dashboard`). Repo tanpa README hampir tidak dibaca perekrut.
- Pin 4–6 repo terbaik, termasuk repo ini.

## Teks LinkedIn (bisa langsung dipakai)

**Headline:**
IT & AI Engineer | Building AI tools for operations & ISO 27001 readiness | Python · TypeScript · Claude API

**About (ringkas):**
I build internal platforms and AI systems for a multi-brand F&B group in Indonesia: reporting pipelines, POS data tooling, attendance apps, and automation used daily across outlets. I'm now leading our information-security groundwork toward ISO/IEC 27001 and Indonesia's PDP Law, and I open-source the tools I build for it. Open to remote AI engineering and security-automation work.
