
# key errors would need to return .25
# i.e.: if i try fetching for 6 different books, i reach
# the max discount that is .25
discounts = {
    0: 0,
    1: 0,
    2: 0.05,
    3: 0.1,
    4: 0.2,
    5: .25,
}


def potter(books):
    different_books = set(books)
    number_of_different_books = len(different_books)

    discount = discounts.get(number_of_different_books, .25)
    different_books_price = (
        (8 * number_of_different_books) * (1 - discount)
    )
    equal_books_price = (len(books) - number_of_different_books) * 8

    return equal_books_price + different_books_price
