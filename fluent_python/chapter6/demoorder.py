from abc import ABC, abstractmethod
from collections import namedtuple

# 2021-11-02
# 6.1.1 经典的策略模式

Customer = namedtuple("customer", "name fidelity")


class LineItem():
    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.price * self.quantity


class Order():
    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = cart
        self.promotion = promotion

    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total

    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion.discount(self)
        return self.total() - discount

    def __repr__(self):
        fmt = '<order total:{:2f} due:{:.2f}>'
        return fmt.format(self.total(), self.due())


# 策略，抽奖基类
class Promotion(ABC):
    @abstractmethod
    def discount(self, order):
        """返回折扣的金额"""


# 第一个具体的策略
class FidelityPromo(Promotion):
    """积分为1000或以上的享受5%折扣"""
    def discount(self, order):
        return order.total() * 0.05 if order.customer.fidelity >= 1000 else 0


# 第二个具体策略
class BulkItemPromo(Promotion):
    """单个商品为20个或以上提供10%折扣"""
    def discount(self, order):
        discount = 0
        for item in order.cart:
            if item.quantity >= 20:
                discount += item.total() * 0.1
        return discount


# 第三个具体策略
class LargeOrderPromo(Promotion):
    """订单中的不同商品达到10个或以上提供7%折扣"""
    def discount(self, order):
        distinct_items = {item.product for item in order.cart}
        if len(distinct_items) >= 10:
            return order.total() * 0.07
        return 0
