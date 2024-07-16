salary = [340, 210, 450, 600, 230, 500, 550]
shuma = 0
for paga in salary:
    shuma = shuma + paga
print(f"Shuma e pagave eshte: {shuma}")

pagamesatare = shuma / len(salary)
print(f"Paga mesatare eshte: {pagamesatare}")

pagaMin = salary[0]
for pagaAktuale in salary:
    if(pagaAktuale < pagaMin):
        pagaMin = pagaAktuale
        print(f"Paga minimale eshte {pagaMin}")

pagaMax = salary[0]
for pagaAktuale in salary:
    if(pagaAktuale > pagaMax):
        pagaMax = pagaAktuale
        print(f"Paga maksimale eshte {pagaMax}")
