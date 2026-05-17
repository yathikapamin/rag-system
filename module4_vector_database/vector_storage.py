import os
import faiss
import numpy as np
import pickle
from datetime import datetime


class VectorDBStorage:

    def __init__(self, db_folder="vector_store"):

        # Create vector store folder
        self.db_folder = db_folder
        os.makedirs(db_folder, exist_ok=True)

        # File paths
        self.index_path = os.path.join(
            db_folder,
            "faiss_index.bin"
        )

        self.metadata_path = os.path.join(
            db_folder,
            "metadata.pkl"
        )

        self.index = None
        self.metadata = []

    def create_index(self, embedding_dimension):

        # Create FAISS index
        self.index = faiss.IndexFlatL2(
            embedding_dimension
        )

    def store_records(self, module3_output):

        if not module3_output:
            return {
                "status": "failed",
                "message": "No input data received"
            }

        # Get embedding size
        embedding_dimension = len(
            module3_output[0]["embedding"]
        )

        # Create vector index
        if self.index is None:
            self.create_index(
                embedding_dimension
            )

        embeddings = []

        for item in module3_output:

            embedding = np.array(
                item["embedding"],
                dtype=np.float32
            )

            embeddings.append(embedding)

            # Metadata storage
            metadata_record = {
                "document_name":
                    item.get("document_name"),

                "page_number":
                    item.get("page_number"),

                "content_type":
                    item.get("content_type"),

                "summary":
                    item.get("summary"),

                "location":
                    item.get(
                        "metadata",
                        {}
                    ).get("location"),

                "timestamp":
                    str(datetime.now())
            }

            self.metadata.append(
                metadata_record
            )

        # Convert embeddings
        embeddings_np = np.array(
            embeddings,
            dtype=np.float32
        )

        # Add vectors to FAISS
        self.index.add(
            embeddings_np
        )

        # Save vector DB
        faiss.write_index(
            self.index,
            self.index_path
        )

        # Save metadata
        with open(
            self.metadata_path,
            "wb"
        ) as file:
            pickle.dump(
                self.metadata,
                file
            )

        return {
            "status": "success",
            "stored_records":
                len(module3_output),

            "vector_db_path":
                self.index_path,

            "metadata_path":
                self.metadata_path
        }
