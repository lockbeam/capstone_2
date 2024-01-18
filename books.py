class Author:
    def __init__(self, name):
        self.name = name
        self.books = []

    def publish(self, title):
        if title in self.books:
            #can't get this message to display BUT it isn't adding the second entry?
            print(title + ' already in published list')
        else:
            self.books.append(title)

    def __str__(self): #be able to read object when printing
        if self.books:
            book_list = ',\n'.join(self.books)
        else:
            book_list = 'This author ain\'t got no books yet'
        #add books as they are 'published' to the book list
        return f'Name: {self.name} \nBooks Published: \n{book_list}'
    
shakespeare = Author('Billiam Shakespeare')
shakespeare.publish('Hamlet II: Even Hammier')
shakespeare.publish('Hamlet II: Even Hammier')
shakespeare.publish('Richard IVM: Might Wanna Name These Guys Something Else Eventually')

print(shakespeare)

swampman = Author('Swampman')
print(swampman)