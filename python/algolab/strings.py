"""String algorithms."""


def longest_common_subsequence_length(left: str, right: str) -> int:
    """Return the LCS length over Unicode code points. O(mn) time, O(min(m, n)) space."""
    if len(left) < len(right):
        left, right = right, left
    if not right:
        return 0

    lengths = [0] * (len(right) + 1)
    for left_char in left:
        diagonal = 0
        for column, right_char in enumerate(right, start=1):
            above = lengths[column]
            if left_char == right_char:
                lengths[column] = diagonal + 1
            else:
                lengths[column] = max(above, lengths[column - 1])
            diagonal = above
    return lengths[-1]
