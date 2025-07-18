from .speech_recognition_result import SpeechRecognitionResult

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class SpeechRecognitionResultText(SpeechRecognitionResult):
    """
    The speech recognition successfully finished

    :param text: Recognized text
    """
    __slots__ = ("text", "_extra", "_client_id", "_type")

    def __init__(self, text = None):
        self.text = text
        self._type = "speechRecognitionResultText"