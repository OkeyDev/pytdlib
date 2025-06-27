import json

from pytdlib.json_hooks import to_object_hook
from pytdlib.types.raw.ok import Ok


def test_hook_simple():
    test_hook = json.dumps({"@type": "Ok"})
    result = json.loads(test_hook, object_hook=to_object_hook)
    assert result == Ok()
