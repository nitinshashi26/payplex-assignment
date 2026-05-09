from paddleocr import PaddleOCR
from transformers import pipeline

ocr_engine = PaddleOCR(use_angle_cls=True, lang="en")
ner_pipeline = pipeline("ner", model="dslim/bert-base-NER")

def process_document(filepath: str):
    ocr_result = ocr_engine.ocr(filepath, cls=True)
    text = " ".join([line[1][0] for line in ocr_result[0]])
    entities = ner_pipeline(text)
    return {"extracted_text": text, "entities": entities}
