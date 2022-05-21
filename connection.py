import os
from typing import Optional
from urllib import parse

import numpy as np
import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

auth_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(auth_manager=auth_manager)


def get_track_id(artist_name: str, track_name: str) -> Optional[str]:
    """Get ID of a Spotify track

    Args:
        artist_name (str): Name of the artist.
        track_name (str): Name of the track.

    Returns:
        Optional[str]: The track's id. If not found returns None.
    """
    response = sp.search(
        q=f'artist:{artist_name} track:{track_name}',
        type='track',
        limit=1
    )
    try:
        return response["tracks"]["items"][0]["id"]
    except IndexError:
        return None
        
