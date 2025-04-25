import glob

name = 0


undone = []
done = []

if name == 0:
    name = input("Hallo! Wie heißt du? ")

print()
print(f"Hallo {name}!")
print()

def Menü():
    print("Was kann ich für dich tun?")
    print()
    print("1 - Aufgabe hinzufügen")
    print("2 - Aufgaben anzeigen")
    print("3 - Aufgaben als erledigt markieren")
    print("4 - Erledigte Aufgaben anzeigen")
    print("5 - Aufgaben löschen")
    print("6 - Daten speichern")
    print("7 - Daten laden")
    print("0 - Beenden")
    print()

def Error():
    print("Bitte gib eine zulässige Zahl ein")
    print()

def save(n):
    with open(f"{n}.txt","w") as file:
                    file.write("Name:\n")
                    file.write(name+"\n")
                    file.write("\n")
                    file.write("Undone:\n")
                    for i in undone:
                        file.write(i+"\n")
                    file.write("\n")
                    file.write("Done:\n")
                    for j in done:
                        file.write(j+"\n")

def show_undone():
    j = 1
    for i in undone:
        print(f"{j} - {i}")
        j += 1


while True:
    Menü()

    try:
        x = int(input("Eingabe: "))
        print()
    except ValueError:
        Error()
        continue


    if x == 0:
        print("Bis bald!")
        exit()


    elif x == 1:
        print("Welche Aufgabe möchtest du hinzufügen?")
        task = input("Eingabe: ")
        undone.append(task)
        print(f"- {task} - hinzugefügt!")


    elif x == 2:
        print("Diese Aufgaben sind noch nicht erledigt:")
        show_undone()


    elif x == 3:
        print("Welche Aufgabe möchtest du als erledigt markieren?")
        print()
        j = 1
        for i in undone:
            print(f"{j} - {i}")
            j += 1

        try:
            d = int(input("Eingabe: "))
            print()
        except ValueError:
            Error()
            continue
        
        if d > 0 and d < j:
            task = undone[d-1]
            print(f"- {task} - wurde als erledigt markiert!")
            undone.pop(d-1)
            done.append(task)
        else:
            Error()


    elif x == 4:
        print("Diese Aufgaben sind bereits erledigt:")
        j = 1
        for i in done:
            print(f"{j} - {i}")
            j += 1
    

    elif x == 5:
        print("Welche Aufgabe möchtest du löschen?")
        j = 1
        for i in undone:
            print(f"{j} - {i}")
            j += 1

        try:
            d = int(input("Eingabe: "))
            print()
        except ValueError:
            Error()
            continue

        if d > 0 and d < j:
            print(f"- {undone[d-1]} - wurde gelöscht!")
            undone.pop(d-1)

        else: 
            Error()
        

    elif x == 6:
        print("Name der Liste:")
        n = input()
        v = f"/Users/lkrei/Documents/Python Scripts/To-Do\\{n}.txt"
       
        if v in glob.glob("/Users/lkrei/Documents/Python Scripts/To-Do/*.txt"):
            print("Liste bereits vorhanden!")
            print("Liste überschreiben? j/n")

            y = input()

            if y == "j":

                save(n)
        
                print(f"Liste '{n}' erfolgreich gespeichert!")
            
            else:
                print(f"Liste '{n}' nicht gespeichert!")

        else:
            save(n)

            print(f"Liste '{n}' erfolgreich gespeichert!")

    
    elif x == 7:
        print("Welche Liste möchtest du laden?")
        for i in glob.glob("/Users/lkrei/Documents/Python Scripts/To-Do/*.txt"):
            print(i[44:-4])
        
        print()
        n = input("Eingabe: ")
        print()
        v = f"/Users/lkrei/Documents/Python Scripts/To-Do\\{n}.txt"

        if v in glob.glob("/Users/lkrei/Documents/Python Scripts/To-Do/*.txt"):
            f = []

            with open(f"{n}.txt") as file:
                for line in file:
                    line = line.replace("\n","")
                    f.append(line)
            
            if "Name:" not in f and "Undone:" not in f and "Done:" not in f:
                print(f"'{n}' ist keine gültige Liste!")
                print()
                continue

            di = 0
            j = 0
            for i in f:
                print(i)
                if i == "Done:":
                    di = j
                j += 1

            name = f[1]
            undone = f[4:di-1]
            done = f[di+1:]
            
        else:
            print(f"Liste '{n}' nicht gefunden")
            

    else:
        Error()
    print()