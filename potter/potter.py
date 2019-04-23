
def potter(books):
    from collections import defaultdict

    dd = defaultdict(int)

    for book in books:
        dd[book] += 1

    total = 0
    discounts = [..]
    if len(dd) == 3:
        total += 24 - 2.4

    for book, count in dd.items():
        if count > 1:
            total += 8 * (count - 1)

    return total
