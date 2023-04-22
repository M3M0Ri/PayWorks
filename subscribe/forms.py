from django import forms

from subscribe.models import Subscribe


class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscribe
        fields = "__all__"

# class SubscribeForm(forms.Form):
#     first_name = forms.CharField(max_length=100, required=False)
#     last_name = forms.CharField(max_length=100)
#     email = forms.EmailField(max_length=100)
# 
#     def clean_first_name(self):
#         data = self.cleaned_data['first_name']
#         if "," in data:
#             raise forms.ValidationError("Invalid First Name")
#         return data

