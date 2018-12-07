/*  SQL  */
select
    project,
    commits,
    contributors,
    REGEXP_REPLACE(address, '\d' ,'!', 'g') as address
from
    repositories
;
