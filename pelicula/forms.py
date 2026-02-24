from django.forms import ModelForm

from pelicula.models import Pelicula


class PeliculaForm(ModelForm):
    class Meta:
        model = Pelicula
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})