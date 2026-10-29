"""Array algorithms."""

def two_sum(nums: list[int], target: int) -> tuple[int, int] | None:
    """Return distinct indices summing to target, or None. O(n) time/space."""
    seen: dict[int, int] = {}
    for index, value in enumerate(nums):
        complement = target - value
        if complement in seen:
            return seen[complement], index
        seen[value] = index
    return None


def maximum_subarray(nums: list[int]) -> int:
    """Return maximum nonempty contiguous sum. O(n) time, O(1) space."""
    if not nums:
        raise ValueError("maximum_subarray requires a nonempty sequence")
    best = current = nums[0]
    for value in nums[1:]:
        current = max(value, current + value)
        best = max(best, current)
    return best
