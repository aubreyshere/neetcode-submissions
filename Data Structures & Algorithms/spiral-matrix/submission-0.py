class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        up = 0
        down = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1
        answer = []

        while down >= up and left <= right: 
            for i in range(left, right + 1):
                answer.append(matrix[up][i])
            up += 1
            for i in range(up, down + 1):
                answer.append(matrix[i][right])
            right -= 1

            if up <= down:
                for i in range(right, left - 1, -1):
                    answer.append(matrix[down][i])
                down -= 1
            if left <= right:
                for i in range(down, up - 1, -1):
                    answer.append(matrix[i][left])
                left += 1

        return answer