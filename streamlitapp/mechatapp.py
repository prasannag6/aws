import streamlit as st
import smjs as su
import difflib

st.markdown("<h1 style='font-size:1.5em;'>GenAI Common Labs - Falcon model</h1>", unsafe_allow_html=True)

# Get user input
user_prompt = st.chat_input("Your prompt")

# Create a sidebar for sliders
st.sidebar.title("Model Parameters")

# Add sliders for temperature, top_p, and top_k
temperature = st.sidebar.slider("Temperature", min_value=0.0, max_value=1.0, value=0.2, step=0.1)
top_p = st.sidebar.slider("Top-p", min_value=0.1, max_value=1.0, value=0.7, step=0.1)
max_new_tokens = st.sidebar.slider("Max New Tokens", min_value=50, max_value=1000, value=500, step=50)
#top_k = st.slider("Top-k", min_value=1, max_value=100, value=50, step=1)

if user_prompt:
    st.markdown("User Input:")
    st.write(user_prompt)  # Display user input

    # Generate model response
    response = su.generate_response(user_prompt, temperature, top_p, max_new_tokens)
    
    if response:
        # Get generated text 
        generated_text = response[0]['generated_text']  
        
        # Compare and remove user prompt
        match = difflib.SequenceMatcher(None, user_prompt, generated_text).find_longest_match(0, len(user_prompt), 0, len(generated_text))
        model_response = generated_text[match.size:] 
        
        st.markdown("Model Response:")
        st.write(model_response) 
        
    else:
        st.warning("No response")
