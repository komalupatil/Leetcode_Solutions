--Leetcode 183. Customers Who Never Order 

select name as customers
from Customers left join Orders on Customers.id = Orders.customerId
where customerId is null