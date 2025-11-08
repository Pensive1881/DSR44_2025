import os
import streamlit as st
from huggingface_hub import InferenceClient

# --- 1) Token from environment / secrets ---
HUGGINGFACE_TOKEN = os.getenv("API_token")                      # common on HF Spaces


if not HUGGINGFACE_TOKEN:
    st.error("Hugging Face API Token not found. Set HF_TOKEN (or HUGGINGFACEHUB_API_TOKEN) in your Space/Secrets.")
    st.stop()

# --- 2) Model & client ---
# Use a chat-capable model that supports the Inference API "chat_completion" endpoint.
MODEL_ID = "openai/gpt-oss-20b"  # ← replace if you prefer another chat model
client = InferenceClient(model=MODEL_ID, token=HUGGINGFACE_TOKEN)

# --- 3) UI ---
st.title("LLM Inference Demo (Hugging Face Inference API)")
st.caption(f"Model: `{MODEL_ID}`")

# simple controls
col1, col2, col3 = st.columns(3)
with col1:
    temperature = st.slider("temperature", 0.0, 2.0, 0.7, 0.1)
with col2:
    top_p = st.slider("top_p", 0.0, 1.0, 0.95, 0.01)
with col3:
    max_tokens = st.slider("max_tokens", 16, 1024, 256, 16)

# keep a running chat history in session state
if "history" not in st.session_state:
    st.session_state.history = []  # list of {"role": "...", "content": "..."}

system_message = "You are a helpful assistant."

# chat UI
for msg in st.session_state.history:
    if msg["role"] == "user":
        st.chat_message("user").write(msg["content"])
    else:
        st.chat_message("assistant").write(msg["content"])

user_prompt = st.chat_input("Send a message")

if user_prompt:
    # show the user's message immediately
    st.chat_message("user").write(user_prompt)

    # build message list for the API: system + history + new user turn
    messages = [{"role": "system", "content": system_message}]
    messages.extend(st.session_state.history)
    messages.append({"role": "user", "content": user_prompt})

    # streaming placeholder
    stream_area = st.chat_message("assistant")
    stream_box = stream_area.empty()

    # --- 4) Call the API with streaming ---
    response_text = ""
    try:
        for event in client.chat_completion(
            messages=messages,
            max_tokens=max_tokens,
            stream=True,
            temperature=temperature,
            top_p=top_p,
        ):
            # Hugging Face returns events with choices[0].delta.content during stream
            if event and getattr(event, "choices", None):
                delta = event.choices[0].delta
                token = getattr(delta, "content", None) or ""
                if token:
                    response_text += token
                    stream_box.markdown(response_text)
    except Exception as e:
        st.error(f"Error from inference endpoint: {e}")
        st.stop()

    # finalize assistant message + persist to history
    stream_box.markdown(response_text if response_text else "_(no content returned)_")
    st.session_state.history.append({"role": "user", "content": user_prompt})
    st.session_state.history.append({"role": "assistant", "content": response_text})