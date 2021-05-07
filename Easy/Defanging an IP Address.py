#Leetcode 1108. Defanging an IP Address

class Solution1:
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


class Solution2:
    def defangIPaddr(self, address: str) -> str:
        if len(address) == 0:
            return address
        return address.replace('.', '[.]')


class Solution3:
    def defangIPaddr(self, address: str) -> str:
        if len(address) == 0:
            return address
        return '[.]'.join(address.split('.'))
