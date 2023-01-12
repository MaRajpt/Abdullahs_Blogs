
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
SPOTIPY_CLIENT_ID ="48984c01bd0540a9ad9ca60d0c178814"
SPOTIPY_CLIENT_SECRET = "53819986356442a8bc38a2fc16610ac0"

songs_list = []

with open("top_10_songs.txt") as file:
    songs = file.readlines()
    for i in songs:
        songs_list.append(i.strip())

auth_manager = SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,client_secret=SPOTIPY_CLIENT_SECRET,)
sp = spotipy.Spotify(auth_manager=auth_manager)


track = sp.search( q=f"track:{'Save The Best For Last'} year:{1992}",type='track')


print(track['tracks']['items'][-1]['uri'])

results = sp.current_user()

print(results)
# user_id = results['id']

# playlist = sp.user_playlist_create(user=SPOTIPY_CLIENT_ID, name="Century", collaborative=False, description='Old memories songs')


# playlists = sp.user_playlists('spotify')
# while playlists:
#     for i, playlist in enumerate(playlists['items']):
#         print("%4d %s %s" % (i + 1 + playlists['offset'], playlist['uri'],  playlist['name']))
#     if playlists['next']:
#         playlists = sp.next(playlists)
#     else:
#         playlists = None
# print(playlists)