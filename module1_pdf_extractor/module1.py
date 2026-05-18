import os
import sys
import json
import argparse

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import fitz  # type: ignore

try:
    import fitz
except Exception:
    print("Missing dependency: PyMuPDF (fitz). Install with: pip install PyMuPDF")
    raise


def process_pdf(pdf_path: str, output_folder: str, output_json: str):
    if not os.path.isfile(pdf_path):
        raise FileNotFoundError(f"PDF not found: {pdf_path}")

    os.makedirs(output_folder, exist_ok=True)

    pdf_document = fitz.open(pdf_path)
    total_pages = len(pdf_document)
    print("Total Pages in PDF:", total_pages)

    module_output = []

    for page_index in range(total_pages):
        page = pdf_document[page_index]
        page_number = page_index + 1

        raw_text = page.get_text("text")
        if isinstance(raw_text, str):
            extracted_text = raw_text.strip()
        elif isinstance(raw_text, (list, tuple)):
            extracted_text = " ".join(map(str, raw_text)).strip()
        else:
            extracted_text = str(raw_text).strip()
        images = page.get_images(full=True)

        if images:
            image_filename = f"page_{page_number}.png"
            image_path = os.path.join(output_folder, image_filename)

            pix = page.get_pixmap()
            pix.save(image_path)

            page_data = {
                "page_number": page_number,
                "content_type": "Image",
                "extracted_content": extracted_text or None,
                "generated_image_path": image_path,
                "content_location": f"Page {page_number}"
            }
        else:
            page_data = {
                "page_number": page_number,
                "content_type": "Text",
                "extracted_content": extracted_text,
                "generated_image_path": None,
                "content_location": f"Page {page_number}"
            }

        module_output.append(page_data)

    with open(output_json, "w", encoding="utf-8") as f:
        json.dump(module_output, f, indent=4, ensure_ascii=False)

    text_pages = sum(1 for p in module_output if p["content_type"] == "Text")
    image_pages = len(module_output) - text_pages

    print("PDF Processing Completed Successfully!")
    print("Module 1 Output Saved Successfully!")
    print("Text Pages:", text_pages)
    print("Image Pages:", image_pages)

    for i in range(min(3, total_pages)):
        page = pdf_document[i]
        raw_text = page.get_text("text")
        if isinstance(raw_text, str):
            text = raw_text
        elif isinstance(raw_text, (list, tuple)):
            text = " ".join(map(str, raw_text))
        else:
            text = str(raw_text)

        print(f"\n----- PAGE {i+1} -----")
        print(text[:1000])


def main(argv=None):
    parser = argparse.ArgumentParser(description="Extract text/images from a PDF and save metadata as JSON.")
    parser.add_argument("pdf", nargs="?", default=os.path.join("Input", "sample.pdf"), help="Path to input PDF")
    parser.add_argument("--out-folder", default="output_images", help="Folder to save page images")
    parser.add_argument("--out-json", default="module1_output.json", help="Output JSON file")

    args = parser.parse_args(argv)

    try:
        process_pdf(args.pdf, args.out_folder, args.out_json)
    except FileNotFoundError as e:
        print(e)
        sys.exit(2)
    except Exception as e:
        print("An error occurred while processing the PDF:", e)
        sys.exit(1)


if __name__ == "__main__":
    main()
