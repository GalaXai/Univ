class Pbook():
    def __init__(self,author,title,year,numOfPages):
        self.author = author
        self.title = title
        self.year = year
        self.numOfPages = numOfPages



class Ebook():
    def __init__(self, author, title, year):
        self.author = author
        self.title = title
        self.year = year
        self.file = author+".pdf"
        

class Book(Pbook,Ebook):
    def __init__(self, author, title, year, numOfPages):
        super().__init__(author, title, year, numOfPages)
        self.file = author+".pdf"

    def Ebook(self):
        print("""Author: {}\nTitle: {}\nYear: {}\nFile format: {}\n""".format(self.author,self.title,self.year,self.file))

    def Pbook(self):
        print("""Author: {}\nTitle: {}\nYear: {}\nNumber of pages: {}\n""".format(self.author,self.title,self.year,self.numOfPages))


if __name__ == '__main__':
    b0 = Book("ME","Ksiazka",2012,5321)
    b0.Ebook()
    b0.Pbook()
