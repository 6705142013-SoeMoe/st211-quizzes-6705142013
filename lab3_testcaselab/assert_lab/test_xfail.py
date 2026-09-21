import pytest

@pytest.mark.xfail(reason="Known bug #123, fix pending")
def test_known_broken_feature():
    assert 1==2

@pytest.mark.xfail(reason="Might pass sometimes")  # This test is expected to fail due to a known bug
def test_actually_wroks_now():
    assert 1==1