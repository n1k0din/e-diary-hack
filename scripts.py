import random

from datacenter.models import Chastisement, Commendation, Lesson, Mark, Schoolkid
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

COMMENDS = (
    'Молодец!',
    'Отлично!',
    'Хорошо!',
    'Гораздо лучше, чем я ожидал!',
    'Ты меня приятно удивил!',
    'Великолепно!',
    'Прекрасно!',
    'Ты меня очень обрадовал!',
    'Именно этого я давно ждал от тебя!',
    'Сказано здорово – просто и ясно!',
    'Ты, как всегда, точен!',
    'Очень хороший ответ!',
    'Талантливо!',
    'Ты сегодня прыгнул выше головы!',
    'Я поражен!',
    'Уже существенно лучше!',
    'Потрясающе!',
    'Замечательно!',
    'Прекрасное начало!',
    'Так держать!',
    'Ты на верном пути!',
    'Здорово!',
    'Это как раз то, что нужно!',
    'Я тобой горжусь!',
    'С каждым разом у тебя получается всё лучше!',
    'Мы с тобой не зря поработали!',
    'Я вижу, как ты стараешься!',
    'Ты растешь над собой!',
    'Ты многое сделал, я это вижу!',
    'Теперь у тебя точно все получится!',
)


def get_schoolkid_by_name(fullname):
    try:
        return Schoolkid.objects.filter(full_name__contains=fullname).get()
    except MultipleObjectsReturned:
        print(f'Error! More than one {fullname}!')
    except ObjectDoesNotExist:
        print(f'Error! {fullname} not found!')


def fix_marks(schoolkid):
    bad_marks = Mark.objects.filter(schoolkid=schoolkid, points__in=[2, 3])
    for bad_mark in bad_marks:
        bad_mark.points = 5
        bad_mark.save()


def remove_chastisements(schoolkid):
    kid_chastisements = Chastisement.objects.filter(schoolkid=schoolkid)
    kid_chastisements.delete()


def create_commendation(schoolkid, subject_title):
    kid_lessons = Lesson.objects.filter(
        year_of_study=schoolkid.year_of_study,
        group_letter=schoolkid.group_letter,
    )

    try:
        lesson = kid_lessons.filter(subject__title=subject_title).order_by('?').get()
    except MultipleObjectsReturned:
        exit(f'Error! More than one {subject_title}!')

    except ObjectDoesNotExist:
        exit(f'Error! {subject_title} not found!')

    Commendation.objects.create(
        schoolkid=schoolkid,
        text=random.choice(COMMENDS),
        created=lesson.date,
        teacher=lesson.teacher,
        subject=lesson.subject,
    )
