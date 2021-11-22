

class House:
    year = 0
    price = 0
    location = 0
    current = 0
    def __init__(self, year, price, location, current):
        self.year = year
        self.price = price
        self.location = location
        self.current = current
    
    def year(self):
        self.year_built = int(input('Enter year house was built: '))
        return year_built
    
    def price(self):
        self.first_price = int(input('Enter initial cost of house: '))
        return first_price
    
    def location(self):
        self.home_location = input('Enter location of the house: ')
        return home_location
    
    def current_val(self):
        first_price * (1 + .08)^(2021 - year_built)
        return current_val
    
    def money_earned():
        current_val - first_price
    
    def __str__(self):
        return 'House Information: \nYear Built: {}\nPurchase Price: {}\nCurrent Value: {}\nLocation: {}'.format(year_built, first_price, current_val, home_location)
