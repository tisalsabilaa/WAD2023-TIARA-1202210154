nilai = int(input("Masukkan nilai : "))
if nilai > 80 :
    print ("Nilai mutu A")
elif 80 > nilai > 70 :
    print ("Nilai mutu AB")
elif 70 > nilai > 65 :
    print ("Nilai mutu B")
elif 65 > nilai > 60 :
    print ("Nilai mutu CB")
elif 60 > nilai > 50 :
    print ("Nilai mutu C")
elif 50 > nilai > 40 :
    print ("Nilai mutu D")
elif nilai < 40 :
    print ("Nilai mutu E")
else :
    print ("Error")