from django import forms


class ReviewForm(forms.Form):
    text = forms.CharField(
        label="Текст",
        widget=forms.Textarea(attrs={"class": "form-control"})
    )
    rating = forms.IntegerField(
        label="Оценка",
        widget=forms.NumberInput(attrs={"class": "form-control"}),
        max_value=10,
        min_value=1
    )