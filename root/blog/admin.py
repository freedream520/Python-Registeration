from django.contrib import admin

# Register your models here.

from .models import Post, Contact, About, Gallery, Slidshow
#from .forms import ContactForm

class PostAdmin(admin.ModelAdmin):
    class Meta:
        model = Post

admin.site.register(Post, PostAdmin)


class ContactAdmin(admin.ModelAdmin):
    class Meta:
        model = Contact

admin.site.register(Contact, ContactAdmin)


class AboutAdmin(admin.ModelAdmin):
    class Meta:
        model = About

admin.site.register(About, AboutAdmin)

class GalleryAdmin(admin.ModelAdmin):
    class Meta:
        model = Gallery

admin.site.register(Gallery, GalleryAdmin)

class SlidshowAdmin(admin.ModelAdmin):
    class Meta:
        model = Slidshow

admin.site.register(Slidshow, SlidshowAdmin)