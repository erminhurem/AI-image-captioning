import streamlit as st
from image_to_text import generate_semantics
from image_caption import generate_caption


st.image("logo.png", use_column_width=True)

file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if file:

    column1, column2 = st.columns(2)

    with column1:
        st.image(file, use_column_width=True)

    with column2:
        with st.spinner("Generating semantics..."):
            semantics = generate_semantics(file)

        # promting the mixtral model for caption generation, tweak the prompt as you like :)
        with st.spinner("Generating caption..."):
            prompt = {"inputs": f"Question:Convert the folowing image semantics"
                                f"'{semantics}' to an instagram caption"
                                f"Make sure to add hash tags and emojis."
                                f" Answer: "
                      }

            generated_caption = generate_caption(prompt)[0]["generated_text"]
            st.subheader("Caption:")
            caption = generated_caption.split("Answer: ")[1]
            
            #styling the text output box
            style = """
                    <style>
                    .styled-text {
                        padding: 20px;
                        border-radius: 15px;
                        border: 2px solid #ccc;
                        box-shadow: 5px 5px 15px #aaa;
                    }
                    </style>
                    """
            styled_text = f"<div class='styled-text'>{caption}</div>"
            st.markdown(style, unsafe_allow_html=True)
            st.markdown(styled_text, unsafe_allow_html=True)
