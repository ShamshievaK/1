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






