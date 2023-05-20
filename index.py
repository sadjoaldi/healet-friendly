

nbVariations = int(input())

alMontees = 0
alDescentes = 0

for loop in range(nbVariations):
    varAltitude = int(input())
    if (varAltitude < 0):
        alDescentes -= varAltitude
    else:
        alMontees += varAltitude

print(alMontees)
print(alDescentes)
