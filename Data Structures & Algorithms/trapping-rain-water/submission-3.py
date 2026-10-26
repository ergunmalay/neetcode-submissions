class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        i = 0
        n = len(height)

        while i < n - 1:
            j = i + 1
            best_j = None

            # Find a right wall
            while j < n:
                if best_j is None or height[j] > height[best_j]:
                    best_j = j

                # Stop if we find a wall >= left wall
                if height[j] >= height[i]:
                    break

                j += 1

            if best_j is None:
                break

            # Calculate water between i and best_j
            total = 0
            water_level = min(height[i], height[best_j])

            for k in range(i + 1, best_j):
                total += water_level - height[k]

            res += total

            # Move left wall to right wall
            i = best_j

        return res