class SuperHero:
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def name(self):
        print(f'Имя героя: {self.name}')

    def double_helth(self):
        self.health_points *= 2
        print(f'Здоровье увеличено: {self.health_points}')

    def __str__(self):
        return (f'Прозвище: {self.nickname}, суперсила: {self.superpower}, здоровье: {self.health_points}')

    def catch_phrase_length(self):
        return len(self.catchphrase)

hero = SuperHero("Тони Старк", "Железный человек", "Интеллект", 100, "Гений, миллиардер, плейбой, филантроп")
print(hero.name)
hero.double_helth()
print(hero)
print(f'Длина кооронной фразы: {hero.catch_phrase_length()}')



class SuperHero:
    def __init__(self, damage, fly, healthpoints):
        self.damage = damage
        self.flip = fly
        self.health = healthpoints

    def increase_health(self, health_points):
        return health_points **2

class SuperHero2(SuperHero):
    def __init__(self, damage, fly, healthpoints):
        super().__init__(damage, fly, healthpoints)

        self.fight = "air"

    def increase_health(self, health_points):
        return health_points **2
    def new_m(self):
        print("True in the True_phrase")

class SuperHero3(SuperHero):
    def __init__(self, damage, fly, healthpoints):
        super().__init__(damage, fly, healthpoints)
        self.fight = "earth"

    def increase_health(self, health_points):
        return health_points ** 2

    def new_m(self):
        print("True in the True_phrase")

class Villian(SuperHero2):
    def __init__(self, damage, fly, healthpoints):
        super().__init__(damage, fly, healthpoints)
        self.people = "monster"

    def gen_x(self):
        pass

    def crit(self, bad):
        return bad.damage ** 2

spiderman = SuperHero2(100, True, 0)
blackwidow = SuperHero3(80, False, 20)
villian = Villian(150, True, 0)



spiderman.new_m()
print(spiderman.increase_health(50))
villian.crit(blackwidow)
print(blackwidow.damage)








    # def new_m(self):
    #     print("True in the True_phrase")





