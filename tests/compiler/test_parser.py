from io import StringIO

from compiler.parser import TlFileParser
from compiler.types import ClassArgument, ClassDefinition, FunctionDefinition

INLINE_TEXT = "//@class AuthenticationCodeType @description Provides information about the method by which an authentication code is delivered to the user"
INLINE_TEXT_RESULT = ClassDefinition(
    class_name="AuthenticationCodeType",
    description="Provides information about the method by which an authentication code is delivered to the user",
    arguments=[],
    parent=None,
)

MULTILINE_TEXT = """
//@description A digit-only authentication code is delivered via a private Telegram message, which can be viewed from another active session
//@length Length of the code
authenticationCodeTypeTelegramMessage length:int32 = AuthenticationCodeType;
"""
MULTILINE_TEXT_RESULT = ClassDefinition(
    class_name="authenticationCodeTypeTelegramMessage",
    description="A digit-only authentication code is delivered via a private Telegram message, which can be viewed from another active session",
    arguments=[
        ClassArgument(name="length", description="Length of the code", type_="int32")
    ],
    parent="AuthenticationCodeType",
)

MULTILINE_TEXT_WITH_INLINE_PARAMS = """
//@description An authentication token received through Apple ID @token The token
emailAddressAuthenticationAppleId token:string = EmailAddressAuthentication;
"""
MULTILINE_TEXT_WITH_INLINE_PARAMS_RESULT = ClassDefinition(
    class_name="emailAddressAuthenticationAppleId",
    description="An authentication token received through Apple ID",
    arguments=[ClassArgument(name="token", description="The token", type_="string")],
    parent="EmailAddressAuthentication",
)


MULTILINE_TEXT_WITH_TRANSFER = """
//@description A text with some entities @text The text @entities Entities contained in the text. Entities can be nested, but must not mutually intersect with each other.
//-Pre, Code and PreCode entities can't contain other entities. BlockQuote entities can't contain other BlockQuote entities. Bold, Italic, Underline, Strikethrough, and Spoiler entities can contain and can be part of any other entities. All other entities can't contain each other
formattedText text:string entities:vector<textEntity> = FormattedText;
"""
MULTILINE_TEXT_WITH_TRANSFER_RESULT = ClassDefinition(
    class_name="formattedText",
    description="A text with some entities",
    arguments=[
        ClassArgument(name="text", description="The text", type_="string"),
        ClassArgument(
            name="entities",
            description="Entities contained in the text. Entities can be nested, but must not mutually intersect with each other. Pre, Code and PreCode entities can't contain other entities. BlockQuote entities can't contain other BlockQuote entities. Bold, Italic, Underline, Strikethrough, and Spoiler entities can contain and can be part of any other entities. All other entities can't contain each other",
            type_="vector<textEntity>",
        ),
    ],
    parent="FormattedText",
)


def create_parser(text: str):
    io_text = StringIO(text)
    return TlFileParser(io_text)


def get_result_by_text(text: str):
    if text == INLINE_TEXT:
        return INLINE_TEXT_RESULT
    if text == MULTILINE_TEXT:
        return MULTILINE_TEXT_RESULT
    if text == MULTILINE_TEXT_WITH_INLINE_PARAMS:
        return MULTILINE_TEXT_WITH_INLINE_PARAMS_RESULT
    if text == MULTILINE_TEXT_WITH_TRANSFER:
        return MULTILINE_TEXT_WITH_TRANSFER_RESULT


def test_one_line_class():
    text = INLINE_TEXT
    parser = create_parser(text)
    assert parser.read_part() == INLINE_TEXT_RESULT


def test_multiple_line_parser():
    text = MULTILINE_TEXT
    parser = create_parser(text)
    assert parser.read_part() == MULTILINE_TEXT_RESULT


def test_multiple_line_parser_with_inline_params_description():
    text = MULTILINE_TEXT_WITH_INLINE_PARAMS
    parser = create_parser(text)
    assert parser.read_part() == MULTILINE_TEXT_WITH_INLINE_PARAMS_RESULT


def test_multiple_line_parser_with_multiple_inline_params_description():
    text = """
//@description Represents a part of the text that needs to be formatted in some unusual way @offset Offset of the entity, in UTF-16 code units @length Length of the entity, in UTF-16 code units @type Type of the entity
textEntity offset:int32 length:int32 type:TextEntityType = TextEntity;
    """
    parser = create_parser(text)
    assert parser.read_part() == ClassDefinition(
        class_name="textEntity",
        description="Represents a part of the text that needs to be formatted in some unusual way",
        arguments=[
            ClassArgument(
                name="offset",
                description="Offset of the entity, in UTF-16 code units",
                type_="int32",
            ),
            ClassArgument(
                name="length",
                description="Length of the entity, in UTF-16 code units",
                type_="int32",
            ),
            ClassArgument(
                name="type", description="Type of the entity", type_="TextEntityType"
            ),
        ],
        parent="TextEntity",
    )


def test_multiple_line_parser_with_transfer_to_next_line():
    parser = create_parser(MULTILINE_TEXT_WITH_TRANSFER)
    assert parser.read_part() == MULTILINE_TEXT_WITH_TRANSFER_RESULT


def test_line_parser_for_two_inline_parts():
    text = "\n\n".join([INLINE_TEXT, INLINE_TEXT])
    parser = create_parser(text)

    assert parser.read_part() == INLINE_TEXT_RESULT
    assert parser.read_part() == INLINE_TEXT_RESULT


def test_line_parser_for_inline_and_multiline_parts():
    for text_part in [
        MULTILINE_TEXT,
        MULTILINE_TEXT_WITH_INLINE_PARAMS,
        MULTILINE_TEXT_WITH_TRANSFER,
    ]:
        text = "\n\n".join([INLINE_TEXT, text_part])
        parser = create_parser(text)
        assert parser.read_part() == INLINE_TEXT_RESULT
        assert parser.read_part() == get_result_by_text(text_part)


def test_line_parser_for_multiple_multiline_parts():
    multiline_cols = [
        MULTILINE_TEXT,
        MULTILINE_TEXT_WITH_INLINE_PARAMS,
        MULTILINE_TEXT_WITH_TRANSFER,
    ]
    for part1 in multiline_cols:
        for part2 in multiline_cols:
            for part3 in multiline_cols:
                text = "\n\n".join([part1, part2, part3])
                parser = create_parser(text)
                assert parser.read_part() == get_result_by_text(part1)
                assert parser.read_part() == get_result_by_text(part2)
                assert parser.read_part() == get_result_by_text(part3)


def test_parser_for_function():
    text = """
---functions---

//@description Returns the current authorization state. This is an offline method. For informational purposes only. Use updateAuthorizationState instead to maintain the current authorization state. Can be called before initialization
getAuthorizationState = AuthorizationState;
    """

    parser = create_parser(text)
    assert parser.read_part() == FunctionDefinition(
        class_name="getAuthorizationState",
        description="Returns the current authorization state. This is an offline method. For informational purposes only. Use updateAuthorizationState instead to maintain the current authorization state. Can be called before initialization",
        arguments=[],
        return_type="AuthorizationState",
    )


def test_ok_parsing():
    text = """
//@description An object of this type is returned on a successful function call for certain functions
ok = Ok;
    """
    parser = create_parser(text)
    assert parser.read_part() == ClassDefinition(
        "ok",
        "An object of this type is returned on a successful function call for certain functions",
        [],
        "Ok",
    )
