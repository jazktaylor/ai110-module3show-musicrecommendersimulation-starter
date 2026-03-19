"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""
from .recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv")
    print(f"Loaded songs: {len(songs)}")

    # User profiles for testing
    user_profiles = [
        {
            "name": "Standard Happy Pop",
            "prefs": {
                "favorite_genre": "pop",
                "favorite_mood": "happy",
                "target_energy": 0.8,
                "likes_acoustic": True
            }
        },
        {
            "name": "Conflicting High Energy Sad",
            "prefs": {
                "favorite_genre": "rock",
                "favorite_mood": "sad",
                "target_energy": 0.9,
                "likes_acoustic": False
            }
        },
        {
            "name": "Extreme Acoustic Classical",
            "prefs": {
                "favorite_genre": "classical",
                "favorite_mood": "uplifting",
                "target_energy": 0.2,
                "likes_acoustic": True
            }
        },
        {
            "name": "Genre Mismatch Happy Metal",
            "prefs": {
                "favorite_genre": "metal",
                "favorite_mood": "happy",
                "target_energy": 0.8,
                "likes_acoustic": False
            }
        }
    ]

    for profile in user_profiles:
        print(f"\n=== Recommendations for: {profile['name']} ===\n")
        recommendations = recommend_songs(profile["prefs"], songs, k=5)
        for idx, rec in enumerate(recommendations, 1):
            song, score, explanation = rec
            print(f"{idx}. {song['title']}")
            print(f"   Score      : {score:.2f}")
            print(f"   Reasons    :")
            for reason in explanation.split('\n'):
                print(f"      - {reason.strip()}")
            print("-" * 40)


if __name__ == "__main__":
    main()
