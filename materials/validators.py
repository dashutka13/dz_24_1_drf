import re

from rest_framework.serializers import ValidationError


class VideoUrlValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value, null=None):
        check_field = dict(value).get(self.field)
        if check_field is not null and "www.youtube.com" not in check_field:
            raise ValidationError('Недопустимая ссылка')
