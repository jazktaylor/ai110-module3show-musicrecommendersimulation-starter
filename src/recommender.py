from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        """Return top k recommended Song objects for a user."""
        # Score each song and sort
        scored = [
            (song, self.score_song(user, song))
            for song in self.songs
        ]
        scored.sort(key=lambda x: x[1][0], reverse=True)  # sort by score
        # Return top k songs
        return [song for song, _ in scored[:k]]

    def score_song(self, user: UserProfile, song: Song) -> Tuple[float, List[str]]:
        """Score a Song for a UserProfile and return score and reasons."""
        score = 0.0
        reasons = []
        # Genre
        if song.genre == user.favorite_genre:
            score += 1.0
            reasons.append("genre match (+1.0)")
        # Mood
        if song.mood == user.favorite_mood:
            score += 2.0
            reasons.append("mood match (+2.0)")
        # Energy
        score_energy = 1.0 - abs(song.energy - user.target_energy)
        score += score_energy
        reasons.append(f"energy closeness (+{score_energy:.2f})")
        # Acousticness
        if user.likes_acoustic:
            score += song.acousticness
            reasons.append(f"acousticness (+{song.acousticness:.2f})")
        else:
            score += (1.0 - song.acousticness)
            reasons.append(f"not acoustic (+{1.0 - song.acousticness:.2f})")
        return score, reasons

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        """Return explanation string for a recommended Song."""
        _, reasons = self.score_song(user, song)
        return "\n".join(reasons)

def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    import csv
    songs = []
    with open(csv_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Convert numeric fields to appropriate types
            row['id'] = int(row['id'])
            row['energy'] = float(row['energy'])
            row['tempo_bpm'] = float(row['tempo_bpm'])
            row['valence'] = float(row['valence'])
            row['danceability'] = float(row['danceability'])
            row['acousticness'] = float(row['acousticness'])
            songs.append(row)
    return songs

def score_song(user_prefs: Dict, song: Dict) -> float:
    """Score a song dict for user_prefs and return score and reasons."""
    """
    Scores a song based on user preferences.
    Returns (score, reasons) for transparency.
    """
    score = 0.0
    reasons = []
    # Categorical matches
    if song['genre'] == user_prefs.get('favorite_genre'):
        score += 1.0
        reasons.append(f"genre match (+1.0)")
    if song['mood'] == user_prefs.get('favorite_mood'):
        score += 2.0
        reasons.append(f"mood match (+2.0)")

    # Numerical features
    # Energy
    if 'target_energy' in user_prefs:
        energy_score = 1.0 - abs(song['energy'] - user_prefs['target_energy'])
        score += energy_score
        reasons.append(f"energy closeness (+{energy_score:.2f})")
    # Example: acousticness preference
    if 'likes_acoustic' in user_prefs:
        if user_prefs['likes_acoustic']:
            score += song['acousticness']
            reasons.append(f"acousticness (+{song['acousticness']:.2f})")
        else:
            score += (1.0 - song['acousticness'])
            reasons.append(f"not acoustic (+{1.0 - song['acousticness']:.2f})")
    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Return top k recommended song dicts for user_prefs."""
    """
    Functional implementation of the recommendation logic.
    Required by src/main.py
    """
    # Score every song and collect explanations
    results = [
        (song, score, ", ".join(reasons))
        for song in songs
        for score, reasons in [score_song(user_prefs, song)]
    ]
    # Sort by score descending
    results = sorted(results, key=lambda x: x[1], reverse=True)
    # Return top k
    return results[:k]
