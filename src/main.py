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

    # User profile for recommender comparisons
    user_prefs = {
        "favorite_genre": "pop",
        "favorite_mood": "happy",
        "target_energy": 0.8,
        "likes_acoustic": True
    }

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("\nTop Recommendations:\n")
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
