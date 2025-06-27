from pytdlib.types.raw.function import Function


class PyTdLibException(Exception):
    def __init__(self) -> None:
        self.__init__()
        pass


class PyTdLibraryLoadException(PyTdLibException):
    def __init__(self, path: str) -> None:
        self.path = path

    def __str__(self) -> str:
        return f"Something went wrong while loading library: {self.path}"


class PyTdLibResponseError(PyTdLibException):
    def __init__(self, command: Function, code: int, description: str) -> None:
        self.command = command
        self.code = code
        self.description = description

    def __str__(self) -> str:
        return f"Error {self.code}: {self.description}. Command: {self.command}"


class PyTdLibClosed(PyTdLibException):
    def __str__(self) -> str:
        return "Library closed. You can't use this methods. Recreate Executor object to use it again"
