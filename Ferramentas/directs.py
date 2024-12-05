import requests

url = 'https://www.cnnbrasil.com.br/'

lista =["admin", "login", "css", "sport"]

for i in lista:
    url_to_check = url + i
    r = requests.get(url + i)

    if r.status_code == 200:
        print(url_to_check)
        print (r.status_code)
        print("########")
    else:
        print("não eh 200")
        continue