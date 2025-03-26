# import streamlit as st
# from modules.chatbot import FAQChatbot

# # Initialize chatbot
# chatbot = FAQChatbot('data/faq_data.json')

# # Streamlit UI
# st.set_page_config(page_title="FAQ Chatbot", page_icon="💬")

# st.title("💬 FAQ Chatbot")
# st.write("Ask me any question!")

# # User input
# user_input = st.text_input("You: ", "")

# if st.button("Get Answer"):
#     if user_input.strip():
#         response_data = chatbot.generate_response(user_input)
#         st.success(f"🤖 **Chatbot:** {response_data['answer']}")
#     else:
#         st.warning("Please enter a question!")

# # Footer
# st.markdown("---")
# st.markdown("📌 **FAQ Chatbot** - Built with Streamlit")


    
    
import streamlit as st
from modules.chatbot import FAQChatbot

# Initialize the chatbot
chatbot = FAQChatbot('data/faq_data.json')

# Streamlit UI
st.title("💬 FAQ Chatbot")
st.write("Ask me any question related to our services! Here are some examples:")

# Sample questions categorized
faq_categories = {
    "Orders & Shipping": [
        "How do I track my order?",
        "What shipping carriers do you use?",
    ],
    "Payments & Discounts": [
        "What payment methods do you accept?",
        "Do you offer student discounts?",
    ],
    "General": [
        "What is your return policy?",
        "How can I contact customer support?",
    ]
}

# Display categorized questions in expanders
for category, questions in faq_categories.items():
    with st.expander(category):
        for q in questions:
            if st.button(q, key=q):
                st.session_state["user_input"] = q

# Dropdown for auto-suggestion
user_input = st.selectbox(
    "Choose a question or type your own:",
    [""] + [q for questions in faq_categories.values() for q in questions],  # Flatten the list
    index=0
)

# Allow users to manually type if they don't select from dropdown
custom_input = st.text_input("Or type your question:", "")

# Determine final input (dropdown or custom)
final_input = custom_input if custom_input else user_input

if st.button("Get Answer"):
    if final_input:
        response_data = chatbot.generate_response(final_input)
        st.write(f"🤖 **Chatbot:** {response_data['answer']}")
    else:
        st.warning("Please enter a question.")
