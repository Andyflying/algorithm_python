class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        m,n=len(matrix)-1,0
        while m>=0 and n<len(matrix[0]):
            if matrix[m][n] > target:
                m=m-1
            elif matrix[m][n] < target:
                n=n+1
            else:
                return True
        return False

