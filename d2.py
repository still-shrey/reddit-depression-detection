import streamlit as st
import joblib
import time

# Page config
st.set_page_config(page_title="Reddit Depression Detection", page_icon="🧠")
st.title("🧠 Reddit Post Depression Detector")

# Model loading
with st.spinner("🚀 Loading model... Please wait..."):
    model = joblib.load("stacked_model.pkl")
    time.sleep(1.5)
st.success("✅ Model loaded and ready for predictions!")


# ===================== 🧠 Sidebar Help Section =====================
st.sidebar.header("🆘 Need Help?")
st.sidebar.write("If you're feeling **depressed or anxious**, please reach out to a **mental health professional**.")

st.sidebar.subheader("📞 Helpline Numbers:")
st.sidebar.markdown("- **National Helpline**: `14416` or `1-800-891-4416` _(Available 24/7)_")

st.sidebar.markdown("🔍 [Click here to find nearby support centers](https://telemanas.mohfw.gov.in/telemanas-dashboard/#/)")
st.sidebar.markdown("📚 [More mental health resources](https://telemanas.mohfw.gov.in/home)")

st.sidebar.markdown("---")
st.sidebar.caption("Your mental health matters 💚")


# Input box
user_input = st.text_area("📝 Enter a Reddit post here:", height=200, placeholder="Type your Reddit post...")

# Predict
if st.button("🔮 Predict"):
    if user_input.strip() == "":
        st.warning("⚠️ Please enter some text before predicting.")
    else:
        prediction = model.predict([user_input])[0]
        prob = model.predict_proba([user_input])[0][1]  # prob of being depressed

        if prediction == 1:
            st.error("😟 Based on your Reddit post, you are **likely to be depressed or in mental stress.**")
            st.caption(f"📊 Prediction confidence: `{prob*100:.2f}%`")

            if prob > 0.7:
                st.markdown("💡 **Here are some resources that might help:**")
                st.markdown("- [The Live Laugh Foundation](https://www.thelivelovelaughfoundation.org/find-help/helplines) – Free support (24/7)")
                st.markdown("- [Talk to Angel](https://www.talktoangel.com/blog/best-mental-health-counselling-platform-in-india-and-the-world) – Online therapy platform")
                st.markdown("- [Tele Manas](https://telemanas.mohfw.gov.in/home) – Indian Govt website for support")
                
        else:
            st.success("😊 Based on your Reddit post, you are **not likely depressed.**")
            st.caption(f"📊 Prediction confidence (depression): `{prob*100:.2f}%`")
