#Leetcode 733. Flood Fill

#similar logic to Number of Islands
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if image == None:
            return None
        
        self.dfs(image,sr,sc,newColor,image[sr][sc])
        
        return image
    
    def dfs(self, image,i,j,newColor,currentColor):
        if i<0 or j<0 or i>=len(image) or j>=len(image[0]):
            return image
        #check visited element
        if image[i][j] == newColor:
            return image
        
        if image[i][j] != currentColor:
            return image
        
        image[i][j] = newColor
        #check all the direction 
        self.dfs(image,i,j-1,newColor,currentColor)
        self.dfs(image,i,j+1,newColor,currentColor)
        self.dfs(image,i-1,j,newColor,currentColor)
        self.dfs(image,i+1,j,newColor,currentColor)