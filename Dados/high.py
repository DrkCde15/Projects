alt = float(input("Digite sua altura: "))

if alt < 1.0:
    print("Anãzinha")
elif alt < 1.6:
    print("Baixinha")
elif 1.6 <= alt <= 1.8:
    print("Normal")
elif 1.8 < alt <= 2.1:
    print("Amazona")
elif  2.1 < alt <= 3.0:
    print("Morte por snu snu")
else:
    print("Caraio é o Godzilla")