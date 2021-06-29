class Product:
    id=0
    name=None
    stoc = 0
    description = None
    price=0


    def __init__(self, id, name, price, stoc, description):
        self.id=id
        self.name=name
        self.price=price
        self.stoc=stoc
        self.description=description
