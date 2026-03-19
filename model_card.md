# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  
SimilarSongs 1.0

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

    SimilarSongs 1.0 is designed to recommend songs that closely match the user's music preferences based on genre, mood, energy, and acousticness. It is intended for real users.


---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

    The model looks at several features of each song. It compares them to what the user says they like. For example, their favorite genre or mood, how energetic they want their music, and whether they prefer acoustic songs. Each song gets points for matching the user's preferences. The model then adds up these points to decide which songs are the best fit. I kept the basic scoring logic and tested with unusual user profiles to see how the system responds.


---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

    The dataset contains 19 songs, each with information about genre, mood, energy, and other musical features. 
    
    Genres like pop, rock, lofi, jazz, classical, reggae, blues, folk, metal, hip hop, country, world, synthwave, indie pop, and electronic are represented. 
    
    Moods include happy, chill, intense, relaxed, moody, focused, uplifting, mellow, melancholic, romantic, dark, playful, adventurous, spiritual, and energetic. 
    
    I added 10 songs to the starter data, but experimental niche genres, are missing from the dataset.


---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

    The system works well for users with common preferences, such as those who like popular genres and moods like pop and happy. It reliably recommends songs that match these preferences, and the top results usually make sense for these users. In most cases involving the pop genre, the recommendations mtched my intuition.


---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

    One weakness of my system is the reliance on strict matching for mood, genre, and energy preferences. Users with extremely drastic preferences may receive poor recommendations if the dataset lacks songs that fit their criteria. This can create filter bubbles and limit diversity in recommendations, especially for edge case profiles.

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

    I tested several user profiles including standard preferences and edge cases to check if the recommender behaved as expected. I looked for whether the top recommendations matched the user's stated preferences and if any unexpected songs appeared. I was surprised that sometimes the same songs appeared for very different profiles. Simple tests showed that the system strongly favors mood and genre matches, but can overlook diversity and nuanced tastes.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

    To improve the model, I would add more user preferences and consider negative preferences (songs or genres users dislike). I would also work on making the explanations clearer and more personalized, so users understand why a song was recommended. Improving diversity among the top results is important, so I would adjust the scoring to avoid recommending the same songs for different profiles. Finally, I would explore ways to handle more complex and nuanced user tastes, like combining multiple moods or genres.


---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps

    Working on this project taught me how recommender systems use simple rules to match users with content, and how even basic scoring can create patterns and biases. I was surprised to see how much the dataset and scoring weights affect the results. This project made me reflect on my personal critiques on music app recommendation after working on my own.

   The biggest thing I learned from this project was how simple algorithms can create recommendations that feel personalized and how specific they must be. Using AI tools helped me brainstorm ideas, debug code, and write explanations faster, but I learned to double-check their suggestions, especially for edge cases and when interpreting results. I was surprised by how much the scoring logic and dataset directly affect the user experience. If I extended this project, I would experiment with focus on making recommendations more diverse and adaptive. My main goal with the algorithm would be to recommend songs that align with the user's preferences while widening their horions. 
