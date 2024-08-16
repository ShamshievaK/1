 #Обьектоно ориентированное програмирование (ООП) - весь старый код берем и пишем по другому
# В ООП входят классы
# отличие def от lambda  в том что def-многоразовая, lambda-один раз
# class Book:  # Все классы с большой буквы:
#     strr = 400
# # обьект/экземпляр класса
# город_воров= Book()
# print(город_воров)
# # внутр достаем через
# print(город_воров.strr)

# методы вызываем через экзампляры через .
class Book:
    strr = 400

    def __init__(self, title, author, color):
        self.title = title
        self.author = author
        self.color = color

    def info(self):
        print(self.title, self.author, self.color, self.strr)

# магические методы - на 1 функцию:
    def __str__(self):
        return (f'Title: {self.title}, Author: {self.author}, Color: {self.color}, Str: {self.strr}')

    def __len__(self):
        return len(self.title + self.author + self.color)
город_воров= Book('город воров', 'Каныкей', 'зеленый')
капитанская_дочка = Book('капитанская_дочка', 'Пушкин', 'серый')

# print(город_воров.strr, город_воров.title, город_воров.author, город_воров.color)   # не совсем правильно когда нету def info (создаем свою функцию и выводим каак внизу)
# город_воров.info()
# капитанская_дочка.info()

print(город_воров)
print(капитанская_дочка)
print(len(город_воров))
print(len(капитанская_дочка))






#принципы ООП