from django.db import models


# Create your models here.


class Card(models.Model):
    # 信用卡的字段信息

    name = models.CharField(max_length=128, null=True, verbose_name="信用卡名字")
    expiration_time = models.DateTimeField(null=True, verbose_name="到期日期")
    repayment_time = models.DateTimeField(null=True, verbose_name="还款日期")
    repay_money = models.FloatField(null=True, verbose_name="还款金额")
