from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from django.utils.html import format_html
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
    Navbar,
    Informations,
    QuickLink,
    SupportedCompany,
    Tractor_Page,
    Equipment,
    Ox,
    AgroChemical,
    SprayPump,
    AgricultureGuidance,
)
from ikhedut.models.fertilizer import Fertilizer

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
    list_display = ("crop", "seller", "quantity", "price", "is_approved","image_preview")
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

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="60" height="60" style="object-fit:cover;border-radius:8px;" />',
                obj.image.url
            )
        return "No Image Avalible"
    
    image_preview.short_description = "Image"
@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ("productname", "price", "city", "is_approved","image_preview")
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
    
    
    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="60" height="60" style="object-fit:cover;border-radius:8px;" />',
                obj.image.url
            )
        return "No Image Avalible"
    
    image_preview.short_description = "Image"

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
    list_display = ("id", "image", "is_active","image_preview")
    list_editable = ("is_active",)
    
    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="60" height="60" style="object-fit:cover;border-radius:8px;" />',
                obj.image.url
            )
        return "No Image Avalible"
    
    image_preview.short_description = "Image"

@admin.register(Slider2)
class Slider2Admin(admin.ModelAdmin):
    list_display = ("image", "is_active","image_preview")
    list_editable = ("is_active",)

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="60" height="60" style="object-fit:cover;border-radius:8px;" />',
                obj.image.url
            )
        return "No Image Avalible"
    
    image_preview.short_description = "Image"
@admin.register(SupportedCompany)
class SupportedCompanyAdmin(SortableAdminMixin,admin.ModelAdmin):
    list_display = ("company_image", "is_active","company_order","image_preview")
    list_editable = ("is_active",)
    
    def image_preview(self, obj):
        if obj.company_image:
            return format_html(
                '<img src="{}" width="80" height="60" style="object-fit:cover;border-radius:8px;" />',
                obj.company_image.url
            )
        return "No Image Avalible"
    
    image_preview.short_description = "Image"

@admin.register(QuickLink)
class QuicklinkAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ("id","q_page_name", "q_page_url", "q_order")
    list_editable = ("q_page_name","q_page_url",)
    
@admin.register(Informations)
class InformationAdmin(SortableAdminMixin, admin.ModelAdmin):
    ordering = ("position",)
    list_display = ("id","info_title", "info_button_url")
    list_editable=("info_title","info_button_url")
    
@admin.register(Tractor_Page)
class TractorAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ("tractor_name", "Price", "order","image_preview")
    
    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="120" height="69" style="object-fit:cover;border-radius:8px;" />',
                obj.image.url
            )
        return "No Image Avalible"
    
    image_preview.short_description = "Image"

@admin.register(Equipment)
class EquipmentAdmin(SortableAdminMixin, admin.ModelAdmin):
    sortable = "order"
    list_display = ("name", "category", "price", "order","image_preview")
    list_editable = ("order",)
    ordering = ("order",)

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="60" height="60" style="object-fit:cover;border-radius:8px;" />',
                obj.image.url
            )
        return "No Image Avalible"
    
    image_preview.short_description = "Image"

@admin.register(Ox)
class OxAdmin(SortableAdminMixin,admin.ModelAdmin):
    list_display = ("name","state","weight_range","order","image_preview")
    list_editable = ("order",)
    search_fields = ("name", "state")
    list_filter = ("state",)
    ordering = ("order",)
    
    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="60" height="60" style="object-fit:cover;border-radius:8px;" />',
                obj.image.url
            )
        return "No Image Avalible"
    
    image_preview.short_description = "Image"

@admin.register(Fertilizer)
class FertilizerAdmin(SortableAdminMixin, admin.ModelAdmin):

    list_display = ("name","weight","price_range","order","image_preview",)

    list_editable = ("order",)
    search_fields = ("name", "nutrient", "best_for")
    ordering = ("order",)

    def image_preview(self, obj):
        if obj.image:       
            return format_html(
                '<img src="{}" width="60" height="60" style="object-fit:cover;border-radius:8px;" />',
                obj.image.url
            )
        return "No Image Avalible"

    image_preview.short_description = "Image"

@admin.register(AgroChemical)
class AgroChemicalAdmin(SortableAdminMixin,admin.ModelAdmin):
    list_display = ("name","type","pack_size","price","order","image_preview",)

    list_editable = ("order",)
    search_fields = ("name", "type")
    list_filter = ("type",)
    ordering = ("order",)

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="60" height="60" style="object-fit:cover;border-radius:8px;" />',
                obj.image.url
            )
        return "No Image Avalible"
    
    image_preview.short_description = "Image"
    
@admin.register(AgricultureGuidance)
class AgricultureGuidanceAdmin(SortableAdminMixin, admin.ModelAdmin):

    list_display = (
        "crop_name",
        "crop_season",
        "crop_Sowing",
        "crop_Yield",
        "order",
        "image_preview",
    )

    search_fields = ("crop_name", "crop_season")
    list_filter = ("crop_season",)

    list_editable = ("order",)
    ordering = ("order",)
    
    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="60" height="60" style="object-fit:cover;border-radius:8px;" />',
                obj.image.url
            )
        return "No Image Avalible"

    image_preview.short_description = "Image"


@admin.register(SprayPump)
class SprayPumpAdmin(SortableAdminMixin, admin.ModelAdmin):

    list_display = ("name","operation_type","pressure","capacity","weight","order","image_preview",)
    list_editable = ("order",)
    search_fields = ("name","operation_type","tagline",)
    ordering = ("order",)

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="60" height="60" style="object-fit:cover;border-radius:8px;" />',
                obj.image.url
            )
        return "No Image Avalible"

    image_preview.short_description = "Image"