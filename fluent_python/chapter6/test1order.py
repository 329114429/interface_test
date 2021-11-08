from collections import namedtuple

Customer = namedtuple('Customer', 'name fidelity')


class LineItem():
    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.quantity * self.price


class Order():
    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion

    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total for item in order.cart)
        return self.__total

    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion(self)
        return self.total() - discount

    def __repr__(self):
        fmt = '<Order total:{:.2f} due:{:.2f}>'
        return fmt.format(self.total(), self.due())


def fidelity_promo(order):
    # 为积分为1000或以上的顾客提供5%折扣
    return order.total() * 0.05 if order.customer.fidelity >= 1000 else 0


def bulk_item_promo(order):
    # 单个商品为20个或以上时提供10%折扣"
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * 0.1
    return discount


# 订单中的不同商品达到10个或以上时提供7%折扣
def large_order_promo(order):
    distinct_item = {item.product for item in order.cart}
    if len(distinct_item) >= 10:
        return order.total() * 0.07
    return 0


promos = [fidelity_promo, bulk_item_promo, large_order_promo]


# 选择可用的最佳折扣
def bset_promo(order):
    return max(promo(order) for promo in promos)


if __name__ == '__main__':
    joe = Customer('joe', 0)
    cart = [LineItem('banan', 4, 1)]
    order = Order(joe, cart, fidelity_promo)  # 把函数作为参数传入
    print(order)
