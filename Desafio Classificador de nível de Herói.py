nomeHeroi = input()
xpHeroi = int(input())
nivelHeroi = 0

if xpHeroi <= 1000:
    nivelHeroi = "Ferro"
elif xpHeroi <= 2000:
    nivelHeroi = "Bronze"
elif xpHeroi <= 5000:
    nivelHeroi = "Prata"
elif xpHeroi <= 7000:
    nivelHeroi = "Ouro"
elif xpHeroi <= 8000:
    nivelHeroi = "Platina"
elif xpHeroi <= 9000:
    nivelHeroi = "Ascendente"
elif xpHeroi <= 10000:
    nivelHeroi = "Imortal"
else:
    nivelHeroi = "Radiante"  

print(f"O Herói de nome {nomeHeroi} está no nível de {nivelHeroi}")

        
