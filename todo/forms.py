from django import forms 

class TodoForm(forms.Form):
    text = forms.CharField(max_length=40, 
        widget=forms.TextInput(
            attrs={'class' : 'form-control', 'placeholder' : 'Define Task', 'aria-label' : 'Todo'}))
    username = forms.CharField(max_length=40,
                           widget=forms.TextInput(
                               attrs={'class': 'form-control', 'placeholder': 'Enter Buddy',
                                      'aria-label': 'Todo','aria-describedby' : 'add-btn'}))
