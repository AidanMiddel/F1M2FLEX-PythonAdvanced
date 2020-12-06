class Mario :

    _lives = 3
    _speed = 30.0

    def __init__(self, snelheid):
        self.snelheid = snelheid

    def mariosnelheid(snel):
        print("Mario's speed is: " , snel.snelheid)



instanceMario = Mario(30)
instanceMario.mariosnelheid()

print( "mario has" , instanceMario._lives , "lives")
instanceMario._speed = 50.5

print("instanceMario snelheid:", instanceMario._speed)

