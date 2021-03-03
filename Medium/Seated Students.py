#CoderByte medium

#The function SeatingStudents(arr) read the array of integers stored in arr which will be in the 
#following format: [K, r1, r2, r3, ...] where K represents the number of desks in a classroom, 
#and the rest of the integers in the array will be in sorted order and will represent the desks
#that are already occupied. All of the desks will be arranged in 2 columns, 
#where desk #1 is at the top left, desk #2 is at the top right, desk #3 is below #1, desk #4 is below #2, etc. 
#Your program should return the number of ways 2 students can be seated next to each other. 
#This means 1 student is on the left and 1 student on the right, or 1 student is directly above or below the other student.
#[12, 2, 6, 7, 11] answer is 6, below is how the desks are arranged and ones in quotes are occupied in this example. 

#   1 "2"
#   3 4
#   5 "6"
#  "7" 8
#   9 10
# "11" 12



#Solution
class Solution:
    def SeatedStudents(self, arr):
        
        totaldesks = int(arr[0])
        occupied = arr[1:]
        #rows = int(K//2)

        count = 0
        for currentDesk in range(1, totaldesks):
            if (self.isOccupied(currentDesk, occupied, totaldesks)):
                continue

            if currentDesk % 2 != 0:
                sideDesk = currentDesk + 1
                if (not self.isOccupied(sideDesk, occupied, totaldesks)):
                    count +=1
            
            belowDesk = currentDesk +2
            if (not self.isOccupied(belowDesk, occupied, totaldesks)):
                    count +=1
            
        return count


    def isOccupied(self, desk, occupied, totaldesks):
        return desk> totaldesks or desk in occupied

out = Solution()
arr1 = [12, 2, 6, 7, 11]
output1 = out.SeatedStudents(arr1)
print(output1)





