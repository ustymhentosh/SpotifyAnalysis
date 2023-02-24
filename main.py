import json
import base64
import requests


def get_token(CLIENT_ID, CLIENT_SECRET):

    auth_code = f'{CLIENT_ID}:{CLIENT_SECRET}'

    coded_credentials = base64.b64encode(auth_code.encode()).decode()

    auth_url = 'https://accounts.spotify.com/api/token'

    auth_data = {'grant_type': 'client_credentials'}

    auth_headers = {'Authorization': f'Basic {coded_credentials}'}

    response = requests.post(auth_url, data = auth_data, headers=auth_headers)

    access_token = response.json().get('access_token')

    return access_token



def get_artist_id_and_name(search_name, token):
    """ Gets artist id """
    # searching input
    search_url = 'https://api.spotify.com/v1/search'
    request_params = {'query': search_name, 'type': 'artist'}
    request_headers = {'Authorization': f'Bearer {token}'}
    response = requests.get(search_url, params=request_params, headers=request_headers)
    response = response.json()["artists"]['items'][0]
    return response['name'], response['id']


def get_artist_top_track(artist_id, token, country = '', market = ''):
    """ gets artist's top track """
    request_params = {'market': 'US'}
    if country:
        request_params['country'] = country
    if market:
        request_params['market'] = market
    
    request_headers = {'Authorization': f'Bearer {token}'}

    search_url = f'https://api.spotify.com/v1/artists/{artist_id}/top-tracks'
    response = requests.get(search_url, params=request_params, headers=request_headers)

    return response.json()['tracks'][0]['name'], response.json()['tracks'][0]['id']


def get_track_markets(track_id, token):
    """ gets track markets """
    search_url = f'https://api.spotify.com/v1/tracks/{track_id}'
    request_headers = {'Authorization': f'Bearer {token}'}
    response = requests.get(search_url, headers=request_headers)
    return response.json()['album']['available_markets']



if __name__ == '__main__':
    client_id = input("enter your client id >>> ")
    client_secret = input("enter your client secret >>> ")

    search_artist = input('\nWrite artist you want to seach here >>> ')
    specific_market = input('\nDefult market is UA\nWrite specifc \
market if you want(if not -> click enter) here >>> ')
    specific_country = input('\nWrite specific country if \
you want(if not -> click enter) here >>> ')

    to_show = input('\nFrom oprions (artist_id, artist_name, top_track_name, top_track_id, track_markets)\n\
 write what you want to see, separated by | (no spaces) here >>> ')

    try:
        token = get_token(client_id, client_secret)
        artist_id = get_artist_id_and_name(search_artist, token)[1]
        artist_name = get_artist_id_and_name(search_artist, token)[0]
        track_id = get_artist_top_track(artist_id, token,\
            specific_country, specific_market)[1]
        track_name = get_artist_top_track(artist_id, token)[0]
        track_markets = get_track_markets(track_id, token)

        dct = {'artist_id': artist_id , 'artist_name': artist_name,\
            'top_track_name': track_name, 'top_track_id': track_id, 'track_markets': track_markets}

        for i in to_show.split('|'):
            print(f'\n{i.replace("_", " ")} is {dct[i]}')
    except:
        print('Something went wrong, maybe check CLIENT_ID/SECTER')


   
