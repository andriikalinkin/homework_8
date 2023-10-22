from django import forms
import phonenumbers


class StudentForm(forms.Form):
    first_name = forms.CharField(
        label="First name"
    )

    last_name = forms.CharField(
        label="Last name"
    )

    phone_number = forms.CharField(
        label="Phone number",
    )

    def clean_first_name(self):
        cleaned_data = self.cleaned_data.get('first_name')

        if len(cleaned_data) > 25:
            raise forms.ValidationError("First name should be 25 characters or less.")

        return cleaned_data

    def clean_last_name(self):
        cleaned_data = self.cleaned_data.get('last_name')

        if len(cleaned_data) > 25:
            raise forms.ValidationError("Last name should be 25 characters or less.")

        return cleaned_data

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get("phone_number")

        if len(phone_number) > 25:
            raise forms.ValidationError("Phone number should be 25 characters or less.")

        try:
            parsed = phonenumbers.parse(phone_number, region=None)
        except phonenumbers.NumberParseException as error:
            raise forms.ValidationError(error.args[0])

        return phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
