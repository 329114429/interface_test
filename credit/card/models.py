from django.db import models
import django.utils.timezone as timezone


# Create your models here.


class Card(models.Model):
    # 信用卡的字段信息

    choice = (
        (u"4", u"0_浦发信用卡"),
        (u"1", u"1_广发信用卡"),
        (u"2", u"2_交通信用卡"),
        (u"0", u"3_中信信用卡"),
        (u"3", u"4_平安信用卡"),
        (u"5", u"5_招商信用卡"),
        (u"12", u"建设信用卡"),
        (u"10", u"借呗"),
        (u"11", u"花呗"),
        (u"9", u"小米借钱"),
        (u"6", u"美团借钱"),
        (u"7", u"京东白条"),
        (u"8", u"京东金条"),
        (u"15", u"民生易贷"),
        (u"16", u"微信借钱"),
        (u"13", u"(已取消)百度有钱花"),
        (u"14", u"(已取消)苏宁借钱"),

    )

    name = models.CharField(max_length=128, choices=choice, null=True, blank=True,
                            verbose_name="信用卡名字")
    expiration_time = models.DateField(null=True, blank=True, verbose_name="到期日期")
    repayment_time = models.DateField(null=True, blank=True, verbose_name="还款日期")
    repay_money = models.FloatField(null=True, blank=True, verbose_name="本期还款金额")
    next_repay_money = models.FloatField(null=True, blank=True, verbose_name="下期还款金额")
    # account_bill = models.DateField(null=True, blank=True, verbose_name="出账单日期")
    # available_credit = models.FloatField(null=True, blank=True, verbose_name="可剩余额度")
    # owe = models.FloatField(null=True, blank=True, verbose_name="总欠债")
    # date_day = models.DateField(null=True, blank=True, verbose_name="记/修 日期")

    remark = models.DateTimeField("备注:记录时间", null=True, blank=True, default=timezone.now)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-expiration_time',)
        verbose_name = verbose_name_plural = "信用卡记录"


class Card_accout_bill(models.Model):
    """出账单日期"""
    choice = (
        (u"0", u"3_中信信用卡"),
        (u"1", u"1_广发信用卡"),
        (u"2", u"2_交通信用卡"),
        (u"3", u"4_平安信用卡"),
        (u"4", u"0_浦发信用卡"),
        (u"5", u"5_招商信用卡"),
        (u"6", u"美团借钱"),
        (u"7", u"京东白条"),
        (u"8", u"京东金条"),
        (u"9", u"小米借钱"),
        (u"10", u"借呗"),
        (u"11", u"花呗"),
        (u"12", u"建设信用卡"),
        (u"13", u"百度有钱花"),
        (u"14", u"苏宁借钱"),
        (u"15", u"民生易贷"),
        (u"16", u"微信借钱"),
    )

    name = models.CharField(max_length=128, choices=choice, null=True, blank=True,
                            verbose_name="信用卡名字")
    account_bill = models.DateField(null=True, blank=True, verbose_name="出账单日期")
    available_credit = models.FloatField(null=True, blank=True, verbose_name="可剩余额度")

    class Meta:
        ordering = ('-account_bill',)
        verbose_name_plural = "出账单日期"
