import streamlit as st
import aws.streamlitapp.smjs as su

st.title("M&E Workshop ChatApp")

# Get user input
user_prompt = st.chat_input("Your prompt")

# Add sliders for temperature, top_p, and top_k
temperature = st.slider("Temperature", min_value=0.1, max_value=2.0, value=0.2, step=0.1)
top_p = st.slider("Top-p", min_value=0.1, max_value=1.0, value=0.7, step=0.1)
max_new_tokens = st.slider("Max New Tokens", min_value=50, max_value=1000, value=500, step=50)
#top_k = st.slider("Top-k", min_value=1, max_value=100, value=50, step=1)

if user_prompt:
    st.markdown("User Input:")
    st.write(user_prompt)  # Display user input

    # Generate model response
    response = su.generate_response(user_prompt, temperature, top_p, max_new_tokens)
    
    if response:
        # Extract the text after '\n' for the first 'generated_text' in the response
        extracted_text = response[0]['generated_text'].split('\n', 1)[1]
        
        st.markdown("Model Response:")
        st.write(extracted_text)  # Display model response
    else:
        st.warning("No model response found.")
