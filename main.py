if __name__ == '__main__':

    year = int(input('Enter the Year Your House was Built: '))

    price = int(input('Enter the Initial Cost of House: '))

    location = input('Enter Location of House: ')

class House:

    def __init__(self, year, price, location):
        self.year = year
        self.price = price
        self.location = location

    def price(self):
        return self.price
    def year(self):
        return year
    def location(self):
        return location
    def current():
        value = price * (1 + .08)^2021 - year
        return value

    def __str__(self):
        print('House Information: \nYear Built: {}\nPurchase Price: {}\nCurrent Value: {}\nLocation: {}'.format(year, price, current, location))

house = House(year, price, location)

print(house)