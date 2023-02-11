class Inventory:

    def __init__(self, items, price: int, count):

        self.items = items
        self.price = price
        self.count = count

    #def stock_opening (self):
    #   self.count = 10

    def inc(self):
        self.count += 1

    def dec(self):
        self.count -= 1

    def stock_balance(self):
        return self.count
        if count <= 5:
          count += 10
        print(count)


watch = Inventory("Casio", 100, 4)
watch1 = Inventory("Seiko", 200, 8)
watch.dec()
watch.dec()
watch.inc()
watch.stock_balance()

print(watch1.items, watch1.price, watch1.count)
print(watch.items, watch.price, watch.count)
print(watch.count)






