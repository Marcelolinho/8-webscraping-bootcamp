from bs4 import BeautifulSoup
import requests

while True:
    page = 1
    op = 0

    stars_dict = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five'}

    stars = int(input('Quantas Estrelas (1-5)?\n'))
    input_star = stars_dict.get(stars)

    for num in range(49):
        website = f'https://books.toscrape.com/catalogue/page-{page}.html'
        response = requests.get(website)
        soup = BeautifulSoup(response.content, 'lxml')

        books = soup.find_all('article', class_='product_pod')
        for book in books:
            star_rating = book.find('p', class_='star-rating')['class'][1]
            stock = book.find('i', class_='icon-ok')

            if star_rating == input_star and stock != None:
                title = book.h3.a['title']
                price = book.find('p', class_='price_color').text
                print(f'Título: {title}, Preço: {price}, Estrelas: {stars} estrelas')

        page += 1
