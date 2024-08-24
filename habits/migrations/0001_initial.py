# Generated by Django 5.1 on 2024-08-24 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Habits",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("place", models.CharField(max_length=140, verbose_name="Место")),
                (
                    "time",
                    models.TimeField(
                        verbose_name="Время, когда надо выполнить привычку"
                    ),
                ),
                (
                    "action",
                    models.CharField(
                        max_length=140, verbose_name="Действие, которое надо сделать"
                    ),
                ),
                (
                    "utc_time",
                    models.TimeField(
                        blank=True,
                        null=True,
                        verbose_name="Время исполнения привычки в формате UTC, вычисляется автоматически по time_offset пользователя",
                    ),
                ),
                (
                    "weekday_offset",
                    models.IntegerField(
                        default=0,
                        verbose_name="Смещение дня недели относительно UTC. Заполняется автоматически.",
                    ),
                ),
                (
                    "periodicity",
                    models.SmallIntegerField(
                        default=1, verbose_name="Периодичность (в днях) - от 1 до 7"
                    ),
                ),
                (
                    "prize",
                    models.CharField(
                        blank=True,
                        max_length=100,
                        null=True,
                        verbose_name="Вознаграждение",
                    ),
                ),
                (
                    "duration",
                    models.SmallIntegerField(
                        verbose_name="Время на выполнение (в минутах) "
                    ),
                ),
                (
                    "is_public",
                    models.BooleanField(
                        choices=[(True, "Публичная"), (False, "Нет")],
                        default=True,
                        verbose_name="Публичная",
                    ),
                ),
                (
                    "monday",
                    models.BooleanField(
                        choices=[(True, "Да"), (False, "Нет")],
                        default=True,
                        verbose_name="Понедельник",
                    ),
                ),
                (
                    "tuesday",
                    models.BooleanField(
                        choices=[(True, "Да"), (False, "Нет")],
                        default=True,
                        verbose_name="Вторник",
                    ),
                ),
                (
                    "wednesday",
                    models.BooleanField(
                        choices=[(True, "Да"), (False, "Нет")],
                        default=True,
                        verbose_name="Среда",
                    ),
                ),
                (
                    "thursday",
                    models.BooleanField(
                        choices=[(True, "Да"), (False, "Нет")],
                        default=True,
                        verbose_name="Четверг",
                    ),
                ),
                (
                    "friday",
                    models.BooleanField(
                        choices=[(True, "Да"), (False, "Нет")],
                        default=True,
                        verbose_name="Пятница",
                    ),
                ),
                (
                    "saturday",
                    models.BooleanField(
                        choices=[(True, "Да"), (False, "Нет")],
                        default=True,
                        verbose_name="Суббота",
                    ),
                ),
                (
                    "sunday",
                    models.BooleanField(
                        choices=[(True, "Да"), (False, "Нет")],
                        default=True,
                        verbose_name="Воскресенье",
                    ),
                ),
                (
                    "is_nice",
                    models.BooleanField(
                        choices=[(True, "Приятная"), (False, "Нет")],
                        default=True,
                        verbose_name="Приятная",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True,
                        help_text="Укажите дату создания",
                        null=True,
                        verbose_name="Дата создания",
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True,
                        help_text="Укажите дату изменения",
                        null=True,
                        verbose_name="Дата изменения",
                    ),
                ),
            ],
            options={
                "verbose_name": "Привычка",
                "verbose_name_plural": "Привычки",
                "ordering": ["-id"],
            },
        ),
    ]
