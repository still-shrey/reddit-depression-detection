# Detecting Depressive Tendencies in Reddit Users using Stacked Ensemble Learning

## Project Overview
This research-oriented project focuses on detecting signs of depression in social media discourse. By leveraging Natural Language Processing (NLP) and Ensemble Learning, the model identifies patterns associated with mental health distress in Reddit posts.

## Methodology
The current implementation uses a **Stacked Generalization (Stacking)** framework to improve classification performance:
- **Data Source:** Reddit (Mental Health related subreddits).
- **Base Learners:** A combination of high-performing ML algorithms (e.g.Logistic Regression, Naive Bayes, Random Forest, XGBoost, Gradient-Boosting).
- **Meta-Model:** Optimized classifier that aggregates base-model predictions for the final output.
- **Features:** TF-IDF Vectorization for textual analysis.

## Repository Contents
- `stacked_model.pkl`: The saved best-performing stacked model (Ready for inference).
- `DataSet35530.csv`: The training data (approx. 32MB) containing Reddit posts and labels.

## Future Roadmap
- [ ] **LLM Integration:** Moving towards Transformer-based architectures (BERT, RoBERTa, or Llama fine-tuning).
- [ ] **Real-time API:** Creating a Streamlit or Flask interface for live text prediction.
- [ ] **Data Expansion:** Incorporating multi-modal data (metadata like post timing and frequency).

## 📖 Usage
To load the model in your local environment:
```python
import joblib

# Load the stacked model
model = joblib.load('stacked_model.pkl')

# Example Prediction
# result = model.predict([processed_text])
