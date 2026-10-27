# NexusQuiz 3D • Aplikasi Kuis Interaktif Kelas Atas

Aplikasi web kuis interaktif kelas atas (*high-end critical thinking & simulation platform*) yang dirancang dengan standar arsitektur **Senior Full-Stack Engineer & Lead UI/UX Designer**.

---

## 🌟 Fitur Utama

1. **Metode Input Ganda**:
   * **Form Builder Manual**: Dialog interaktif untuk merancang soal HOTS lengkap dengan skenario kasus, pemilihan model 3D, feedback miskonsepsi per opsi, dan konsep inti pembahasan.
   * **Parser Otomatis Word (.docx)**: Ekstraksi cerdas dokumen Microsoft Word menggunakan tokenizer berbasis token hierarkis (`[SOAL]`, `[TAKSONOMI]`, `[MODEL_3D]`, `Feedback:`, dll.) via `mammoth.js`.

2. **Kualitas Konten Anti AI-Slop (HOTS)**:
   * Setiap soal memiliki skenario dunia nyata bermakna (*real-world case study*).
   * Taksonomi Bloom tingkat tinggi (*Analyze, Evaluate, Create*).
   * **Diagnostic Feedback**: Setiap opsi salah memiliki bedah miskonsepsi logis spesifik, menolak format tebakan hafalan biasa.

3. **Elemen Interaktif 3D (Three.js)**:
   * Rendering WebGL performa tinggi (60-120 FPS) dengan pencahayaan sinematik (*Directional + Ambient + Rim Light*), partikel latar belakang, dan bayangan lembut.
   * Model prosedural 3D dinamis yang berganti sesuai konteks soal:
     * **Topografi Vaskular Jantung & RCA** (Kardiologi).
     * **Airfoil Aerodinamika Transonik & Garis Alir** (Teknik Dirgantara).
     * **Struktur Heliks Ganda DNA & Residu Pengikat** (Biologi Molekuler).
   * Kontrol orbit penuh: drag rotasi, zoom in/out, reset kamera, dan toggle auto-rotate.

4. **Halaman Pembahasan & Analisis Kinerja**:
   * **Donut Chart Interaktif**: Rasio respons Benar (Emerald), Salah (Rose), dan Dilewati (Amber) dengan persentase akurasi di tengah cincin.
   * **Statistik Skor & HOTS Mastery**: Akumulasi skor (+100 poin per HOTS), durasi rata-rata per soal, dan grafik batang penguasaan taksonomi.
   * **Accordion Bedah Soal Mendalam**: Menampilkan konsep inti, langkah pembuktian rasional, serta dekonstruksi opsi pengecoh.
   * Filter pembahasan: *Semua*, *Hanya yang Salah*, *Hanya yang Benar*.

5. **Audio Haptics & UI/UX Mewah**:
   * Synthesizer audio berbasis **Web Audio API** tanpa perlu file MP3 eksternal (suara klik halus, melodi benar 3-nada, umpan balik salah, dan kuis selesai).
   * Palet warna Dark-Mode Obsidian (`#060911`) dengan efek *frosted glass* (*backdrop-filter blur*), tipografi **Plus Jakarta Sans**, dan **JetBrains Mono**.

---

## 🚀 Cara Menjalankan

Aplikasi ini bersifat **zero-dependency runtime** (dapat langsung dibuka di browser tanpa perlu install Node/Python terlebih dahulu):

1. **Langsung via Browser**:
   * Cukup klik dua kali pada file `index.html` atau klik kanan > **Open with Google Chrome / Microsoft Edge**.
2. **Via Visual Studio Code**:
   * Buka folder ini di VS Code: `code .`
   * Buka dengan ekstensi **Live Server** (klik *Go Live* di pojok kanan bawah), atau gunakan VS Code Simple Browser.

---

## 📁 Struktur Berkas

```
.
├── index.html              # Antarmuka utama aplikasi (Three.js + Tailwind + Mammoth + Logic)
├── sample-questions.json   # Basis data soal default berkualitas HOTS
├── template_format.txt     # Dokumentasi format token impor Word (.docx)
├── package.json            # Konfigurasi dependensi project
└── README.md               # Dokumentasi lengkap arsitektur
```
