from django import forms
from django.core.exceptions import ValidationError
import magic

class BitForm(forms.Form):
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

    def is_svg(self):
        content = self
        with magic.Magic(flags=magic.MAGIC_MIME_TYPE) as m:
            mime = m.id_buffer(content.read())
        if not mime == "image/svg+xml":
            raise ValidationError('keine SVG-Datei')

    bitname = forms.CharField(label="Bit-Name")
    author = forms.CharField(label="Autor")
    creation_date = forms.DateField(label="Erstellungsdatum")
    license = forms.ChoiceField(choices = LICENSE_CHOICES, label="Lizenz")
    bit_image = forms.ImageField(label="PNG")
    bit_vector = forms.FileField(label="SVG", validators=[is_svg])
    reserved = forms.BooleanField(label="reserviert?", required = False)
    reserved_for = forms.CharField(label="reserviert für", required = False)

class ClaimForm(forms.Form):
    claimed_by = forms.CharField(label="reserviert für", required=True)
