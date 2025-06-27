import re

# https://stackoverflow.com/questions/1175208/elegant-python-function-to-convert-camelcase-to-snake-case
CAMEL_TO_SNAKE_REGEX = re.compile(r"(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])")


def get_class_relative_import(type_: str):
    type_ = CAMEL_TO_SNAKE_REGEX.sub("_", type_).lower()
    return f"pytdlib.types.raw.{type_}"


def filter_mobile_phone(phone: str):
    return "".join(i for i in phone if i.isdigit())
