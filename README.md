<div align="center">

<h1 id="readme-top"> SISTEM PENCATATAN NILAI MAHASISWA</h1>
<h3 align="center"> Program digunakan untuk mencatat dan melihat histori nilai mahasiswa. Data harus tersimpan secara dinamis. </h3>

  <p align="center">
   Nama: Muhammad Thoriq Kamil | NIM: 047 | KELAS: B | GANJIL
    <br />
<div align= "left">
<br>
  
## Penjelasan kode program: <br>
**1. Import modul** <br>
<img width="299" height="58" alt="image" src="https://github.com/user-attachments/assets/744fdb3e-4521-483d-8924-e76ce4e23ced" /> <br>
Baris-baris ini memuat modul yang dibutuhkan.<BR>
import json: untuk memanggil file json agar bisa digunakan dalam program.<br>
import prettytable: dipanggil untuk membuat tampilan dalam bentuk tabel kjadi rapi dan mudah dibaca.<br>
import os: dipanggil untuk membersihkan tampilan terminal pada sistem operasi Windows agar tampilan program lebih rapi saat dijalankan. <br>
<br>

**2.Memuat data dari file json** <br>
<img width="298" height="62" alt="Screenshot 2026-10-07 213713" src="https://github.com/user-attachments/assets/dc576386-898c-4486-bb6c-77517e291e61" /> <br>
Program mencoba membuka berkas nilai_mhs.json dalam mode baca ("r"). Fungsi json.load() mengubah isi berkas menjadi list Python dan menyimpannya pada variabel data. Apabila berkas belum ada, Python menghasilkan kesalahan FileNotFoundError yang ditangkap oleh blok except, kemudian data diisi dengan list kosong. Dengan demikian program tetap dapat berjalan pada penggunaan pertama.<br>
<br>

**3. Function simpanData** <br>
<img width="299" height="58" alt="Screenshot 2026-10-07 213728" src="https://github.com/user-attachments/assets/98ae848d-5fc7-4fd1-9f60-38bfbd788dee" /> <br>
Fungsi ini menulis seluruh isi variabel data ke dalam berkas JSON menggunakan mode tulis ("w"). Parameter indent=4 membuat isi berkas tertata rapi dan mudah dibaca. Fungsi ini menjamin data yang ditambahkan tersimpan secara permanen.<br>
<br>

**4.Validasi Input** <br>
<img width="443" height="296" alt="image" src="https://github.com/user-attachments/assets/c90b9247-97c4-474d-bac8-da8ae4ec6857" />
<br>
Terdapat tiga validasi input berupa input angka, input teks, dan input nilai: <br>
1. Input angka: Function ini dimulai dengan while looping, meminta input berupa angka(int) yang di validasi dengan try except. Saat dalam kondisi try akan masuk ke if else untuk memastikan input harus bulat positif, dan jika benar function akan di return, masuk ke kondisi except ketika input bukan angka(int). <br>
2. Input teks: Function ini dimulai dengan while looping, masuk ke if, meminta input berupa string dan akan di return jika benar, jika kosong, maka akan masuk ke kondisi else dengan output print {nama parameter} tidak boleh kosong. <br>
3. Input nilai: Function ini dimulai dengan while looping, meminta input berupa angka bisa desimal(float) yang di validasi dengan try except. Saat dalam kondisi try akan masuk ke if else untuk memastikan input harus diantara bilangan 0-100, dan jika benar function akan di return, masuk ke kondisi except ketika input bukan angka(int). <br>
<br>

**5. Function tanbahData** <br>
<img width="308" height="138" alt="Screenshot 2026-10-07 221936" src="https://github.com/user-attachments/assets/af23d394-fc3a-4d78-9e6b-6933bbb51183" /> <br>
Fungsi ini mengumpulkan tiga input yang sudah tervalidasi, lalu menambahkannya sebagai dictionary baru ke list data menggunakan append(). Setelah itu simpanData() dipanggil untuk menulis perubahan ke berkas. Tanpa pemanggilan simpanData(), data baru hanya berada di memori dan akan hilang ketika program ditutup. <bR>
<br>

**6. Function tampilkanData** <br>
Apabila list data kosong, program menampilkan pesan bahwa belum ada data. Jika terdapat data, program membuat objek PrettyTable dengan empat kolom. Fungsi enumerate(data, start=1) menghasilkan nomor urut yang dimulai dari 1 beserta isi tiap data mahasiswa (mhs). Setiap data kemudian ditambahkan sebagai baris tabel menggunakan add_row() dan tabel dicetak dengan print(table). <br>
<br>

**9. Function Menu Utama (main)** <br>
Fungsi main() merupakan pusat kendali program. Perulangan while True menampilkan menu secara berulang. Metode .strip() berfungsi untuk menghapus spasi di awal dan akhir input agar pilihan menu tidak salah terbaca. Struktur if-elif-else memanggil fungsi sesuai pilihan pengguna. Perulangan berhenti menggunakan break ketika pengguna memilih menu (3) yaitu keluar. Baris main() diakhir dipanggil untuk menjalankan program secara keseluruhan yang dimuali dari menu utama terlebih dahulu (main).<br>
<br>
<br>
<br>


## Output: <br>
<img width="299" height="130" alt="image" src="https://github.com/user-attachments/assets/33f1cef2-0a03-43e3-a25e-62b10c5cabfb" /> <BR>
Tampilan terminal menggunakan import os, dan output dari memanggil menu utama (main), serta tes input tidak sesuai pada menu pilihan.
<br>
<br>

<img width="335" height="117" alt="Screenshot 2026-10-07 230056" src="https://github.com/user-attachments/assets/9245fb1b-7ffd-41f3-9964-aa274c564abe" /> <br>
Output menu pilihan 1 yaitu tampilan data yang disusun menggunakan prettytable<br>
Cek kesesuaian dengan file nilai_mhs.json: <br>
<img width="413" height="218" alt="Screenshot 2026-10-07 230117" src="https://github.com/user-attachments/assets/a70767f4-7b58-4110-a6a1-63c006238f20" /><br>
<br>
<br>

<img width="333" height="191" alt="Screenshot 2026-10-07 230819" src="https://github.com/user-attachments/assets/98fdbba4-1fc3-476a-8ba1-04bf680b951f" /> <br>
Output menu pilihan 2 yaitu tambah data yang diperiksa kredibilitas dari function validasi yang digunakan di function tambah data ini. <br>
<br>
<br>

<img width="332" height="272" alt="image" src="https://github.com/user-attachments/assets/fd8caf2d-1012-4e15-a2b7-febf410dae82" /><br>
Output setelah program diakhiri dan dimulai kembali, data nama dan nikai dari "Wowok" tetap tersimpan dan dapat ditampilkan.<br>
Cek pada file nilai_mhs.json: <br>
<img width="332" height="272" alt="Screenshot 2026-10-07 231926" src="https://github.com/user-attachments/assets/a2de1497-a6a2-4a3a-821a-51344fa071af" />









