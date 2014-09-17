from django.db import models

# Create your models here.

class Bit(models.Model):
    PUBDOM="CC0 (Public Domain)"
    USABLE="für OE verwendbar"
    WTFPL="WTFPL"
    UNKNWN="unbekannt (aus Gründen)"

    LICENSE_CHOICES = (
            (PUBDOM, "CC0 (Public Domain)"),
            (USABLE, "für die OE nutzbar"),
            (WTFPL, "nutzbar unter WTF PL"),
            (UNKNWN, "unbekannt"),
            )

    bit_image = models.ImageField(verbose_name='Bitbild', upload_to="img/")
    bit_vector = models.FileField(verbose_name='Bit-SVG', upload_to="svg/")
    bitname = models.CharField(max_length=50, verbose_name='Bit-Name', unique=True)
    author = models.CharField(max_length=100, verbose_name='Autor')
    creation_date = models.DateField(verbose_name='Erstell-Datum')
    license = models.CharField(max_length=100, verbose_name='Lizenz', choices = LICENSE_CHOICES)
    reserved = models.BooleanField(default=False, verbose_name='Reserviert?')
    reserved_for = models.CharField(max_length=100,blank=True, verbose_name='Reserviert für')

    def __str__(self):
        return self.bitname

    def id_is_even(self):
        return self.id % 2 == 0
