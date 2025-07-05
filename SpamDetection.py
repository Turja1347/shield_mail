import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import streamlit as st

#  Load dataset
data = pd.read_csv("spam.csv")

#  Remove duplicates
data.drop_duplicates(inplace=True)

#  Replace category labels
data['Category'] = data['Category'].replace(['ham','spam'],['Not Spam','Spam'])

#  Split data
mess = data['Message']
cat = data['Category']
(mess_train, mess_test, cat_train, cat_test) = train_test_split(mess, cat, test_size=0.2)

#  Vectorize text
cv = CountVectorizer(stop_words='english')
features = cv.fit_transform(mess_train)

#  Train model
model = MultinomialNB()
model.fit(features, cat_train)

#  Prepare test data
features_test = cv.transform(mess_test)

#  Prediction function
def predict(messege):
    input_messege = cv.transform([messege]).toarray()
    result = model.predict(input_messege)
    return result

#  Streamlit Interface
st.header('🛡️ ShieldMail — Spam Mail & Text Detection')

#  Demo output
output = predict('congratulation you won a lottery')

#  User Input
input_mess = st.text_input('💬 Enter Message Here')

if st.button('✅ Validate'):
    output = predict(input_mess)[0]
    if output == "Spam":
        st.error("⚠️ This message is likely *Spam*.")
    else:
        st.success("✅ This message is *Not Spam*.")

#  Sidebar Information
st.sidebar.title("📊 App Information")
st.sidebar.markdown("🛡️ *ShieldMail* helps you detect spam messages using a trained Naive Bayes classifier.")

st.sidebar.markdown("### 🔍 Features")
st.sidebar.markdown("- 🧠 Spam/Not Spam prediction")
st.sidebar.markdown("- 💬 Real-time input")
st.sidebar.markdown("- 🧹 Cleaned and preprocessed data")

st.sidebar.markdown("### 🛠️ Tech Stack")
st.sidebar.markdown("- 🐍 Python")
st.sidebar.markdown("- 📦 scikit-learn")
st.sidebar.markdown("- 🌐 Streamlit")
st.sidebar.markdown('👨‍💻 Developed by: [*Turja Mondal*](https://www.linkedin.com/in/turjamondal01/)', unsafe_allow_html=True)
st.sidebar.markdown("---")

