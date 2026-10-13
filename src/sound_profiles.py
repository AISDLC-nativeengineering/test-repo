class SoundProfile:
    def __init__(self, id, bass, treble, audio_balance):
        self.id = id
        self.bass = bass
        self.treble = treble
        self.audio_balance = audio_balance


def create_sound_profile(profile_data):
    # Example implementation of saving profile
    profile = SoundProfile(
        id=profile_data['id'],
        bass=profile_data['bass'],
        treble=profile_data['treble'],
        audio_balance=profile_data['audio_balance']
    )
    return profile


def list_sound_profiles():
    # Example returning dummy profiles
    return [
        SoundProfile(id="profile1", bass=70, treble=50, audio_balance=60),
        SoundProfile(id="profile2", bass=60, treble=40, audio_balance=70)
    ]


def apply_sound_profile(profile_id):
    # Example mock logic for real-time application
    print(f"Applying sound profile {profile_id} to headphones.")