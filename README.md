# LaporanCitra
# Praktikum 10: Pengolahan Citra Digital - Deteksi Tepi dan Evaluasi Citra

**Mata Kuliah:** Pengolahan Citra Digital  
**Oleh:** Richie Pranata  

---

## 📌 Deskripsi Singkat
Repositori ini berisi implementasi dan laporan untuk **Praktikum 10**. Fokus utama dari tugas ini adalah menerapkan algoritma pengolahan citra digital untuk mendeteksi tepi pada gambar (menggunakan metode Canny) dan melakukan evaluasi terhadap hasil segmentasi citra tersebut menggunakan metrik *Intersection over Union* (IoU).

## ⚙️ Persyaratan (Prerequisites)
Pastikan lingkungan pengembangan Anda sudah terpasang perangkat lunak dan *library* berikut:
* **Python 3.x**
* **OpenCV** (`cv2`) - Untuk pemrosesan citra.
* **NumPy** (`numpy`) - Untuk pengolahan matriks piksel.
* **Matplotlib** (`matplotlib`) - Untuk visualisasi hasil.

## Langkah-Langkah Implementasi

Berikut adalah penjelasan runtut mengenai langkah-langkah teknis yang dilakukan:

### 1. Load Data dan Pre-processing
Program dimulai dengan membaca file gambar menggunakan OpenCV. Citra kemudian dikonversi ke format *grayscale* (skala abu-abu). Tahap ini penting karena algoritma deteksi tepi bekerja berdasarkan perubahan intensitas cahaya, bukan warna. Selain itu, dilakukan *Gaussian Blur* untuk mereduksi *noise* agar hasil deteksi lebih bersih.

### 2. Deteksi Tepi dengan Algoritma Canny
Setelah citra siap, program menerapkan algoritma **Canny Edge Detection**. Proses ini mencakup:
*   **Pencarian gradien intensitas citra:** Menentukan arah dan besarnya perubahan warna.
*   **Non-maximum suppression:** Digunakan untuk menipiskan garis tepi agar hanya piksel dengan nilai tertinggi yang dipertahankan.
*   **Hysteresis Thresholding:** Menentukan garis tepi yang kuat (*strong*) dan lemah (*weak*) berdasarkan nilai ambang batas.

### 3. Evaluasi Menggunakan Metrik IoU
Untuk menguji keakuratan, hasil segmentasi/deteksi dibandingkan dengan citra referensi (*ground truth*). Program menghitung nilai **Intersection over Union (IoU)** dengan cara membagi luas irisan antara hasil program dan referensi dengan luas gabungan keduanya. Semakin mendekati angka 1, maka hasil deteksi dianggap semakin akurat.

### 4. Visualisasi dan Hasil Akhir
Program akan menampilkan jendela yang menunjukkan perbandingan antara:
*   Citra Asli.
*   Hasil Deteksi Tepi (Canny).
*   Hasil Evaluasi.

---

## 💻 Cara Menjalankan Program

1.  **Clone repositori ini:**
    ```bash
    git clone [https://github.com/](https://github.com/)[USERNAME_GITHUB]/[NAMA_REPOSITORI].git
    ```

2.  **Masuk ke direktori:**
    ```bash
    cd [NAMA_REPOSITORI]
    ```

3.  **Jalankan program:**
    ```bash
    python main.py
    ```

---

*Cara instalasi dependensi:*
```bash
pip install opencv-python numpy matplotlib

