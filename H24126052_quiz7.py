library = {}

def add_book():
    """
    Prompts the user to enter the title, genre, and price of a book separated by vertical bars.
    Adds the book to the library dictionary with the title as the key and the genre and price as the value.
    Prints a message indicating that the book has been added.
    Returns True to indicate that the book was successfully added.
    """
    try:
        book_info = input("\nEnter the title, genre, and price of the book (separated by | ): ")
        # 提示使用者輸入書名、類別和價格，用豎線 | 分隔
        title, genre, price = book_info.split('|')
        # 將輸入的書名、類別和價格用豎線分割成三個變數
        library[title.strip()] = (genre.strip(), float(price.strip()))
        # 將書名、類別和價格存入字典中，去掉前後的空格並將價格轉換為浮點數
        print(f"\nAdded {title.strip()} to the library.")
        print()
        # 提示書已添加
        return True
    except ValueError:
        # 如果輸入格式不對，捕捉異常
        print("Error: Please enter the title, genre, and price (separated by | )")
        return False

def remove_book():
    """
    Prompts the user to enter the title of a book to remove.
    Removes the book from the library if it is found and prints a message indicating that the book has been removed.
    If the book is not found, prints an error message and returns False.
    Returns True if the book is successfully removed.
    """
    title = input("Enter the title of the book to remove: ").strip()
    # 提示使用者輸入要移除的書名，去掉前後空格
    if title in library:
        # 如果書在圖書館中
        del library[title]
        # 刪除書
        print(f"\nRemoved {title} from the library.")
        print()
        # 提示書已刪除
        return True
    else:
        # 如果書不在圖書館中
        print(f"\nError : {title} not found in the library.")
        print()
        # 提示錯誤
        return False

def get_book_info():
    """
    Prompts the user to enter the title of a book to get information about.
    Prints the title, genre, and price of the book if it is found in the library.
    If the book is not found, prints an error message.
    """
    title = input("Enter the title of the book : ").strip() #去除頭尾空白
    # 提示使用者輸入書名，去掉前後空格
    if title in library:
        # 如果書在圖書館中
        genre, price = library[title]
        # 獲取書的類別和價格
        print(f"\nTitle: {title}\nGenre: {genre}\nPrice: ${price:.1f}")
        # 打印書的詳細信息
        print()
    else:
        # 如果書不在圖書館中
        print(f"\nError : {title} not found in the library.")
        print()
        # 提示錯誤

def list_books():
    """
    Lists all books in the library in alphabetical order by title.
    If the library is empty, prints a message indicating that it is empty and returns False.
    Returns True if there are books in the library.
    """
    if not library:
        # 如果圖書館是空的
        print("\nThe library is empty.\n")
        print()
        # 提示信息
        return False
    for title, (genre, price) in sorted(library.items()):
        # 遍歷圖書館中的所有書，按書名字母順序排列
        print(f"{title} ({genre}, ${price:.2f})")
        # 打印每本書的詳細信息
    print()
    return True

def list_books_by_genre():
    """
    Prompts the user to enter a genre to search for.
    Lists all books in the library that match the specified genre in alphabetical order by title.
    If no books are found in the specified genre, prints an error message and returns False.
    Returns True if at least one book is found in the specified genre.
    """
    genre_to_search = input("Enter the genre to search for: ").strip()
    print()
    # 提示使用者輸入要查找的類別，去掉前後空格
    found_books = {}  # 初始化一個空字典，用於存儲符合條件的書籍

    # 從 library 中迭代每個鍵值對
    for title, (genre, price) in library.items():
        # 檢查這本書的類別是否匹配用戶輸入的類別
        if genre == genre_to_search:
            # 如果匹配，將這本書添加到 found_books 字典中
            found_books[title] = (genre, price)

    # 現在 found_books 包含所有類別匹配的書籍
    
    if not found_books:
        # 如果沒有找到匹配的書
        print(f"No books found in the {genre_to_search} genre.\n")
        # 提示錯誤
        return False

    for title, (genre, price) in sorted(found_books.items()):
        # 遍歷找到的書，按書名字母順序排列
        print(f"{title} ({genre}, ${price:.2f})")
        # 打印每本書的詳細信息
    print()
    return True

while True:
    # 不斷顯示選單直到使用者選擇退出
    print("Menu:\n1. Add a book\n2. Remove a book\n3. Get book information\n4. List all books\n5. List books by genre\n6. Quit")
    choice = input("Enter your choice (1-6): ")
    if choice == "1":
        add_book_return = add_book()
        # 添加書
        if add_book_return:
            list_books()
            # 如果添加成功，列出所有書
    elif choice == "2":
        remove_book_return = remove_book()
        # 移除書
        if remove_book_return:
            list_books()
            # 如果移除成功，列出所有書
    elif choice == "3":
        get_book_info()
        # 獲取書的信息
    elif choice == "4":
        print()
        list_books()
        # 列出所有書
    elif choice == "5":
        list_books_by_genre()
        # 按類別列出書
    elif choice == "6":
        break
        # 退出迴圈
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")
        # 提示錯誤選擇

print("Goodbye!")
# 提示再見信息
