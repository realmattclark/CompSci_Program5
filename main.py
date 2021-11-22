
if __name__ == '__main__':
    print('Welcome to the House Calculator')

    class House:
        
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
            self.first_price * (1 + .08)^(2021 - year_built)
            return current_val
    
        def money_earned(self):
            self.money_earned = current_val - first_price
            return money_earned
    
        def __str__(self):
            return 'House Information: \nYear Built: {}\nPurchase Price: {}\nCurrent Value: {}\nLocation: {}'.format(year_built, first_price, current_val, home_location)
    c1 = House(year = 1958, price = 100000, location = 'Kansas City', current = 0)