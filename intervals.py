def merge_intervals(intervals):
    """Merge overlapping or adjacent intervals.
    merge_intervals([(1, 3), (2, 5), (8, 10)]) -> [(1, 5), (8, 10)]
    merge_intervals([(1, 5), (2, 3)])           -> [(1, 5)]
    Each interval is (start, end) with start <= end.
    """
    # Dacă lista e goală, returnăm o listă goală
    if not intervals:
        return []

    # 1. Sortăm intervalele crescător, în funcție de punctul de început
    sorted_intervals = sorted(intervals, key=lambda x: x[0])

    # 2. Punem primul interval în lista finală
    merged = [sorted_intervals[0]]

    # 3. Parcurgem restul intervalelor
    for current in sorted_intervals[1:]:
        # Ne uităm la ultimul interval pe care l-am adăugat în lista finală
        last_merged = merged[-1]

        # Dacă începutul intervalului curent este mai mic sau egal cu finalul ultimului interval adăugat...
        # înseamnă că se suprapun!
        if current[0] <= last_merged[1]:
            # Le unim: actualizăm finalul intervalului vechi cu valoarea cea mai mare
            merged[-1] = (last_merged[0], max(last_merged[1], current[1]))
        else:
            # Nu se suprapun, așa că îl adăugăm pur și simplu ca pe un interval nou
            merged.append(current)

    return merged
