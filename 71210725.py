import json

with open ('mahasiswa.json', 'r') as file:
    mahasiswa = json.load(file)

    n = dict()
    jumlah = int(input('Masukkan jumlah mahasiswa baru : '))

    for i in range(jumlah):
        nama = input("Masukkan nama Anda : ")
    
        hobi_list = []
        hobi = int(input("Masukkan Jumlah Hobi : "))
        for j in range(hobi):
            hobby = input("Masukkan Hobi ke-{} : ".format(j+1))
            hobi_list.append(hobby)
  
        prestasi = input("Masukkan prestasi Anda : ")

        print("===Data berhasil ditambahkan===\n")

        n[nama] = [{"Biodata" : {"Hobi" : hobi_list, "Prestasi" : prestasi}}]

    mahasiswa.update(n)

with open('mahasiswa.json', 'w') as file:
    json.dump(mahasiswa,file)