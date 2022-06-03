from  django import forms
from .models import Subscribe


class subs_page(forms.ModelForm):
    name= forms.CharField(label='Name',
                          widget=forms.TextInput(attrs={"placeholder": "Name",
                                                        "class": "form-control",
                                                        "type": "text"
                                                        }
                                                 )
                          )
    phone=forms.IntegerField(label='Phone Number',
                             widget=forms.NumberInput(attrs={"placeholder":"Phone Number",
                                                              "class": "form-control",
                                                              "type":"tel"
                                                              }
                                                      )
                             )
    email=forms.EmailField(label='Email Address',
                           widget=forms.EmailInput(attrs={"placeholder":"Email",
                                                          "class":"form-control",
                                                         }
                                                   )
                           )
    headlines=forms.BooleanField(required=True)
    bussiness=forms.BooleanField(required=False)
    entertainment=forms.BooleanField(required=False)
    health=forms.BooleanField(required=False)
    science=forms.BooleanField(required= False)
    technology=forms.BooleanField(required=False)
    sports=forms.BooleanField(required=False)
    class Meta:
        model=Subscribe
        fields=["name",
                "phone",
                "email",
                "headlines",
                "bussiness",
                "entertainment",
                "health",
                "science",
                "technology",
                "sports"
                ]
