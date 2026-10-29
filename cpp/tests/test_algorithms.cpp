#include "algorithms.hpp"
#include <cassert>
#include <climits>
#include <vector>
int main() {
    using namespace algolab;
    assert((two_sum({2, 7, 11, 15}, 9) == std::make_optional(std::pair<std::size_t, std::size_t>{0, 1})));
    assert((two_sum({3, 3}, 6).has_value()));
    assert(!two_sum({1, 2}, 8).has_value());
    assert((two_sum({INT_MIN, INT_MAX}, -1).has_value()));
    assert(maximum_subarray({-2, 1, -3, 4, -1, 2, 1, -5, 4}) == 6);
    assert(maximum_subarray({-5, -1, -9}) == -1);
    bool threw = false;
    try { (void)maximum_subarray({}); } catch (const std::invalid_argument&) { threw = true; }
    assert(threw);
    assert(lower_bound_index({1, 2, 2, 4}, 2) == 1);
    assert(lower_bound_index({}, 2) == 0);
}
