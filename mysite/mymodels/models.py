from django.db import models


# Create your models here.

class Person(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    birth_date = models.DateField()

    def baby_boomer_status(self):
        import datetime
        if self.birth_date < datetime.date(1945, 8, 1):
            return "Pre_boomer"
        elif self.birth_date < datetime.date(1965, 1, 1):
            return "Baby boomer"
        else:
            return "Post-boomer"

    @property
    def full_name(self):
        return "{} , {}".format(self.first_name, self.last_name)


class Musician(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    instrument = models.CharField(max_length=32)


class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=32)
    release_data = models.DateField()
    num_stars = models.IntegerField()


class MusicPerson(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=32)
    members = models.ManyToManyField(MusicPerson, through='Menbership')

    def __str__(self):
        return self.name


class Menbership(models.Model):
    person = models.ForeignKey(MusicPerson, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=32)


class Ox(models.Model):
    horn_length = models.IntegerField()

    class Meta:
        ordering = ['horn_length']
        verbose_name_plural = "oxen"


class Bolg(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def save(self, *args, **kwargs):
        if self.name == "Yoko one's bolg":
            return ""
        else:
            super().save(*args, **kwargs)  # Call the "real" save() method.


class CommonInfo(models.Model):
    name = models.CharField(max_length=32)
    age = models.PositiveIntegerField()

    class Meta:
        abstract = True
        ordering = ['name']


class Unmanage(models.Model):
    class Meta:
        abstract = True
        managed = False


class Student(CommonInfo, Unmanage):
    home_group = models.CharField(max_length=32)

    class Meta(CommonInfo.Meta, Unmanage.Meta):
        db_table = "student_info"


class Base(models.Model):
    m2m = models.ManyToManyField(
        CommonInfo,
        related_name="%(app_label)s_%(class)s_related",
        related_query_name="%(app_label)s_%(class)ss",
    )

    class Meta:
        abstract = True


class ChildA(Base):
    pass


class ChildB(Base):
    pass
