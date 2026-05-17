import json
from vector_storage import VectorDBStorage


def main():

    # Read input from Module 3 output
    with open("sample_input.json", "r") as file:
        module3_output = json.load(file)

    # Initialize vector storage
    vector_db = VectorDBStorage()

    # Store records
    result = vector_db.store_records(module3_output)

    # Print result
    print("\nModule 4 Output:")
    print(json.dumps(result, indent=4))


if __name__ == "__main__":
    main()
