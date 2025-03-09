
import streamlit as st
from PIL import Image
import openai
from nltk.sentiment.vader import SentimentIntensityAnalyzer

openai.api_key = "your-openai-api-key"
sid = SentimentIntensityAnalyzer()

def get_chatbot_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

def analyze_sentiment(text):
    sentiment_score = sid.polarity_scores(text)
    if sentiment_score['compound'] >= 0.05:
        return "Positive"
    elif sentiment_score['compound'] <= -0.05:
        return "Negative"
    else:
        return "Neutral"

st.title("AI Chatbot with Real-time Sentiment Analysis")

# Chat interface
user_input = st.text_input("You:", "")
if 'messages' not in st.session_state:
    st.session_state.messages = []

if user_input:
    # User message
    st.session_state.messages.append(f"You: {user_input}")
    
    # Get chatbot response
    bot_response = get_chatbot_response(user_input)
    st.session_state.messages.append(f"Bot: {bot_response}")

    # Analyze sentiment
    sentiment = analyze_sentiment(user_input)
    st.session_state.messages.append(f"Sentiment: {sentiment}")

# Display chat history
for message in st.session_state.messages:
    st.write(message)
