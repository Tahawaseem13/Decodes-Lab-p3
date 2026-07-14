import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


courses = [
    {
        "Course": "Python for Beginners",
        "Category": "Programming"
    },
    {
        "Course": "Advanced Python",
        "Category": "Programming"
    },
    {
        "Course": "Machine Learning",
        "Category": "AI"
    },
    {
        "Course": "Deep Learning",
        "Category": "AI"
    },
    {
        "Course": "Web Development",
        "Category": "Web"
    },
    {
        "Course": "Java Programming",
        "Category": "Programming"
    },
    {
        "Course": "Data Science",
        "Category": "AI"
    },
    {
        "Course": "Frontend Development",
        "Category": "Web"
    }
]

# Create DataFrame
df = pd.DataFrame(courses)
df["Content"] = df["Course"] + " " + df["Category"]

print("=" * 50)
print("      AI COURSE RECOMMENDATION SYSTEM")
print("=" * 50)

print(df[["Course", "Category"]])

choice = input("\nEnter your interests (comma separated): ")

interests = [
    interest.strip().lower()
    for interest in choice.split(",")
]

vectorizer = TfidfVectorizer()

tfidf_matrix = vectorizer.fit_transform(df["Content"])

user_vector = vectorizer.transform([choice])

similarity = cosine_similarity(
    user_vector,
    tfidf_matrix
)

recommendations = df[
    df["Category"].str.lower().isin(interests)
].copy()
recommendations["Score"] = similarity.flatten()[
    recommendations.index
] * 100
print("\n========== Top Recommendations ==========")

if len(recommendations) > 0:

    top_recommendations = recommendations.sort_values(
        by="Score",
        ascending=False
    ).head(5)
    top_recommendations["Score"] = top_recommendations["Score"].round(2)
    print(top_recommendations[["Course", "Category", "Score"]])

else:
    print(" No matching courses found.")
    print("\nTry searching with:")
    print("- AI")
    print("- Programming")
    print("- Web")
    print("- Data Science")
    
print("\nThank you for using the AI Recommendation System!")  