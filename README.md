# PySonic

Create a robust music backend system powered by MySQL database and Python operators, enabling seamless management of artists, albums, songs, playlists, and user interactions with efficient CRUD operations and secure authentication.

## Endpoints

### 1. Authentication

-   **POST /auth/register**: Create a user account.
-   **POST /auth/login**: Login into your account.
-   **GET /auth/logout**: Logout from your account.

### 2. User Info

-   **GET /auth/current-user**: Get user information

### 3. Artist

-   **GET /artists**: Retrieve a list of all artists.
-   **GET /artists/{artist_id}**: Retrieve details of a specific artist.
-   **POST /artists**: Create a new artist.
-   **PATCH /artists/{artist_id}**: Update details of an existing artist.
-   **DELETE /artists/{artist_id}**: Delete an artist.

### 4. Song

-   **GET /songs/all**: Retrieve a list of all songs.
-   **GET /songs/{song_id}**: Retrieve details of a specific song.
-   **POST /songs/create**: Create a new song.
-   **PATCH /songs/{song_id}**: Update details of a specific song (if created by the current user).
-   **DELETE /songs/{song_id}**: Delete a specific song. (if created by the current user).

### 5. Albums

-   **GET /albums/all**: Retrieve a list of all albums.
-   **GET /albums/{album_id}**: Retrieve details of a specific album.
-   **POST /albums/create**: Create a new album.
-   **PATCH /albums/{album_id}**: Update details of a specific album (if created by the current user).
-   **DELETE /albums/{album_id}**: Delete a specific album (if created by the current user).

### 6. Playlist

-   **GET /playlists/all**: Retrieve a list of all playlists (created by the current user).
-   **GET /playlists/{playlist_id}**: Retrieve details of a specific playlist (created by the current user).
-   **POST /playlists**: Create a new playlist.
-   **PATCH /playlists/{playlist_id}**: Update details of an existing playlist.
-   **DELETE /playlists/{playlist_id}**: Delete a playlist.
-   **PATCH /playlists/{playlist_id}/add**: Add a song to a specific playlist (created by the current user)
-   **PATCH /playlists/{playlist_id}/remove**: Remove a song from a specific playlist (created by the current user)

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

-   **Song Table**:

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

## Requests Examples

### 1. Auth
### 2. Artist
### 3. Song
### 4. Album
### 5. Playlist

