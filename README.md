# brain_tumor

Analyser:


Overview
The Medical Assistant Chatbot for Brain MRI Analysis is a Streamlit application designed to help users analyze MRI images of the brain. Using the advanced Google Gemini 1.5 Pro model, this app provides detailed insights into tumor localization, size, segmentation, and other key aspects based on uploaded MRI scans.
Features
•	Upload MRI Images: Users can upload MRI images in PNG, JPG, or JPEG formats.
•	Detailed Analysis: The app provides a comprehensive analysis of the MRI image, including:
o	Tumor Localization
o	Tumor Size and Shape
o	Tumor Segmentation
o	Structural Deviation
o	Recommendations and Next Steps
•	User-Friendly Interface: An intuitive interface guides users through the upload and analysis process.
How to Use
1.	Upload an MRI Image:
o	Click on the “🖼️ Upload MRI Image” button to select and upload your MRI image file.
2.	Get Analysis:
o	Once the image is uploaded, click on the “🧾 Get Analysis” button to start the analysis.
o	The application will process the image and provide detailed insights based on the uploaded MRI scan.
3.	Review Results:
o	The analysis results will be displayed under the headings: Tumor Localization, Tumor Size and Shape, Tumor Segmentation, Structural Deviation, and Recommendations and Next Steps.
Prerequisites
•	Python 3.x
•	Streamlit: Install using pip install streamlit
•	Google Generative AI: Ensure you have a Google API key for accessing the Gemini model.
Setup
1.	Clone the Repository:
git clone <repository-url>
cd <repository-directory>
2.	Install Dependencies:
pip install streamlit google-generativeai
3.	Set Up API Key:
o	Set your Google API key as an environment variable:
export GOOGLE_API_KEY=<your-google-api-key>
4.	Run the App:
streamlit run app.py
Notes
•	Image Quality: For the best results, ensure that the MRI image is clear and properly scanned.
•	Disclaimer: The app provides insights based on the uploaded MRI scan but does not substitute professional medical advice. Consult with a doctor before making any medical decisions.
Troubleshooting
•	Issues with Uploading: Ensure the file format is correct and the image is not corrupted.
•	API Key Issues: Verify that the Google API key is set correctly and has the necessary permissions.
Contributing
Feel free to submit issues or pull requests if you encounter bugs or have suggestions for improvements.
License
This project is licensed under the MIT License. See the LICENSE file for details.


Chatbot:

# Brain Tumor ChatBot

This project is a Streamlit-based web application that allows users to interact with a chatbot designed to provide insights related to brain tumors. The chatbot leverages the Google Gemini 1.5 Pro or Flash model for generating responses based on user queries and the content of a provided PDF document.

## Features

- Model Selection: Users can choose between different versions of the Gemini model (e.g., Gemini 1.5 Flash, Gemini 1.5 Pro).
- PDF Interaction: Extracts text and images from a PDF file and uses the text to generate relevant responses.
- Customizable Parameters: Users can adjust parameters like temperature, top-p, and max tokens for fine-tuning the model's responses.
- Image Display: Displays images extracted from the PDF document.

## Prerequisites

Before running the app, make sure you have the following installed:

- Python 3.8 or higher
- [Streamlit](https://streamlit.io/)
- [Google Generative AI SDK](https://developers.generativeai.google/)
- [PyMuPDF (fitz)](https://pymupdf.readthedocs.io/)
- [pypdf](https://pypdf.readthedocs.io/)
- [Pillow](https://pillow.readthedocs.io/)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your_username/brain-tumor-chatbot.git
   cd brain-tumor-chatbot
2.	Install the required Python packages:
bash
Copy code
pip install streamlit google-generativeai pypdf pymupdf pillow
3.	Set up your Google API key by exporting it as an environment variable:
bash
Copy code
export GOOGLE_API_KEY=your_google_api_key
For Windows:
cmd
Copy code
set GOOGLE_API_KEY=your_google_api_key
Usage
1.	Update the path variables in the code to match your local file system:
python
Copy code
path2 = '/Users/your_username/your_directory'
pdf_file_path = 'D:/Projects/Brain_Tumour/brain_tumor_pdf.pdf'
2.	Run the Streamlit app:
bash
Copy code
streamlit run app.py
3.	Open your web browser and go to the provided local URL (usually http://localhost:8501).
4.	Upload a PDF, enter a question related to the document, and click "Submit" to receive a response from the chatbot.
License
This project is licensed under the MIT License. See the LICENSE file for more details.
Acknowledgements
•	Streamlit
•	Google Generative AI
•	PyMuPDF
•	pypdf
•	Pillow

