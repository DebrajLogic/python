import requests


def get_books():
    url = 'https://api.freeapi.app/api/v1/public/books'
    response = requests.get(url)
    data = response.json()
    books = data['data']['data']
    for book in books:
        print('*' * 70)
        book_data = book['volumeInfo']
        book_price_info = book['saleInfo'].get('listPrice')
        price = book_price_info and book_price_info.get('amount')
        currency = book_price_info and book_price_info['currencyCode']
        title = book_data['title']
        description = book_data['description']
        rating = book_data.get('ratingsCount')
        authors = book_data['authors']
        print('title: ', title)
        print('description: ', description)
        print(f'price: {currency} {price}')
        print('rating: ', rating)
        print('authors:', [author for author in authors])

        print('*' * 70)
        print('\n')


get_books()
