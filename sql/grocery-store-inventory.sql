select id, name, stock from products
where producent like 'CompanyA' and stock <= 2
order by id
;
