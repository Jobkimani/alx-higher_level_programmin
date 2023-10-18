SQL - Additional Queries
In this project, I continued to practice SQL queries, focusing on permissions, joins, and constraints.

Usage 🐬
Execute the script 3-force_name.sql to direct the database for querying. Provide the database to query from as a MySQL command line argument:

shell
Copy code
$ cat 3-force_name.sql | mysql -hlocalhost -uroot -p hbtn_0d_2
Execute Tasks 10-101 by querying the database using hbtn_0d_tvshows.sql.

Execute Tasks 102-103 by querying the database using hbtn_0d_tvshows_rate.sql.

Tasks 📃
0. My privileges!

0-privileges.sql: MySQL script listing all privileges for users user_0d_1 and user_0d_2.
1. Root user

1-create_user.sql: MySQL script creating the user user_0d_1 with all privileges and password user_0d_1_pwd.
2. Read user

2-create_read_user.sql: MySQL script creating the database hbtn_0d_2 and user user_0d_2 with password user_0d_2_pwd. user_0d_2 has only SELECT privilege on the database hbtn_0d_2.
3. Always a name

3-force_name.sql: MySQL script creating the force_name table with columns:
id: INT
name: VARCHAR(256) (non-null)
4. ID can't be null

4-never_empty.sql: MySQL script creating the id_not_null table with columns:
id: INT (default value = 1)
name: VARCHAR(256)
5. Unique ID

5-unique_id.sql: MySQL script creating the unique_id table with columns:
id: INT (default value = 1, must be unique)
name: VARCHAR(256)
6. States table

6-states.sql: MySQL script creating the hbtn_0d_usa database with a states table:
id: INT (unique, auto-generated, non-null, primary key)
name: VARCHAR(256) (non-null)
7. Cities table

7-cities.sql: MySQL script creating the hbtn_0d_usa database with a cities table:
id: INT (unique, auto-generated, non-null, primary key)
state_id: INT (non-null, foreign key referencing id in the states table)
name: VARCHAR(256) (non-null)
8. Cities of California

8-cities_of_california_subquery.sql: MySQL script listing all California cities from the hbtn_0d_usa database, ordered by ascending city id.
9. Cities by States

9-cities_by_state_join.sql: MySQL script listing all cities in the hbtn_0d_usa database, ordered by ascending city id.
10. Genre ID by show

10-genre_id_by_show.sql: MySQL script listing shows from hbtn_0d_tvshows with at least one linked genre, ordered by ascending tv_shows.title and tv_show_genres.genre_id.
11. Genre ID for all shows

11-genre_id_all_shows.sql: MySQL script listing all shows from the hbtn_0d_tvshows database, ordered by ascending tv_shows.title and tv_show_genres.genre_id. If a show has no genre, it displays NULL.
12. No genre

12-no_genre.sql: MySQL script listing all shows from hbtn_0d_tvshows without a linked genre, ordered by ascending tv_shows.title and tv_show_genres.genre_id.
13. Number of shows by genre

13-count_shows_by_genre.sql: MySQL script listing all genres from hbtn_0d_tvshows and displaying the number of linked shows for each genre, ordered by descending number of linked shows. Genres with no linked shows are not displayed.
14. My genres

14-my_genres.sql: MySQL script using the hbtn_0d_tvshows database to list all genres of the show "Dexter," ordered by ascending genre name.
15. Only Comedy

15-comedy_only.sql: MySQL script listing all comedy shows in the hbtn_0d_tvshows database, ordered by ascending show title.
16. List shows and genres

16-shows_by_genre.sql: MySQL script listing all shows and linked genres from the hbtn_0d_tvshows database, ordered by ascending show title and genre name.
17. Not my genre

100-not_my_genres.sql: MySQL script using the hbtn_0d_tvshows database to list all genres not linked to the show "Dexter," ordered by ascending genre name.
18. No Comedy tonight!

101-not_a_comedy.sql: MySQL script listing all shows without the comedy genre in the hbtn_0d_tvshows database, ordered by ascending show title.
19. Rotten tomatoes

102-rating_shows.sql: MySQL script listing all shows from hbtn_0d_tvshows_rate ordered by their rating in descending order.
20. Best genre

103-rating_genres.sql: MySQL script listing all genres from the hbtn_0d_tvshows_rate database ordered by their rating in descending order.




