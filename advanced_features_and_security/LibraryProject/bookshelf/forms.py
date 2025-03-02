from django import forms
from .models import Book  # Import model if the form is related to it

class ExampleForm(forms.ModelForm):
    """
    This is an example form for adding/editing a book entry.
    """
    class Meta:
        model = Book  # Change this to another model if needed
        fields = ["title", "author", "publication_year"]

    # Optional: Add additional validation
    def clean_title(self):
        title = self.cleaned_data.get("title")
        if len(title) < 3:
            raise forms.ValidationError("Title must be at least 3 characters long.")
        return title

