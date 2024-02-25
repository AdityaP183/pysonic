# PySonic

Create a robust music backend system powered by MySQL database and Python operators, enabling seamless management of artists, albums, songs, playlists, and user interactions with efficient CRUD operations and secure authentication.

## Introduction

## Endpoints

### 1. Authentication

-   **POST /register**: Create a user account.
-   **POST /login**: Login into your account.
-   **GET /logout**: Logout from your account.

### 2. User Info

-   **GET /user/info**: Get user information

### 3. Artist

-   **GET /artists**: Retrieve a list of all artists.
-   **GET /artists/{artist_id}**: Retrieve details of a specific artist.
-   **POST /artists**: Create a new artist.
-   **PUT /artists/{artist_id}**: Update details of an existing artist.
-   **DELETE /artists/{artist_id}**: Delete an artist.

### 4. Song

-   **GET /songs**: Retrieve a list of all songs.
-   **GET /songs/{song_id}**: Retrieve details of a specific song.
-   **POST /songs**: Create a new song.
-   **PUT /songs/{song_id}**: Update details of an existing song.
-   **DELETE /songs/{song_id}**: Delete a song.

### 5. Albums

-   **GET /albums**: Retrieve a list of all albums.
-   **GET /albums/{album_id}**: Retrieve details of a specific album.
-   **POST /albums**: Create a new album.
-   **PUT /albums/{album_id}**: Update details of an existing album.
-   **DELETE /albums/{album_id}**: Delete an album.

### 6. Playlist

-   **GET /playlists**: Retrieve a list of all playlists.
-   **GET /playlists/{playlist_id}**: Retrieve details of a specific playlist.
-   **POST /playlists**: Create a new playlist.
-   **PUT /playlists/{playlist_id}**: Update details of an existing playlist.
-   **DELETE /playlists/{playlist_id}**: Delete a playlist.

## Database

Database schema about the tables in the database and the columns in the table.

-   **Artists Table**:

    -   ArtistID (Primary Key)
    -   ArtistName
    -   Avatar
    -   CreatedByUserID (Foreign Key referencing Users Table)

-   **Albums Table**:

    -   AlbumID (Primary Key)
    -   AlbumTitle
    -   ArtistID (Foreign Key referencing Artists Table)
    -   ReleaseYear
    -   GenreID (Foreign Key referencing Genres Table)
    -   CreatedByUserID (Foreign Key referencing Users Table)

-   **Tracks Table**:

    -   TrackID (Primary Key)
    -   TrackTitle
    -   AlbumID (Foreign Key referencing Albums Table)
    -   Duration
    -   TrackNumber
    -   CreatedByUserID (Foreign Key referencing Users Table)

-   **Genres Table**:

    -   GenreID (Primary Key)
    -   GenreName

-   **Playlists Table**:

    -   PlaylistID (Primary Key)
    -   PlaylistName
    -   CreatedByUserID (Foreign Key referencing Users Table)

-   **PlaylistTracks Table** (for Many-to-Many relationship between Playlists and Tracks):

    -   PlaylistID (Foreign Key referencing Playlists Table)
    -   TrackID (Foreign Key referencing Tracks Table)
    -   TrackOrder (to maintain the order of tracks within a playlist)

-   **Users Table** (if you want to implement user management and user-specific playlists):

    -   UserID (Primary Key)
    -   Username
    -   Password
    -   Email

-   **UserPlaylists Table** (for Many-to-Many relationship between Users and Playlists):

    -   UserID (Foreign Key referencing Users Table)
    -   PlaylistID (Foreign Key referencing Playlists Table)

-   **UserCreations Table**:

    -   CreationID (Primary Key)
    -   UserID (Foreign Key referencing Users Table)
    -   ItemType (e.g., "Album", "Track", "Playlist")
    -   ItemID (Foreign Key referencing the corresponding table based on ItemType)
    -   CreationDate
