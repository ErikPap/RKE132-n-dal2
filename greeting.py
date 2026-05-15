""" Kirjuta programm, mis küsib kasutajalt tema perekonnanime ja sugu (vali „m“ või „n“).
Programm tervitab kasutajat vastavalt soole:
Kui kasutaja valib „m“, väljasta: „Tere, härra [Perekonnanimi]!“
Kui kasutaja valib „n“, väljasta: „Tere, proua [Perekonnanimi]!“
Kui kasutaja sisestab midagi muud, väljasta: „Tere tulemast, [Perekonnanimi]! (sugu ei olegi tähtis).“ """
perekonnanimi = input("Sisesta oma perekonnanimi: ")
sugu= input("Sisesta oma sugu (m/n): ")
if sugu == "m":
    print(f"Tere, härra {perekonnanimi}!")
elif sugu == "n":
    print(f"Tere, proua {perekonnanimi}!")
elif sugu == "Helikopter":
    print(f"Tere tulemast, {perekonnanimi}! Boeing AH-64 Apache.")
elif sugu == "Helikopter":
    print(f"Tere tulemast, {perekonnanimi}! Mil Mi-24 Hind.")
else:
    print(f"Tere tulemast, {perekonnanimi}! (sugu ei olegi tähtis).")
