class Dogs():
    """一次模拟小狗的尝试"""

    def __init__(self, name, age):
        """初始化数据"""
        self.name = name
        self.age = age

    def sit(self):
        """蹲下"""
        print(self.name.title() + " sit")

    def roll_over(self):
        """打滚"""
        print(self.name.title() + " roll")


my_dog = Dogs("willie", 6)
my_dog.sit()
my_dog.roll_over()

your_dog = Dogs("lucy", 3)
your_dog.sit()
your_dog.roll_over()
