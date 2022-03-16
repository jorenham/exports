import pytest

from .spam import ham
from .spam.ham import *


def test_single():
    assert public_all(), ham.__all__
    assert public_export(), ham.__all__

    with pytest.raises(NameError):
        assert private()

    assert external(), ham.__all__
    assert external_alt(), ham.__all__
