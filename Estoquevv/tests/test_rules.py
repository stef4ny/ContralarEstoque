from app.domain.rules import is_low_stock


def test_is_low_stock():
    assert is_low_stock({"quantity": 0})
    assert is_low_stock({"quantity": 2}, threshold=2)
    assert not is_low_stock({"quantity": 3}, threshold=2)
