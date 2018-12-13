select senshi_name as sailor_senshi,
    real_name_jpn as real_name,
    cats.name as cat,
    schools.school as school
from sailorsenshi
    left join cats
    on sailorsenshi.cat_id = cats.id
    left join schools
    on school_id = schools.id
;