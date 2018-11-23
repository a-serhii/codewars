select age as age, count(name) as total_people 
from people 
group by age 
having count(name) > 9;
