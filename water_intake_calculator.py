""" Arstid soovitavad juua päevas 2 liitrit vett.
Kirjuta programm, mis küsib kasutajalt, kui palju klaase vett ta juba joonud on. Oletame, et üks klaas = 250 ml.
Programm arvutab, mitu protsenti päevanormist on täidetud, ja annab tagasisidet:
Kui protsent < 50: väljasta: „Joo rohkem vett, keha vajab seda!“
Kui protsent < 100: väljasta: „Tubli, jätka samas vaimus!“
Kui protsent ≥ 100: väljasta: „Suurepärane, oled oma päevase eesmärgi täitnud!“ """

Klaas = int(input("Kui palju klaase vett sa juba joonud oled? "))
total_ml = Klaas * 250
percent = (total_ml / 2000) * 100
if percent < 50:
    print("Joo rohkem vett, keha vajab seda!")
elif percent < 100:
    print("Tubli, jätka samas vaimus!")
else:
    print("Suurepärane, oled oma päevase eesmärgi täitnud!")
