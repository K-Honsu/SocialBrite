import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "socials.settings")
import django
django.setup()


import pandas as pd
from event.models import Registration
from django.conf import settings

def export_registrations_to_excel():
    registrations = Registration.objects.all()

    # Create a DataFrame from the registrations data
    data = {
        'Student': [str(registration.student) for registration in registrations],
        'Event': [str(registration.event_detail) for registration in registrations],
    }
    df = pd.DataFrame(data)

    # Specify the file path for the Excel file
    file_path = settings.BASE_DIR / 'registrations.xlsx'  # Change the file path as desired

    # Export the DataFrame to an Excel file
    df.to_excel(file_path, index=False)

export_registrations_to_excel()
