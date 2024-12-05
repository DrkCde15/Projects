import whois11 #importando o modulo whois
import sys #biblioteca de sistema eletrônico
import os #biblioteca de sistema operacional

arg1 = sys.argv[9]
print(arg1)

print(whois11.whois(input("Alvo: ")))