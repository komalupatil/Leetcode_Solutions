#Leetcode 1108. Defanging an IP Address

#Solution1
class Solution:
    def defangIPaddr(self, address: str) -> str:
        if len(address) == 0:
            return address
        newIP = ""
        for i in address:
            if i == '.':
                newIP += '[.]'
            else:
                newIP += i
        return newIP



#Solution2
class Solution:
    def defangIPaddr(self, address: str) -> str:
        if len(address) == 0:
            return address
        return address.replace('.', '[.]')



#Solution3
class Solution:
    def defangIPaddr(self, address: str) -> str:
        if len(address) == 0:
            return address
        return '[.]'.join(address.split('.'))
