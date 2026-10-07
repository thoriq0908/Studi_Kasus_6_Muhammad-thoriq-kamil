import json
from prettytable import PrettyTable
import os

os.system("cls")


try:
    with open("nilai_mhs.json", "r", encoding="utf-8") as f:
        data = json.load(f)
except FileNotFoundError:
    data = []

def simpanData():
    with open("nilai_mhs.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
        return


def input_angka(nomor):
    while True:
        teks = input(nomor)
        try:
            angka = int(teks)         
            if angka < 0:             
                print("Input tidak boleh negatif, silahkan input kembali")
            else:
                return angka
        except ValueError:             
            print("Input harus berupa angka, silahkan input kembali")

def input_teks(pesan, nama_field):
    while True:
        teks = input(pesan)
        if teks != "":
            return teks
        else:
            print(f"{nama_field} tidak boleh kosong, silahkan input kembali")

def input_nilai():
    while True:
        try:
            nilai = float(input("Nilai: "))
            if 0 <= nilai <= 100:
                return nilai
            else:
                print("Nilai harus antara 0 sampai 100!")
        except ValueError:
            print("Nilai harus berupa angka!")


def tambahData(data):
    print("\n--- Tambah Nilai Baru ---")
    nama_isi = input_teks("Nama         : ", "Nama")
    nim_isi = input_angka("NIM          : ")
    nilai_isi = input_nilai()

    data.append({
        "Nama": nama_isi,
        "NIM": nim_isi,
        "Nilai": nilai_isi
    })
    simpanData()
    print("Data berhasil ditambahkan dan tersimpan ke nilai_mhs.json!")



def tampilkanData(data):
    if not data:
        print("\nBelum ada data nilai yang tersimpan.")
        return
    else:
        table = PrettyTable()
        table.field_names = ["No", "NIM", "Nama", "Nilai"]
        for i, mhs in enumerate(data, start=1):
            table.add_row([i, mhs['NIM'], mhs['Nama'], mhs['Nilai']])
        print(table)


def main():


    while True:
        print("\n===== SISTEM PENCATATAN NILAI MAHASISWA =====")
        print("1. Lihat semua data nilai")
        print("2. Tambah nilai baru")
        print("3. Keluar")
        pilihan = input("Pilih menu (1/2/3): ").strip()

        if pilihan == "1":
            tampilkanData(data)
        elif pilihan == "2":
            tambahData(data)
        elif pilihan == "3":
            print("Terima kasih, program selesai.")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")

main()  