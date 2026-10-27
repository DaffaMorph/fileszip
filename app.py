import os
import io
import zipfile
from datetime import datetime
from flask import Flask, render_template, request, send_file, jsonify
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Konfigurasi batas ukuran maksimal upload (contoh: 100 MB)
app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024  # 100 MB

@app.route('/')
def index():
    """Menampilkan halaman utama antarmuka pengguna (Web UI)."""
    return render_template('index.html')

@app.route('/compress', methods=['GET', 'POST'])
def compress_files():
    """
    Menerima satu atau beberapa file dari form,
    mengompresnya menjadi arsip .zip di dalam memori,
    lalu mengirimkan berkas .zip langsung untuk diunduh.
    """
    if request.method == 'GET':
        return jsonify({
            'success': False,
            'message': 'Endpoint ini memerlukan metode POST dengan berkas yang diunggah.'
        }), 400
    # 1. Validasi keberadaan file di request
    if 'files' not in request.files:
        return jsonify({
            'success': False,
            'message': 'Tidak ada berkas yang dikirim dalam permintaan.'
        }), 400

    uploaded_files = request.files.getlist('files')

    # Filter file kosong / tidak dipilih
    valid_files = [f for f in uploaded_files if f and f.filename.strip() != '']

    if not valid_files:
        return jsonify({
            'success': False,
            'message': 'Silakan pilih setidaknya satu berkas untuk dikompres.'
        }), 400

    # 2. Penamaan otomatis berkas .zip
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    if len(valid_files) == 1:
        # Jika hanya 1 file, ambil nama file asli (tanpa ekstensi) + timestamp
        original_base_name = os.path.splitext(secure_filename(valid_files[0].filename))[0]
        if not original_base_name:
            original_base_name = "archive"
        zip_filename = f"{original_base_name}_{timestamp}.zip"
    else:
        # Jika banyak file, gunakan penamaan kolektif + timestamp
        zip_filename = f"archive_{timestamp}.zip"

    # 3. Proses kompresi file ke dalam memory buffer (io.BytesIO)
    # Keuntungan in-memory: cepat dan tidak meninggalkan file sampah di server
    memory_zip = io.BytesIO()
    added_files_count = 0
    errors = []
    used_names = set()

    try:
        with zipfile.ZipFile(memory_zip, mode='w', compression=zipfile.ZIP_DEFLATED) as zf:
            for file_storage in valid_files:
                original_name = file_storage.filename
                safe_name = secure_filename(original_name)

                # Fallback jika nama file menjadi kosong setelah diamankan
                if not safe_name:
                    safe_name = f"file_{added_files_count + 1}"

                # Tangani duplikasi nama file di dalam zip yang sama
                base_name, ext = os.path.splitext(safe_name)
                counter = 1
                unique_name = safe_name
                while unique_name in used_names:
                    unique_name = f"{base_name}_{counter}{ext}"
                    counter += 1
                used_names.add(unique_name)

                # Cek integritas bacaan & tangani file corrupt
                try:
                    file_bytes = file_storage.read()

                    # Validasi file kosong jika diinginkan (opsional: tetap masukkan atau beri peringatan)
                    if len(file_bytes) == 0:
                        # File 0-byte tetap bisa diarsipkan, namun dicatat
                        pass

                    # Tulis ke file zip
                    zf.writestr(unique_name, file_bytes)
                    added_files_count += 1
                except Exception as read_err:
                    errors.append(f"Gagal memproses '{original_name}': {str(read_err)}")

        if added_files_count == 0:
            return jsonify({
                'success': False,
                'message': 'Gagal mengompresi berkas. Semua berkas rusak atau tidak dapat dibaca.',
                'errors': errors
            }), 422

        # Posisikan pointer buffer kembali ke awal agar siap dibaca
        memory_zip.seek(0)

        # Kirim langsung file zip ke browser user sebagai unduhan
        return send_file(
            memory_zip,
            mimetype='application/zip',
            as_attachment=True,
            download_name=zip_filename
        )

    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Terjadi kesalahan internal saat kompresi: {str(e)}'
        }), 500

@app.errorhandler(413)
def request_entity_too_large(error):
    """Penanganan error jika total ukuran file melebihi batas konfigurasi."""
    return jsonify({
        'success': False,
        'message': 'Total ukuran berkas terlalu besar! Maksimal upload adalah 100 MB.'
    }), 413

if __name__ == '__main__':
    # Jalankan server lokal di port 5000
    print("==================================================")
    print(" Server File Zipper berjalan di: http://127.0.0.1:5000")
    print(" Tekan CTRL+C untuk menghentikan server.")
    print("==================================================")
    app.run(debug=True, host='127.0.0.1', port=5000)
