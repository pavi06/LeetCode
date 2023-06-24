class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        top=0
        left=0
        right=len(matrix[0])
        bottom=len(matrix)
        res=[]
        while left<right and top<bottom:
            #to iterate the first row
            for i in range(left,right):
                res.append(matrix[top][i])
            top+=1
            #to iterate the last column
            for i in range(top,bottom):
                res.append(matrix[i][right-1])
            right-=1
            if not (left<right and top<bottom):
                break
            #to iterate the bottom row
            for i in range(right-1,left-1,-1):
                res.append(matrix[bottom-1][i])
            bottom-=1
            #to iterate the first column
            for i in range(bottom-1,top-1,-1):
                res.append(matrix[i][left])
            left+=1
        return res
            
        