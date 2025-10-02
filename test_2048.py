import pytest
from _2048 import merge_left, merge_right

left_cases = [
    (
        [[2, 2, None, None], [None, None, None, None], [None, None, None, None], [None, None, None, None]],
        [[4, None, None, None], [None, None, None, None], [None, None, None, None], [None, None, None, None]]
    ),
    (
        [[None, 2, 2, None], [None, None, None, None], [None, None, None, None], [None, None, None, None]],
        [[4, None, None, None], [None, None, None, None], [None, None, None, None], [None, None, None, None]]
    ),
    (
        [[2, 2, 2, 2], [None, None, None, None], [None, None, None, None], [None, None, None, None]],
        [[4, 4, None, None], [None, None, None, None], [None, None, None, None], [None, None, None, None]]
    ),
    (
        [[2, None, 2, 2], [None, None, None, None], [None, None, None, None], [None, None, None, None]],
        [[4, 2, None, None], [None, None, None, None], [None, None, None, None], [None, None, None, None]]
    ),
    (
        [[512, 512, 256, 256], [None, None, None, None], [None, None, None, None], [None, None, None, None]],
        [[1024, 512, None, None], [None, None, None, None], [None, None, None, None], [None, None, None, None]]
    ),
    (
        [[None, None, None, None], [None, None, None, None], [None, None, None, None], [None, None, None, None]],
        [[None, None, None, None], [None, None, None, None], [None, None, None, None], [None, None, None, None]]
    ),
    (
        [[2, None, None, 2], [None, None, None, None], [None, None, None, None], [None, None, None, None]],
        [[4, None, None, None], [None, None, None, None], [None, None, None, None], [None, None, None, None]]
    ),
    (
        [[4, 4, 4, None], [None, None, None, None], [None, None, None, None], [None, None, None, None]],
        [[8, 4, None, None], [None, None, None, None], [None, None, None, None], [None, None, None, None]]
    ),
    (
        [[128, 128, None, 128], [None, None, None, None], [None, None, None, None], [None, None, None, None]],
        [[256, 128, None, None], [None, None, None, None], [None, None, None, None], [None, None, None, None]]
    ),
    (
        [[4, None, 4, 4], [None, None, None, None], [None, None, None, None], [None, None, None, None]],
        [[8, 4, None, None], [None, None, None, None], [None, None, None, None], [None, None, None, None]]
    ),
    (
        [[8, None, None, None], [None, None, None, None], [None, None, None, None], [None, None, None, None]],
        [[8, None, None, None], [None, None, None, None], [None, None, None, None], [None, None, None, None]]
    ),
    (
        [[2, 4, 2, 4], [None, None, None, None], [None, None, None, None], [None, None, None, None]],
        [[2, 4, 2, 4], [None, None, None, None], [None, None, None, None], [None, None, None, None]]
    ),
    (
        [[None, 2, None, 2], [None, None, None, None], [None, None, None, None], [None, None, None, None]],
        [[4, None, None, None], [None, None, None, None], [None, None, None, None], [None, None, None, None]]
    ),
    (
        [[256, None, 256, None], [None, None, None, None], [None, None, None, None], [None, None, None, None]],
        [[512, None, None, None], [None, None, None, None], [None, None, None, None], [None, None, None, None]]
    ),
]

right_cases = [
    (
        [[2, 2, None, None], [None, None, None, None], [None, None, None, None], [None, None, None, None]],
        [[None, None, None, 4], [None, None, None, None], [None, None, None, None], [None, None, None, None]]
    ),
    (
        [[None, 2, 2, None], [None, None, None, None], [None, None, None, None], [None, None, None, None]],
        [[None, None, None, 4], [None, None, None, None], [None, None, None, None], [None, None, None, None]]
    ),
    (
        [[2, 2, 2, 2], [None, None, None, None], [None, None, None, None], [None, None, None, None]],
        [[None, None, 4, 4], [None, None, None, None], [None, None, None, None], [None, None, None, None]]
    ),
    (
        [[2, None, 2, 2], [None, None, None, None], [None, None, None, None], [None, None, None, None]],
        [[None, None, 2, 4], [None, None, None, None], [None, None, None, None], [None, None, None, None]]
    ),
    (
        [[512, 512, 256, 256], [None, None, None, None], [None, None, None, None], [None, None, None, None]],
        [[None, None, 1024, 512], [None, None, None, None], [None, None, None, None], [None, None, None, None]]
    ),
    (
        [[None, None, None, None], [None, None, None, None], [None, None, None, None], [None, None, None, None]],
        [[None, None, None, None], [None, None, None, None], [None, None, None, None], [None, None, None, None]]
    ),
    (
        [[2, None, None, 2], [None, None, None, None], [None, None, None, None], [None, None, None, None]],
        [[None, None, None, 4], [None, None, None, None], [None, None, None, None], [None, None, None, None]]
    ),
    (
        [[4, 4, 4, None], [None, None, None, None], [None, None, None, None], [None, None, None, None]],
        [[None, None, 4, 8], [None, None, None, None], [None, None, None, None], [None, None, None, None]]
    ),
    (
        [[128, 128, None, 128], [None, None, None, None], [None, None, None, None], [None, None, None, None]],
        [[None, None, 128, 256], [None, None, None, None], [None, None, None, None], [None, None, None, None]]
    ),
    (
        [[4, None, 4, 4], [None, None, None, None], [None, None, None, None], [None, None, None, None]],
        [[None, None, 4, 8], [None, None, None, None], [None, None, None, None], [None, None, None, None]]
    ),
    (
        [[8, None, None, None], [None, None, None, None], [None, None, None, None], [None, None, None, None]],
        [[None, None, None, 8], [None, None, None, None], [None, None, None, None], [None, None, None, None]]
    ),
    (
        [[2, 4, 2, 4], [None, None, None, None], [None, None, None, None], [None, None, None, None]],
        [[2, 4, 2, 4], [None, None, None, None], [None, None, None, None], [None, None, None, None]]
    ),
    (
        [[None, 2, None, 2], [None, None, None, None], [None, None, None, None], [None, None, None, None]],
        [[None, None, None, 4], [None, None, None, None], [None, None, None, None], [None, None, None, None]]
    ),
    (
        [[256, None, 256, None], [None, None, None, None], [None, None, None, None], [None, None, None, None]],
        [[None, None, None, 512], [None, None, None, None], [None, None, None, None], [None, None, None, None]]
    ),
]

@pytest.mark.parametrize("board, expected", left_cases)
def test_merge_left(board, expected):
    assert merge_left(board) == expected

@pytest.mark.parametrize("board, expected", right_cases)
def test_merge_right(board, expected):
    assert merge_right(board) == expected
