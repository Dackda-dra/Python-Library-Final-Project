#camelCase

#design a GUI for a library that must
# 1. Be able to add a book
# 2. store the book name, author, and genre
# 3. List all stored books
# 4. Check if a book in the list is available or not
# 5. check in/out selected book

#Optional:
# 1. create a search


import tkinter as tk

import tkinter.messagebox

from PIL import ImageTk, Image



#create global variables
bookNameList = []
bookAuthorList = []
bookGenreList = []
bookAvailable = []


# open file and extract stored names

with open("Books.txt",'r') as data_file:
    for line in data_file:
        data = line.split()
        bookNameList.append(data[0])
        bookAuthorList.append(data[1])
        bookGenreList.append(data[2])
        bookAvailable.append(int(data[3]))

#not sure if I need to close this?***


class library:
    

    
    
    
    
    #functions
    def addBook(self):
        #create window
        self.addBookWindow = tk.Tk()
        #title window
        self.addBookWindow.title('Add a Book')
        
        # Create frames
        self.bookNameFrame = tk.Frame(self.addBookWindow)
        self.bookAuthorFrame  = tk.Frame(self.addBookWindow)
        self.bookGenreFrame  = tk.Frame(self.addBookWindow)
        self.bookAvailFrame = tk.Frame(self.addBookWindow)
        self.finishedFrame = tk.Frame(self.addBookWindow)
        
        #widgets for frames
        #--------------------------- Name
        self.bookNamePrompt = tk.Label(self.bookNameFrame,
                                    text='Enter book name: ')
        self.getBookName = tk.Entry(self.bookNameFrame,
                                        width=10,
                                        borderwidth=1,
                                        relief='solid')
        #---------------------------------------- Author
        self.bookAuthorPrompt = tk.Label(self.bookAuthorFrame,
                                    text='Enter book author: ')
        self.getBookAuthor = tk.Entry(self.bookAuthorFrame,
                                        width=10,
                                        borderwidth=1,
                                        relief='solid')
        #-------------------------------Genre
        self.bookGenrePrompt = tk.Label(self.bookGenreFrame,
                                    text='Enter book genre: ')
        self.getBookGenre = tk.Entry(self.bookGenreFrame,
                                        width=10,
                                        borderwidth=1,
                                        relief='solid')
        #initalizebool
        self.getBookAvailCB = tk.BooleanVar()
        self.getBookAvailCB.set(1)
        #-------------------Available CheckButton is not working at all-------------------------------------************ check button error here
        self.getBookAvail = tk.Checkbutton(self.bookAvailFrame,
                                           text='Is this book Available? WIP',
                                           onvalue=1,
                                           offvalue=0,
                                           variable=self.getBookAvailCB)
        
        #------------------------------------done
        self.addButton = tk.Button(self.finishedFrame,
                                 text='Add Book',
                                 command=self.addBookCycle)
        self.quitButton = tk.Button(self.finishedFrame,
                                    text='Done',
                                    command=self.addBookWindow.destroy)
        
        
        
        #pack widgets
        self.bookNamePrompt.pack(side='left')
        self.getBookName.pack(side='right')
        self.bookAuthorPrompt.pack(side='left')
        self.getBookAuthor.pack(side='right')
        self.bookGenrePrompt.pack(side='left')
        self.getBookGenre.pack(side='right')
        self.getBookAvail.pack(side='right')
        self.addButton.pack(side='left')
        self.quitButton.pack(side='right')
        #pack frames
        self.bookNameFrame.pack()
        self.bookAuthorFrame.pack()
        self.bookGenreFrame.pack()
        self.bookAvailFrame.pack()
        self.finishedFrame.pack()
        
        #enter loop maybe?
        
        
    #this is a command of addBook
    def addBookCycle(self):
        
        bookName = str(self.getBookName.get())
        bookAuthor = str(self.getBookAuthor.get())
        bookGenre = str(self.getBookGenre.get())
        
        if self.getBookAvailCB.get() == 1:
            bookAvail = 1
            
        else:
            bookAvail = 0
        
        # good flag
        nameFlag = True
        authorFlag = True
        genreFlag = True
        
        #check for spaces
        for ch in bookName:
            if ch.isspace():
                tk.messagebox.showinfo('Error:',' Book name must contain no Spaces.')
                nameFlag = False
                
         #check space in author       
        for ch in bookAuthor:
            if ch.isspace():
                tk.messagebox.showinfo('Error:',' Book author must contain no Spaces.')
                authorFlag = False
                
            #check space in genre
        for ch in bookGenre:
            if ch.isspace():
                tk.messagebox.showinfo('Error:',' Book genre must contain no Spaces.')
                genreFlag = False
                
            
        if nameFlag == True and authorFlag == True and genreFlag == True:
 
            bookNameList.append(bookName)
            bookAuthorList.append(bookAuthor)
            bookGenreList.append(bookGenre)
            bookAvailable.append(bookAvail)
        
    
    
    def listBooks(self):
        
        
        #create widget
        self.listOfBooksTestWindow = tk.Tk()
        self.listOfBooksTestWindow.title('List of Books')
        
        #create scroll bar
        listBooksScroll = tk.Scrollbar(self.listOfBooksTestWindow, orient='vertical')
        #createlistbox + scrollcmd
        self.listOfBooksTest = tk.Listbox(self.listOfBooksTestWindow, height='10', width='20', yscrollcommand=listBooksScroll.set)
        listBooksScroll.config(command=self.listOfBooksTest.yview)
        
        #createframe for buttons
        listButtonsFrame = tk.Frame(self.listOfBooksTestWindow)
        
        #create picture frame
        self.listPictureFrame = tk.Frame(self.listOfBooksTestWindow)
        #add picture ?? no way to place in frame******************************************************************************* picture error here
        self.listPicture = ImageTk.PhotoImage(Image.open('bookshelf1.jpg'))
        self.listPictureLabel = tk.Label(image=self.listPicture)
       
        #create buttons for CheckIn,Out, Available
        self.checkInButton = tk.Button(listButtonsFrame,
                                  text='Check In',
                                  command=self.checkIn)
        
        self.checkOutButton = tk.Button(listButtonsFrame,
                                           text='Check Out',
                                           command=self.checkOut)
        
        self.checkAvailButton = tk.Button(listButtonsFrame,
                                          text='Check Availability',
                                          command=self.checkAvail)
        
        # quit button
    
        self.listQuitButton = tk.Button(listButtonsFrame,
                                    text='Done',
                                    command=self.listOfBooksTestWindow.destroy)
        
        
        #pack
        self.listPictureLabel.pack()
        self.checkInButton.pack()
        self.checkOutButton.pack()
        self.checkAvailButton.pack()
        self.listQuitButton.pack()
        listBooksScroll.pack(side='right', fill='y')
        self.listOfBooksTest.pack(side='left', fill='both', expand='1')
        
        #pack frame
        self.pictureFrame.pack()
        listButtonsFrame.pack(side='bottom')
        
        
        insertBookArray = ['','','']
        count = 0
            
        for len in bookNameList:
            insertBookArray[0] = bookNameList[count]
            insertBookArray[1] = bookAuthorList[count]
            insertBookArray[2] = bookGenreList[count]
            insertBook = str(insertBookArray[0] + ' ' + insertBookArray[1] + ' ' + insertBookArray[2])
            self.listOfBooksTest.insert('end',insertBook)
            count = count + 1
  
    
    def checkIn(self):
        for item in self.listOfBooksTest.curselection():
            index = item
            bookAvailable[index] = 1
    
    def checkOut(self):
        for item in self.listOfBooksTest.curselection():
            index = item
            bookAvailable[index] = 0
        
    def checkAvail(self):
        
        for item in self.listOfBooksTest.curselection():
            index = int(item)
 
        getBookAvailbility = int(bookAvailable[index])
        
        if getBookAvailbility == 1:
            tk.messagebox.showinfo('Results', bookNameList[index] + ' is available.')
        else:
            tk.messagebox.showinfo('Results', bookNameList[index] + ' is not available.')
            
        
    def quitSave(self):
                
        #open file
        saveBooks = open("Books.txt",'w')
        #initalize add var
        #stringFile = []
        testStrings = ''
        count = 0
        #start loop to add
        for len in bookNameList:
            testStrings = (bookNameList[count] + ' ' 
                              + bookAuthorList[count] + ' ' 
                              + bookGenreList[count] + ' ' + 
                              str(bookAvailable[count]) + '\n')
            saveBooks.write(testStrings)
            count = count + 1
            
        #finish
        #wanted to add close all windows here but didn't know how to check if window is open
        self.mainWindow.destroy()

    
    # create 6 frames
    
    def GUI(self):
        #create window
        self.mainWindow = tk.Tk()
        
        #title window
        self.mainWindow.title("Python Library")
        
        #create frames
        self.menuFrame = tk.Frame(self.mainWindow)
        self.buttonsFrame = tk.Frame(self.mainWindow)
        self.quitFrame = tk.Frame(self.mainWindow)
        
        #picture frame
        self.pictureFrame = tk.Frame(self.mainWindow)
        self.pictureFrame.place(anchor='center', relx=0.5, rely=0.5)
        
        
        #create picture
        self.menuPicture = ImageTk.PhotoImage(Image.open("stackbooks1.jpg"))
        # create picture label
        self.pictureLabel = tk.Label(image=self.menuPicture)
        self.pictureLabel.pack()
        
        #menuwidgets
        self.menuLabel = tk.Label(self.mainWindow,
                                         text='Select one of the below options')
        #button widgets
        
        self.addBookButton = tk.Button(self.buttonsFrame,
                                 text='Add Book',
                                 command=self.addBook)
        
       
        self.listBooksButton = tk.Button(self.buttonsFrame,
                                  text='List Books',
                                  command=self.listBooks)
        
        
        #quit widgets
        self.quitButton = tk.Button(self.quitFrame,
                                    text='Quit',
                                    command=self.quitSave)
        
        #pack widgets and labels
        self.menuLabel.pack()
        self.addBookButton.pack()
        self.listBooksButton.pack()
        self.quitButton.pack()
        
        #pack frames
        self.pictureFrame.pack()
        self.menuFrame.pack()
        self.buttonsFrame.pack()
        self.quitFrame.pack()
        
        #enter loop
        tk.mainloop()
        

        
        
        
if __name__ == '__main__':
    final = library()
    final.GUI()
    