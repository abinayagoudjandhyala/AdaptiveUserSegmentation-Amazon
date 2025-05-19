# AdaptiveUserSegmentation-Amazon

## Project Overview

This project implements **user segmentation** and **prediction** for Amazon customers by applying clustering and classification techniques on user data. The segmentation model groups users into meaningful clusters based on their behavior and demographics, while the classification model predicts the segment of a new user based on their input features.

The application provides an interactive web interface built with **Gradio** to input user details, predict their segment, and display targeted marketing strategies tailored to each segment.

---

🌐 **Live Output** : [Open App](https://abinayagoudjandhyala23-usersegmentation.hf.space)

---
## Features

* **Segmentation:** Groups Amazon users into 4 distinct clusters based on behavioral data.
* **Classification:** Predicts the segment of a new user from input features.
* Provides actionable marketing strategies for each segment.
* User-friendly, real-time interactive UI using Gradio.
* Easy to run locally or deploy on cloud platforms.

---

## Data & Model Details

* **Clustering:** Performed using a clustering algorithm (e.g., KMeans) on user behavior data.
* **Classification:** Trained model to assign users to one of the clusters based on their features.
* Input features include:

  * Age
  * Income
  * Rating (0-100)
  * Gender
* Derived features:

  * Income per Age
  * Behavior Score (Income × Rating)
* The classification model and scaler are saved as `.sav` files using `pickle`.

---

## Getting Started

### Prerequisites

* Python 3.7+
* Python packages:

  ```bash
  pip install gradio scikit-learn pandas numpy
  ```

### Files

* `app.py` — Gradio app interface and prediction logic.
* `cluster_classifier.sav` — Saved classification model.
* `scaler.sav` — Saved feature scaler.

---

## Running the Application Locally

1. Place the model and scaler files alongside `app.py`.
2. Install dependencies.
3. Run:

   ```bash
   python app.py
   ```
4. Open the local URL provided by Gradio in your browser.

---

## Deployment

Deploy on platforms like:

* Hugging Face Spaces (free and easy for Gradio apps)
* Heroku
* Any cloud server supporting Python apps

---

## Usage Instructions

Input user details such as Age, Income, Rating (0-100), and Gender. The app predicts their segment and presents a marketing strategy customized for that segment.

---

## Segments and Strategies

* **Young High Spenders**
  Focus on premium offers, influencer marketing, and loyalty rewards.

* **Mid-Age Budget Seekers**
  Promote discounts, budgeting aids, and seasonal sales.

* **Valuable Loyalists**
  Engage with personalized messaging, VIP perks, and feedback.

* **Low-Value Users**
  Boost engagement via tutorials, entry-level offers, and support.

---

## Future Work

* Incorporate more features like engagement scores.
* Visualize user input relative to cluster centroids.
* Enable dynamic clustering on updated data.
* Containerize for easier deployment and scaling.

---

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).  
You are free to use, modify, and distribute this project with proper attribution.

---

## Contact

- **Name:** Abinaya Goud 
- **GitHub:** [https://github.com/abinayagoudjandhyala](https://github.com/abinayagoudjandhyala)
