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
    PYTHON_KEYWORDS = ["class", "def", "if", "else", "is", "not", "for", "while", "import", "print", "True", "False", "and", "or", "as", "assert", "await", "async", "del", "elif", "break", "continue", "except", "finally", "from", "global", "in", "lambda", "nonlocal", "pass", "raise", "try", "with", "yield"]   # Khởi tạo tập hợp các từ khóa của Python

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
    JAVA_KEYWORDS = ["abstract", "assert", "boolean", "break", "byte", "case", "catch", "char", "class", "const", "continue", "default", "do", "double", "else", "enum", "extends", "final", "finally", "float", "for", "goto", "if", "implements", "import", "instanceof", "int", "interface", "long", "native", "new", "package", "private", "protected", "public", "return", "short", "static", "strictfp", "super", "switch", "synchronized", "this", "throw", "throws", "transient", "try", "void", "volatile", "while"]   # Khởi tạo tập hợp các từ khóa của Java

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
    CPP_KEYWORDS = ["and", "and_eq", "asm", "auto", "bitand", "bitor", "bool", "break", "case", "catch", "char", "class", "compl", "const", "const_cast", "continue", "default", "delete", "do", "double", "dynamic_cast", "else", "enum", "explicit", "export", "extern", "false", "float", "for", "friend", "goto", "if", "inline", "int", "long", "mutable", "namespace", "new", "not", "not_eq", "operator", "or", "or_eq", "private", "protected", "public", "register", "reinterpret_cast", "return", "short", "signed", "sizeof", "static", "static_cast", "struct", "switch", "template", "this", "throw", "true", "try", "typedef", "typeid", "typename", "union", "unsigned", "using", "virtual", "void", "volatile", "wchar_t", "while", "xor", "xor_eq"]   # Khởi tạo tập hợp các từ khóa của C++

    # Overwrite lại phương thức preprocess của lớp cha để tiền xử lý đoạn code C++
    def preprocess(self, code: str) -> str:
        code = re.sub(r"\/\/.*", " ", code)   # Xóa các comment trong đoạn code
        code = re.sub(r"\s+", " ", code)    # Thay thế nhiều khoảng trắng liên tiếp bằng một khoảng trắng
        return code

    # Overwrite lại phương thức extract_keywords của lớp cha để trích xuất các từ khóa của Python
    def extract_keywords(self, code: str) -> Set[str]:
        return set(word for word in code.split() if word in self.CPP_KEYWORDS)
