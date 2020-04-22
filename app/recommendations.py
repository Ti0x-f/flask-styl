import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

def get_recommendations(search):

    #Init
    sp = spotipy.Spotify(client_credentials_manager = SpotifyClientCredentials())

    #Search: return JSON of the first result
    result = sp.search(q = search, type = 'track', limit = 1)

    #Get ID of the track. Need a list for the recommendation lookup
    id_list = [result['tracks']['items'][0]['id']]

    return sp.recommendations(seed_tracks = id_list, limit = 10)

def get_covers(recommendations):

    #Init
    sp = spotipy.Spotify(client_credentials_manager = SpotifyClientCredentials())

    id_list = [track['id'] for track in recommendations['tracks']]

    tracks = sp.tracks(id_list)

    cover_links = [image['album']['images'][2]['url'] for image in tracks['tracks']]

    return cover_links

def display(recommendations, covers):

    html_display = ''
    for idx, track in enumerate(recommendations['tracks']):

        html_display += f'''
            <tr>
                <td><img src = "{covers[idx]}"></td>
                <td>{track['name']}</td>
                <td>{track['artists'][0]['name']}</td>
                <td><a href = "{track['external_urls']['spotify']}">Play It</a></td>
            </tr>'''

    with open('app/templates/recommendations.html', 'w') as html_file:
        html_file.write(html_display)
