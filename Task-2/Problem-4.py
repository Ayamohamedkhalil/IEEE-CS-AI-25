booksDictionary = dict()
def addBook():
    bookId=input("Enter book Id : ").strip()
    while True:
      if not bookId or len(bookId.strip())==0 :
          print("Invalid formar of Id,Please Try again!")
          bookId=input("Enter book Id :").strip()
      elif bookId in booksDictionary:  
        print(f"Warning: Duplicate ID {bookId} found. Please enter a unique ID.")
        bookId=input("Enter book Id : ").strip()
      else :
        break  
    title = input("Enter book title: ").strip() 

    while True:
       if   title == "" or len(title.strip())==0:
        print("Invalid format of book title. Please enter the book title again!")
        title = input("Enter book title: ").strip()
       else:
        break

  

    author=input("Enter book author : ").strip()
    while True:
       if  not author.replace(" ", "").isalpha() or len(author.strip())==0 or author == "":
            print("Invalid format of author name,Please Enter The Book Author Again !")
            author=input("Enter book author : ").strip()
       else:
            break

    publicationYear=input("Enter book publication year : ")
    while True:
        if not publicationYear.isnumeric() or int(publicationYear) <= 0 or int(publicationYear) >=2026 or len(publicationYear.strip())==0 :
            print("Invalid publication year,Please Enter The Book Publication Year Again !")
            publicationYear=input("Enter book publication year : ")
        else:
            break
    booksDictionary[bookId] = {"title":title, "author":author, "publicationYear":publicationYear}
    print("Book added successfully!")
   


def viewBooks():

    if len(booksDictionary) == 0:
        print("No books found in the library.")
    else:
        for bookId, details in booksDictionary.items():
            print(f"Book ID: {bookId}")
            for key, value in details.items():
                print(f"{key}: {value}")
            print()

if __name__ == "__main__":
  while True : 
    print("=====================================================")   
    print("              Catalog of books              ")
    
    print("1.Add book")
    print("2.View books") 
    print("3.Exit")
    print("=====================================================")
    option=input("Enter Your Option (1-3) : ")
    match (option):
        case "1":
           addBook()
        case "2":
            viewBooks()
        
        case "3" :
            print("Exiting from the Catalog") 
            break    
        case _:
            print("Invalid option, Please try again !")                