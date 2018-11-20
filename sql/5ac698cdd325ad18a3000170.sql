select name, sum(f.won) as won, sum(f.lost) as lost
from fighters as f 
join winning_moves as w 
on f.move_id = w.id 
where w.move not in ('Hadoken', 'Shouoken', 'Kikoken')
group by f.name 
order by won desc 
limit 6;
