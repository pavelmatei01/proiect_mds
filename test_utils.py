import pytest
from utils import clamp, merge_sorted, parse_pair, unique_sorted
from hypothesis import given, assume
from hypothesis import strategies as st

# ==========================================
# 1. TESTE UNITARE SIMPLE (Cum ai făcut la început)
# ==========================================

# --- Teste pentru clamp ---
def test_clamp_inside_range():
    assert clamp(5, 0, 10) == 5

def test_clamp_outside_below():
    assert clamp(-5, 0, 10) == 0

def test_clamp_outside_above():
    assert clamp(15, 0, 10) == 10

def test_clamp_boundaries():
    assert clamp(0, 0, 10) == 0
    assert clamp(10, 0, 10) == 10

def test_clamp_lo_equals_hi():
    assert clamp(5, 5, 5) == 5

# --- Teste pentru merge_sorted ---
def test_merge_sorted_normal():
    assert merge_sorted([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]

def test_merge_sorted_empty():
    assert merge_sorted([], [1, 2]) == [1, 2]
    assert merge_sorted([1, 2], []) == [1, 2]

def test_merge_sorted_duplicates():
    assert merge_sorted([1, 2, 2], [2, 3]) == [1, 2, 2, 2, 3]

# --- Teste pentru parse_pair ---
def test_parse_pair_valid():
    assert parse_pair("10:20") == (10, 20)

def test_parse_pair_no_separator():
    with pytest.raises(ValueError):
        parse_pair("hello")

def test_parse_pair_bad_numbers():
    with pytest.raises(ValueError):
        parse_pair("a:b")

# --- Teste pentru unique_sorted ---
def test_unique_sorted_normal():
    assert unique_sorted([3, 1, 2, 1]) == [1, 2, 3]



# ==========================================
# 2. TESTE BAZATE PE PROPRIETĂȚI (Hypothesis)
# ==========================================

# --- Proprietăți pentru clamp ---
@given(st.integers(), st.integers(), st.integers())
def test_clamp_in_bounds(x, lo, hi):
    assume(lo <= hi) 
    result = clamp(x, lo, hi)
    assert lo <= result <= hi

@given(st.integers(), st.integers(), st.integers())
def test_clamp_idempotence(x, lo, hi):
    assume(lo <= hi)
    first_clamp = clamp(x, lo, hi)
    second_clamp = clamp(first_clamp, lo, hi)
    assert first_clamp == second_clamp

@given(st.lists(st.integers(), min_size=3, max_size=3).map(sorted))
def test_clamp_noop(sorted_numbers):
    lo = sorted_numbers[0]
    x = sorted_numbers[1]
    hi = sorted_numbers[2]
    assert clamp(x, lo, hi) == x

# --- Proprietăți pentru merge_sorted ---
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