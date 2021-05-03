#Leetcode 1507. Reformat Date

class Solution1:
    def reformatDate(self, date: str) -> str:
        d = {'Jan':'01', 'Feb':'02', 'Mar':'03', 'Apr':'04', 'May':'05', 'Jun':'06', 'Jul':'07', 'Aug':'08', 'Sep':'09', 'Oct':'10', 'Nov':'11', 'Dec':'12'}
        result = []
        date = date.split()
        result.append(date.pop())
        result.append(str(d[date.pop()]))
        day = ""
        for i in range(len(date[0])):
            if date[0][i].isdigit():
                continue
            if len(date[0][:i]) == 1:
                result.append('0' + date[0][:i])
            else:
                result.append(date[0][:i])
            break
        return '-'.join(result)


class Solution2:
    def reformatDate(self, date: str) -> str:
        months = {'Jan':'01', 'Feb':'02', 'Mar':'03', 'Apr':'04', 'May':'05', 'Jun':'06', 'Jul':'07', 'Aug':'08', 'Sep':'09', 'Oct':'10', 'Nov':'11', 'Dec':'12'}
        date_out = ""
        day, month, year = date.split()
        day = '0' + day[0] if len(day) == 3 else day[:2]
        date_out = year + '-' + months[month] + '-' + day
        return date_out