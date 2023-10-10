harga = int(input("Masukkan harga : "))
jumlah = int(input("Masukkan jumlah : "))
total = harga*jumlah
pajak = total*(1/10)

if jumlah > 5 :
    potongan = total*(5/100)
else :
    potongan = 0

grand_total = (total+pajak)-potongan
print ("total harga : ",total)
print ("Pajak : ",pajak)
print ("Grand Total : ",grand_total)