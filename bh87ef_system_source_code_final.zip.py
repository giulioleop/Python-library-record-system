#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import datetime
import random
import itertools
        
def date_format():
    counter = None
    while counter != 2:
        counter = 0
        inputDate = input("Enter a valid date in format 'dd/mm/yy': ")
        for item in list(inputDate):
            if '/' == item:
                counter += 1
    return inputDate

def validate_date():
    isValidDate = False
    while isValidDate == False:
        select_date = date_format()
        day,month,year = select_date.split('/')

        isValidDate = True
        try :
            datetime.datetime(int(year),int(month),int(day))
        except ValueError :
            isValidDate = False

        if(isValidDate) :
            return datetime.datetime.strptime(select_date, '%d/%m/%y')


# In[ ]:


class Book:
    
    book_ID = itertools.count()
    
    def __init__ (self, title, author, year, publisher, n_of_available_copies, publication_date):
                  
        self.book_ID = next (Book.book_ID)
        self.title = title
        self.author = author
        self.year = year
        self.publisher = publisher
        self.n_of_available_copies = n_of_available_copies
        self.publication_date = publication_date
        
    # 1. A method to create new book records. It creates an empty book instance and then calls the method set_book_details to set the attributes
    
    def create_book ():
        title = None
        author = None
        year = None
        publisher = None
        n_of_available_copies = None
        publication_date = None
        book = Book (title, author, year, publisher, n_of_available_copies, publication_date)
        book.set_book_details()
        return book
    
    def set_book_details (self):
        title = self.set_book_title()
        author = self.set_book_author()
        year = self.set_book_year()
        publisher = self.set_book_publisher()
        n_of_available_copies = self.set_book_number_of_copies()
        publication_date = self.set_book_publication_date()
        book = Book (title, author, year, publisher, n_of_available_copies, publication_date)
        print("A new book has been registered")
        return book
    
    # 2. methods to set: title, author, year, publisher, number of available copies and publication date
        
    def set_book_title(self):
        set_title = input ("Enter the book's title:")
        self.title = set_title
    
    def set_book_author(self):
        set_author = input ("Enter the book's author:")
        self.author = set_author
    
    def set_book_year(self):
        while True:
            try:
                set_year = int(input("Enter the book's year:"))
                while set_year < 0 or set_year > 2100:
                    set_year = int(input("Invalid input. Enter a year between 0 and 2100:"))
                break
            except ValueError:
                print ("Invalid input. Enter a year between 0 and 2100: ")
                continue
        self.year = set_year
        
    def set_book_publisher(self):
        set_publisher = input ("Enter the book's publisher:")
        self.publisher = set_publisher
        
    def set_book_number_of_copies(self):
        while True:
            try:
                set_number_of_copies = int(input("Enter the number of available copies:"))
                while set_number_of_copies < 1:
                    set_number_of_copies = int(input("Available copies can't be <1. Enter the number of available copies:"))
                break
            except ValueError:
                print ("Invalid input. Enter the number of available copies:")
                continue
        self.n_of_available_copies = set_number_of_copies
        
    def set_book_publication_date(self):
        while True:
            try:
                set_publication_date = int(input("Enter the book's publication date:"))
                while set_publication_date < 0 or set_publication_date > 2100:
                    set_publication_date = int(input("Invalid input. Enter a year between 0 and 2100:"))
                break
            except ValueError:
                print ("Invalid input. Enter a year between 0 and 2100: ")
                continue
        self.publication_date = set_publication_date
        
    ############################
    
    # 3. methods to return: title, author, year, publisher, available number of copies and publication date.
    
    def get_book_title(self):
        return self.title
    
    def get_author(self):
        return self.author   
    
    def get_book_year(self):
        return self.year
        
    def get_book_publisher(self):
        return self.publisher
    
    def get_book_number_of_copies(self):
        return self.n_of_available_copies
        
    def get_book_publication_date(self):
        return self.publication_date
    
    ###########################
    
    # Method to print out the book representation
    def display_book(self): 
        print ("Book ID:", self.book_ID, "\nBook title:", self.title, "\nBook author:", self.author, 
               "\nBook year:", self.year, "\nBook publisher:", self.publisher, 
               "\nAvailable copies:", self.n_of_available_copies, "\nPublication date:", self.publication_date, "\n") 


# In[ ]:


class BookList():
    
    # 1. collection to store book instances
    def __init__ (self):
        self.book_list = []
                
    def __len__(self):
        return len(self.book_list)
     
    # method to add a book to the list
    def add_book_to_list(self, book):
        if book in self.book_list:
            book.n_of_available_copies = (book.n_of_available_copies) +1
        else:
            self.book_list.append(book)
            book.n_of_available_copies = book.n_of_available_copies +1
        return self.book_list
    
    # 2. A method to search through the collection and find a book by title, author, publisher OR publication date
    def search_book(self, book_to_search):
        search_success = []
        for book in self.book_list:
            if book_to_search == book.title or book_to_search == book.author or book_to_search == book.publisher or book_to_search == book.publication_date:
                search_success.append(book)
                book.display_book()
                return book
        if len(search_success) == 0:
            print ("Sorry, book not found")
            return None
        
    # book leaving the library (n_available copies - 1) , specified by title
    def book_goes_on_loan (self, title_of_book_to_loan):
        for book in self.book_list:
            if title_of_book_to_loan == book.title:
                if book.n_of_available_copies <= 0:
                    book.display_book()
                    print("Sorry, the book is not available at this time")
                    break
                elif book.n_of_available_copies >0:
                    book.n_of_available_copies = book.n_of_available_copies -1
                
                    
    # 3. Remove book, specified by title                
    def deleting_book_record (self, title_of_book_to_delete):
        search_success =[]
        for book in self.book_list:
            if title_of_book_to_delete == book.title:
                search_success.append(book)
                self.book_list.remove(book)
                print('Book has been deleted from the records')
        if len(search_success) ==0:
            print('Sorry, book not found')
            
    # 4. method to return the total number of books stored in the collection
    def number_of_books (self):
        counter = 0
        total_n_av_copies = []
        for book in self.book_list:
            total_n_av_copies.append(self.book_list[counter].n_of_available_copies)
            counter += 1
        print ("The number of unique books available is: ", len(self.book_list), 
               "\nThe number of total books in the library is: ", sum(total_n_av_copies))
    
    # prints all books in list
    def display_book_list(self):
        counter = 0
        for item in self.book_list:
            self.book_list[counter].display_book()
            counter += 1


# In[ ]:


class User:
    
    def __init__ (self, user_name, first_name, surname, house_number, street_name, postcode, email, DOB):
        self.user_name = user_name
        self.first_name = first_name
        self.surname = surname
        self.house_number = house_number
        self.street_name = street_name
        self.postcode = postcode
        self.email = email
        self.DOB = DOB
        
    # 1. Create a new user instance
    def create_user ():
        user_name = None
        first_name = None
        surname = None
        house_number = None
        street_name = None
        postcode = None
        email = None
        DOB = None
        user = User (user_name, first_name, surname, house_number, street_name, postcode, email, DOB)
        return user
    
    def set_user_details(self, user_list):
        # setting a unique username
        list_of_usernames = []
        for user in user_list.user_list:
            list_of_usernames.append(user.user_name)
        print (list_of_usernames)
        new_user_name = input("Enter the username:")
        while new_user_name in list_of_usernames:
            new_user_name = input("Username not available. Choose another username:")
        self.user_name = new_user_name
        # setting the other details
        first_name = self.set_firstname()
        surname = self.set_surname()
        self.house_number = input ("Enter the user's house number:")
        self.street_name = input ("Enter the user's street name:")
        self.postcode = input ("Enter the user's postcode:")
        email = self.set_email()
        DOB = print ("Enter date of birth:"), self.set_DOB()
        user = User (self.user_name, first_name, surname, self.house_number, self.street_name, self.postcode, email, DOB)
        print("A new user has been created")
        return user
    
    #######################################
    
    # 2. Functions to return: user’s username, firstname, surname, house number, street name, 
    # postcode, email address, and date of birth.
    
    def get_user_name (self):
        return self.user_name
    def get_first_name(self):
        return self.first_name
    def get_surname(self):
        return self.surname
    def get_house_number (self):
        return self.house_number
    def get_street_name (self):
        return self.street_name
    def get_postcode (self):
        return self.postcode
    def get_email (self):
        return self.email
    def get_DOB (self):
        return self.DOB
    
    #########################################
    
    # 3. Edit user’s firstname, surname, email address, and date of birth.
    
    def set_firstname(self):
        new_first_name = input("Enter the first name:")
        self.first_name = new_first_name
    def set_surname(self):
        new_surname = input("Enter the surname:")
        self.surname = new_surname
    def set_email (self):
        new_email = input('Enter the email address:')
        while '@' not in list(new_email) or '.' not in list(new_email):
            new_email = input("Enter a valid email address:")
        self.email = new_email
    def set_DOB (self):
        new_DOB = validate_date()
        self.DOB = new_DOB
    
   ######################################### 
    
    def display_user (self): 
        print (
                'Username: "', self.user_name, 
               '"\nUser first name: "', self.first_name, 
               '"\nUser surname:"', self.surname, 
                '"\nHouse number:"', self.house_number,
                '"\nStreet name:"', self.street_name,
                '"\nPostcode:"', self.postcode,
                '"\nEmail:"', self.email,
                '"\nDOB:"', self.DOB, '"\n'
                )


# In[ ]:


class UserList:
    
    # 1.A function to store a collection of user instances
    def __init__(self):
        self.user_list = []
        
    def __len__(self):
        return len(self.user_list)
    
    #def __getitem__(self, i):
     #   return self.user_list[i]
    
    # method to add a user instance to the user list
    def add_user(self, user):
        if user in self.user_list:
            print ('User already exists')
            pass
        else:
            self.user_list.append(user)
        return self.user_list
    
    # 2. method to remove a user by user’s firstname. Inform if there are two or more users with same firstname and give choice to delete by username.
    def delete_user (self, firstname_of_user_to_delete):
        search_user = []
        for user in self.user_list:
            if firstname_of_user_to_delete == user.first_name:
                search_user.append(user)
                
        if len(search_user) == 1:
            search_user[0].display_user()
            confirm = "None"
            while confirm != "yes" or confirm != "esc":
                confirm = input('Enter "yes" to confirm user deletion or "esc" to cancel:')
                if confirm == "yes":
                    self.user_list.remove(search_user[0])
                    break
                elif confirm == "esc":
                    break
        elif len(search_user) == 0:
            print('Sorry, user not found')
        elif len(search_user) >1:
            print ('More than 1 user found with the same name\n')
            for user in search_user:
                user.display_user()
            select_user = input('Type username of the user to delete or type anything else to cancel:')
            counter = 0
            for user in self.user_list:
                if select_user == self.user_list[counter].user_name:
                    self.user_list.remove(user)
                    print ('User deleted')
                counter += 1
    
    # 3.Method to count the number of users in the system
    def number_of_users (self):
        return len(self.user_list)
    
    # 4. A method to return a user’s detail by the username.
    def search_user(self, username_of_user_to_search):
        search_succes = []
        for user in self.user_list:
            if username_of_user_to_search == user.user_name:
                search_succes.append(user)
                print(user.display_user())
                return user
        if len(search_succes) == 0:
            print('User not found')
            return None
            
    
    # Printing user's list
    def display_user_list(self):
        for item in self.user_list:
            item.display_user()


# In[ ]:


class Loan:
    def __init__ (self, user, book, borrow_date):
        self.user = user
        self.book = book
        self.borrow_date = borrow_date
        
    ##############################################
    
    def create_empty_loan ():
        user = None
        book = None
        borrow_date = None
        loan = Loan (user, book, borrow_date)
        return loan
    
    #1. method for a user to borrow a book. (this is actually finalised by adding it to the LoanedBooks list with the method add_loaned_book)
    def borrow_book (self, user_list, book_list):
        select_user = user_list.search_user(input ("Enter the username who wants to borrow a book: "))
        if select_user == None:
            return None

        select_book = book_list.search_book(input ("Enter the title of the book to borrow: "))
        if select_book == None:
            return None
        self.user = select_user
        self.book = select_book
        self.borrow_date = validate_date()
        loan = Loan(self.user, self.book, self.borrow_date)
        return loan
    
    def display_loan(self):
        print ("\nBorrow date:", self.borrow_date, "\n")
        self.user.display_user(), self.book.display_book() 


# In[ ]:


class LoanedBooks:
    def __init__(self):
        self.loaned_books = []
        
    def display_loaned_books(self):
        counter = 0
        for item in self.loaned_books:
            print (
                "User:", [self.loaned_books[counter].user.user_name, self.loaned_books[counter].user.first_name, 
                  self.loaned_books[counter].user.surname], "; Book:", [self.loaned_books[counter].book.title, 
                   self.loaned_books[counter].book.author], "Borrow date: ", [self.loaned_books[counter].borrow_date]
                  )
            counter += 1
    
      # method to add loan object to list of loaned books
    def add_loaned_book(self, book_list, loan):
        counter = 0
        for book in book_list.book_list:
            if book_list.book_list[counter].title == loan.book.title:
                book_list.book_goes_on_loan(book.title)
            counter += 1
        self.loaned_books.append(loan)
        print('Book added to books on loan')
        return self.loaned_books
    
    """
    def remove_loan(self,loan):
        if loan not in self.loaned_books:
            pass
        else:
            self.loaned_books.remove(loan)
        return self.loaned_books
    """
       
       
    # 2. A method for a user to return a book.
    def return_book (self, user_list, book_list):
        select_user = user_list.search_user(input ("Enter the username who wants to return a book: "))
        if select_user == None:
            return None
        counter = 0
        print("This user has borrowed the following books:\n")
        for loan in self.loaned_books:
            if select_user.user_name == self.loaned_books[counter].user.user_name:
                print (self.loaned_books[counter].book.display_book())
                the_user_is = self.loaned_books[counter].user.user_name
            counter += 1    
        
        select_book = (input("Enter the title of the book you would  like to return:"))
        counter2 = 0
        counter3 = 0
        for loan in self.loaned_books:
            if the_user_is == self.loaned_books[counter2].user.user_name and select_book == self.loaned_books[counter2].book.title:
                self.loaned_books[counter2].book.display_book() 
                
                # this loop of the function is to add +1 number of available copies in the library
                for book in book_list.book_list:
                    if book_list.book_list[counter3].title == self.loaned_books[counter2].book.title:
                        book_list.add_book_to_list(book)
                    counter3 += 1
                    
                self.loaned_books.remove(loan)
                print ('The book has been returned')
            counter2+=1
        return self.loaned_books

    #3. A method to count the total number of books a user is currently borrowing.
    def count_all_books_of_1_user (self, user_list, loan):
        select_user = user_list.search_user(input ("Enter the username who wants to return a book: "))
        if select_user == None:
            return None
        counter = 0
        n_of_books = 0
        print("This user has borrowed the following books:\n")
        while counter < len(self.loaned_books):
            if select_user.user_name == self.loaned_books[counter].user.user_name:
                n_of_books += 1
                print (self.loaned_books[counter].book.display_book())
            counter += 1  
        print ("\nThe total number of books this user is currently borrowing is:", n_of_books)
    
    
    # 4. A method to return all the overdue books along with the users’ username and firstname.A book is considered overdue if on loan for over 30 days.
    
    def overdue_books_from_user(self, user_list):
        select_user = user_list.search_user(input ("Enter the username of the user to check if it has overdue books: "))
        max_loan_duration = datetime.timedelta(30)
        if select_user == None:
            return None
        if select_user != None:
            print("\nThe user:\nUsername:", select_user.get_user_name(), "\nFirstname:", select_user.get_first_name(), "\nhas the following overdue books:\n")
        counter = 0
        for loan in self.loaned_books:
            if select_user.user_name == loan.user.user_name:
                if (datetime.datetime.today()) - (loan.borrow_date) > max_loan_duration:
                    loan.book.display_book()
            
               
    #5. A method to return the firstname, surname and email address name of a borrower of a given book.
    
    def user_firstn_surn_email (self, user_list):
        select_user = user_list.search_user(input ("Enter the username of the user: "))
        if select_user == None:
            return None
        for loan in self.loaned_books:
            if select_user.user_name == loan.user.user_name:
                print ("\nFirst name:", loan.user.get_first_name(), "\nSurname:", loan.user.get_surname(), "\nEmail address:", loan.user.get_email())


# In[ ]:


list_of_books = BookList()
list_of_users = UserList()
books_on_loan = LoanedBooks()


# In[ ]:


book1 = Book ('a game of thrones', 'george martin', 1995, 'random house', 9, 2012)
book2 = Book ('the lord of the rings', 'jrr tolkien', 1948, 'fantasy books', 30, 2012)
book3 = Book ('harry potter', 'jk rowling', 1998, 'fantasy books', 1, 2020)

list_of_books.add_book_to_list(book1)
list_of_books.add_book_to_list(book2)
list_of_books.add_book_to_list(book3)


# In[ ]:


book4 = Book.create_book()

list_of_books.add_book_to_list(book4)


# In[ ]:


book1.display_book()


# In[ ]:


list_of_books.search_book('a game of thrones')


# In[ ]:


list_of_books.display_book_list()


# In[ ]:


list_of_books.number_of_books ()


# In[ ]:


list_of_books.deleting_book_record ('a game of thrones')
list_of_books.display_book_list()


# In[ ]:


book1.set_book_number_of_copies()


# In[ ]:


user1 = User ('mj23','michael', 'jordan', 7, 'Woodside', 'SW19', 'mj23@gmail.com', '17/02/1963')
list_of_users.add_user(user1)


# In[ ]:


user2 = User ('flash', 'usain', 'bolt', 6, 'hertford lodge', 'E19', 'flash@gmail.com', '21/08/1986')
list_of_users.add_user(user2)


# In[ ]:


list_of_users.delete_user('michael')


# In[ ]:


list_of_users.display_user_list()


# In[ ]:


user3 = User.create_user()
user3.set_user_details(list_of_users)


# In[ ]:


list_of_users.add_user(user3)


# In[ ]:


loan1 = Loan.create_empty_loan()
loan1.borrow_book(list_of_users, list_of_books)

loan2 = Loan.create_empty_loan()
loan2.borrow_book(list_of_users, list_of_books)


# In[ ]:


loan3 = Loan.create_empty_loan()
loan3.borrow_book(list_of_users, list_of_books)

#loan4 = Loan.create_empty_loan()
#loan4.borrow_book(list_of_users, list_of_books)


# In[ ]:


books_on_loan.add_loaned_book(list_of_books, loan1)
books_on_loan.add_loaned_book(list_of_books, loan2)
books_on_loan.add_loaned_book(list_of_books, loan3)
#books_on_loan.add_loaned_book(list_of_books, loan4)


# In[ ]:


books_on_loan.display_loaned_books()


# In[ ]:


books_on_loan.count_all_books_of_1_user(list_of_users, loan3)


# In[ ]:


books_on_loan.overdue_books_from_user(list_of_users)


# In[ ]:


books_on_loan.user_firstn_surn_email(list_of_users)


# In[ ]:


books_on_loan.return_book(list_of_users, list_of_books)


# In[ ]:


books_on_loan.display_loaned_books()


# In[ ]:


list_of_books.display_book_list()


# In[ ]:


book5 = Book.create_book()

list_of_books.add_book_to_list(book5)


# In[ ]:


user4 = User.create_user()
user4.set_user_details(list_of_users)


# In[ ]:





# In[ ]:




