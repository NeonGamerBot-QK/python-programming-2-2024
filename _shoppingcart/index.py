def build_cart():
    cart = []
    def add_item(item, price):
        cart.append({
            "item": item,
            "price": price
        })
        pass
    def remove_item(item):
        cart = cart.pop(item)
        pass
    def view_cart():
        return cart;
        pass
    def _get_price(i):
        return i['price'] 
    def total_price():
        return sum(map(_get_price, cart))
        pass 
    return add_item, remove_item,view_cart, total_price
    

cart0 = build_cart()

cart1 = build_cart()
# print(cart0)
# print()