from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import streamlit as st
import random

mystic_phrases = [
    "The runes are restless tonight...",
    "A raven whispers your fate...",
    "The stars have aligned, poorly...",
    "The spirits hum with uncertainty...",
    "Your aura glows... ominously.",
    "The third moon rises, beware the cheese!",
    "A shadow passes over your destiny...",
    "The tea leaves say: maybe?",
    "The crystals vibrate in your favor...",
    "The prophecy was written in spaghetti..."
]

load_dotenv()

st.set_page_config(page_title="Mystic Oracle 🔮", page_icon="🔮")
st.title("🔮 Mystic Oracle Bot")
st.markdown("_Seek answers from the unknown. Ask your question and behold the prophecy._")
model = ChatOpenAI(model='gpt-3.5-turbo')

question = st.text_input("Ask the Mystic Oracle anything...", placeholder="e.g., Should I eat pizza today?")
if st.button("Reveal Prophecy"):
    if question.strip() == "":
        st.warning("The spirits require a question.")
    else:
        oracle_prompt = (
            f"You are the Mystic Oracle, an ancient and mystical being who speaks in cryptic, funny, or spooky prophecies.\n"
            f"A mortal has asked: '{question}'\n"
            f"Respond with a short, mystical prophecy including a sprinkle of humor, metaphors, or spooky omens."
        )
        
        result = model.invoke(oracle_prompt)
        mystic_prepix = random.choice(mystic_phrases)
        final_message = f"🔮 {mystic_prepix}\n\n{result.content}"

        # Display the result
        st.markdown("---")
        st.markdown(f"### 🔮 Prophecy:")
        st.markdown(f"```{final_message}```")




