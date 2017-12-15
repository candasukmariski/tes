import random
soal = {"Indonesia":"Jakarta","Singapura":"Singapura"}
negara = list(random.choice(soal.key()))
print("Apa nama Ibu Kota dari Negara" + negara)
jawab = input("jawaban: ")
if jawab == str(soal.get(negara)):
	print("Benar!")
else:
	print("Salah!")