import pytest

from .spam import *


def test_single():
    assert public_all()
    assert public_export()

    with pytest.raises(NameError):
        assert private()

    assert external()
    assert external_alt()
