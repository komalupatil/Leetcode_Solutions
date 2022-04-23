--Leetcode 182. Duplicate Emails

select p1.id, p1.email 
from Person p1 join Person p2 
on p1.email = p2.email
and p1.id < p2.id
