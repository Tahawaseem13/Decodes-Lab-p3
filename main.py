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

print("\n========== Available Categories ==========")
print(df["Category"].unique())


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

    recommendations = recommendations.sort_values(
        by="Score",
        ascending=False
    )

    print(
        recommendations[
            ["Course", "Category", "Score"]
        ]
    )

else:
    print("No recommendations found.")