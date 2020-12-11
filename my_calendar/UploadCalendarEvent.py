from studentHelper.models import Events, Description
from django.core.exceptions import EmptyResultSet, MultipleObjectsReturned, ObjectDoesNotExist
from datetime import date, timedelta
from datetime import datetime
from django.core import serializers
from django.utils import timezone
from collections import defaultdict

class ParsedEvent:

    start_date: str
    end_date: str
    description: str
    size: int

    def __init__(self, start_date, end_date, description, size):
        self.start_date = start_date
        self.end_date = end_date
        self.description = description
        self.size = size


class UploadCalendarEvent():
    def __init__(self, user):
        self.__user = user

    def get_user(self):
        return self.__user

    def execute(self, choose=False, shift="main"):
         # get events from db
         # Gap between times in calendar
         cal_size = 30
         data = {}
         today = date.today()
         day = today.weekday()
         if shift == "main":
             start_date = timezone.now().replace(hour=0, minute=0, second=0) - timedelta(days=day)
             end_date = timezone.now().replace(hour=23, minute=59, second=59) + timedelta(days=(6-day))
         else:
             start_date = datetime.strptime(shift, '%Y-%m-%d')
             end_date = start_date + timedelta(days=6)

         try:
             events = Events.objects.get_all_events(self.get_user().id, start_date, end_date)

             for event in events:
                 checked = False
                 extra = Description.objects.get_descriptions(event, choose).first()
                 key = str(event.start_date.weekday())
                 if event.period_type == "ONCE" and extra != None:
                     sd = event.start_date.time()
                     ed = event.end_date.time()

                     size = ((event.end_date - event.start_date).total_seconds())//(60 * cal_size)
                     event = ParsedEvent(str(sd), str(ed), str(extra.description), range(int(size)))

                     if key in data:
                         data[key].append(event)
                     else:
                         helper = {key: [event]}
                         data.update(helper)

                #TODO nie działa
                 elif event.period_type == "DAILY" and extra != None:
                     for i in range(event.start_date.weekday(), 7):
                         event = ParsedEvent(str(""), "Codziennie", str(extra.description), range((cal_size//60) * 24))
                         if str(i) in data:
                             data[str(i)].append(event)
                         else:
                             helper = {str(i): [event]}
                             data.update(helper)




         except(EmptyResultSet, MultipleObjectsReturned, ObjectDoesNotExist) as e:
             print("e")

         next_shift = start_date.date() + timedelta(days=7)
         prev_shift = start_date.date() - timedelta(days=7)
         data.update({"next_shift": str(next_shift)})
         data.update({"prev_shift": str(prev_shift)})

         return data
