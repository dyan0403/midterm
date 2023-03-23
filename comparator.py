import difflib
from preprocess import Preprocessor
from typing import Set

# Tạo class CodeComparator để so sánh 2 đoạn code
class CodeComparator:
    def __init__(self, code1: str, code2: str, preprocessor: Preprocessor):
        self.code1 = preprocessor.preprocess(code1)   # Tiền xử lý đoạn code thứ nhất
        self.code2 = preprocessor.preprocess(code2)   # Tiền xử lý đoạn code thứ hai
        self.keywords1 = preprocessor.extract_keywords(code1)     #2 đoạn mã nguồn code1 và code2 sẽ được tiền xử lý bằng preprocessor được truyền vào 
        self.keywords2 = preprocessor.extract_keywords(code2)     #để loại bỏ các ký tự không cần thiết và chuẩn hóa các từ khóa trong mã nguồn, sau đó lưu trữ chúng vào self.code1 và self.code2.

    # Tạo hàm compare để so sánh độ tương đồng giữa 2 đoạn code      
    def compare(self) -> float:     
        d = difflib.SequenceMatcher(None, self.code1, self.code2)     # Sử dụng module "difflib" để tính toán độ tương đồng
        similarity = d.ratio() * 100
        return similarity
