class e_book:
    def __init__(self,title,author,numberOfPages):
        self.title = title
        self.author = author
        self.numberOfPages = numberOfPages
        self.currentPage =0
        self.isBookOpen = False
        
    def openBook(self):
        self.isBookOpen = True

    def closeBook(self):
        self.isBookOpen = False

    def readPages(self,number):
        if self.isBookOpen == True:
            for i in range(number):
                if self.currentPage < self.numberOfPages:
                    self.currentPage += 1
                else:
                    print("You've Reached the end of the book")
                    break
        else:
            print("e-Book is closed")

    def cover(self):
        print("{} written by {} has {} pages".format(self.title,self.author,self.numberOfPages))

    def bookStatus(self):
        if self.isBookOpen == True:
            print("{} by {} curently page {} out of {}".format(self.title,self.author,self.currentPage,self.numberOfPages))
        else:
            print("e-Book is closed")



if __name__ == '__main__':
    p0 = e_book("Title","Someone",700)
    p0.cover()
    p0.openBook()
    p0.bookStatus()
    p0.readPages(250)
    p0.bookStatus()
    p0.readPages(550)
    p0.bookStatus()
    p0.closeBook()
    p0.readPages(300)