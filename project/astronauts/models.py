from django.db import models
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel

class AstronautsIndexPage(Page):
  intro_text = RichTextField(blank=True)
  intro_image = models.ForeignKey(
    'wagtailimages.Image',
    on_delete=models.SET_NULL,
    related_name='+',
    null=True,
    blank=True
  )

  content_panels = Page.content_panels + [
    FieldPanel('intro_text', classname="full"),
    ImageChooserPanel('intro_image'),
  ]