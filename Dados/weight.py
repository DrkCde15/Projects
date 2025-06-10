peso = float(input("Digite o peso: "))

if 10 <= peso < 40:
    print("Raquitica")
    
elif peso <= 49:
    print("Peso normal")
    
elif 50 <= peso <= 60:
    print("Ippo")
    
elif 60 <= peso <= 100:
    print("Delicia")
    
elif 80 < peso <= 130:
    print("Gostosa")
    
else:
    print("This Carla")