select title, rating from movies join ratings where movies.id =
ratings.movie_id and year = 2010 order by rating desc, title;