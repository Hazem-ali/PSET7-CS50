select name from people where id in
(
select person_id from stars where movie_id in
(select id from movies where movies.id in
(select movie_id from stars where person_id =
(select id from people where name = "Kevin Bacon")
))
) and name != "Kevin Bacon";