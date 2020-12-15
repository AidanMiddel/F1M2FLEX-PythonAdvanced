class student_1:
    naamvar = "Aidan"
    lengtevar = 181.5
    leeftijdvar = 16
    hongervar = True
    naamvarss = "Gerrit"

    def honger(self):
        print(f"ik heb honger is: {student_1.hongervar}")

    def naam(self):
        print(f"en mijn maan is {student_1.naamvar}.")

    def naamvarsss(self):
        print(student_1.naamvarss)

class student_2(student_1):
    random_lijstje_nummersvar = [1, 5, 9]
    random_lijstje_range_nummersvar = range(5, 9)

    def __init__(self):
        naamvar = "niet Aidan"
        hongervar = False
    
    def naamvarsss(self):
        super().naamvarsss()
        print(f"hallo mijn naam is: {student_2.naamvarss}")

    def honger(self):
        print(f"ik heb honger is nu: {student_2.hongervar}")


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
run2.naamvarsss()
