# Initialisation des variables
montant = 10000
taux = 5

# Calcul du gain annuel
gain = montant * taux / 100
print("Gain annuel :", gain, "euros")

# Augmentation du capital
montant = montant + 5000
taux = taux + 2

# Nouveau gain
gain = montant * taux / 100
print("Nouveau gain :", gain, "euros")

# Retrait de 10 % du montant total
montant = montant * 0.90
taux = taux - 1

# Calcul final
gain = montant * taux / 100
print("Montant final :", montant, "euros")
print("Nouveau gain :", gain, "euros")
