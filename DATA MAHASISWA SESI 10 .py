# Membuat list untuk menyimpan data mahasiswa
data_mahasiswa = []

# Data mahasiswa
mahasiswa1 = {
    "NIM": "24001",
    "Nama": "Iwan",
    "Nilai": 85
}

mahasiswa2 = {
    "NIM": "24002",
    "Nama": "Landi",
    "Nilai": 90
}

mahasiswa3 = {
    "NIM": "24003",
    "Nama": "Rian",
    "Nilai": 78
}

# Menambahkan dictionary ke dalam list
data_mahasiswa.append(mahasiswa1)
data_mahasiswa.append(mahasiswa2)
data_mahasiswa.append(mahasiswa3)

# Menampilkan data mahasiswa
print("===== DATA MAHASISWA =====")

for i, mahasiswa in enumerate(data_mahasiswa, start=1):
    print(f"\nMahasiswa {i}")
    print("NIM   :", mahasiswa["NIM"])
    print("Nama  :", mahasiswa["Nama"])
    print("Nilai :", mahasiswa["Nilai"])