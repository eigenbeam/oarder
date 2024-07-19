def create_order():
    return "1234"


def test_order():
    order_id = create_order()
    assert len(order_id) > 0
