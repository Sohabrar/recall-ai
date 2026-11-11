
import streamlit as st
from datetime import datetime

# PAGE CONFIGURATION
st.set_page_config(
    page_title="Recall AI",
    page_icon="🧠",
    layout="wide"
)

# APP TITLE
st.title("🧠 Recall AI")
st.subheader("Your Personal Memory Assistant")

st.write(
    "Remember your experiences. "
    "Learn from your past. Grow every day."
)

# TEMPORARY MEMORY STORAGE
if "memories" not in st.session_state:
    st.session_state.memories = []

# RESET BUTTON
if st.sidebar.button("🗑️ Reset Demo Memories"):
    st.session_state.memories = []
    st.rerun()

# SIDEBAR NAVIGATION
menu = st.sidebar.radio(
    "Navigation",
    [
        "Home",
        "Daily Journal",
        "My Memories",
        "Recall AI Chat"
    ]
)

# HOME PAGE
if menu == "Home":

    st.header("Welcome to Recall AI 🌱")

    st.write(
        "Your journey of memories and personal growth starts here."
    )

    st.metric(
        "Memories Saved",
        len(st.session_state.memories)
    )

    st.info(
        "Start writing about your day to build your personal memory collection."
    )

# DAILY JOURNAL
elif menu == "Daily Journal":

    st.header("📝 Write About Your Day")

    entry = st.text_area(
        "What happened today?",
        placeholder="Write about your experiences, feelings and lessons..."
    )

    if st.button("Save Memory"):

        cleaned_entry = entry.strip()

        if not cleaned_entry:

            st.warning("Please write something first.")

        elif any(
            memory["text"] == cleaned_entry
            for memory in st.session_state.memories
        ):

            st.warning("This memory already exists!")

        else:

            st.session_state.memories.append({
                "date": datetime.now().strftime("%d %B %Y"),
                "text": cleaned_entry
            })

            st.success("Your memory has been saved successfully! 💚")

# MY MEMORIES
elif menu == "My Memories":

    st.header("📚 Your Memories")

    if st.session_state.memories:

        for index, memory in enumerate(
            reversed(st.session_state.memories),
            start=1
        ):

            st.write(f"### Memory {index}")

            st.caption("📅 " + memory["date"])

            st.info(memory["text"])

            st.divider()

    else:

        st.info(
            "No memories yet. Start by writing about your day!"
        )

# RECALL AI CHAT
elif menu == "Recall AI Chat":

    st.header("💬 Talk to Recall AI")

    st.write(
        "Your personal memory assistant is coming to life!"
    )

    question = st.text_input(
        "Ask something about your memories"
    )

    if st.button("Ask Recall AI"):

        if question.strip():

            st.info(
                "Gemini AI integration is coming in our next development phase."
            )

        else:

            st.warning("Please enter a question.")

# FOOTER
st.divider()

st.caption(
    "Recall AI | Your past can guide your future 💚"
)