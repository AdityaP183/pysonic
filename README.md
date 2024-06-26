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

-   **POST /artists**: Create a new artist.
-   **GET /artists**: Retrieve a list of all artists.
-   **GET /artists/{artist_id}**: Retrieve details of a specific artist.
-   **PATCH /artists/{artist_id}**: Update details of an existing artist.
-   **DELETE /artists/{artist_id}**: Delete an artist.

### 4. Song

-   **POST /songs**: Create a new song.
-   **GET /songs**: Retrieve a list of all songs.
-   **GET /songs/{song_id}**: Retrieve details of a specific song.
-   **PATCH /songs/{song_id}**: Update details of a specific song (if created by the current user).
-   **DELETE /songs/{song_id}**: Delete a specific song. (if created by the current user).

### 5. Albums

-   **POST /albums**: Create a new album.
-   **GET /albums**: Retrieve a list of all albums.
-   **GET /albums/{album_id}**: Retrieve details of a specific album.
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
