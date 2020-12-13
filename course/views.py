from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from studentHelper.models import Course, Teacher, Marks, Goals
from studentHelper.views import main_view

from .forms import MarkForm, RulesForm


@login_required(login_url='/login')
def course_view(request, pk):
    TYPES = {
    "PLUS": "+",
    "MINUS": "-",
    "PKT": "pkt",
    "MARK": "ocena",
    }
    context = {
        'course': Course.objects.get_record_by_id(pk),
        'forms': Course.objects.get_all_forms_by_id(pk),
        'marks': Marks.objects.getMarks(pk),
        'goals': Goals.objects.get_records_by_course_id(pk)
    }
    #TODO czy da się inaczej?
    for el in context['marks']:
        el['mark_type'] = TYPES[el['mark_type']]

    if context['course'].client_id != request.user:
        return main_view(request)

    return render(request, "course.html", context)


@login_required(login_url='/login')
def temp(request):
    pass


@login_required(login_url='/login')
def add_mark_view(request, pk):

    if request.method == 'POST':
        mark = MarkForm(request.POST)

        if mark.is_valid():
            m = mark.save(commit=False)
            m.course_id = Course.objects.get_record_by_id(pk)
            m.save()
            return redirect('/course/'+str(pk))
    else:
        mark = MarkForm()

    return render(request, "new_mark.html", {"mark_form": mark, "pk": pk})

@login_required(login_url='/login')
def edit_mark_view(request, pk):
    my_mark = Marks.objects.get_record_by_id(pk)

    if request.method == 'POST':
        mark = MarkForm(request.POST, instance=my_mark)

        if mark.is_valid():
            mark.save()
            return redirect('/course/'+str(my_mark.course_id.id))
    else:
        #TODO info?
        mark = MarkForm(instance=my_mark)

    return render(request, "new_mark.html", {"mark_form": mark, "pk": pk, "edit": True })


@login_required(login_url='/login/')
def new_pass_rules(request, pk):
    if request.method == 'POST':
        rules = RulesForm(request.POST, course_id=pk)
        if rules.is_valid():
            rules.save()
            return redirect('/course/'+str(pk))
    else:
        rules = RulesForm(course_id=pk)
    return render(request, 'new_pass_rules.html', {'rules_form': rules, "pk": pk})
