from datetime import datetime

def get_date():
    now = datetime.now()
    return now.strftime("%d.%m.%Y")

