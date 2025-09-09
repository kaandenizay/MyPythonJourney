CREATE TABLE songs (_id INTEGER PRIMARY KEY, track INTEGER, title TEXT NOT NULL, album INTEGER);
CREATE TABLE albums (_id INTEGER PRIMARY KEY, name TEXT NOT NULL, artist INTEGER);
CREATE TABLE artists (_id INTEGER PRIMARY KEY, name TEXT NOT NULL);

SELECT songs.track, songs.title, albums.name FROM songs
JOIN albums ON songs.album = albums._id
WHERE albums.name = "Forbidden"
ORDER BY songs.track;

SELECT artists.name, albums.name, songs.track, songs.title FROM songs
JOIN albums ON songs.album = albums._id
JOIN artists ON albums.artist = artists._id
WHERE artists.name = "Deep Purple";

SELECT * FROM artists
WHERE artists.name = "Mehitabel";

UPDATE artists SET name = "One Kitten"
WHERE artists.name = "Mehitabel";

SELECT songs.title FROM songs
JOIN albums ON songs.album = albums._id
JOIN artists ON albums.artist = artists._id
WHERE artists.name = "Aerosmith"
ORDER BY songs.title;

SELECT count(*) FROM songs
JOIN albums ON songs.album = albums._id
JOIN artists ON albums.artist = artists._id
WHERE artists.name = "Aerosmith";

SELECT count(DISTINCT songs.title ) FROM songs
JOIN albums ON songs.album = albums._id
JOIN artists ON albums.artist = artists._id
WHERE artists.name = "Aerosmith";