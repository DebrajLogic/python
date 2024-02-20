import requests


def get_product():
    url = 'https://api.freeapi.app/api/v1/public/randomproducts/product/random'
    response = requests.get(url)
    data = response.json()
    product = data['data']
    title = product['title']
    description = product['description']
    price = product['price']
    rating = product['rating']
    print('Product Details:')
    print('title:', title)
    print('description:', description)
    print('price:', price)
    print('rating:', rating)


def get_products():
    url = 'https://api.freeapi.app/api/v1/public/randomproducts'
    response = requests.get(url)
    data = response.json()
    products = data['data']['data']
    for product in products:
        print('\n')
        title = product['title']
        description = product['description']
        price = product['price']
        rating = product['rating']
        print('Product Details:')
        print('title:', title)
        print('description:', description)
        print('price:', price)
        print('rating:', rating)


def main():
    try:
        get_products()
    except Exception as e:
        print('Failed to fetch data!')


if __name__ == '__main__':
    main()
