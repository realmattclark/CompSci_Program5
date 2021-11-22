

while True:

    if __name__ == '__main__':

        year = int(input('Enter the Year Your House was Built: '))

        price = int(input('Enter the Initial Cost of House: '))

        location = input('Enter Location of House: ')

        current = 0

    class House:

        def __init__(self, year, price, location, current):
            self.year = str(year)
            self.price = str(price)
            self.location = location
            self.current = current

        def price(self):
            return self.price
        def year(self):
            return year
        def location(self):
            return location
        def current(self):
            price*(1 + .08)**2021-year
            return current

        def __str__(self):
            pass
    house = House(year, price, location, current)

    print('House Information: ')
    print('Year Built: {}'.format(year))
    print('Initial Price: {}'.format(price))
    print('Location: {}'.format(location))
    print('Current Value: {}'.format(current))
    
    choice = input('Enter Y/y to enter another home or N/n to quit')
    if choice == 'y' or 'Y':
        continue
    elif choice == 'n' or 'N':
        break

