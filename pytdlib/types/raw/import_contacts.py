from .function import Function



### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class ImportContacts(Function):
    """
    Adds new contacts or edits existing contacts by their phone numbers; contacts' user identifiers are ignored

    :param contacts: The list of contacts to import or edit; contacts' vCard are ignored and are not imported
    :return: :class:`ImportedContacts`
    """
    __slots__ = ("contacts", "_extra", "_client_id", "_type")

    def __init__(self, contacts = None):
        self.contacts = contacts
        self._type = "importContacts"