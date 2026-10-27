"""
CLI File Zipper Tool (Versi Antarmuka Terminal / CLI)
Cara pakai:
  python zipper_cli.py file1.txt file2.pdf gambar.png
  python zipper_cli.py --output custom_name.zip file1.txt file2.pdf
"""

import sys
import os
import zipfile
import argparse
from datetime import datetime

def compress_cli(file_paths, output_name=None):
    if not file_paths:
        print("[!] Error: Tidak ada berkas yang dipilih untuk dikompres.")
        return False

    # Filter dan verifikasi berkas yang valid
    valid_files = []
    for path in file_paths:
        if not os.path.exists(path):
            print(f"[x] File tidak ditemukan / corrupt: {path}")
            continue
        if os.path.isdir(path):
            print(f"[-] Catatan: '{path}' adalah direktori, akan dilewati (hanya berkas didukung).")
            continue
        valid_files.append(path)

    if not valid_files:
        print("[!] Error: Tidak ada berkas valid yang dapat dikompresi.")
        return False

    # Penamaan otomatis jika tidak ditentukan oleh pengguna
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    if not output_name:
        if len(valid_files) == 1:
            base = os.path.splitext(os.path.basename(valid_files[0]))[0]
            output_name = f"{base}_{timestamp}.zip"
        else:
            output_name = f"archive_{timestamp}.zip"
    else:
        if not output_name.lower().endswith('.zip'):
            output_name += '.zip'

    print(f"\n[*] Memulai pengompresan {len(valid_files)} berkas...")
    compressed_count = 0

    try:
        with zipfile.ZipFile(output_name, 'w', zipfile.ZIP_DEFLATED) as zf:
            for file_path in valid_files:
                file_name = os.path.basename(file_path)
                try:
                    zf.write(file_path, arcname=file_name)
                    print(f" [+] Berhasil dikompres: {file_name}")
                    compressed_count += 1
                except Exception as e:
                    print(f" [x] Gagal membaca berkas '{file_name}': {e}")

        if compressed_count > 0:
            zip_size = os.path.getsize(output_name) / 1024
            print(f"\n[v] Selesai! Berkas zip tersimpan di: {os.path.abspath(output_name)}")
            print(f"[i] Total ukuran berkas arsip: {zip_size:.2f} KB\n")
            return True
        else:
            print("[!] Gagal mengompres seluruh berkas.")
            if os.path.exists(output_name):
                os.remove(output_name)
            return False

    except Exception as e:
        print(f"[!] Terjadi kesalahan saat membuat file zip: {e}")
        return False

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Program Kompresi Berkas ke format .ZIP")
    parser.add_argument('files', nargs='+', help="Daftar berkas yang ingin dikompresi")
    parser.add_argument('-o', '--output', help="Nama file .zip keluaran (opsional, otomatis jika dikosongkan)", default=None)

    args = parser.parse_args()
    compress_cli(args.files, args.output)
