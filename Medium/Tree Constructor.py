#coderbyte medium
#determine if an array of integer pairs can form a binary tree properly
#There is one root node, and every child node has parent
#Example: Input: ["(1,2)", "(2,4)", "(5,7)", "(7,2)", "(9,5)"]
#                   / \
#                  /   \
#                child  parent
#a = ["(1,2)", "(2,4)", "(5,7)", "(7,2)", "(9,5)"]
#for i in range(len(a)):
#    pair = a[i].split(",")
#    print(pair[0], pair[1])

class Solution:
    def TreeConstructor(self, strArr):
        parents = {}
        children = {}

        for i in range(len(strArr)):
            pair = strArr[i].split(",")
            child = pair[0][1]
            parent = pair[1][0]

            if parent in parents.keys():
                parents[parent].append(child)
            else:
                parents[parent] = [child]

            #check if each parent has at most 2 child nodes
            if len(parents[parent]) > 2:
                return False
            
            if child in children.keys():
                return False
            else:
                children[child] = parent
            
            root_count = 0
            if parent not in children.keys():
                root_count +=1
            else:
                root_count = 0
            if root_count > 1:
                return False

        return True

out = Solution()

strArr1 = ["(1,2)", "(2,4)", "(5,7)", "(7,2)", "(9,5)"]
strArr2 = ["(1,2)", "(3,2)", "(2,12)", "(5,2)"]

output1 = out.TreeConstructor(strArr1)
print(output1)
output2 = out.TreeConstructor(strArr2)
print(output2)