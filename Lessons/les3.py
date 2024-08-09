# Принципы ООП, GIT clone
# Принципы: наследование (код передает), полиморфизм(должен все наследованное, можно изменить, всять  метод или переменную и в нововм классе изменить ее ), инкапсуляция, абстракция
# DRY - не повторяйся

#Супер класс\Родительский класс
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def reads(self):
        print('Я читаю книгу под авторством: ', self.author)

    def __str__(self):
        return (f'название: {self.title}\n',
                f'автор: {self.author}\n',
                f'цена: {self.price}\n')

tamirlan = Book('blich', 'Tamirlan', 2500)
print(tamirlan)
tamirlan.reads()

# Дочкпний класс
class Novella(Book): ...
    def __init__(self, title, author, price, pnj):
        super().__init__(title, author,price)
        Book.__init__(self, title, author, price)
        self.pnj = pnj

    def __str__(self):
        return (f'{super().__str__()}'
                f'{self.pnj}')

    def reads(self):
        print('я читаю книгу под авторством: ', self.author, 'и я купил ее за ', self.price)

dan = Novella('наруто', 'Дэн', '2000', '70x70')
# dan.reads()
# print(dan)

class Reads:
    def __init__(self, name):
        self.name = name

    def reads(self):
        print(f'я {self.name} читаю манги')

    def anime(self):
        print(f'я {self.name} смотрю аниме')
beka = Reads


#
#
#
#
# class Novella:...
# class Manga: ...
# class Anime: ...
# ##