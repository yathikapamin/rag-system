import json

from embedding_module import (
    EmbeddingGenerator
)

INPUT_FILE = (
    "sample_input.json"
)

OUTPUT_FILE = (
    "sample_output.json"
)


def main():

    try:

        with open(
            INPUT_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            input_data = (
                json.load(file)
            )

        generator = (
            EmbeddingGenerator()
        )

        output = (
            generator.process(
                input_data
            )
        )

        with open(
            OUTPUT_FILE,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                output,
                file,
                indent=4
            )

        print(
            "Embeddings generated successfully."
        )

    except Exception as e:

        print(
            f"Error: {e}"
        )


if __name__ == "__main__":

    main()