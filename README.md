# Reddit Depression Detection via Multi-Stage Stacked Ensemble Learning

## Project Overview
This research-oriented project focuses on detecting signs of depression in social media discourse. By leveraging **Natural Language Processing (NLP)** and **Stacked Generalization (Stacking)**, the model identifies patterns associated with mental health distress in Reddit posts.

## Methodology & Experiments
The implementation uses a multi-level stacking framework to improve classification performance. Two major experiments were conducted:

### Experiment 1: Traditional ML Stacking (Top Performer)
* **Base Learners:** Logistic Regression (LR), Naive Bayes (NB), K-Nearest Neighbors (KNN), Support Vector Machine (SVM), and Random Forest (RF).
* **Meta-Model:** Optimized classifier aggregating the top 3 base models.
* **Result:** Achieved a peak **Accuracy of 96%**.
* **Model File:** `stacked_model.pkl`

### Experiment 2: Boosting/Tree-Based Stacking
* **Base Learners:** XGBoost, AdaBoost, and Gradient Boosting.
* **Result:** While robust, this configuration yielded slightly lower accuracy compared to the Traditional ML Stack.

## Streamlit Dashboard (`d2.py`)
To make the research accessible, I developed an interactive web application featuring:
* **Live Text Inference:** Predicts mental health status from real-time user input.
* **Confidence Scoring:** Displays the probability percentage of the detection.

## 📂 Repository Contents
* `stacked_model.pkl`: The saved best-performing stacked model (96% Accuracy).
* `DataSet35530.csv`: Training data (approx. 32MB) containing Reddit posts and labels.
* `d2.py`: Streamlit-based web interface script.
* `requirements.txt`: List of necessary Python libraries.

---

## 🚀 Installation & Setup Guide
Follow these steps to run the project locally:

### 1. Clone the Repository
```bash
git clone [https://github.com/still-shrey/reddit-depression-detection.git](https://github.com/still-shrey/reddit-depression-detection.git)
cd reddit-depression-detection
```

### 2. Install Dependencies
Ensure you have Python installed, then run:
```bash
pip install -r requirements.txt
```
### 3. Run the Application
Launch the interactive dashboard by running:
```bash
streamlit run d2.py
```



