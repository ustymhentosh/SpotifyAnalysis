# Spotify_analysis

> This Python program uses the Spotify Web API to get information about an artist, their top track and available markets.
> 

### Usage:

Run this in your terminal

```powershell
...\Spotify_analysis> python main.py
```

Enter all informational that is required

```powershell
enter your client id >>> 
enter your client secret >>> 
```

Here is an two examples of right input after client id & client secret were given

![Untitled](https://github.com/ustymhentosh/Spotify_analysis/blob/develop/photos/EX_1.png)

![Untitled](https://github.com/ustymhentosh/Spotify_analysis/blob/develop/photos/EX_2.png)

### Functions:

### **`get_token(CLIENT_ID, CLIENT_SECRET)`**

This function retrieves an access token from the Spotify Web API using the client ID and client secret provided. The access token is used in subsequent API requests.

### **`get_artist_id_and_name(search_name, token)`**

This function retrieves the ID and name of the first artist that matches the search query.

### **`get_artist_top_track(artist_id, token, country='', market='')`**

This function retrieves the top track of the specified artist. Optionally, you can specify a country or market to search in.

### **`get_track_markets(track_id, token)`**

This function retrieves the available markets for the specified track.

### **Credits**

This project was created by **[Ustym Hentosh](https://github.com/ustymhentosh)**.