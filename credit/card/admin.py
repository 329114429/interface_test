from django.contrib import admin

# Register your models here.
from .models import Card, Card_accout_bill


class CreditCard(admin.ModelAdmin):
    # 需要显示的字段信息
    list_display = (
        "name",
        "expiration_time",
        "repayment_time",
        "repay_money",
        # "account_bill",
        "next_repay_money",
        # "available_credit",
        # "owe",
        # "date_day",
    )
    ordering = ["-expiration_time"]

    list_filter = ("expiration_time", "repayment_time")

    # 设置哪些字段可以点击进入编辑界面，默认是第一个字段
    list_display_links = ("name", "expiration_time", "repayment_time", "repay_money",)

    search_fields = ['name', 'expiration_time', ]


class AccoutAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "account_bill",
        "available_credit",
    )
    ordering = ["-account_bill"]

    list_display_links = ("name", "account_bill", "available_credit")

    search_fields = ['name', 'available_credit', ]


## 注册时，在第二个参数写上 admin model
admin.site.register(Card, CreditCard)
admin.site.register(Card_accout_bill, AccoutAdmin)
