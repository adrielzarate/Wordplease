from django.core.exceptions import ValidationError
from django.forms import ModelForm

from blogs.models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        exclude = ['owner']

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image is not None and 'image' not in image.content_type:
            raise ValidationError('El archivo no es una imagen valida')
        return image

    def clean(self):
        super().clean()
