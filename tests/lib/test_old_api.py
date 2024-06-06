import pytest

import openaix
from openaix.lib._old_api import APIRemovedInV1


def test_basic_attribute_access_works() -> None:
    for attr in dir(openaix):
        dir(getattr(openaix, attr))


def test_helpful_error_is_raised() -> None:
    with pytest.raises(APIRemovedInV1):
        openaix.Completion.create()  # type: ignore

    with pytest.raises(APIRemovedInV1):
        openaix.ChatCompletion.create()  # type: ignore
