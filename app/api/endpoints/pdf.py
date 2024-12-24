import tempfile
import os
import requests
from fastapi import APIRouter, HTTPException
from typing import Dict, Tuple
import PyPDF2
from app.models.schemas import URLInput
from app.services.ml_service import MLService

router = APIRouter()
ml_service = MLService()


def download_pdf(url: str) -> str:
    try:
        temp_pdf = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")

        response = requests.get(url, timeout=90)
        response.raise_for_status()

        temp_pdf.write(response.content)
        temp_pdf.close()

        return temp_pdf.name

    except requests.exceptions.Timeout:
        raise HTTPException(
            status_code=408, detail="Request timed out while downloading PDF"
        )
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=400, detail=f"Error downloading PDF: {str(e)}")
    except Exception as e:
        if temp_pdf and os.path.exists(temp_pdf.name):
            os.unlink(temp_pdf.name)
        raise HTTPException(
            status_code=500, detail=f"Unexpected error while downloading PDF: {str(e)}"
        )


def extract_text_from_pdf(pdf_path: str) -> str:
    try:
        with open(pdf_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            text = ""
            for page in reader.pages:
                text += page.extract_text() + "\n\n"
        return text.strip()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing PDF: {str(e)}")
    finally:
        if os.path.exists(pdf_path):
            os.unlink(pdf_path)


@router.post("/classify_pdf/")
async def classify_pdf(input_data: URLInput) -> Dict[str, str]:
    try:
        pdf_path = download_pdf(input_data.url)

        text = extract_text_from_pdf(pdf_path)

        prediction, prob = ml_service.predict(text)

        return {
            "classification": str(prediction),
            "confidence": f"{prob:.2f}",
            "status": "success",
        }

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Unexpected error during classification: {str(e)}"
        )
