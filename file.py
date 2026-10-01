print("===== Library =====".upper())
def add_book():
    title = input("enter your title ?")
    author = input("enter athor name ?")
    if title.strip() == "" or author.strip() == "":
        return
    try:
        with open("library.txt","r") as file:
            for line in file:
                old_title,old_author,available = line.strip().split(",")
                if old_title.lower() == title.strip().lower() and old_author == author.strip().lower():
                    return f"book already exist."
    except FileNotFoundError:
        message = "new file created ✅"
    else:
        message = "book added successfully ✅"
    with open("library.txt","a") as file:
        file.write(f"{title},{author},True\n")
    return message

def display_books():
    try:
        with open("library.txt","r") as file:
            for index,line in enumerate(file):
                title,author,available = line.strip().split(",")
                print(f"{index+1}. title: {title}\nauthor: {author}\navailable: {available}")
    except FileNotFoundError:
        print("No book yet")
def searchBook():
    search = str(input("Search your book choice ?"))
    with open("library.txt","r") as file:
        for index,line in enumerate(file):
            title,author,available = line.strip().split(",")
            if search.strip().lower() == title.strip().lower():
                return f"{index+1}. title: {title}\nauthor: {author}\navailable: {available}"
        return "book not found"
def borrowed():
    borrow_book = input("borrow book: ")
    books = []
    found = False
    with open("library.txt","r") as file:
        for line in file:
            title,author,available = line.strip().split(",")
            if borrow_book.strip().lower() == title.lower():
                found = True
                if available == "True":
                    available = "False"
                    message = f"{title} borrowed ✅"
                else:
                    message = f"{title} has been borrowed."
            books.append(f"{title},{author},{available}\n") 
    if not found:
        return "book not found."                       
    with open("library.txt","w") as file:
        file.writelines(books)
        return message
def returned():
    books = []
    found = False
    return_book = input("return book: ")
    with open("library.txt","r") as file:
        for line in file:
            title,author,available = line.strip().split(",")
            if return_book.strip().lower() == title.lower():
                found = True
                if available == "False":
                    available = "True"
                    message = f"{title} returned ✅"
                else:
                    message = f"{title} not borrowed"
            books.append(f"{title},{author},{available}\n")
    if not found:
        return "book not found"
    with open("library.txt","w") as file:
        file.writelines(books)
    return message

def deleted():
    delete_book = input("delete book: ")
    found = False
    books = []
    with open("library.txt","r") as file:
        for line in file:
            title,author,available = line.strip().split(",")
            if delete_book.strip().lower() != title.lower():
                books.append(line)
            else:
                found = True
                message = f"{title} has been removed"
    if not found:
        return "book not found"
    with open("library.txt","w") as file:
        file.writelines(books)
    return message
def statistics():
    total = 0
    borrowed = 0
    accessible = 0
    with open("library.txt","r") as file:
        for line in file:
            title,author,available = line.strip().split(",")
            total+=1
            if available == "True":
                accessible+=1
            else:
                borrowed+=1
    return f"Total book: {total}\nbook borrowed: {borrowed}\nbook available: {accessible}"
while True:
    print(f"1. Add Book\n2. View Books\n3. Search book\n4. Borrow Book\n5. Return book\n6. Delete Book\n7. Statistics\n8. Exit")
    choice = input("Choose: ")
    if choice.isdigit():
        if choice == "1":
            print(add_book())
        elif choice == "2":
            display_books()
        elif choice == "3":
            print(searchBook())
        elif choice == "4":
            print(borrowed())
        elif choice == "5":
            print(returned())
        elif choice == "6":
            print(deleted())
        elif choice == "7":
            print(statistics())
        elif choice == "8":
            break
    else:
        print("Invalid choice")       
            


