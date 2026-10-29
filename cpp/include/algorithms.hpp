#pragma once
#include <algorithm>
#include <cstddef>
#include <optional>
#include <stdexcept>
#include <unordered_map>
#include <utility>
#include <vector>

namespace algolab {
inline std::optional<std::pair<std::size_t, std::size_t>> two_sum(const std::vector<int>& nums, int target) {
    std::unordered_map<long long, std::size_t> seen;
    for (std::size_t i = 0; i < nums.size(); ++i) {
        const long long complement = static_cast<long long>(target) - nums[i];
        if (auto it = seen.find(complement); it != seen.end()) return {{it->second, i}};
        seen[nums[i]] = i;
    }
    return std::nullopt;
}
inline long long maximum_subarray(const std::vector<int>& nums) {
    if (nums.empty()) throw std::invalid_argument("nonempty sequence required");
    long long current = nums[0], best = current;
    for (std::size_t i = 1; i < nums.size(); ++i) {
        current = std::max(static_cast<long long>(nums[i]), current + nums[i]);
        best = std::max(best, current);
    }
    return best;
}
inline std::size_t lower_bound_index(const std::vector<int>& nums, int target) {
    return static_cast<std::size_t>(std::lower_bound(nums.begin(), nums.end(), target) - nums.begin());
}
} // namespace algolab
