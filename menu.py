import logging
from app import books

logger = logging.getLogger('scraping.menu')

USER_CHOICE = '''Enter one of the following...
'b' - To look at top 5 best books
'c' - To look at top 5 cheapest books
'n' - To just get the next book in the catalogue
'bc' - To look at top 10 best and cheapest books
'q' - To exit

Enter your choice : '''

def print_best_books():
    logger.info('Finding best books by ratings...')
    best_books = sorted(books, key = lambda x : x.rating * -1)[:5]
    for book in best_books:
        print(book)

def print_cheapst_books():
    logger.info('Finding cheapest books by price...')
    cheapest_books = sorted(books, key = lambda x : x.price)[:5]
    for book in cheapest_books:
        print(book)

def print_best_cheapest_books():
    best_cheapest_books = sorted(books, key=lambda x: (x.rating * -1,x.price))[:10]
    for book in best_cheapest_books:
        print(book)

books_generator = (book for book in books)

def get_next_book():
    logger.info('Finding next book from generator of all books...')
    print(next(books_generator))


def menu():
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input == 'b':
            print_best_books()
        elif user_input == 'c':
            print_cheapst_books()
        elif user_input == 'bc':
            print_best_cheapest_books()
        elif user_input == 'n':
            get_next_book()
        else:
            print("Enter proper character...")
        user_input = input(USER_CHOICE)
    logger.debug('Terminating program...')

menu()