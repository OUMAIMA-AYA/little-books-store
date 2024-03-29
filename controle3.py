def ajouter_livre():
    f=open('liverfile', 'a')
    L = []
    L.append(input("Nom du livre: "))
    L.append(input("Auteur: "))
    L.append(input("Prix: "))
    f.write(str(L) + '\n')
    f.close()
def afficher_liver():
   f = open('liverfile', 'r')
   print(f.read())
   f.close()
def rechercher_livre(nom):
    f = open('liverfile', 'r')
    for line in f:
       if nom in line:
          print(line)
    f.close()
def modifier_prix(nom_liv, nov_prix):
    lines = []
    f=open('liverfile', 'r')
    for line in f:
       if nom_liv in line:
          line_parts = [elem.strip() for elem in line[1:-2].split(",")]
          line_parts[2] = str(nov_prix)
          line = str(line_parts)
       lines.append(line)
    f=open('liverfile', 'w')
    f.writelines(lines)       
def supprimer_livre(nom_liv):
    f = open('liverfile', 'r')
    lines = f.readlines()
    f.close()
    with open('liverfile', 'w') as f:
        for line in lines:
            if nom_liv not in line:
                f.write(line)
while True:
    print("Que souhaitez-vous faire?")
    print("0 - Quitter")
    print("1 - Ajouter un livre")
    print("2 - Afficher les livres")
    print("3 - Rechercher un livre")
    print("4 - Modifier le prix d'un livre")
    print("5 - Supprimer un livre")
    choix = input("Entrez votre choix:")
    if choix == '0':
        break
    elif choix == '1':
      ajouter_livre()
    elif choix == '2':
      afficher_liver()
    elif choix == '3':
      nom = str(input('donner le nom de livre :'))
      rechercher_livre(nom)
    elif choix == '4':
      nom_liv = str(input("donner nom de livre pour modifier le prix: "))
      nov_prix = float(input("donner nouveau prix de livre: "))
      modifier_prix(nom_liv, nov_prix)
    elif choix == '5':
      nom_liv = str(input("donner nom de livre pour le supprimer: "))
      supprimer_livre(nom_liv)  
    else:
       print("Option invalide. veuillez choisir a nouveau")                   