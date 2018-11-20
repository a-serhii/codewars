select people.id, people.name, count(toys.name) as toy_count
from people
join toys on people.id = toys.people_id group by people.id;
