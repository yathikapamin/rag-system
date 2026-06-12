import torch
from transformers import AutoTokenizer, AutoModel
from datetime import datetime


class ValidationService:

    @staticmethod
    def validate(data):

        required_fields = [
            "document_id",
            "page_number",
            "content_type",
            "generated_summary"
        ]

        for field in required_fields:

            if field not in data:
                raise ValueError(
                    f"Missing required field: {field}"
                )

        if not data["generated_summary"].strip():
            raise ValueError(
                "generated_summary cannot be empty"
            )

        return True


class PreprocessingService:

    @staticmethod
    def clean_text(text):

        text = text.strip()

        text = " ".join(text.split())

        return text


class EmbeddingService:

    def __init__(self):

        self.model_name = (
            "sentence-transformers/all-MiniLM-L6-v2"
        )

        print("Loading embedding model...")

        self.tokenizer = AutoTokenizer.from_pretrained(
            self.model_name
        )

        self.model = AutoModel.from_pretrained(
            self.model_name
        )

    def mean_pooling(
        self,
        model_output,
        attention_mask
    ):

        token_embeddings = model_output[0]

        input_mask_expanded = (
            attention_mask
            .unsqueeze(-1)
            .expand(token_embeddings.size())
            .float()
        )

        return (
            torch.sum(
                token_embeddings *
                input_mask_expanded,
                1
            )
            /
            torch.clamp(
                input_mask_expanded.sum(1),
                min=1e-9
            )
        )

    def generate_embedding(self, text):

        encoded_input = self.tokenizer(
            text,
            padding=True,
            truncation=True,
            return_tensors="pt"
        )

        with torch.no_grad():

            model_output = self.model(
                **encoded_input
            )

        embedding = self.mean_pooling(
            model_output,
            encoded_input["attention_mask"]
        )

        return embedding[0].tolist()


class Formatter:

    @staticmethod
    def format_output(
        input_data,
        embedding_vector
    ):

        return {

            "document_id":
            input_data["document_id"],

            "page_number":
            input_data["page_number"],

            "content_type":
            input_data["content_type"],

            "generated_summary":
            input_data["generated_summary"],

            "embedding_dimension":
            len(embedding_vector),

            "embedding_vector":
            embedding_vector,

            "processing_status":
            "success",

            "timestamp":
            datetime.now().isoformat()
        }


class EmbeddingGenerator:

    def __init__(self):

        self.validator = ValidationService()

        self.preprocessor = (
            PreprocessingService()
        )

        self.embedding_service = (
            EmbeddingService()
        )

        self.formatter = Formatter()

    def process(self, data):

        self.validator.validate(data)

        cleaned_text = (
            self.preprocessor.clean_text(
                data["generated_summary"]
            )
        )

        data["generated_summary"] = (
            cleaned_text
        )

        embedding = (
            self.embedding_service
            .generate_embedding(
                cleaned_text
            )
        )

        return self.formatter.format_output(
            data,
            embedding
        )