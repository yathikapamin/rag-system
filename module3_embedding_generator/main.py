import json

from embedding_module import (
    EmbeddingGenerator
)


INPUT_FILE = "sample_input.json"

OUTPUT_FILE = "sample_output.json"


def main():

    try:

        with open(
            INPUT_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            input_data = json.load(file)

        generator = (
            EmbeddingGenerator()
        )

        result = generator.process(
            input_data
        )

        with open(
            OUTPUT_FILE,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                result,
                file,
                indent=4
            )

        print(
            "Embedding generation successful."
        )

    except Exception as error:

        print(
            f"Error: {error}"
        )


if __name__ == "__main__":

    main()