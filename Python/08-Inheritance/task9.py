class pbook():
    def __init__(self,author,title,year,numOfPages):
        self.author = author
        self.title = title
        self.year = year
        self.numOfPages = numOfPages



class ebook():
    def __init__(self, author, title, year):
        self.author = author
        self.title = title
        self.year = year
        self.file = author+".pdf"
        

class book(pbook,ebook):
    def __init__(self, author, title, year, numOfPages):
        super().__init__(author, title, year, numOfPages)
        self.file = author+".pdf"

    def ebook(self):
        print("""Author: {}\nTitle: {}\nYear: {}\nFile format: {}\n""".format(self.author,self.title,self.year,self.file))

    def pbook(self):
        print("""Author: {}\nTitle: {}\nYear: {}\nNumber of pages: {}\n""".format(self.author,self.title,self.year,self.numOfPages))


if __name__ == '__main__':
    b0 = book("ME","Ksiazka",2012,5321)
    b0.ebook()
    b0.pbook()
