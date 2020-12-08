class student_1:
    naamvar = "Aidan"
    lengtevar = 181.5
    leeftijdvar = 16
    hongervar = True

    def honger(self):
        print(f"ik heb honger is: {student_1.hongervar}")

    def naam(self):
        print(f"en mijn maan is {student_1.naamvar}.")

class student_2(student_1):
    random_lijstje_nummersvar = [1, 5, 9]
    random_lijstje_range_nummersvar = range(5, 9)

    def __init__(self):
        naam = "niet Aidan"
        honger = False

    def honger(self):
        print(f"ik heb honger is nu: {student_2.hongervar}")

    def naam(self):
        super().naam()
        print("de functie heb ik in class B gezet, en daarom laat deze funtie deze tekst zien")

run1 = student_1()
run2 = student_2()

print(f"variable naam in class student_1 is {student_1.naamvar}")
print(f"variable lengte in class student_1 is {student_1.lengtevar}")
print(f"variable leeftijd in class student_1 is {student_1.leeftijdvar}")
print(f"variable honger in class student_1 is {student_1.hongervar}")
print(f"variable random_lijstje_nummers in class student_2 is {student_2.random_lijstje_nummersvar}")
print(f"variable random_lijstje_range_nummers in class student_2 is {student_2.random_lijstje_range_nummersvar}")

run1.honger()
run2.honger()
run2.naam()
