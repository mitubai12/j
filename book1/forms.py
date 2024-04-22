from django import forms

from book1.models import Book, Review


class BookForm(forms.Form):
    image = forms.ImageField(required=False)
    title = forms.CharField(max_length=100, min_length=5)
    description = forms.CharField(widget=forms.Textarea)
    released = forms.DateField()
    rate = forms.FloatField()
    tag = forms.CharField()
    category = forms.CharField()

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        text = cleaned_data.get('text')

        if title and text and title.lower() == text.lower():
            raise forms.ValidationError('Заголовок и текст не должны совпадать')
        return cleaned_data

    def clean_title(self):
        title = self.cleaned_data['title']
        if 'dalban' in title.lower():
            raise forms.ValidationError('Слово "dalban" недопустимо в заголовке')
        return title

    def clean_rate(self):
        rate = self.cleaned_data['rate']
        if rate < 0:
            raise forms.ValidationError('Оценка не может быть отрицательной')
        return rate

    def clean_released(self):
        released = self.cleaned_data['released']
        if released < 1900:
            raise forms.ValidationError("Год выпуска не можеть быть настолько старый")
        return released


class BookForm2(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["image", "title", "description", "released", "rate", "tag", "category"]
        widgets = {
            'image': forms.ClearableFileInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'title': forms.TextInput(
                attrs={
                    'placeholder': 'Введите заголовок',
                    'class': 'form-control'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Введите текст',
                    'rows': 5,
                    'cols': 30,
                    'class': 'form-control'
                }
            ),
            'released': forms.TextInput(
                attrs={
                    'placeholder': 'Введите год выхода книги',
                    'class': 'form-control'
                }
            ),
            'rate': forms.NumberInput(
                attrs={
                    'placeholder': 'Введите оценку',
                    'class': 'form-control'
                }
            ),
            'tag': forms.SelectMultiple(
                attrs={
                    'class': 'form-control'
                }
            ),
            'category': forms.SelectMultiple(
                attrs={
                    'class': 'form-control'
                }
            ),
        }

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        text = cleaned_data.get('text')

        if title and text and title.lower() == text.lower():
            raise forms.ValidationError('Заголовок и текст не должны совпадать')
        return cleaned_data

    def clean_title(self):
        title = self.cleaned_data['title']
        if 'dalban' in title.lower():
            raise forms.ValidationError('Слово "dalban" недопустимо в заголовке')
        return title

    def clean_rate(self):
        rate = self.cleaned_data['rate']
        if rate < 0:
            raise forms.ValidationError('Оценка не может быть отрицательной')
        return rate

    def clean_released(self):
        released = self.cleaned_data['released']
        if released < 1900:
            raise forms.ValidationError("Год выпуска не можеть быть настолько старый")
        return released


class ReviewForm(forms.Form):
    text = forms.CharField(required=False)
    book = forms.CharField(max_length=100, min_length=5)


class ReviewForm2(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["text", "book"]
        widgets = {
            'text': forms.TextInput(
                attrs={
                    'placeholder': 'Введите отзыв',
                    'class': 'form-control'
                }
            ),
            'book': forms.SelectMultiple(
                attrs={
                    'class': 'form-control'
                }
            ),
        }

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        text = cleaned_data.get('text')

        if title and text and title.lower() == text.lower():
            raise forms.ValidationError('Заголовок и текст не должны совпадать')
        return cleaned_data

    def clean_title(self):
        title = self.cleaned_data['title']
        if 'dalban' in title.lower():
            raise forms.ValidationError('Слово "dalban" недопустимо в заголовке')
        return title

    def clean_rate(self):
        rate = self.cleaned_data['rate']
        if rate < 0:
            raise forms.ValidationError('Оценка не может быть отрицательной')
        return rate

    def clean_released(self):
        released = self.cleaned_data['released']
        if released < 1900:
            raise forms.ValidationError("Год выпуска не можеть быть настолько старый")
        return released
