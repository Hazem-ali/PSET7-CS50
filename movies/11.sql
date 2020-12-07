select title from movies join ratings where id = ratings.movie_id and id in
(select movie_id from stars where person_id = (select id from people where name = "Chadwick Boseman"))
order by rating desc limit 5;