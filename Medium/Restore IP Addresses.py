#Leetcode 93. Restore IP Addresses

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        def valid(segment):
            return int(segment) <= 255 if segment[0] != '0' else len(segment) == 1
            
        def update_output(curr_pos):
            """
            Append the current list of segments 
            to the list of solutions
            """
            segment = s[curr_pos + 1:n]
            if valid(segment):
                segments.append(segment)
                output.append('.'.join(segments))
                segments.pop()    
            
        def backtrack(prev_pos = -1, dots = 3):
            """
            prev_pos : the position of the previously placed dot
            dots : number of dots to place
            """
            # The current dot curr_pos could be placed 
            # in a range from prev_pos + 1 to prev_pos + 4.
            # The dot couldn't be placed 
            # after the last character in the string.
            for curr_pos in range(prev_pos + 1, min(n - 1, prev_pos + 4)):
                segment = s[prev_pos + 1:curr_pos + 1]
                if valid(segment):
                    segments.append(segment)  # place dot
                    if dots - 1 == 0:  # if all 3 dots are placed
                        update_output(curr_pos)  # add the solution to output
                    else:
                        backtrack(curr_pos, dots - 1)  # continue to place dots
                    segments.pop()  # remove the last placed dot
        
        n = len(s)
        output, segments = [], []
        backtrack() 
        return output