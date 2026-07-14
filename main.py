import pandas as pd


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

print("\n========== Available Categories ==========")
print(df["Category"].unique())


choice = input("\nEnter your interests (comma separated): ")

interests = [
    interest.strip().lower()
    for interest in choice.split(",")
]

recommendations = df[
    df["Category"].str.lower().isin(interests)
].copy()

recommendations["Score"] = 100
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