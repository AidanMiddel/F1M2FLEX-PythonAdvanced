class Mario :

    _lives = 3
    _speed = 30.0

    def __init__(self, lives, speed, jump, fat):
        self.lives = lives
        self.speed = speed
        self.jump = jump
        self.fat = fat

    def nice(pretty):
        print(f"mario has {pretty.lives} lives")
        print(f"mario has {pretty.speed} speed")
        print(f"mario can jump = {pretty.jump}")
        print(f"mario is fat = {pretty.fat}")




instanceMario = Mario(3, 30.0, True, True)
instanceMario.nice()


