from django.contrib.auth.forms import UserCreationForm


class MyUserCreationForm(UserCreationForm):

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data

    class Meta(UserCreationForm.Meta):
        fields = ('username', 'password1', 'password2',)
