from django.db import models
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Skills(models.Model):
    name=models.CharField(_("skill_name"), max_length=50)
    created=models.DateTimeField(_("created"), auto_now_add=True)
    modified=models.DateTimeField(_("modified"), auto_now=True)
    class Meta:
        verbose_name = _("Skill")
        verbose_name_plural = _("skills")

    def __str__(self):
        return self.name

class About_Me(models.Model):
    fullname=models.CharField(_("my_name"), max_length=50)
    description=models.TextField(_("my_description"))
    skills=models.ManyToManyField(Skills, verbose_name=_("skills"))
    image=models.ImageField(_("image"), upload_to='my_image')
    whatsapp=models.CharField(_("whatsapp_id"), max_length=150,blank=True,null=True)
    telegram=models.CharField(_("telegram_id"), max_length=150,blank=True,null=True)
    linkdin=models.CharField(_("linkdin_id"), max_length=150,blank=True,null=True)
    github=models.CharField(_("github_id"), max_length=150,blank=True,null=True)
    instagram=models.CharField(_("instagram_id"), max_length=150,blank=True,null=True)
    phone=models.CharField(_("my_number"), max_length=11)
    email=models.EmailField(_("email"), max_length=254)
    created=models.DateTimeField(_("created"), auto_now_add=True)
    modified=models.DateTimeField(_("modified"), auto_now=True)

    class Meta:
        verbose_name = _("About_me")
        verbose_name_plural = _("About_me")

    def __str__(self):
        return self.fullname

    def image_tag(self):
        return format_html('<img width=100px height=100px src="{}" />'. format(self.image.url))
