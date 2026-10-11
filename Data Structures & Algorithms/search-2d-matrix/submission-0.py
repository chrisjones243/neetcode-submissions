class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        X, Y = len(matrix), len(matrix[0])
        
        low = 0
        high = X * Y - 1

        while low <= high:
            p = low + (high - low) // 2
            p_x = p // Y
            p_y = p % Y

            if target > matrix[p_x][p_y]:
                low = p + 1
            elif target < matrix[p_x][p_y]:
                high = p - 1
            else:
                return True
        return False
