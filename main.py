from openai import OpenAI
import streamlit as st

st.title("GPT")
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])



col1, col2 = st.columns(2)
with col1:

    # use case
    usecase = st.selectbox(
        "Select use case",
        ["chat", "image"]
    )

    # set model
    if usecase == "chat":
        model_options = ["gpt-4", "gpt-4-32k", "gpt-3.5-turbo"]
    else:
        model_options = ["dall-e-3", "dall-e-2"]

with col2:

    # model to use
    model = st.selectbox(
        "Select model",
        model_options
    )
    st.session_state["openai_model"] = model

if usecase == "chat":

    # initialize messages
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # display messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # get user input
    if prompt := st.chat_input("What is up?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)

        with st.chat_message("assistant"):
            stream = client.chat.completions.create(
                model=st.session_state["openai_model"],
                messages=[
                    {"role": m["role"], "content": m["content"]}
                    for m in st.session_state.messages
                ],
                stream=True,
            )
            response = st.write_stream(stream)
        st.session_state.messages.append({"role": "assistant", "content": response})

elif usecase == "image":
    
        # input text
        text = st.text_area("Enter text")
        col1, col2 = st.columns(2)
        with col1:
            # input number of images
            n_wanted = st.number_input("Number of images", min_value=1, value=1)
        with col2:
            # size
            size = st.selectbox("Size", ["256x256", "512x512", "1024x1024"])
        
        if st.session_state["openai_model"]=="dall-e-3":
            col1, col2 = st.columns(2)
            with col1:
                style = st.selectbox("Style", ["vivid", "natural"])
            with col2:
                quality = st.selectbox("Quality", ["hd", "standard"])
            n_wanted = 1
        else:
            style = None
            quality = None

        if text and st.button("Generate image"):
            response = client.images.generate(
                model=st.session_state["openai_model"],
                prompt=text,
                size="1024x1024",
                quality=quality,
                style=style,
                n=n_wanted
            )

            image_url = response.data[0].url
            st.image(image_url, use_column_width=True)
            st.markdown(f"[Download image]({image_url})")



