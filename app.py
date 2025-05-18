import gradio as gr
import pickle
import pandas as pd

# Load the model and scaler
with open("cluster_classifier.sav", "rb") as f:
    clf = pickle.load(f)

with open("scaler.sav", "rb") as f:
    scaler = pickle.load(f)

# Cluster to segment mapping
cluster_map = {
    0: "Young High Spenders",
    1: "Mid-Age Budget Seekers",
    2: "Valuable Loyalists",
    3: "Low-Value Users"
}

# Strategy for each segment
segment_strategies = {
    "Young High Spenders": (
        "Strategy:\n"
        "- Offer exclusive premium deals and early access to new products.\n"
        "- Use influencer marketing and social media campaigns.\n"
        "- Implement loyalty programs with personalized rewards."
    ),
    "Mid-Age Budget Seekers": (
        "Strategy:\n"
        "- Highlight discounts, bundles, and value-for-money offers.\n"
        "- Provide budgeting tools and transparent pricing.\n"
        "- Send targeted emails with seasonal sales and coupons."
    ),
    "Valuable Loyalists": (
        "Strategy:\n"
        "- Engage through personalized communications and VIP events.\n"
        "- Reward long-term loyalty with special perks.\n"
        "- Use feedback surveys to improve their experience."
    ),
    "Low-Value Users": (
        "Strategy:\n"
        "- Focus on engagement campaigns to increase interaction.\n"
        "- Offer entry-level products and trial options.\n"
        "- Educate users with tutorials and customer support."
    )
}

def predict_segment(age, income, rating, gender):
    sex = 1 if gender == "Female" else 0
    income_per_age = income / age if age != 0 else 0
    behavior_score = income * rating

    input_df = pd.DataFrame([{
        "Age": age,
        "Income": income,
        "Rating": rating,
        "Income_per_Age": income_per_age,
        "Behavior_Score": behavior_score
    }])

    scaled_features = scaler.transform(input_df)
    cluster = clf.predict(scaled_features)[0]
    segment = cluster_map.get(cluster, "Unknown Segment")
    strategy = segment_strategies.get(segment, "No strategy available.")

    return f"🎯 Predicted Segment: {segment}\n\n{strategy}"

# Gradio UI
interface = gr.Interface(
    fn=predict_segment,
    inputs=[
        gr.Number(label="Age"),
        gr.Number(label="Income"),
        gr.Number(label="Rating (0-100)"),
        gr.Radio(choices=["Male", "Female"], label="Gender")
    ],
    outputs=gr.Textbox(label="User Segment & Strategy"),
    title="Amazon User Segment Predictor",
    description="Enter user details to classify them into a marketing segment and view recommended strategy."
)

if __name__ == "__main__":
    interface.launch(share=True)
