from typing import TextIO

from compiler.types import ClassArgument, ClassDefinition, FunctionDefinition


class TlFileParser:
    def __init__(self, file: TextIO) -> None:
        self.source = file
        self.is_function_section = False

    def _read_char(self):
        return self.source.read(1)

    def _backward_char(self):
        self.source.seek(self.source.tell() - 1)

    def _read_to_stop_symbol(self, stop_symbols: str):
        text = ""
        symbol = ""
        while (symbol := self._read_char()) not in stop_symbols:
            text += symbol

        # symbol = '' if EOF. Fuck Python
        if symbol:
            self._backward_char()

        return text

    def _skip_whitespaces(self):
        while (symbol := self._read_char()) and symbol in " \n\t":
            pass
        if symbol:
            self._backward_char()

    def _get_char(self):
        value = self.source.read(1)
        if value:
            self._backward_char()
        return value

    def read_part(self) -> ClassDefinition | FunctionDefinition | None:
        self._skip_whitespaces()
        if not self._get_char():
            return None

        if self._get_char() == "-":
            assert self._read_char() == "-"
            assert self._read_char() == "-"
            assert self._read_char() == "-"
            assert self._read_to_stop_symbol("-") == "functions"
            assert self._read_char() == "-"
            assert self._read_char() == "-"
            assert self._read_char() == "-"
            self.is_function_section = True
            self._skip_whitespaces()

        class_info = {}
        # Reading metadata for class
        # While new line comment starts
        argument_name = ""
        while self._get_char() == "/":
            assert self._read_char() == "/"
            assert self._read_char() == "/"
            while (symbol := self._get_char()) and symbol != "\n":
                current_symbol = self._read_char()

                if current_symbol == "@":
                    argument_name = self._read_to_stop_symbol(" ")
                    self._read_char()
                    text = self._read_to_stop_symbol("@\n").strip()
                    class_info[argument_name] = text
                elif current_symbol == "-":
                    text = self._read_to_stop_symbol("@\n").strip()
                    class_info[argument_name] = class_info[argument_name] + " " + text
                else:
                    raise ValueError(f"Unknown symbol: {current_symbol}")

            if symbol == "\n":
                self._read_char()

        # For one-line class definition
        symbol = self._get_char()
        if symbol == "" or symbol == "\n" or symbol == " ":
            assert not self.is_function_section
            return ClassDefinition(
                class_name=class_info["class"],
                description=class_info.get("description"),
                arguments=[],
                parent=None,
            )

        class_name = self._read_to_stop_symbol(" ")
        self._read_char()

        arguments = []
        while self._get_char() != "=":
            argument = self._read_to_stop_symbol(" ")
            self._read_char()

            arg_name, arg_type = argument.split(":")
            arguments.append(
                ClassArgument(
                    name=arg_name, description=class_info.get(arg_name), type_=arg_type
                )
            )

        # Read = and ' '
        self._read_char()
        self._read_char()

        parent_name = self._read_to_stop_symbol(";")
        self._read_char()
        if not self.is_function_section:
            return ClassDefinition(
                class_name=class_name,
                description=class_info.get("description"),
                arguments=arguments,
                parent=parent_name,
            )
        else:
            return FunctionDefinition(
                class_name=class_name,
                description=class_info.get("description"),
                arguments=arguments,
                return_type=parent_name,
            )
