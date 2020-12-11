import datetime
from app1.models import *


def get_timetable(date, user_class):
    time_list = OneLesson.objects.filter(date=date).filter(a_class=user_class)
    lessons_and_time = [{'number': 1, 'time': '09:00-09:45', 'title': '', 'homework': '', 'comment': ''},
                        {'number': 2, 'time': '10:00-10:45', 'title': '', 'homework': '', 'comment': ''},
                        {'number': 3, 'time': '11:00-11:45', 'title': '', 'homework': '', 'comment': ''},
                        {'number': 4, 'time': '12:00-12:45', 'title': '', 'homework': '', 'comment': ''},
                        {'number': 5, 'time': '13:00-13:45', 'title': '', 'homework': '', 'comment': ''},
                        {'number': 6, 'time': '14:00-14:45', 'title': '', 'homework': '', 'comment': ''},
                        {'number': 7, 'time': '15:00-15:45', 'title': '', 'homework': '', 'comment': ''}
                        ]
    for lesson in time_list:
        one_lesson = list(filter(lambda x: x['time'] == str(lesson.lesson_time), lessons_and_time))[0]
        one_lesson['title'] = str(lesson)
        one_lesson['homework'] = lesson.homework
        one_lesson['comment'] = lesson.comment_teacher
    return lessons_and_time


def get_timetable_week(date, user_class):
    date_from = date - datetime.timedelta(days=date.weekday())
    date_to = date + datetime.timedelta(days=6 - date.weekday())
    result = []
    while date_from <= date_to:
        result.append({'date': get_date_to_string(date_from), 'lessons': get_timetable(date_from, user_class)})
        date_from += datetime.timedelta(days=1)
    return result


def get_date_to_string(date):
    week_days = ['понедельник', 'вторник', 'среду', 'четверг', 'пятница', 'субботу', 'воскресенье']
    return week_days[date.weekday()] + ' ' + date.strftime('%d.%m.%Y')
