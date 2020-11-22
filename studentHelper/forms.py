from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Events, Description, Course, Teacher
from bootstrap_datepicker_plus import DateTimePickerInput
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.forms.widgets import HiddenInput


# pip install django-bootstrap-datepicker-plus
# pip install django-bootstrap4


class EventForm(ModelForm):

    class Meta:
        model = Events
        fields = ['start_date', 'end_date', 'period_type']
        widgets = {
            'start_date': DateTimePickerInput(),
            'end_date': DateTimePickerInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["start_date"].label = "Początek wydarzenia"
        self.fields["end_date"].label = "Koniec wydarzenia"
        self.fields["period_type"].label = "Okres trwania"
        for key in self.fields:
            self.fields[key].error_messages['required'] = "To pole jest wymagane."

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get("start_date")
        end_date = cleaned_data.get("end_date")
        period = cleaned_data.get("period_type")
        print(start_date.date())
        print(end_date.date())
        print(period)


        if start_date and end_date:
            if start_date > end_date:
                raise ValidationError(
                    "Podróż w czasie jest niemożliwa :)"
                )
            elif period == "ONCE" and start_date.date() != end_date.date():
                raise ValidationError(
                    "Pojedyncze wydarzenie = Wydarzenie w jednym dniu. \n \
                    Co tutaj jest niejasne? :D"
                )

            elif start_date < timezone.now().replace(hour=0, minute=0, second=0):
                raise ValidationError(
                    "Po co dodawać wydarzenia, które już się nie spełnią? :o"
                )
            elif period == "DAILY" and start_date.date() == end_date.date():
                raise ValidationError(
                    "Opcja codziennie wymaga co najmniej dwóch dni -_- "
                )

class DescriptionForm(ModelForm):

    class Meta:
        model = Description
        fields = ['description']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["description"].label = "Opis"
        for key in self.fields:
            self.fields[key].error_messages['required'] = "To pole jest wymagane."

class DescourseForm(ModelForm):

    class Meta:
        model = Description
        fields = ['course', 'description']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["course"].widget = HiddenInput()
        self.fields["course"].initial = True
        self.fields["description"].label = "Opis"
        self.fields["description"].help_text = "To będzie wyświetlane w kalendarzu"
        for key in self.fields:
            self.fields[key].error_messages['required'] = "To pole jest wymagane."

class CourseForm(ModelForm):

    class Meta:
        model = Course
        fields = ['name', 'ECTS', 'type']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["name"].label = "Nazwa kursu"
        self.fields["name"].help_text = "Poprawna nazwa kursu"
        self.fields["ECTS"].label = "ECTS"
        self.fields["ECTS"].initial = 0
        self.fields["type"].label = "Typ zajęć"
        for key in self.fields:
            self.fields[key].error_messages['required'] = "To pole jest wymagane."


class TeacherForm(ModelForm):

    class Meta:
        model = Teacher
        fields = ['name', 'surname', 'title', 'webpage']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["name"].label = "Imię prowadzącego"
        self.fields["surname"].label = "Nazwisko prowadzącego"
        self.fields["title"].label = "Tytuł prowadzącego"
        self.fields["webpage"].label = "Strona internetowa prowadzącego"
        self.fields["webpage"].initial = "brak"
        for key in self.fields:
            self.fields[key].error_messages['required'] = "To pole jest wymagane."
