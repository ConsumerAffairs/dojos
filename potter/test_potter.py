from potter import potter

books = [
    'the philosophers stone',
    'the chamber of secrets',
    'the prisoner of azkaban',
    'the goblet of fire',
    'the order of the phoenix',
    'the half-blood prince',
    'the deathly hallows',
]


def test_potter_returns():
    potter(books)


def test_no_books():
    assert potter([]) == 0


def test_one_book():
    assert potter([books[-1]]) == 8


def test_equal_books():
    assert potter([books[0], books[0], books[0]]) == 24


def test_different_books():
    assert potter([books[0], books[1]]) == 16


def test_three_different_books():
    full_price = 24
    discount = 2.4
    assert potter(books[0:3]) == full_price - discount


def test_three_different_books_one_equal():
    assert potter(books[0:3] + [books[0]]) == (24 - 2.4) + 8
