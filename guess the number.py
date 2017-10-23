import random

Zufallszahl = 1
Zahl = 1
Zahl2 = 1
z = 0
i = 0

print("Rate eine zufals zahl mit groesser oder kleiner\n")
Zahl = int(input("Geben sie die hoechst moegliche zahl ein\nEinGabe:"))
#for an input of an int

Zufallszahl = random.randint(1, Zahl)
#gets an random number between 1 and the input

while i != 1:
	Zahl2 = int(input("\nGeben sie eine zahl ein\nEinGabe:"))
	#for an input of an int
	if Zahl2 == Zufallszahl:
		i = 1
	else:
		if Zahl2 > Zufallszahl:
			print("Die Zahl ist kleiner\n")
		if Zahl2 < Zufallszahl:
			print("DIe Zahl ist groesser\n")
	z = z + 1

print("\nKorrekt ")
print("Die Zufallszahl war  ",Zufallszahl)
print("Versuche gebraucht   ",z)
zahl = input("")
