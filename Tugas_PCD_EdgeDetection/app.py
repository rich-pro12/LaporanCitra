import streamlit as st
import cv2
import numpy as np
from PIL import Image
import io
import time

# Konfigurasi Halaman
st.set_page_config(page_title='Edge Detection App', page_icon='🔍', layout='wide')
st.title('🔍 Edge Detection: Sobel & Canny')

# --- Sidebar Controls ---
st.sidebar.header('⚙️ Parameter')
method = st.sidebar.selectbox('Metode', ['Sobel', 'Canny', 'Keduanya'])

if method in ['Sobel', 'Keduanya']:
    st.sidebar.subheader('Sobel')
    sobel_ksize = st.sidebar.slider('Kernel Size', 1, 7, 3, step=2)
    sobel_thresh = st.sidebar.slider('Sobel Threshold', 0, 255, 50)

if method in ['Canny', 'Keduanya']:
    st.sidebar.subheader('Canny')
    sigma = st.sidebar.slider('Sigma (Gaussian)', 0.1, 3.0, 1.4, 0.1)
    low_t = st.sidebar.slider('Low Threshold', 10, 150, 50)
    high_t = st.sidebar.slider('High Threshold', 50, 300, 150)

# --- Upload Gambar ---
uploaded_file = st.file_uploader('Upload Gambar', type=['jpg', 'jpeg', 'png'])

if uploaded_file is not None:
    # Konversi ke NumPy Array dan Grayscale
    img = np.array(Image.open(uploaded_file))
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    total_pixels = gray.shape[0] * gray.shape[1]
    
    st.write("---")
    # Tentukan jumlah kolom berdasarkan metode yang dipilih
    num_cols = 3 if method == 'Keduanya' else 2
    cols = st.columns(num_cols)
    
    # Tampilkan Gambar Original
    cols[0].image(img, caption='Original Image', use_column_width=True)
    
    # Variabel untuk menyimpan hasil
    sobel_edges = None
    canny_edges = None

    # TODO: Proses Sobel
    if method in ['Sobel', 'Keduanya']:
        t0 = time.perf_counter()
        # Sobel via OpenCV untuk real-time speed
        gx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=sobel_ksize)
        gy = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=sobel_ksize)
        mag = np.sqrt(gx**2 + gy**2)
        sobel_edges = np.where(mag >= sobel_thresh, 255, 0).astype(np.uint8)
        sobel_time = (time.perf_counter() - t0) * 1000
        
        col_idx = 1
        cols[col_idx].image(sobel_edges, caption='Sobel Edge Detection', use_column_width=True)
        
    # TODO: Proses Canny
    if method in ['Canny', 'Keduanya']:
        t0 = time.perf_counter()
        ksize = int(6 * sigma + 1)
        if ksize % 2 == 0: ksize += 1
        blurred = cv2.GaussianBlur(gray, (ksize, ksize), sigmaX=sigma)
        canny_edges = cv2.Canny(blurred, low_t, high_t)
        canny_time = (time.perf_counter() - t0) * 1000
        
        col_idx = 2 if method == 'Keduanya' else 1
        cols[col_idx].image(canny_edges, caption='Canny Edge Detection', use_column_width=True)

    # TODO: Tampilkan statistik
    st.write("---")
    st.subheader("📊 Statistik Pemrosesan")
    stat_cols = st.columns(2)
    
    if method in ['Sobel', 'Keduanya']:
        edge_count = np.sum(sobel_edges == 255)
        density = edge_count / total_pixels
        with stat_cols[0]:
            st.markdown("**Metode Sobel**")
            st.write(f"- **Waktu Proses:** {sobel_time:.2f} ms")
            st.write(f"- **Jumlah Piksel Tepi:** {edge_count:,}")
            st.write(f"- **Edge Density:** {density:.4f}")
            
            # Fitur Download (Menyimpan hasil ke file)
            img_pil = Image.fromarray(sobel_edges)
            buf = io.BytesIO()
            img_pil.save(buf, format="PNG")
            st.download_button(label="⬇️ Download Hasil Sobel", data=buf.getvalue(), file_name="sobel_result.png", mime="image/png")

    if method in ['Canny', 'Keduanya']:
        edge_count = np.sum(canny_edges == 255)
        density = edge_count / total_pixels
        with stat_cols[1] if method == 'Keduanya' else stat_cols[0]:
            st.markdown("**Metode Canny**")
            st.write(f"- **Waktu Proses:** {canny_time:.2f} ms")
            st.write(f"- **Jumlah Piksel Tepi:** {edge_count:,}")
            st.write(f"- **Edge Density:** {density:.4f}")
            
            # Fitur Download (Menyimpan hasil ke file)
            img_pil = Image.fromarray(canny_edges)
            buf = io.BytesIO()
            img_pil.save(buf, format="PNG")
            st.download_button(label="⬇️ Download Hasil Canny", data=buf.getvalue(), file_name="canny_result.png", mime="image/png")

    st.success('✅ Deteksi tepi selesai!')