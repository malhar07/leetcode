/* Write your T-SQL query statement below */
with delivery_pref AS (
    select customer_id,
    order_date,
    customer_pref_delivery_date,
    ROW_NUMBER() OVER(Partition by customer_id order by order_date) as delivery_number
    FROM delivery
)
select Round(sum(case when order_date = customer_pref_delivery_date then 1 else 0 end ) *100.0 /
Count(*), 2) as immediate_percentage
FROM  delivery_pref
where delivery_number = 1;