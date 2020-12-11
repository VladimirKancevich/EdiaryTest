from django.db import models
from datetime import date


class Classes(models.Model):
    number = models.CharField(max_length=7)

    def __str__(self):
        return self.number

    class Meta:
        verbose_name = 'Класс'
        verbose_name_plural = 'Классы'


class Users(models.Model):
    login = models.CharField('Логин', unique=True, max_length=200)
    password = models.CharField('Пароль', max_length=200)
    name = models.CharField('ФИО', max_length=200)
    is_active = models.BooleanField('Работает/Учится', default=True)

    def __str__(self):
        return self.login

    class Meta:
        abstract = True


class Students(Users):
    user_class = models.ForeignKey(Classes, on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Ученик'
        verbose_name_plural = 'Ученики'


class Teachers(Users):
    pass

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'


class Lessons(models.Model):
    name = models.CharField(max_length=200, unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'


class GradeType(models.IntegerChoices):
    lesson_work = 1, 'Работа на уроке'
    test = 2, 'Самостоятельная работа'
    control_test = 3, 'Контрольная работа'
    homework = 4, 'Домашняя работа'


class LessonStatus(models.IntegerChoices):
    active = 1, 'Активный'
    canceled = 2, 'Отменен'
    switched = 3, 'Замена'


class GradeList(models.IntegerChoices):
    one = 1, '1'
    two = 2, '2'
    three = 3, '3'
    four = 4, '4'
    five = 5, '5'


class TimeSlot(models.Model):
    time_begin = models.TimeField(unique=True)
    time_end = models.TimeField(unique=True)

    def __str__(self):
        return self.time_begin.isoformat(timespec='minutes') + "-" + self.time_end.isoformat(timespec='minutes')

    class Meta:
        verbose_name = 'Время урока'
        verbose_name_plural = 'Время уроков'


class OneLesson(models.Model):
    date = models.DateField()
    lesson_time = models.ForeignKey(TimeSlot, on_delete=models.PROTECT)
    lesson = models.ForeignKey(Lessons, on_delete=models.PROTECT)
    homework = models.CharField(max_length=500, blank=True)
    teacher = models.ForeignKey(Teachers, on_delete=models.PROTECT)
    a_class = models.ForeignKey(Classes, on_delete=models.PROTECT)
    lesson_status = models.IntegerField(choices=LessonStatus.choices, default=1)
    comment_teacher = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.lesson.name

    class Meta:
        verbose_name = 'Расписание урока'
        verbose_name_plural = 'Расписание уроков'
        constraints = [
            models.UniqueConstraint(fields=['date', 'lesson_time', 'a_class'], name='unique_lesson')
        ]


def norm_view_for(grade_type):
    if grade_type == 1:
        return 'Работа на уроке'
    elif grade_type == 2:
        return 'Самостоятельная работа'
    elif grade_type == 3:
        return 'Контрольная работа'
    elif grade_type == 4:
        return 'Домашняя работа'
    else:
        return ' Ошибка '


class Grade(models.Model):
    # оценка
    student = models.ForeignKey(Students, on_delete=models.PROTECT)
    lesson = models.ForeignKey(OneLesson, on_delete=models.PROTECT)
    grade = models.IntegerField(choices=GradeList.choices)
    grade_type = models.IntegerField(choices=GradeType.choices)
    # дата за которую ставится оценка
    grade_date = models.DateField(default=date.today)

    def __str__(self):
        return str(self.student) + ' Оценка: ' + str(self.grade) + ' ' + norm_view_for(self.grade_type) + ' ' + str(
            self.lesson) + ' ' + str(self.grade_date)

    class Meta:
        verbose_name = 'Оценка'
        verbose_name_plural = 'Оценки'


class LogUser(models.Model):
    key = models.ForeignKey(Students, on_delete=models.PROTECT)
