class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        sum = 0
        
        for i in range(len(points) - 1):
            diagonalStep = abs(min(abs(points[i + 1][0] - points[i][0]),
                               abs(points[i + 1][1] - points[i][1])))
            remainingStep = 0
            
            if abs(points[i + 1][0] - points[i][0]) < abs(points[i + 1][1] - points[i][1]):
                remainingStep = abs(points[i + 1][1] - points[i][1]) - diagonalStep
            elif abs(points[i + 1][0] - points[i][0]) > abs(points[i + 1][1] - points[i][1]):
                remainingStep = abs(points[i + 1][0] - points[i][0]) - diagonalStep
            
            sum += remainingStep + diagonalStep
        
        return sum