from src.processing import sort_by_date, filter_by_state


def test_sort_by_date(processing_dict, sort_by_date_result):
    assert sort_by_date(processing_dict) == sort_by_date_result


def test_filter_by_state(processing_dict, filter_by_state_result):
    assert filter_by_state(processing_dict) == filter_by_state_result
