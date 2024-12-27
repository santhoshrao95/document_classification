**Problem Description**
This project focuses on building a machine learning pipeline to classify product-related PDFs into one of four categories: Lighting, Fuses, Cables, or Others. The dataset consists of training and testing information with links to hosted PDFs and their respective target classes.

**Solution Overview**
A FastAPI app was developed for inference, enabling users to input a PDF URL and retrieve the predicted category along with class probabilities. The app includes the following key components:
  Text Extraction Pipeline: Processes PDFs to extract text content.
  Classification Model: Predicts the product category using a trained machine learning model.
  Inference Pipeline: Facilitates real-time predictions via a hosted API or notebook interface.
  
**How to Run**
The inference can be executed using the inference.ipynb notebook, which interacts with the FastAPI app for predictions.
