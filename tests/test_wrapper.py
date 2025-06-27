from unittest.mock import patch

from pytdlib.wrapper import validate_lib_path


def test_validate_lib_path():
    with patch("pathlib.Path.is_dir", return_value=True):
        assert (
            validate_lib_path("/home/dev/tdlib/") == "/home/dev/tdlib/lib/libtdjson.so"
        )
        assert validate_lib_path("~/tdlib/") == "~/tdlib/lib/libtdjson.so"
        assert validate_lib_path("./tdlib/") == "tdlib/lib/libtdjson.so"

    with patch("pathlib.Path.is_dir", return_value=False):
        assert validate_lib_path("./tdlib/lib/libtdjson.so") == "tdlib/lib/libtdjson.so"
        assert validate_lib_path("/home/dev/tdlib/lib/libtdjson.so")
