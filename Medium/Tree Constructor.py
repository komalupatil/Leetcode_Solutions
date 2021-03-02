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

            if len(parents[parent]) > 2:
                return False
            
            if child in children.keys():
                return False
            else:
                children[child] = parent
            
        return True

out = Solution()
strArr1 = ["(1,2)", "(2,4)", "(5,7)", "(7,2)", "(9,5)"]
strArr2 = ["(1,2)", "(3,2)", "(2,12)", "(5,2)"]

out1 = out.TreeConstructor(strArr1)
print(out1)
out2 = out.TreeConstructor(strArr2)
print(out2)