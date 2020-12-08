class Plane :

    _lives = 1
    _speed = 30.0
    _bomber = 1
    _ammunition = 5

    def __init__(self, levens, snelheid, bommer, munitie):
        self.levens = levens
        self.snelheid = snelheid
        self.bommer = bommer
        self.munitie = munitie

    def planelives(leef):
        print("Plane's lives is: " , leef.planelives)
    
    def planespeed(snel):
        print("Plane's speed is: " , snel.planespeed)

    def planebommer(bom):
        print("Plane has bommer: ", bom.planebommer)

    def planeammunition(kogels):
        print("Plane has" , kogels.planeammunition , "boms in storage")


littleplane = Plane(1, 30, 1, 5)
littleplane.planelives()
littleplane.planespeed()
littleplane.planebommer()
littleplane.planeammunition()

