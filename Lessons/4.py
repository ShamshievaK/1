#принципы ООП инкасуляция абстракция множ наследование
# это все наследование
from les3 import Book, Novella, Reads
class Manga: ...
def reads (self):
    print(f'я люблю мангу: {self.title}')
manga = Manga('берсерк', 'кентаро миура', '2500', '70x70')
# manga.reads()
# print(manga)

# MRO -порядок выполнения методов
print(Manga.mro())

# инкапсуляция

class Anime(Novella, Reads):...

anime=Anime

print(Anime.mro())
