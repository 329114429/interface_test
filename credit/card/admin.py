from django.contrib import admin

# Register your models here.
from .models import Card


class CreditCard(admin.ModelAdmin):
    # 需要显示的字段信息
    list_display = ("name", "expiration_time", "repayment_time", "repay_money")

    # 设置哪些字段可以点击进入编辑界面，默认是第一个字段
    list_display_links = ("name", "expiration_time")


## 注册时，在第二个参数写上 admin model
admin.site.register(Card, CreditCard)
