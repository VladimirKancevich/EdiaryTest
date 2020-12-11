from app1.models import Classes, Students, Teachers, Lessons, OneLesson, Grade, TimeSlot
import datetime

import json

with open('data.json', 'r') as file:
    data = json.load(file)

for cls in data['classes']:
    classes = Classes(number=cls['name'])
    classes.save()

for les in data['lessons']:
    lesson = Lessons(name=les['name'], is_active=les['is_active'])
    lesson.save()

for tch in data['teachers']:
    teacher = Teachers(login=tch['login'], password=tch['password'], name=tch['name'])
    teacher.save()

for time in data['TimeSlot']:
    [begin, end] = time['time'].split('-')
    [hours, minutes] = begin.split(':')
    time_begin = datetime.time(int(hours), int(minutes))
    [hours, minutes] = end.split(':')
    time_end = datetime.time(int(hours), int(minutes))
    time_slot = TimeSlot(time_begin=time_begin, time_end=time_end)
    time_slot.save()