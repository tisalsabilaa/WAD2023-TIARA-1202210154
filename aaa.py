
kode = (input('Kode Penjualan : '))
tanggal = input('Masukkan Tanggal : ')
Barang = input('Nama Barang ; ')
harga = int(input('Harga Barang : '))
jumlah = int(input('Jumlah Barang : '))
total = harga*jumlah
pajak = (11/100)*total
grandtotal = total+pajak

print ('Kode Penjualan :',kode)
print('Tanggal :',tanggal)
print('Nama barang : ',Barang)
print('Jumlah barang : ',jumlah)
print('Total : ',total)
print('Pajak :',pajak)
print ('Grand total : ',grandtotal)
