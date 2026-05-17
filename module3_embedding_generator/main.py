import json

from config import OUTPUT_PATH

from services.validation_service import validate_input
from services.preprocessing_service import clean_text
from services.embedding_service import generate_embedding

from utils.formatter import format_output
from utils.logger import log


def main():

    try:

        log("Loading input data...")

        with open("input/sample_input.json", "r") as file:
            input_data = json.load(file)

        log("Validating input data...")

        validate_input(input_data)

        log("Cleaning summary text...")

        cleaned_summary = clean_text(
            input_data["generated_summary"]
        )

        input_data["generated_summary"] = cleaned_summary

        log("Generating embeddings...")

        embedding_data = generate_embedding(cleaned_summary)

        log("Formatting final output...")

        final_output = format_output(
            input_data,
            embedding_data
        )

        log("Saving output JSON...")

        with open(OUTPUT_PATH, "w") as outfile:
            json.dump(final_output, outfile, indent=4)

        log("Embedding generation completed successfully!")

    except Exception as e:

        error_output = {
            "processing_status": "failed",
            "error": str(e)
        }

        with open(OUTPUT_PATH, "w") as outfile:
            json.dump(error_output, outfile, indent=4)

        log(f"ERROR: {str(e)}")


if __name__ == "__main__":
    main()