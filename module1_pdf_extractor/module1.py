import os
import sys
import json
import argparse

try:
    import fitz as fitz  # type: ignore
except ImportError:
    print("Missing dependency: PyMuPDF")
    print("Install using: pip install PyMuPDF")
    sys.exit(1)


class PDFExtractor:
    """
    PDF Extractor Class
    Extracts text and images from PDF pages
    and stores metadata in JSON format.
    """

    def __init__(self, pdf_path, output_folder, output_json):
        self.pdf_path = pdf_path
        self.output_folder = output_folder
        self.output_json = output_json
        self.module_output = []

    def validate_pdf(self):
        """Check whether PDF file exists."""
        if not os.path.isfile(self.pdf_path):
            raise FileNotFoundError(
                f"PDF file not found: {self.pdf_path}"
            )

    def create_output_folder(self):
        """Create output folder if not present."""
        os.makedirs(self.output_folder, exist_ok=True)

    def extract_content(self):
        """Extract text and images from PDF."""

        self.validate_pdf()
        self.create_output_folder()

        pdf_document = fitz.open(self.pdf_path)

        total_pages = len(pdf_document)
        print(f"Total Pages in PDF: {total_pages}")

        for page_index in range(total_pages):

            page = pdf_document[page_index]
            page_number = page_index + 1

            raw_text = page.get_text("text")

            if isinstance(raw_text, str):
                extracted_text = raw_text.strip()
            elif isinstance(raw_text, (list, tuple)):
                extracted_text = " ".join(
                    map(str, raw_text)
                ).strip()
            else:
                extracted_text = str(raw_text).strip()

            images = page.get_images(full=True)

            if images:

                image_filename = f"page_{page_number}.png"
                image_path = os.path.join(
                    self.output_folder,
                    image_filename
                )

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

            self.module_output.append(page_data)

        pdf_document.close()

    def save_json(self):
        """Save extracted data into JSON file."""

        with open(
            self.output_json,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                self.module_output,
                file,
                indent=4,
                ensure_ascii=False
            )

    def display_summary(self):
        """Display extraction summary."""

        text_pages = sum(
            1 for page in self.module_output
            if page["content_type"] == "Text"
        )

        image_pages = len(self.module_output) - text_pages

        print("\nPDF Processing Completed Successfully!")
        print("Module 1 Output Saved Successfully!")
        print(f"Text Pages : {text_pages}")
        print(f"Image Pages: {image_pages}")

    def preview_pages(self, count=3):
        """Preview first few pages."""

        pdf_document = fitz.open(self.pdf_path)

        for i in range(min(count, len(pdf_document))):

            page = pdf_document[i]
            text = page.get_text("text")

            print(f"\n----- PAGE {i + 1} -----")
            print(text[:1000])

        pdf_document.close()

    def run(self):
        """Execute complete extraction process."""

        self.extract_content()
        self.save_json()
        self.display_summary()
        self.preview_pages()


def main():

    parser = argparse.ArgumentParser(
        description="PDF Text and Image Extractor"
    )

    parser.add_argument(
        "pdf",
        nargs="?",
        default=os.path.join(
            "Input",
            "sample.pdf"
        ),
        help="Input PDF file"
    )

    parser.add_argument(
        "--out-folder",
        default="output_images",
        help="Folder to save images"
    )

    parser.add_argument(
        "--out-json",
        default="module1_output.json",
        help="Output JSON file"
    )

    args = parser.parse_args()

    try:

        extractor = PDFExtractor(
            pdf_path=args.pdf,
            output_folder=args.out_folder,
            output_json=args.out_json
        )

        extractor.run()

    except FileNotFoundError as error:
        print(error)
        sys.exit(2)

    except Exception as error:
        print("Error:", error)
        sys.exit(1)


if __name__ == "__main__":
    main()