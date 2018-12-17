SELECT
    count(name) as unique_products,
    producer
FROM
    products
group by producer
order by unique_products DESC, producer
;
