#leetcode 760. Find Anagram Mappings
#solution1 using simple dictionary approach

class AnagramMappings:
    def mapping(self, A, B):
        val = {}
        result = []
        for i in range(len(B)):
            val[B[i]] = i
        for j in range(len(A)):
            result.append(val[A[j]])   
        return result

obj = AnagramMappings()
A1 = [12, 28, 46, 32, 50]
B1 = [50, 12, 32, 46, 28]
result = obj.mapping(A1, B1)
print(result)


#solution 2 using comprehension


class AnagramMappings:
    def mapping(self, A, B):
        lookup = {val:i for i, val in enumerate(B)}
        return [lookup[val] for val in A]

obj = AnagramMappings()
A1 = [12, 28, 46, 32, 50]
B1 = [50, 12, 32, 46, 28]
result = obj.mapping(A1, B1)
print(result)
            
        
        
