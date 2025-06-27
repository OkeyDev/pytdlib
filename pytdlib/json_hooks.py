import importlib
from typing import Type

from pytdlib.types.raw.tl_object import TlObject
from pytdlib.utils import get_class_relative_import


def load_object(type_: str) -> Type:
    type_ = type_[0].upper() + type_[1:]
    import_path = get_class_relative_import(type_)
    module = importlib.import_module(import_path)
    return getattr(module, type_)


def to_object_hook(dct: dict):
    obj_type = dct.pop("@type", None)
    if obj_type:
        client_id = dct.pop("@client_id", None)
        extra = dct.pop("@extra", None)
        obj: TlObject = load_object(obj_type)(**dct)
        obj._client_id = client_id
        obj._extra = extra
        return obj
    raise ValueError(f"Unknown object type ({obj_type}): {dct}")
