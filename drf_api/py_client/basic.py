import requests

# endpoint = 'http://localhost:8000/api/'

# get_response = requests.get(endpoint, params={'abc': 123}, json={'query': 'hello'})
# print(get_response.text) 
# print(get_response.status_code)

# --------------------------------- # 


print(
    f'''
        1. Display All the books.
        2. Create a book.
        3. Get a perticular book by id.
        4. Update a book.
        5. Delete a book.
    '''
)
while True:
    option = input('Enter a option: ')

    if option == '1':
        books_endpoint = 'http://127.0.0.1:8000/book/'

        book_data = requests.get(books_endpoint)
        print(f'{book_data.text} - {book_data.status_code}')

    elif option == '2':
        book_title = input("Enter a book title: ")

        books_endpoint = 'http://127.0.0.1:8000/book/'
        book_author = input("Enter a book Author")

        book_data = {
            "title": book_title,
            "author": book_author
        }
        
        book = requests.post(books_endpoint, json=book_data)
# --------------------------------- # 
