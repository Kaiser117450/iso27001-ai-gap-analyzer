# Draf Pengajuan: Anthropic Cyber Verification Program (CVP)

Sumber: Claude Help Center, "Cyber Verification Program" (diperbarui Oktober 2026), dan pengumuman Anthropic tanggal 6 Oktober 2026.

## Apakah Anda perlu CVP?

CVP **bukan sertifikasi dan bukan pekerjaan berbayar.** CVP hanya mengurangi pemblokiran oleh safety classifier untuk pekerjaan keamanan tertentu, seperti analisis malware dan validasi eksploit. Untuk proyek ini (review kode, threat modeling, gap analysis, mencari kerentanan di kode sendiri), model Claude biasa **sudah cukup tanpa CVP.**

Ajukan CVP hanya jika pekerjaan keamanan defensif Anda benar-benar terblokir.

## Syarat untuk individu

- Individu hanya bisa mendapat **Defense Access**, dan harus memakai **paket Claude berbayar**. Red Team Access hanya untuk organisasi.
- Contoh individu yang memenuhi syarat menurut Anthropic: "individual researchers with a track record of reported vulnerabilities".
- Anda harus lolos verifikasi identitas, menjelaskan pekerjaan keamanan Anda, dan menyatakan kontrol keamanan yang Anda pakai. Mulai 15 Desember 2026, Defense Access mewajibkan MFA tahan-phishing (passkey/security key) dan tidak lagi memakai API key.
- Cara mengajukan: masuk ke Verification Portal (portal.anthropic.com), buka **Programs**, pilih **Cyber Verification Program**, lalu **Apply**. Keputusan biasanya dikirim lewat email dalam 7 hari kerja.
- **Hanya Anda yang bisa mengirim pengajuan ini.** Tidak ada yang bisa menjamin Anda lulus.

**Opsi lain yang lebih kuat:** jika perusahaan tempat Anda bekerja mengajukan sebagai organisasi untuk mengamankan sistemnya sendiri (POS, data member, aplikasi internal), admin organisasi bisa membagikan seat kepada Anda.

## Draf jawaban "Describe your security work" (sesuaikan, jujur, bahasa Inggris)

> I am the IT & Business Development Officer for a multi-brand F&B group in Indonesia (Ayam Guling Enakko, Hisana Fried Chicken, Roscik). I build and maintain internal systems, including POS data pipelines, P&L reporting, attendance apps and customer loyalty data, and I am responsible for securing them.
>
> My security work is defensive and limited to systems my employer owns: hardening authentication and access control, reviewing our own code for vulnerabilities, preparing for ISO/IEC 27001 and Indonesia's Personal Data Protection Law, and triaging security events in our cloud services (Supabase, Vercel, Google Workspace). I open-source the tooling, e.g. an ISO 27001 Annex A gap analyzer: https://github.com/Kaiser117450/iso27001-ai-gap-analyzer
>
> I am requesting Defense Access because [jelaskan tugas spesifik yang benar-benar terblokir, misalnya menganalisis file mencurigakan yang diterima staf outlet]. Account security: MFA via passkey on my Anthropic, Google and GitHub accounts.

Jangan menulis klaim yang tidak bisa Anda buktikan. Anthropic memverifikasi pelamar dan bisa mencabut akses.
