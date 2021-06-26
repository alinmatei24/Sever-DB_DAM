class Product:
    id=0
    name=None
    price=0
    stoc=0
    description=None

    def __init__(self, id, name, price, stoc, description):
        self.id=id
        self.name=name
        self.price=price
        self.stoc=stoc
        self.description=description
