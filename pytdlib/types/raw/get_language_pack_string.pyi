from .function import Function

from .language_pack_string_value_deleted import LanguagePackStringValueDeleted
from .language_pack_string_value_ordinary import LanguagePackStringValueOrdinary
from .language_pack_string_value_pluralized import LanguagePackStringValuePluralized

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class GetLanguagePackString(Function[LanguagePackStringValueOrdinary | LanguagePackStringValuePluralized | LanguagePackStringValueDeleted]):
    """
    Returns a string stored in the local database from the specified localization target and language pack by its key. Returns a 404 error if the string is not found. Can be called synchronously

    :param language_pack_database_path: Path to the language pack database in which strings are stored
    :param localization_target: Localization target to which the language pack belongs
    :param language_pack_id: Language pack identifier
    :param key: Language pack key of the string to be returned
    :return: :class:`LanguagePackStringValueOrdinary | LanguagePackStringValuePluralized | LanguagePackStringValueDeleted`
    """
    __slots__ = ("language_pack_database_path", "localization_target", "language_pack_id", "key", "_extra", "_client_id", "_type")

    def __init__(self, language_pack_database_path: str = "", localization_target: str = "", language_pack_id: str = "", key: str = ""):
        self.language_pack_database_path = language_pack_database_path
        self.localization_target = localization_target
        self.language_pack_id = language_pack_id
        self.key = key
        self._type = "getLanguagePackString"