import os
import pandas as pd
import PyPDF2
from typing import List, Dict


def extract_text_from_pdfs(pdf_directory: str) -> pd.DataFrame:
    """
    Extract text from all PDFs in a directory and return as DataFrame

    Args:
        pdf_directory (str): Path to directory containing PDF files

    Returns:
        pd.DataFrame with columns: filename, num_pages, text, status
    """
    results = []

    pdf_files = [f for f in os.listdir(pdf_directory) if f.endswith(".pdf")]
    print(f"Found {len(pdf_files)} PDF files")

    for filename in pdf_files:
        pdf_path = os.path.join(pdf_directory, filename)
        print(f"Processing: {filename}")

        try:
            with open(pdf_path, "rb") as file:
                reader = PyPDF2.PdfReader(file)
                text = ""
                for page in reader.pages:
                    text += page.extract_text() + "\n\n"

                results.append(
                    {
                        "filename": filename,
                        "num_pages": len(reader.pages),
                        "text": text.strip(),
                        "status": "Success",
                    }
                )

        except Exception as e:
            print(f"Error processing {filename}: {str(e)}")
            results.append(
                {
                    "filename": filename,
                    "num_pages": None,
                    "text": None,
                    "status": f"Failed: {str(e)}",
                }
            )

    df = pd.DataFrame(results)

    print("\nExtraction Summary:")
    print(f"Total PDFs processed: {len(df)}")
    print(f"Successfully extracted: {sum(df['status'] == 'Success')}")
    print(f"Failed: {sum(df['status'] != 'Success')}")

    return df
