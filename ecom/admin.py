from django.contrib import admin
from .models import Customer,Product,Orders,Feedback,Supplier,CustomerReport,ProductPurchaseReport,SalesReport
# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    pass
admin.site.register(Customer, CustomerAdmin)

class ProductAdmin(admin.ModelAdmin):
    pass
admin.site.register(Product, ProductAdmin)

class OrderAdmin(admin.ModelAdmin):
    pass
admin.site.register(Orders, OrderAdmin)

class FeedbackAdmin(admin.ModelAdmin):
    pass
admin.site.register(Feedback, FeedbackAdmin)

class CustomerReportAdmin(admin.ModelAdmin):
    pass
admin.site.register(CustomerReport, CustomerReportAdmin)

class ProductPurchaseReportAdmin(admin.ModelAdmin):
    pass
admin.site.register(ProductPurchaseReport, ProductPurchaseReportAdmin)

class SalesReportAdmin(admin.ModelAdmin):
    pass
admin.site.register(SalesReport, SalesReportAdmin)

class SupplierAdmin(admin.ModelAdmin):
    pass
admin.site.register(Supplier, SupplierAdmin)
# Register your models here.
