from .history import HistoryController
from .library import LibraryController
from .mixer import MixerController
from .playback import PlaybackController
from .playlists import PlaylistsController
from .tracklist import TracklistController

_version_ = '2.0'

_all_ = [
    PlaybackController,
    TracklistController,
    MixerController,
    LibraryController,
    PlaylistsController,
    HistoryController
]

mopidy_eventlist = [
   'track_playback_paused',
   'track_playback_resumed',
   'track_playback_started',
   'track_playback_ended',
   'playback_state_changed',
   'tracklist_changed',
   'playlists_loaded',
   'playlist_changed',
   'playlist_deleted',
   'options_changed',
   'volume_changed',
   'mute_changed',
   'seeked',
   'stream_title_changed',
   'audio_message'  # extra event for gstreamer plugins like spectrum
]