from django import forms
from warcraft.models import Cinematic, Music, Screenshot


class CinematicForm(forms.ModelForm):
    class Meta:
        model = Cinematic
        fields = '__all__'


class MusicForm(forms.ModelForm):
    class Meta:
        model = Music
        fields = '__all__'


class ScreenshotForm(forms.ModelForm):
    class Meta:
        model = Screenshot
        fields = '__all__'
