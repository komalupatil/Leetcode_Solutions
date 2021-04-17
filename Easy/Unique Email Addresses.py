#leetcode 929. Unique Email Addresses

#Solution 


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        result = set()
        for email in emails:
            local, domain = email.split("@")
            if '+' in local:
                local = local.split('+')[0]
            result.add(local.replace('.', '') + "@" + domain)
        return len(result)