from django import forms 
from .models import events,Activity,activity_tags,classes,venues,Category,sports_classes

from django.forms.widgets import DateInput


# class Eventform(forms.Form):
#     class Meta:
#         model=events
#         fields='__all__'
        
#     widgetss={
#             'name':forms.CharField(max_length=500,label='Event Name')
#         }
class DateInput(forms.DateInput):
    input_type = 'date'

class CatgoryForm(forms.Form):
    class Meta:
        model=Category
        fields=['name']
        
    widgets={
        'name':forms.Select([('Event','Event'),('Class','Class'),('Venue','Venue')])
    }
    
class EventForm(forms.ModelForm):
    class Meta:
        model=Activity
        fields=['catagory','activityname','activity_description','activity_image','pricing_types','arabic_activityname','arabic_activitydescription','location','mail_id','mobile_no','prioriy','tickt_types','status_choice','start_date','end_date','start_time','end_time','landmark']
        
    widgets={
        'catagory':forms.CharField(initial='Event'),
        'event_names':forms.CharField(max_length=500),
        #'activityname': forms.TextInput(attrs={'maxlength': 900}),
        'activity_description': forms.Textarea(attrs={'placeholder': 'Activity Description In English'}),
        'arabic_activityname': forms.TextInput(attrs={'maxlength': 500}),
        'arabic_activitydescription': forms.Textarea(attrs={'placeholder': 'Activity Description In Arabic'}),
       
        'pricing_types': forms.Select(choices=[('Free', 'Free'), ('Paid', 'Paid')]),
       
        'location': forms.TextInput(attrs={'maxlength': 500}),
        'mail_id': forms.EmailInput(attrs={'maxlength': 70}),
        'mobile_no': forms.TextInput(attrs={'maxlength': 200}),
        'prioriy': forms.NumberInput(),  # No need for label here
        'tickt_types': forms.Select(choices=[('Slots', 'Slots'), ('Ticket', 'Ticket')]),
        'status_choice': forms.Select(choices=[('Published', 'Published'), ('UnPublished', 'UnPublished')]),
        'start_date': forms.DateInput(format=('%YY-%m-%d'),attrs={'placeholder':'Enter a date in the format YYYY-MM-DD','type': 'date'}),

        # 'start_date':forms.DateField(placeholder: 'Enter a date in the format YYYY-MM-DD',
        #                                                              required=True,
        #                                                              disabled=False,
        #                                                              widget=forms.DateInput(attrs={'type':'date','class': 'datepicker','placeholder':'YY-MM-DD'}),
        #                                                              input_formats=['%Y-%m-%d', '%m/%d/%Y', '%m/%d/%y'],
        #                                                              validators=[],label='start_date'),
        'end_date':forms.DateField( help_text='Enter a date in the format YYYY-MM-DD',
                                                                     required=True,
                                                                     disabled=False,
                                                                     widget=forms.DateInput(attrs={'type':'date','class': 'datepicker','placeholder':'YY-MM-DD'}),
                                                                     input_formats=['%Y-%m-%d', '%m/%d/%Y', '%m/%d/%y'],
                                                                     validators=[],label='end_date'),

        'start_time':forms.TimeField(),
        'end_time':forms.TimeField(),
        'landmark': forms.TextInput(attrs={'maxlength': 500}),
        'activity_image': forms.FileInput(),  # Using FileInput for ImageField
    }
    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        # Optionally, you can remove the default values from rendering by the user
        self.fields['catagory'].widget.attrs['readonly'] = True
    


class ClassForm(forms.ModelForm):
    class Meta:
        model=Activity
        fields=['catagory','activityname','activity_description','arabic_activityname','arabic_activitydescription','activity_image','pricing_types','location','mail_id','mobile_no','prioriy','tickt_types','status_choice','start_date','end_date','start_time','end_time','capacity','catagory','select_sports','stundent_leval']
    
    widgets={
        'catagory':forms.CharField(initial='Class'),
        'activityname':forms.CharField(max_length=500),
        #'activityname': forms.TextInput(attrs={'maxlength': 900}),
        'activity_description': forms.Textarea(attrs={'placeholder': 'Activity Description In English'}),
        'arabic_activityname': forms.TextInput(attrs={'maxlength': 500}),
        'arabic_activitydescription': forms.Textarea(attrs={'placeholder': 'Activity Description In Arabic'}),
        
        'pricing_types': forms.Select(choices=[('Free', 'Free'), ('Paid', 'Paid')]),
        
        'select_sports':forms.Select(choices=[("Basketball","Basketball"),("Football","Football"),("Swimming","Swimming"),("Volley Ball","Volley Ball"),('Music','Music')]),
        'stundent_leval':forms.Select(choices=[('Beginner','Beginner'),('InterMediate','InterMediate'),('Expert','Expert')]),
        
        'location': forms.TextInput(attrs={'maxlength': 500}),
        'mail_id': forms.EmailInput(attrs={'maxlength': 70}),
        'mobile_no': forms.TextInput(attrs={'maxlength': 200}),
        'prioriy': forms.NumberInput(),  # No need for label here
        'tickt_types': forms.Select(choices=[('Slots', 'Slots'), ('Ticket', 'Ticket')]),
        'status_choice': forms.Select(choices=[('Published', 'Published'), ('UnPublished', 'UnPublished')]),
        'start_date':forms.DateField( help_text='Enter a date in the format YYYY-MM-DD',
                                                                     required=True,
                                                                     disabled=False,
                                                                     widget=forms.DateInput(attrs={'type':'date','class': 'datepicker','placeholder':'YY-MM-DD'}),
                                                                     input_formats=['%Y-%m-%d', '%m/%d/%Y', '%m/%d/%y'],
                                                                     validators=[],label='start_date'),
        'end_date':forms.DateField( help_text='Enter a date in the format YYYY-MM-DD',
                                                                     required=True,
                                                                     disabled=False,
                                                                     widget=forms.DateInput(attrs={'type':'date','class': 'datepicker','placeholder':'YY-MM-DD'}),
                                                                     input_formats=['%Y-%m-%d', '%m/%d/%Y', '%m/%d/%y'],
                                                                     validators=[],label='end_date'),
        'start_time':forms.TimeField( input_formats=['%H:%M:%S', '%H:%M', '%I:%M %p'],label='start_time'),
        'end_time':forms.TimeField( input_formats=['%H:%M:%S', '%H:%M', '%I:%M %p'],label='end_time'),
        'landmark': forms.TextInput(attrs={'maxlength': 500}),
        'activity_image': forms.FileInput(),  # Using FileInput for ImageField
        
    }
    def __init__(self, *args, **kwargs):
        super(ClassForm, self).__init__(*args, **kwargs)
        # Optionally, you can remove the default values from rendering by the user
        self.fields['catagory'].widget.attrs['readonly'] = True
    
    
class VenueForm(forms.ModelForm):
    class Meta:
        model=Activity
        fields=['catagory','activityname','activity_description','activity_image','pricing_types','arabic_activityname','arabic_activitydescription','location','mail_id','mobile_no','prioriy','tickt_types','status_choice','start_date','end_date','start_time','end_time','landmark','venue_names']
        
    widgets={
        'catagory':forms.CharField(initial='Venue'),
        'venue_names':forms.CharField(max_length=500),
        #'activityname': forms.TextInput(attrs={'maxlength': 900}),
        'activity_description': forms.Textarea(attrs={'placeholder': 'Activity Description In English'}),
        'arabic_activityname': forms.TextInput(attrs={'maxlength': 500}),
        'arabic_activitydescription': forms.Textarea(attrs={'placeholder': 'Activity Description In Arabic'}),
       
        'pricing_types': forms.Select(choices=[('Free', 'Free'), ('Paid', 'Paid')]),
       
        'location': forms.TextInput(attrs={'maxlength': 500}),
        'mail_id': forms.EmailInput(attrs={'maxlength': 70}),
        'mobile_no': forms.TextInput(attrs={'maxlength': 200}),
        'prioriy': forms.NumberInput(),  # No need for label here
        'tickt_types': forms.Select(choices=[('Slots', 'Slots'), ('Ticket', 'Ticket')]),
        'status_choice': forms.Select(choices=[('Published', 'Published'), ('UnPublished', 'UnPublished')]),
        'start_date':forms.DateField(widget=DateInput(attrs={'type': 'text', 'id': 'id_start_date'})),
        'end_date':forms.DateField( help_text='Enter a date in the format YYYY-MM-DD',
                                                                     required=True,
                                                                     disabled=False,
                                                                     widget=forms.DateInput(attrs={'type':'date','class': 'datepicker','placeholder':'YY-MM-DD'}),
                                                                     input_formats=['%Y-%m-%d', '%m/%d/%Y', '%m/%d/%y'],
                                                                     validators=[],label='end_date'),
        'start_time':forms.TimeField( input_formats=['%H:%M:%S', '%H:%M', '%I:%M %p'],label='start_time',),
        'end_time':forms.TimeField( input_formats=['%H:%M:%S', '%H:%M', '%I:%M %p'],label='end_time'),
        'landmark': forms.TextInput(attrs={'maxlength': 500}),
        'activity_image': forms.FileInput(),  # Using FileInput for ImageField
    }
    def __init__(self, *args, **kwargs):
        super(VenueForm, self).__init__(*args, **kwargs)
        # Optionally, you can remove the default values from rendering by the user
        self.fields['catagory'].widget.attrs['readonly'] = True
    
        
# class ActivityForm(forms.ModelForm):
#     class Meta:
#         model=Activity
#         fields=['activityname','activity_description','activity_image','pricing_types','arabic_activityname','arabic_activitydescription','location','mail_id','mobile_no','prioriy','tickt_types','status_choice','start_date','end_date','start_time','end_time','landmark','capacity']
        
#     widgets = {
#         'activityname': forms.TextInput(attrs={'maxlength': 900}),
#         'activity_description': forms.Textarea(attrs={'placeholder': 'Activity Description In English'}),
#         'activity_image': forms.FileInput(),  # Using FileInput for ImageField
#         'pricing_types': forms.Select(choices=[('Free', 'Free'), ('Paid', 'Paid')]),
#         'arabic_activityname': forms.TextInput(attrs={'maxlength': 500}),
#         'arabic_activitydescription': forms.Textarea(attrs={'placeholder': 'Activity Description In Arabic'}),
#         'location': forms.TextInput(attrs={'maxlength': 500}),
#         'mail_id': forms.EmailInput(attrs={'maxlength': 70}),
#         'mobile_no': forms.TextInput(attrs={'maxlength': 200}),
#         'prioriy': forms.NumberInput(),  # No need for label here
#         'tickt_types': forms.Select(choices=[('Slots', 'Slots'), ('Ticket', 'Ticket')]),
#        # 'created_at': forms.DateTimeInput(),  # Using DateTimeInput for DateTimeField
#         'status_choice': forms.Select(choices=[('Published', 'Published'), ('UnPublished', 'UnPublished')]),
#         'start_date': forms.DateInput(),  # Using DateInput for DateField
#         'end_date': forms.DateInput(),  # Using DateInput for DateField
#         'start_time': forms.TimeInput(),  # Using TimeInput for TimeField
#         'end_time': forms.TimeInput(),  # Using TimeInput for TimeField
#         'landmark': forms.TextInput(attrs={'maxlength': 500}),
#         'capacity': forms.NumberInput(),  # No need for label here
#     }
        
# class ActivityTagForm(forms.Form):
#     class Meta:
#         model=activity_tags
#         fields="__all__"
        
#     widgets={
#             "tag": forms.SelectMultiple(choices=[('Social Events','Social Events'),('Cultural Events','Cultural Events'),('Educational Events','Educational Events'),('Sporting Events','Sporting Events'),('Political Events','Political Events'),('Entertainment Events','Entertainment Events'),('Fundraising Events','Fundraising Events')],attrs={'class': 'form-control class1', 'placeholder': 'activity_type'})
#         }
        
        
# class ClassessForm(forms.Form):
#     class Meta:
#         model=classes
#         fields='__all__'
        
#     widgets={
#             'name':forms.Select(choices=[('Class','Class'),('Event','Event'),('Venue','Venue')],attrs={'placeholder':'Select Event Type'}),
            
#         }
        
        
# class VenueForm(forms.Form):
#    class Meta:
#        model=venues
#        fields='__all__'
        
#    widgets={
#            'name':forms.CharField(max_length=600,label='Venue Name')
#        }
        
# class SportsAndArts(forms.Form):
#    class Meta:
#        model=sports_classes
#        fields='__all__'
        
#    widgets={
#            'name':forms.Textarea(attrs={'placeholder':'Sports or Classess Name'}),
#            'select_sports':forms.Select(choices=[ ("Basketball","Basketball"),
#                                                    ("Football","Football"),
#                                                     ("Swimming","Swimming"),
#                                                     ("Volley Ball","Volley Ball"),
#                                                     ('Music','Music')],attrs={'placeholder':'Select Sports Or Class type'}),
#             'stundent_leval':forms.Select(choices=[ ('Beginner','Beginner'),
#                                                     ('InterMediate','InterMediate'),
#                                                     ('Expert','Expert')])
            
#         }
        
