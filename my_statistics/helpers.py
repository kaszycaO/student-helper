from studentHelper.models import Prediction, Course, Events, Components
from django.db.models import Max, Min
from datetime import date


def get_times_by_courses(client_id):
    courses = Course.objects.get_records_by_client_id(client_id)
    course_names = []
    times = []
    for course in courses:
        time = 0
        predictions = Prediction.objects.get_records_by_course_id(course)
        for p in predictions:
            if p.actual_time != '':
                time += p.actual_time
        course_names.append(course.course_name)
        times.append(time)
    return course_names, times


def get_days_to_end_of_semester(client_id):
    classes = Events.objects.get_classes_by_client_id(client_id)
    lastDay = classes.aggregate(Max('end_date'))['end_date__max'].date()
    return (lastDay - date.today()).days


def get_number_of_days_in_semester(client_id):
    classes = Events.objects.get_classes_by_client_id(client_id)
    firstDay = classes.aggregate(Min('end_date'))['end_date__min'].date()
    lastDay = classes.aggregate(Max('end_date'))['end_date__max'].date()
    return (lastDay - firstDay).days


def get_ratios_by_courses(client_id):
    courses = Course.objects.get_records_by_client_id(client_id)
    course_names = []
    ratios = []
    for course in courses:
        actual = 0
        estimated = 0
        predictions = Prediction.objects.get_records_by_course_id(course)
        for p in predictions:
            if p.actual_time != '':
                actual += p.actual_time
                estimated += p.pred_time
        if actual != 0:
            ratios.append(estimated/actual)
            course_names.append(course.course_name)
    return course_names, ratios

