<h1>brain_tumor</h1>
<p>Analyser:</p>
<p>Overview
The Medical Assistant Chatbot for Brain MRI Analysis is a Streamlit application designed to help users analyze MRI images of the brain. Using the advanced Google Gemini 1.5 Pro model, this app provides detailed insights into tumor localization, size, segmentation, and other key aspects based on uploaded MRI scans.</p>
<p>Features:</p>
<ul>
<li>
<p>Upload MRI Images: Users can upload MRI images in PNG, JPG, or JPEG formats.</p>
</li>
<li>
<p>Detailed Analysis: The app provides a comprehensive analysis of the MRI image, including:</p>
<ul>
<li>Tumor Localization</li>
<li>Tumor Size and Shape</li>
<li>Tumor Segmentation</li>
<li>Structural Deviation</li>
<li>Recommendations and Next Steps</li>
<li>User-Friendly Interface: An intuitive interface guides users through the upload and analysis process.</li>
</ul>
</li>
</ul>
<p>How to Use</p>
<p>1.Upload an MRI Image:</p>
<ul>
<li>Click on the “🖼 Upload MRI Image” button to select and upload your MRI image file.</li>
</ul>
<p>2.Get Analysis:</p>
<p>Start numbering with offset:</p>
<ul>
<li>Once the image is uploaded, click on the “🧾 Get Analysis” button to start the analysis.</li>
<li>The application will process the image and provide detailed insights based on the uploaded MRI scan.</li>
</ul>
<p>3.Review Results:</p>
<ul>
<li>The analysis results will be displayed under the headings: Tumor Localization, Tumor Size and Shape, Tumor Segmentation, Structural Deviation, and Recommendations and Next Steps.</li>
</ul>
<p>Prerequisites:</p>
<ul>
<li>Python 3.x</li>
<li>Streamlit: Install using pip install</li>
<li>Google Generative AI: Ensure you have a Google API key for accessing the Gemini model.</li>
</ul>
<p>Setup:</p>
<p>1.Clone the Repository:</p>
<h2>Code</h2>
<pre><code>// git cloning
git clone &lt;repository-url&gt;
</code></pre>
<p>2.Install Dependencies:</p>
<ul>
<li>pip install streamlit google-generativeai</li>
</ul>
<p>3.Set Up API Key:</p>
<ul>
<li>Set your Google API key as an environment variable</li>
</ul>
<pre><code class="hljs">export GOOGLE_API_KEY=&lt;your-google-api-key&gt;

</code></pre>
<p>4.Run the App:</p>
<ul>
<li>streamlit run <a href="http://app.py">app.py</a></li>
</ul>
<p>Notes</p>
<ul>
<li>Image Quality: For the best results, ensure that the MRI image is clear and properly scanned.</li>
<li>Disclaimer: The app provides insights based on the uploaded MRI scan but does not substitute professional medical advice. Consult with a doctor before making any medical decisions.</li>
</ul>
<p>Troubleshooting</p>
<ul>
<li>Issues with Uploading: Ensure the file format is correct and the image is not corrupted.</li>
<li>API Key Issues: Verify that the Google API key is set correctly and has the necessary permissions.</li>
</ul>
<p>Contributing:</p>
<p>Feel free to submit issues or pull requests if you encounter bugs or have suggestions for improvements.</p>
<p>License:</p>
<p>This project is licensed under the MIT License. See the LICENSE file for details.</p>


<h1>Brain Tumor ChatBot</h1>
<p>This project is a Streamlit-based web application that allows users to interact with a chatbot designed to provide insights related to brain tumors. The chatbot leverages the Google Gemini 1.5 Pro or Flash model for generating responses based on user queries and the content of a provided PDF document.</p>
<h2>Features</h2>
<ul>
<li>Model Selection: Users can choose between different versions of the Gemini model (e.g., Gemini 1.5 Flash, Gemini 1.5 Pro).</li>
<li>PDF Interaction: Extracts text and images from a PDF file and uses the text to generate relevant responses.</li>
<li>Customizable Parameters: Users can adjust parameters like temperature, top-p, and max tokens for fine-tuning the model’s responses.</li>
<li>Image Display: Displays images extracted from the PDF document.</li>
</ul>
<h2>Prerequisites</h2>
<ul>
<li>Python 3.8 or higher</li>
<li><a href="https://streamlit.io/">Streamlit</a></li>
<li><a href="https://developers.generativeai.google/">Google Generative AI SDK</a></li>
<li><a href="https://pymupdf.readthedocs.io/">PyMuPDF (fitz)</a></li>
<li><a href="https://pypdf.readthedocs.io/">pypdf</a></li>
<li><a href="https://pillow.readthedocs.io/">Pillow</a></li>
</ul>
<h2>Installation</h2>
<p>1.Clone the Repository:</p>
<h2>Code</h2>
<pre><code>git clone https://github.com/your_username/brain-tumor-chatbot.git
</code></pre>
<ul>
<li>cd brain-tumor-chatbot</li>
</ul>
<p>2.Install the required Python packages</p>
<ul>
<li>pip install streamlit google-generativeai pypdf pymupdf pillow</li>
</ul>
<p>3.Set up your Google API key by exporting it as an environment variable:</p>
<ul>
<li>Set your Google API key as an environment variable</li>
</ul>
<pre><code class="hljs">export GOOGLE_API_KEY=your_google_api_key
</code></pre>
<p>For Windows:</p>
<pre><code class="hljs">set GOOGLE_API_KEY=your_google_api_key
</code></pre>
<p>Usage:</p>
<p>1.Update the path variables in the code to match your local file system:
python</p>
<pre><code class="hljs">path2 = '/Users/your_username/your_directory'
pdf_file_path = 'D:/Projects/Brain_Tumour/brain_tumor_pdf.pdf'
</code></pre>
<p>2.Run the Streamlit app:</p>
<pre><code class="hljs">streamlit run app.py
</code></pre>
<p>3.Open your web browser and go to the provided local URL (usually <a href="http://localhost:8501">http://localhost:8501</a>).</p>
<p>4.Upload a PDF, enter a question related to the document, and click “Submit” to receive a response from the chatbot.</p>
<p>License</p>
<p>This project is licensed under the MIT License. See the LICENSE file for more details.</p>
<p>Acknowledgements</p>
<ul>
<li>Streamlit</li>
<li>Google Generative AI</li>
<li>PyMuPDF</li>
<li>pypdf</li>
<li>Pillow</li>
</ul>