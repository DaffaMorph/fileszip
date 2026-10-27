# 📦 File Zipper & Compressor (Python Flask & CLI)

Aplikasi sederhana untuk mengunggah satu atau banyak berkas, mengompresnya secara otomatis menjadi format `.zip`, dan langsung mengunduh hasilnya. Dilengkapi antarmuka Web UI modern (drag-and-drop) dan juga versi antarmuka baris perintah (CLI).

---

## ✨ Fitur Utama

1. **Multi-File Upload**: Mendukung upload satu atau beberapa berkas sekaligus via Web UI (drag & drop) atau CLI.
2. **Kompresi Otomatis**: Berkas dikompres menggunakan algoritma `ZIP_DEFLATED` standar.
3. **In-Memory Streaming (Web)**: Menggunakan buffer memori (`io.BytesIO`), sehingga tidak menumpuk file sampah di server dan sangat cepat.
4. **Unduhan Otomatis (Direct Download)**: Berkas `.zip` langsung diunduh otomatis oleh browser setelah proses kompresi selesai, lengkap dengan link unduh ulang jika diperlukan.
5. **Penamaan Otomatis**:
   - Jika hanya 1 berkas: `<nama_file_asli>_<timestamp>.zip` (contoh: `laporan_20261027_193000.zip`).
   - Jika banyak berkas: `archive_<timestamp>.zip` (contoh: `archive_20261027_193000.zip`).
6. **Penanganan Error Lengkap**:
   - Validasi jika tidak ada berkas yang dipilih.
   - Pengecekan file corrupt / unreadable stream.
   - Penanganan duplikasi nama file di dalam zip yang sama.
   - Sanitasi nama file dengan `secure_filename` (mencegah directory traversal).
   - Batasan ukuran upload (default: 100 MB).

---

## 📁 Struktur Berkas

```
file-zipper-app/
├── app.py                 # Backend server Flask (Web UI)
├── zipper_cli.py          # Script CLI alternatif untuk terminal
├── requirements.txt       # Dependensi Python (Flask)
├── templates/
│   └── index.html         # Antarmuka web responsif & modern
└── README.md              # Dokumentasi & panduan
```

---

## 🚀 Panduan Menjalankan Program

### 1. Prasyarat
Pastikan Python (versi 3.8 ke atas) telah terpasang di komputer Anda:
```bash
python --version
```

### 2. Masuk ke Direktori Program
Buka Terminal / Command Prompt / PowerShell, lalu masuk ke folder project:
```bash
cd file-zipper-app
```

### 3. Pasang Dependensi
Install paket yang diperlukan (`Flask`):
```bash
pip install -r requirements.txt
```

---

### Cara 1: Menjalankan Versi Web UI (Direkomendasikan)

1. Jalankan server:
   ```bash
   python app.py
   ```
2. Buka browser Anda dan akses alamat:
   ```
   http://127.0.0.1:5000
   ```
3. Tarik & lepaskan (drag and drop) berkas Anda atau klik untuk memilih file.
4. Klik tombol **"Kompres ke .ZIP & Unduh"**.
5. File `.zip` akan otomatis terunduh ke komputer Anda!

---

### Cara 2: Menjalankan Versi CLI (Baris Perintah)

Jika Anda ingin mengompresi langsung dari terminal tanpa membuka browser:

```bash
# Mengompres satu atau beberapa berkas (nama otomatis dengan timestamp)
python zipper_cli.py dokumen.pdf gambar.png catatan.txt

# Menentukan nama output file zip sendiri:
python zipper_cli.py --output berkas_saya.zip file1.docx file2.xlsx
```
