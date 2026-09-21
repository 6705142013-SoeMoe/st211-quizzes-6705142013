import pytest


@pytest.mark.smoke
def test_login():
    assert True


@pytest.mark.smoke
def test_register():
    assert True


@pytest.mark.slow
def test_large_data():
    assert True


@pytest.mark.regression
def test_old_feature():
    assert True