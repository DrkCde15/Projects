import phonenumbers
from phonenumbers import timezone, geocoder, carrier
from phonenumbers.phonenumberutil import NumberParseException

numero = input("Digite o número de telefone com o código do país: ")

try:
    # Analisando a string para o número de telefone
    numeroTelefone = phonenumbers.parse(numero)

    # Verifica se o número é válido
    if phonenumbers.is_valid_number(numeroTelefone):
        # Imprimindo o fuso horário usando o módulo timezone
        fusoHorario = timezone.time_zones_for_number(numeroTelefone)
        print("Fuso horário:", ', '.join(fusoHorario))

        # Imprimindo a geolocalização do número usando o módulo geocoder
        geolocalizacao = geocoder.description_for_number(numeroTelefone, "pt")
        print("Localização:", geolocalizacao)

        # Imprimindo o nome da operadora usando o módulo carrier
        operadora = carrier.name_for_number(numeroTelefone, "pt")
        print("Operadora:", operadora)
    else:
        print("O número de telefone inserido não é válido.")
except NumberParseException:
    print("O formato do número de telefone está incorreto.")
