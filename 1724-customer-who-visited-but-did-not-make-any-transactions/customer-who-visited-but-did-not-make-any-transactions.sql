/* Write your T-SQL query statement below */
-- select v.customer_id, count(*) AS count_no_trans
-- from visits v
-- left join transactions t
-- on v.visit_id = t.visit_id
-- where transaction_id is null
-- group by customer_id;

select v.customer_id, count(*) AS count_no_trans
from visits v
left join transactions t
on v.visit_id = t.visit_id
where v.visit_id not in
(
    select distinct visit_id from transactions
)
group by customer_id;