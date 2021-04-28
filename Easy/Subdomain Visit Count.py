#Leetcode 811. Subdomain Visit Count

class Solution1:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        d = {}
        
        for domain in cpdomains:
            domain = domain.split()
            if domain[1] in d:
                d[domain[1]] += int(domain[0])
            else:
                d[domain[1]] = int(domain[0])
            if domain[1].count('.') > 1:
                domain_new = domain[1].split('.')
                if domain_new[-1] in d:
                    d[domain_new[-1]] += int(domain[0])
                else:
                    d[domain_new[-1]] = int(domain[0])
                domain_new.pop(0)
                domain_new = ".".join(domain_new)
                if domain_new in d:
                    d[domain_new] += int(domain[0])
                else:
                    d[domain_new] = int(domain[0])
            else:
                new_domain = domain[1].split(".")
                if new_domain[1] in d:
                    d[new_domain[1]] += int(domain[0])
                else:
                    d[new_domain[1]] = int(domain[0])
        result = []
        string = ""
        for key, val in d.items():
            string += str(val)
            string += " "
            string += key
            result.append(string)
            string = ""
        return result

class Solution2:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        ans = collections.Counter()
        for domain in cpdomains:
            count, domain = domain.split()
            ans[domain] += int(count)
            
            for i in range(len(domain)):
                if domain[i] == '.':
                    ans[domain[i+1:]] += int(count)
        return ["{} {}".format(cnt, dom) for dom, cnt in ans.items()]