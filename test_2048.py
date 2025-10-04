import pytest
import json
from _2048 import merge_left, merge_right, merge_up, merge_down

def load_test_files(filepath):
    with open(filepath, 'r') as file:
        data = json.load(file)
    
    test_cases = []

    for item in data:
        test_cases.append((item['input'], item['expected']))
    
    return test_cases

merge_left_cases = load_test_files('tests/merge_left.txt')
merge_right_cases = load_test_files('tests/merge_right.txt')
merge_up_cases = load_test_files('tests/merge_up.txt')
merge_down_cases = load_test_files('tests/merge_down.txt')

@pytest.mark.parametrize("input, output", merge_left_cases)
def test_merge_left(input, output):
    assert merge_left(input, mock=True) == output

@pytest.mark.parametrize("input, output", merge_right_cases)
def test_merge_right(input, output):
    assert merge_right(input, mock=True) == output

@pytest.mark.parametrize("input, output", merge_up_cases)
def test_merge_up(input, output):
    assert merge_up(input, mock=True) == output

@pytest.mark.parametrize("input, output", merge_down_cases)
def test_merge_down(input, output):
    assert merge_down(input, mock=True) == output
