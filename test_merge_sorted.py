import pytest
from hypothesis import given
from hypothesis import strategies as st
from merge_sorted import merge_sorted

# --- Teste unitare ---
def test_merge_sorted_normal():
    assert merge_sorted([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]

def test_merge_sorted_empty():
    assert merge_sorted([], [1, 2]) == [1, 2]
    assert merge_sorted([1, 2], []) == [1, 2]

def test_merge_sorted_duplicates():
    assert merge_sorted([1, 2, 2], [2, 3]) == [1, 2, 2, 2, 3]

# --- Teste bazate pe proprietăți ---
sorted_lists = st.lists(st.integers()).map(sorted)

@given(sorted_lists, sorted_lists)
def test_merge_sorted_is_sorted(a, b):
    result = merge_sorted(a, b)
    assert result == sorted(result)

@given(sorted_lists, sorted_lists)
def test_merge_sorted_length(a, b):
    result = merge_sorted(a, b)
    assert len(result) == len(a) + len(b)

@given(sorted_lists, sorted_lists)
def test_merge_sorted_permutation(a, b):
    result = merge_sorted(a, b)
    assert sorted(result) == sorted(a + b)
