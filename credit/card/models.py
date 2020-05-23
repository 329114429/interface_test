from django.db import models


# Create your models here.


class Card(models.Model):
    # 信用卡的字段信息

    choice = (
        (u"0", u"中信信用卡"),
        (u"1", u"广发信用卡"),
        (u"2", u"交通信用卡"),
        (u"3", u"平安信用卡"),
        (u"4", u"浦发信用卡"),
        (u"12", u"建设信用卡"),
        (u"5", u"微信借钱"),
        (u"6", u"美团借钱"),
        (u"7", u"京东白条"),
        (u"8", u"京东金条"),
        (u"9", u"小米借钱"),
        (u"10", u"借呗"),
        (u"11", u"花呗"),
    )

    name = models.CharField(max_length=128, choices=choice, null=True, blank=True,
                            verbose_name="信用卡名字")
    expiration_time = models.DateField(null=True, blank=True, verbose_name="到期日期")
    repayment_time = models.DateField(null=True, blank=True, verbose_name="还款日期")
    repay_money = models.FloatField(null=True, blank=True, verbose_name="还款金额")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = "信用卡记录"
