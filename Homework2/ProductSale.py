# Joseph Stefanoni
# 9/19/24
# Modifying the class example of Product and Sale (in file ProductSale.py) so that the Product class keeps track of the product inventory.
from __future__ import annotations
from typing import List

# forward reference used for class Sale
class Product:
    __lastSale: Sale = None
    __ProductInventory: int = 0

    def __init__(self, sale: Sale, init_inventory: int = 0):
        self.__lastSale = sale
        self.__ProductInventory = init_inventory

    def setLastSale(self, lastSale: Sale):
        self.__lastSale = lastSale
        
    def setInventory(self, init_inventory):
        self.__ProductInventory = init_inventory

    @property
    def getLastSale(self) -> Sale:
        return self.__lastSale
      
    def getInventory(self):
        return self.__ProductInventory

    def __getitem__(self, item):
        return self

# no forward reference needed since Product is defined
class Sale:
    __saleTimes = 0
    __productSold: List[Product] = None
    __saleNumber: int = 0

    def __init__(self, product: List[Product]):  #, saleNumber: int = 1):
        Sale.__saleTimes += 1
        self.__product = product
        self.__saleNumber = Sale.__saleTimes
        for index, product in enumerate(product):
            product[index].setLastSale(self)
            product[index].setInventory(product[index].getInventory() - 1)

    def setProductsSold(self, productSold: List[Product]):
        self.__productSold = productSold

    @property
    def getSaleNumber(self) -> int:
        return self.__saleNumber


productOne = Product(sale=None, init_inventory=20)
productTwo = Product(sale=None, init_inventory=17)

print(f"Inventory:")
print(f"\tProduct 1 count: {productOne.getInventory()}")
print(f"\tProduct 2 count: {productTwo.getInventory()}")

saleOne = Sale([productOne, productTwo])
print(f"Processing Sale 1.")

print(f"Updated Inventory:")
print(f"\tProduct 1 count: {productOne.getInventory()}")
print(f"\tProduct 2 count: {productTwo.getInventory()}")

saleTwo = Sale([productOne])
saleThree = Sale([productTwo])
print(f"Processing Sales 2 & 3.")

print(f"Updated Inventory:")
print(f"\tProduct 1 count: {productOne.getInventory()}")
print(f"\tProduct 2 count: {productTwo.getInventory()}")

# print(f"{productOne.getLastSale.getSaleNumber}, {productTwo.getLastSale.getSaleNumber}")
