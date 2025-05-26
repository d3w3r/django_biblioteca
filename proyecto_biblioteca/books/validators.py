from django.core.exceptions import ValidationError

def autor_validator(value: str):
    stripped = value.strip()
    if stripped == "":
        raise ValidationError("Is not a valid Autor name")

def libro_validator(value: str):
    words = value.split()
    if (len(words) < 5):
        raise ValidationError("Min of words for resumen is 10")

def resena_validator(value: int):
    if 0 <= value <= 5:
        raise ValidationError("Min value 0 and max value 5")