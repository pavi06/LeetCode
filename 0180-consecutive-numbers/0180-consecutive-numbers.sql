# Write your MySQL query statement below
# self join concept,----their id shld be increasing..=> id-1
select distinct a.num ConsecutiveNums from 
logs a inner join logs b
on a.id = b.id-1
inner join logs c
on b.id = c.id-1
where a.num = b.num and b.num = c.num
