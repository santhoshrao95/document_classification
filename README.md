# Document Classification with Machine Learning

## Problem Description
This project focuses on building a machine learning pipeline to classify product-related PDFs into one of four categories: **Lighting**, **Fuses**, **Cables**, or **Others**. The dataset comprises training and testing information with URLs to hosted PDFs and their respective target classes.

---

## Solution Overview
A **FastAPI** app has been developed to provide an efficient inference pipeline. Users can input a PDF URL and receive:

- **The predicted category** of the document.
- **Confidence scores** for each class.

---

## Key Components

1. **Text Extraction Pipeline**: Downloads and processes PDFs to extract textual content for classification.
2. **Classification Model**: Trained on product-related PDFs to predict categories with high accuracy.
3. **Inference Pipeline**: Real-time predictions are made accessible through a FastAPI-based API or a Jupyter notebook.

---

## How to Run

### Clone the repository:
```bash
git clone https://github.com/santhoshrao95/document_classification.git
```

### Install dependencies:
```bash
pip install -r requirements.txt
```

### Start the FastAPI server:
```bash
uvicorn app.main:app --reload
```

### Use the Jupyter notebook:
Open **inference.ipynb** to interact with the API and classify PDFs by providing their URLs.

---

## Core Functionality
The FastAPI app implements a `/classify_pdf/` endpoint that accepts a PDF URL, extracts text, and classifies it into one of the four categories.

### Key Functions

#### `download_pdf(url: str)`
- Downloads the PDF from the given URL and saves it to a temporary file.
- Handles timeouts and request failures with appropriate error responses.
- Ensures the temporary file is cleaned up after use.

#### `extract_text_from_pdf(pdf_path: str)`
- Reads the downloaded PDF and extracts text using **PyPDF2**.
- Iterates through all pages to gather text content.
- Deletes the temporary file once processing is complete.

#### `classify_pdf(input_data: URLInput)`
The API endpoint that handles the classification process:

1. **Downloads the PDF** using the provided URL.
2. **Extracts the text content**.
3. **Passes the text** to the **MLService** class for prediction.
4. **Returns the classification label**, confidence score, and success status.

---

## MLService

This service handles the classification logic:
- The text is preprocessed and passed to a trained ML model for inference.
- The model outputs the **predicted category** and **confidence scores**.

---

## License
This project is licensed under the [MIT License](LICENSE).

---

## Contact
For questions or suggestions, feel free to reach out at [santhoshrao95@example.com](mailto:santhoshrao95@example.com).

