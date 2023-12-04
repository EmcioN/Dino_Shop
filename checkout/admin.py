from django.contrib import admin
from .models import Checkout, OrderItem


@admin.register(Checkout)
class CheckoutAdmin(admin.ModelAdmin):
    list_display = ('user', 'email', 'total_price', 'status',
                    'created_at', 'payment_method', 'transaction_id')
    list_filter = ('status', 'created_at', 'payment_method')
    search_fields = ('user__username', 'email', 'transaction_id')
    readonly_fields = ('created_at', 'transaction_id')

    fieldsets = (
        (None, {
            'fields': ('user', 'email', 'username_in_game', 'server',
                       'total_price', 'status', 'payment_method')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('transaction_id',),
        }),
    )


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('checkout', 'dinosaur', 'quantity')
    list_filter = ('dinosaur',)
    search_fields = ('checkout__user__username', 'dinosaur__name')
