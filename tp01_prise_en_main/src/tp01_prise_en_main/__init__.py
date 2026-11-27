module = input("Nom du module : ")
note_cc = float(input("Note de contrôle continu : "))
note_projet = float(input("Note de projet : "))
note_examen = float(input("Note d'examen : "))
moyenne = note_cc * 0.2 + note_projet * 0.2 + note_examen * 0.6
print("Module :", module)
print("Moyenne pondérée :", moyenne)
if moyenne >= 10:
    print("Module valide")
else:
    print("Module non valide")