import requests
import os


def download_pdfs_from_urls(urls, pdf_dir):
    
    failed_urls = []
    failed_ids = []
    timeout_urls = []
    timeout_ids = []

    def download_single_pdf(url, pdf_dir, filename, idx):
        try:
            response = requests.get(url, timeout=90)
            response.raise_for_status()

            filepath = os.path.join(pdf_dir, filename)
            with open(filepath, "wb") as f:
                f.write(response.content)
            return True
        except requests.exceptions.Timeout:
            print(f"Skipping document {idx} due to high wait time (>120 seconds)")
            timeout_urls.append(url)
            timeout_ids.append(idx)
            return False
        except Exception as e:
            print(f"Error downloading {url}: {str(e)}")
            failed_urls.append(url)
            failed_ids.append(idx)
            return False

    os.makedirs(pdf_dir, exist_ok=True)

    for idx, url in enumerate(urls):
        if isinstance(url, str) and url.strip():
            filename = f"doc_{idx}.pdf"
            success = download_single_pdf(url, pdf_dir, filename, idx)
            if not success:
                print(f"Failed to download doc_{idx}")

    print(f"Total failed downloads: {len(failed_urls)}")

    return {
        "failed_urls": failed_urls,
        "failed_ids": failed_ids,
        "timeout_urls": timeout_urls,
        "timeout_ids": timeout_ids,
    }
