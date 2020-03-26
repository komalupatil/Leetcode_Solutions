#leetcode 929. Unique Email Addresses

#Solution (using split, join and replace function and set)


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        result = set()
        for email in emails:
            email_split = email.split("@")
            local_name = email_split[0]
            new_local_name = local_name.split("+")
            new_local_name = new_local_name[0].replace(".", "")
            result.add(new_local_name + "@" + email_split[1] )
        return len(result)
