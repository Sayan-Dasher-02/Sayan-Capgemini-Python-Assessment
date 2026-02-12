class shoppingcart:
    products = {'iphone':5, 'imac':3, 'ipad':2, 'iwatch':4}
    prices = {'iphone':900, 'imac':5000, 'ipad':3000, 'iwatch':4000}
    
    def __init__(self):
        self.cart = {}

    def add_product(self, name, quantity):
        if name not in shoppingcart.products.keys():
            raise Exception(f'Cannot add products{name}')
        if quantity > shoppingcart.products[name]:
            raise Exception(f'Product out of stocks.')
        
        item = {'name':name, 'quantity':quantity, 'price':shoppingcart.prices[name]}
        self.cart.append(item)
        shoppingcart.products[name] = shoppingcart.products[name] - quantity

    def remove_product(self, name, quantity):
        for item in self.cart:
            if name == item['name']:
                if item['quantity'] == 1:
                    self.cart.remove(item)
                else:
                    item['quantity'] = item['quantity'] - 1

    def total_cost(self):
        total = 0
        for item in self.cart:
            total = total + item['quantity'] * item['price']
        return total
    
c1 = shoppingcart()
c2 = shoppingcart()
c1.add_product('iphone', 6)
print(c1.total_cost())