from django.forms import ModelForm
from .models import Move
from django.core.validators import ValidationError

class MoveForm(ModelForm):
    class Meta:
        model = Move
        exclude = []
    def clear(self):
        x = self.cleaned_data.get("x")
        y = self.cleaned_data.get("y")
        game = self.instance.game
        try:
            if game.board()[y][x] is not None:
                raise ValidationError("Invalid Move, Squre is Not empty!")
        except IndexError:
            raise ValidationError("Invalid Co ordinates")
        return self.cleaned_data