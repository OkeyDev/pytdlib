from .giveaway_participant_status import GiveawayParticipantStatus

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class GiveawayParticipantStatusDisallowedCountry(GiveawayParticipantStatus):
    """
    The user can't participate in the giveaway, because they phone number is from a disallowed country

    :param user_country_code: A two-letter ISO 3166-1 alpha-2 country code of the user's country
    """
    __slots__ = ("user_country_code", "_extra", "_client_id", "_type")

    def __init__(self, user_country_code = None):
        self.user_country_code = user_country_code
        self._type = "giveawayParticipantStatusDisallowedCountry"