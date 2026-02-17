from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from ikhedut.models import (
    Contact,
    Signup,
    Ad,
    CropSale,
    Order,
    OrderItem,
    Slider,
    Slider2,
    Slider_content,
    Navbar
)
from ikhedut.models.index import QuickLink, SupportedCompany

admin.site.register(Contact)
admin.site.register(Signup)

@admin.register(Navbar)
class NavbarAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ("id","page_name", "page_url", "order")
    list_editable = ("page_name","page_url",)
    

@admin.register(Slider_content)
class Slider_content_admin(admin.ModelAdmin):
    list_display = ("id","first_line_text", "second_line_text",)
    list_editable = ("first_line_text","second_line_text")

    def has_add_permission(self, request):
        return False
    
@admin.register(CropSale)
class CropSaleAdmin(admin.ModelAdmin):
    list_display = ("crop", "seller", "quantity", "price", "is_approved")
    list_filter = ("is_approved",)
    search_fields = ("crop", "seller__username")
    list_editable = ("is_approved",)
    

    actions = ["approve_selected", "reject_selected"]

    def save_model(self, request, obj, form, change):
        if not obj.seller:
            obj.seller = request.user
        super().save_model(request, obj, form, change)

    def approve_selected(self, request, queryset):
        queryset.update(is_approved=True)

    def reject_selected(self, request, queryset):
        for obj in queryset:
            if obj.image:
                obj.image.delete(save=False)
            obj.delete()

@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ("productname", "price", "city", "is_approved")
    list_filter = ("is_approved", "city")
    search_fields = ("productname", "city", "fullname")
    list_editable = ("is_approved",)
    

    actions = ["approve_ads", "reject_ads"]

    def approve_ads(self, request, queryset):
        queryset.update(is_approved=True)

    approve_ads.short_description = "Approve selected ads"

    def reject_ads(self, request, queryset):
        for obj in queryset:
            if obj.image:
                obj.image.delete(save=False)
            obj.delete()

    reject_ads.short_description = "Reject selected ads"

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ("product", "quantity", "price")

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "fullname",
        "mobile",
        "payment_method",
        "status",
        "total_amount",
        "created_at",
    )

    list_filter = (
        "status",
        "payment_method",
        "created_at",
    )

    search_fields = (
        "user__username",
        "fullname",
        "mobile",
        "upi_id",
    )

    ordering = ("-created_at",)

    readonly_fields = (
        "user",
        "total_amount",
        "created_at",
        "cancel_requested_at",
    )

    inlines = [OrderItemInline]

    actions = ["approve_cancellation"]

    def approve_cancellation(self, request, queryset):
        updated = queryset.filter(
            status="cancel_requested"
        ).update(status="cancelled")

        self.message_user(
            request,
            f"{updated} order(s) cancelled successfully."
        )

    approve_cancellation.short_description = (
        "Approve selected cancellation requests"
    )

@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ("id", "image", "is_active")
    list_editable = ("is_active",)

@admin.register(Slider2)
class Slider2Admin(admin.ModelAdmin):
    list_display = ("image", "is_active")
    list_editable = ("is_active",)

@admin.register(SupportedCompany)
class SupportedCompanyAdmin(SortableAdminMixin,admin.ModelAdmin):
    list_display = ("company_image", "is_active","company_order")
    list_editable = ("is_active",)
    

@admin.register(QuickLink)
class QuicklinkAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ("id","q_page_name", "q_page_url", "q_order")
    list_editable = ("q_page_name","q_page_url",)
