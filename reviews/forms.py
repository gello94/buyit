from django.forms import ModelForm, Textarea, Form
from .models import Review

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['review_summary', 'rating', 'comment']
        widgets = {
            'comment': Textarea(attrs={'cols': 40, 'rows': 5})
        }
