from .downloaded_file_counts import DownloadedFileCounts
from .update import Update

### FILE IS AUTOGENERATED. DO NO EDIT IT BY HAND ###

class UpdateFileDownload(Update):
    """
    A file download was changed. This update is sent only after file download list is loaded for the first time

    :param file_id: File identifier
    :param complete_date: Point in time (Unix timestamp) when the file downloading was completed; 0 if the file downloading isn't completed
    :param is_paused: True, if downloading of the file is paused
    :param counts: New number of being downloaded and recently downloaded files found
    """
    __slots__ = ("file_id", "complete_date", "is_paused", "counts", "_extra", "_client_id", "_type")

    def __init__(self, file_id: int = 0, complete_date: int = 0, is_paused: bool = False, counts: DownloadedFileCounts | None = None):
        self.file_id = file_id
        self.complete_date = complete_date
        self.is_paused = is_paused
        self.counts = counts
        self._type = "updateFileDownload"