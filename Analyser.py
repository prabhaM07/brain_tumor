import streamlit as st
import google.generativeai as genai
import os

# Configure the Google Generative AI with the API key
GOOGLE_API_KEY = os.environ.get('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)

# Define a function to upload files to Gemini
def upload_to_gemini(path, mime_type=None):
    file = genai.upload_file(path, mime_type=mime_type)
    return file

# Create the generative model
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-pro",
    generation_config=generation_config,
    system_instruction= """
As a highly skilled medical practitioner specializing in brain tumor MRI image analysis, you are tasked with examining medical images for a renowned hospital. Your expertise is crucial in identifying abnormalities, diseases, or health issues that may be present in the MRI image.
Your responsibilities include:
When users ask about an MRI scan, you should provide detailed explanations based on the following guidelines:

1. Tumor Localization: Describe the location of any highlighted areas on the MRI, indicating the presence of a mass or tumor and its relationship to surrounding brain structures.

2. Tumor Size and Shape: Provide insights into the size and shape of the highlighted region, and explain how this information is useful for assessing the tumor’s extent and planning for further steps.

3. Tumor Segmentation: Explain the importance of segmentation in quantifying the tumor's volume and how it can be used to monitor the tumor's progression over time or its response to treatment.

4. Structural Deviation: Describe any observed mass effects, such as midline shifts or pressure on adjacent brain structures, and what these may indicate about the impact of the tumor on the surrounding brain.

5. Recommendations and Next Steps: Based on your analysis, suggest potential next steps, including recommendations like hospitals and doctors who are specialized for this treatment. Additionally, provide recommendations like food diets and regular exercises.

Important Notes:
1. Clarity of the Image: In cases where the image quality impedes clear analysis, note that certain aspects are 'Unable to be determined based on the provided image.'
2. Disclaimer: Accompany your analysis with the disclaimer: "Consult with the Doctor before making any decisions."

Please provide the output response with these 5 headings: Tumor Localization, Tumor Size and Shape, Tumor Segmentation, Structural Deviation, Recommendations and Next Steps.
Please ensure that your responses are based on these guidelines and provide accurate, helpful information about the MRI scan.
"""
)

# Streamlit application layout
st.title("🧠 Medical Assistant Chatbot for Brain MRI Analysis")
st.write("Upload an MRI image and get detailed analysis on tumor localization, size, segmentation, and more.")

# Upload MRI image
uploaded_file = st.file_uploader("🖼️ Upload MRI Image", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # Show a spinner while processing the image
    with st.spinner('🔍 Uploading the MRI image...'):
        # Save the uploaded file temporarily
        file_path = f"temp_{uploaded_file.name}"
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        # Upload file to Gemini
        mime_type = f"image/{uploaded_file.type.split('/')[-1]}"
        file = upload_to_gemini(file_path, mime_type)

        # Start the chat session
        chat_session = model.start_chat(
            history=[
                {
                    "role": "user",
                    "parts": [file],
                },
            ]
        )

        # Get analysis button
        if st.button("🧾 Get Analysis"):
            response = chat_session.send_message(
                "Please analyze the uploaded MRI scan based on the provided guidelines."
            )
            st.success("✅ Analysis Complete!")
            st.markdown(response.text)

        # Clean up the temporary file
        os.remove(file_path)
else:
    st.info("📥 Please upload an MRI image to get started!")

# Add some footer information
st.markdown(
    """
    ---
    💡 **Tip**: Ensure the MRI image is clear and properly scanned for the best results.
    """
)
