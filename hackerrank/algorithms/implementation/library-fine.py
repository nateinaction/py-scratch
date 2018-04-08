def libraryFine(return_day, return_month, return_year, due_day, due_month, due_year):
    if due_year < return_year:
        return 10000
    if due_month < return_month and due_year == return_year:
        return 500 * (return_month - due_month)
    if due_day < return_day and due_month == return_month and due_year == return_year:
        return 15 * (return_day - due_day)
    return 0


if __name__ == '__main__':
    print(libraryFine(6, 6, 2015, 6, 6, 2016))  # expect 0
    print(libraryFine(9, 6, 2015, 6, 6, 2015))  # expect 45
    print(libraryFine(9, 9, 2015, 6, 6, 2015))  # expect 1500
    print(libraryFine(9, 6, 2016, 6, 6, 2015))  # expect 10000
    print(libraryFine(28, 2, 2015, 15, 4, 2015))  # expect 0
    print(libraryFine(15, 7, 2014, 1, 7, 2015))  # expect 0
