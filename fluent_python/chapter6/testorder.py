from abc import ABC, abstractmethod
from collections import namedtuple

Customer = namedtuple('Customer', 'name fidelity')


class LineItem():
    def init(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.quantity * self.price


class Order():
    # 上下文
    def init(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion

    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)
        else:
            return self.__total

    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion.discount(self)
        return self.total() - discount

    def __repr__(self):
        fmt = '<Order totle:{:.2f}, due:{:.2f}>'
        return fmt.format(self.total(), self.due())


class Promotion(ABC):
    # 策略抽象类
    @abstractmethod
    def discount(self, order):
        # 返回折扣金额，正值
        pass


class FidelityPromotion(Promotion):
    # 第一个具体策略
    # 积分超过1000或以上顾客提供5%折扣
    def discount(self, order):
        return order.total() * (0.05) if order.customer.fidelity >= 1000 else 0


class BulkItemPromition(Promotion):
    # 第二个具体策略
    # 单个商品超过20个或以上时提供10%的折扣
    def discount(self, order):
        discount = 0
        for item in order.cart:
            if item.quantity >= 20:
                discount += item.total() * (0.1)
        return discount


class LargeOrderPromotion(Promotion):
    # 第三个具体策略
    # 不同的商品达到10个或以上提供7%折扣
    def discount(self, order):
        distinct_items = {item.product for item in order.cart}
        if len(distinct_items) >= 10:
            return order.total() * (0.07)
        return 0
