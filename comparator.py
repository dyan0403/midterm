import difflib
from preprocess import Preprocessor
from typing import Set

# Tạo class CodeComparator để so sánh 2 đoạn code
class CodeComparator:
    def __init__(self, code1: str, code2: str, preprocessor: Preprocessor):
        self.code1 = preprocessor.preprocess(code1)   
        self.code2 = preprocessor.preprocess(code2)   
   

    def compare(self) -> float:   
        similarity = difflib.SequenceMatcher(None, self.code1, self.code2)
        return similarity.ratio()*100
