class book():
    def __init__(self, author, title, year):
        self.author = author
        self.title = title
        self.year = year



class pbook(book):
    def __init__(self, author, title, year,numOfPages):
        super().__init__(author, title, year)
        self.numOfPages = numOfPages

    def __str__(self):
        return """Author: {}\nTitle: {}\nYear: {}\nNumber of pages: {}\n""".format(self.author,self.title,self.year,self.numOfPages)#super().__str__()



class ebook(book):
    def __init__(self, author, title, year):
        super().__init__(author, title, year)
        self.file = author+".pdf"
        
    def __str__(self):
        return """Author: {}\nTitle: {}\nYear: {}\nFile format: {}\n""".format(self.author,self.title,self.year,self.file)


if __name__ == '__main__':
    b0 = pbook("ME","GOOD BOOK",2012,9327)
    print(b0)
    b1 = ebook("YOU","NOT BAD BOOK",2021)
    print(b1)
