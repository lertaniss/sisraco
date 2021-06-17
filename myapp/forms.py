from django import forms
from .models import Onibus, Paradas
class OnibusForm(forms.ModelForm):
	class Meta:
		model = Onibus
		fields = ('oni_nome',)

class ParadasForm(forms.ModelForm):
	class Meta:
		model = Paradas
		fields = ('par_nome',)
