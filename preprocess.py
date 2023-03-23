import re
from typing import Set

# Định nghĩa lớp Preprocessor với hai phương thức là preprocess() và extract_keywords()
class Preprocessor:
    def preprocess(self, code: str) -> str:
        pass
    
    def extract_keywords(self, code: str) -> Set[str]:
        pass

# Định nghĩa lớp PythonPreprocessor, kế thừa từ lớp Preprocessor
class PythonPreprocessor(Preprocessor):
    PYTHON_KEYWORDS = {"True", "try", "while", "with", "yield"}   # Khởi tạo tập hợp các từ khóa của Python

    # Overwrite lại phương thức preprocess của lớp cha để tiền xử lý đoạn code Python
    def preprocess(self, code: str) -> str:
        code = re.sub(r"#.*", "", code)   # Xóa các comment trong đoạn code
        code = re.sub(r"\s+", " ", code)    # Thay thế nhiều khoảng trắng liên tiếp bằng một khoảng trắng
        return code

    # Overwrite lại phương thức extract_keywords của lớp cha để trích xuất các từ khóa của Python
    def extract_keywords(self, code: str) -> Set[str]:
        return set(word for word in code.split() if word in self.PYTHON_KEYWORDS)

# Định nghĩa lớp JavaPreprocessor, kế thừa từ lớp Preprocessor
class JavaPreprocessor(Preprocessor):
    JAVA_KEYWORDS = {"try", "void", "volatile", "while"}   # Khởi tạo tập hợp các từ khóa của Java

    # Overwrite lại phương thức preprocess của lớp cha để tiền xử lý đoạn code Java
    def preprocess(self, code: str) -> str:   
        code = re.sub(r"\/\/.*", " ", code)   # Xóa các comment trong đoạn code
        code = re.sub(r"\s+", " ", code)    # Thay thế nhiều khoảng trắng liên tiếp bằng một khoảng trắng
        return code

    # Overwrite lại phương thức extract_keywords của lớp cha để trích xuất các từ khóa của Python
    def extract_keywords(self, code: str) -> Set[str]:
        return set(word for word in code.split() if word in self.JAVA_KEYWORDS)

# Định nghĩa lớp CppPreprocessor, kế thừa từ lớp Preprocessor
class CppPreprocessor(Preprocessor):
    CPP_KEYWORDS = {"alignas", "alignof", "and"}   # Khởi tạo tập hợp các từ khóa của C++

    # Overwrite lại phương thức preprocess của lớp cha để tiền xử lý đoạn code C++
    def preprocess(self, code: str) -> str:
        code = re.sub(r"\/\/.*", " ", code)   # Xóa các comment trong đoạn code
        code = re.sub(r"\s+", " ", code)    # Thay thế nhiều khoảng trắng liên tiếp bằng một khoảng trắng
        return code

    # Overwrite lại phương thức extract_keywords của lớp cha để trích xuất các từ khóa của Python
    def extract_keywords(self, code: str) -> Set[str]:
        return set(word for word in code.split() if word in self.CPP_KEYWORDS)
