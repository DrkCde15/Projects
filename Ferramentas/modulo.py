from  atck import * #importando tudo da pasta atck
print(ddos("youtube.com"))
print(ping("youtube.com"))
print(nmap("youtube.com"))


import whois11 #importando o modulo whois
print(whois11.whois(input("Alvo: ")))