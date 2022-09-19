from datetime import datetime,timedelta 

ahora = datetime.now()
dentro_de_una_semana = ahora + timedelta(days=7)
hace_un_year = ahora - timedelta(days=365)

print(ahora)
print(dentro_de_una_semana)

print(ahora.strftime("%B - %d - %Y"))
print(dentro_de_una_semana.strftime("%B / %d / %Y"))
print(hace_un_year)