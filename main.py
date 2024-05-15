print("Bienvenue au calculaeur (Calculateur santé / sans T) ")
a = input("Avez-vous déjeuné ce matin ?(o/n)")
b = float(input("Quelle fraction de votre alimentation a consisté des fruit et légumes ?"))
c = float(input("Combien de minutes d'activités physique avez-vous effectué ce matin ?"))
print("Calcul des conseils en cours...")
if b < 0.2 or b > 0.8:
      print("Vous ne mangez pas équilibré tous les jours !Visez 50% de fruits et légumes. ")
elif c <= 30:
  print("Vous ne faites pas suffisement de sport! Visez 30 minutes par jour en moyenne.")
elif   c >= 30 and a == "n":
  print("Attention! Vous ne devez pas faire du sport sur un estomac vide")
  print("Fin de calcul!")

d = input("Voulez-vous ajouter une journée ?(o/n)")
if   d == "o":
     a = input("Avez-vous déjeuné ce matin ?(o/n)")
     b = float(input("Quelle fraction de votre alimentation a consisté des fruit et légumes ?"))
     c = int(input("Combien de minutes d'activités physique avez-vous effectué ce matin ?"))

else:
    print("Passez une belle journée!")