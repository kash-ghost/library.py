#name-pushkar saroha
#date-november16,2025
#project-library inventory & borrowing system
#course-Problem Solving with Python

#task1 welcome

print("="*30)
print("WELCOME TO THE LIBRARY")
print("INVENTORY & BORROW SYSTEM")
print("="*30)
print("Manage books,search title,borrow and return books")
print("="*30)
books={}
borrowed={}
while True:
    print("library menu")
    print("1-add book")
    print("2-view books")
    print("3-search book")
    print("4-borrow book")
    print("5-return book")
    print("6-exit")
    choice = input("Enter your choice: ")    
#task2 adding books to list part=

    if choice=="1":
        print("adding new book")
        book_id=input("enter book id-")
        if book_id in books:
            print("book id already exists...")
            continue
        title=input("enter book title-")
        author=input("enter book authors name-")
        try:
            copies = int(input("enter no. of copies to be added-"))
        except ValueError:
            print("invalid no. book not added")
            continue
        books[book_id]={"title":title,"author":author,"copies":copies}
        print("book is added")
#task3 book list part=

    elif choice=="2":
        print("library book list")
        if not books:
            print("No books avilable at the current moment to be issued")
        else:
            print(f"{'ID':<10}{'TITLE':<25}{'AUTHOR':<20}{'COPIES'}")
            for book_id, info in books.items():
                print(f"{book_id:<10}{info['title']:<25}{info['author']:<20}{info['copies']}")
            print()
#task3 search part =

    elif choice=="3":
        print("book search")
        print("1-search by book id")
        print("2-search by book title")
        search_choice = input("enter choice-")
        if search_choice=="1":
            book_id=input("enter book id-")
            if book_id in books:
                info = books[book_id]
                print(f"Found: {info['title']} by {info['author']} ({info['copies']} copies)")
            else:
                print("not found")
        elif search_choice=="2":
            title=input("Enter book title-").lower()
            found=False
            for info in books.values():
                if title in info['title'].lower():
                    print(f"{info['title']} by {info['author']} - Copies: {info['copies']}")
                    found = True
            if not found:
                print("book not found.")
        print()
#task4 borrow book part=

    elif choice=="4":
        print("book borrowing")
        student=input("enter students name-")
        if student in borrowed:
            print("This student has already borrowed a book, no new books will be issued")
            continue
        book_id=input("enter book id to borrow-") 
        if book_id in books:
            if books[book_id]["copies"]>0:
                books[book_id]["copies"] -= 1
                borrowed[student]=book_id
                print("Book issued")
            else:
                print("not avilable")
        else:
            print("invalid book id")
#task5 return part=

    elif choice=="5":
        print("returning books")
        student = input("enter students name-")
        if student in borrowed:
            book_id=borrowed[student]
            books[book_id]["copies"]+=1
            del borrowed[student]
            print("book return accepted")
            borrowed_list=[f"{s}->{b}"for s,b in borrowed.items()]
            print("cxurrently borrowed books-", borrowed_list,)
        else:
            print("No books issued by this student this student")
#task6 exitting loop=

    elif choice=="6":
        print("exiting the app...tata waves*")
        break
    else:
        print("invalid choice")
