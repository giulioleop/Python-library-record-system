# Python-library-record-system

Programming Tasks
Design and implement a software system for a fictitious library system. Your system should follow object oriented programming approach. It should contain the following components each represented in a Python class:

Books: Define a Python class with methods to do the following:

A way to create new book records. Each record should have should include the following data:
Randomly generated book ID, title, author, year, publisher, number of available copies and publication date.
Different methods to set each of the following book data, one method per data:
title, author, year, publisher, number of available copies and publication date.
Different methods to return each the following book data, one method per data:
title, author, year, publisher, number of copies, available number of copies and publication date.
The class should include error checking (e.g., exception handling) and well documented by comments.
BookList: Define a Python class with methods to do the following:

Create a method to store a collection (e.g., dictionary, lists, tuple etc.). The collection should store book instances that are created from the Book class.
A method to search through the collection and find a book by one of the following data: title, author, publisher OR publication date.
A method to remove a book from the collection. The book should be specified by its title.
A method to return the total number of books stored in the collection.
The class should include error checking (e.g., exception handling) and well documented by comments.
Users: Define a Python class with functions to do the following:

A function to create a user with the following details:
username, firstname, surname, house number, street name, postcode, email address, and date of birth.
Different function to return a user’s username, firstname, surname, house number, street name, postcode, email address, and date of birth.
Different functions to edit a user’s firstname, surname, email address, and date of birth.
The class should include error checking and well documented by comments.
UserList: Define a Python class with functions to do the following:

A function to store a collection (e.g., dictionary, lists, tuple etc.) of user instances that are created with the class Users.
A method to remove a user from the collection by giving the user’s firstname. This operation must inform program users if there are two or more users with same firstname.
A method to count the number of users in the system.
A method to return a user’s detail by the username.
The class should include appropriate error checking (e.g., exception handling) and well documented by comments.
 Loans: Define a Python class with methods to do the following:

A method for a user to borrow a book.
A method for a user to return a book.
A method to count and return the total number of books a user is currently borrowing.
A method to return all the overdue books along with the users’ username and firstname. The username and firstname of the user should be retrieved through the appropriate methods in the User class.
A method to return the firstname, surname and email address name of a borrower of a given book. This method should make use of the appropriate methods in the User class.
The class should include appropriate error checking (e.g., exception handling) and well documented by comments.
