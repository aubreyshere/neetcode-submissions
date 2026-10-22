class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) - 1

        while left <= right:
            mid = left  + (right - left) // 2

            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] > target:
                right = mid - 1
            elif matrix[mid][0] < target and right > mid and matrix[mid + 1][0] > target:
                break            
            else:
                left = mid + 1

        left = 0
        right = len(matrix[0]) - 1

        while left <= right:
            midCol = left + (right - left) // 2

            if matrix[mid][midCol] == target:
                return True
            elif matrix[mid][midCol] > target:
                right = midCol - 1
            else:
                left = midCol + 1

        return False               
        