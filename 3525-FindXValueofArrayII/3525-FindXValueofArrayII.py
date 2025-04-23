# Last updated: 4/23/2025, 5:42:29 PM
class Solution:
    def resultArray(self, nums: list[int], k: int, queries: list[list[int]]) -> list[int]:
        n = len(nums)

        # Find next power of 2 for segment tree size
        size = 1
        while size < n:
            size *= 2

        # Identity node: (product_mod_k, count_of_remainders)
        identity_node = (1, [0] * k)

        # Initialize the segment tree with identity nodes
        tree = [identity_node for _ in range(2 * size)]

        # Fill the leaves of the tree with values from nums
        for i in range(n):
            rem = nums[i] % k  # remainder of nums[i] % k
            remainder_count = [0] * k
            remainder_count[rem] = 1
            tree[size + i] = (rem, remainder_count)

        # Fill the rest of the leaves with identity nodes
        for i in range(n, size):
            tree[size + i] = identity_node

        # Combine two nodes for segment tree (merge function)
        def combine(left_node, right_node):
            left_prod, left_count = left_node
            right_prod, right_count = right_node

            # Combined product modulo k
            combined_prod = (left_prod * right_prod) % k

            # Combine remainder counts
            combined_count = [0] * k
            for r in range(k):
                combined_count[r] += left_count[r]
            for r in range(k):
                new_r = (left_prod * r) % k
                combined_count[new_r] += right_count[r]

            return (combined_prod, combined_count)

        # Build the segment tree from leaves to root
        for i in range(size - 1, 0, -1):
            tree[i] = combine(tree[2 * i], tree[2 * i + 1])

        results = []

        # Process each query
        for index, new_val, start, target_rem in queries:
            # Step 1: Update nums[index] to new_val
            new_rem = new_val % k
            new_count = [0] * k
            new_count[new_rem] = 1
            tree_index = size + index
            tree[tree_index] = (new_rem, new_count)

            # Rebuild the affected part of the tree (bottom-up)
            tree_index //= 2
            while tree_index:
                tree[tree_index] = combine(tree[2 * tree_index], tree[2 * tree_index + 1])
                tree_index //= 2

            # Step 2: Query the range [start, n) to get the product and remainder counts
            left = start + size
            right = n + size
            left_result = identity_node
            right_result = identity_node

            while left < right:
                if left % 2 == 1:
                    left_result = combine(left_result, tree[left])
                    left += 1
                if right % 2 == 1:
                    right -= 1
                    right_result = combine(tree[right], right_result)
                left //= 2
                right //= 2

            # Final combined node contains the result of the range
            final_node = combine(left_result, right_result)

            # Get count of suffixes with product % k == target_rem
            results.append(final_node[1][target_rem])

        return results