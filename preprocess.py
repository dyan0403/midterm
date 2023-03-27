import re
from abc import ABC, abstractmethod

class Processor(ABC):
    @abstractmethod
    def preprocess(self, code: str) :
        pass
    

class Preprocessor(Processor):
    def preprocess(self, code: str) :
        pass


class PythonPreprocessor(Preprocessor):
    PYTHON_KEYWORDS = ["class", "def", "if", "else", "is", "not", "for", "while", "import", "print", "True", "False", "and", "or", "as", "assert", "await", "async", "del", "elif", "break", "continue", "except", "finally", "from", "global", "in", "lambda", "nonlocal", "pass", "raise", "try", "with", "yield"]

    def preprocess(self, code: str) -> str:
        code = re.sub(r"#.*", "", code)  
        code = re.sub(r"\s+", " ", code)    
        words = filter(lambda word: word not in JavaPreprocessor.PYTHONPYTHON_KEYWORDS, code.split())
        return " ".join(words)


class JavaPreprocessor(Preprocessor):
    JAVA_KEYWORDS = ["abstract", "assert", "boolean", "break", "byte", "case", "catch", "char", "class", "const", "continue", "default", "do", "double", "else", "enum", "extends", "final", "finally", "float", "for", "goto", "if", "implements", "import", "instanceof", "int", "interface", "long", "native", "new", "package", "private", "protected", "public", "return", "short", "static", "strictfp", "super", "switch", "synchronized", "this", "throw", "throws", "transient", "try", "void", "volatile", "while"]

    def preprocess(self, code: str) -> str:   
        code = re.sub(r"\/\/.*", " ", code)
        code = re.sub(r"\s+", " ", code)
        words = filter(lambda word: word not in JavaPreprocessor.JAVA_KEYWORDS, code.split())
        return " ".join(words)



class CppPreprocessor(Preprocessor): 
    CPP_KEYWORDS = ["and", "and_eq", "asm", "auto", "bitand", "bitor", "bool", "break", "case", "catch", "char", "class", "compl", "const", "const_cast", "continue", "default", "delete", "do", "double", "dynamic_cast", "else", "enum", "explicit", "export", "extern", "false", "float", "for", "friend", "goto", "if", "inline", "int", "long", "mutable", "namespace", "new", "not", "not_eq", "operator", "or", "or_eq", "private", "protected", "public", "register", "reinterpret_cast", "return", "short", "signed", "sizeof", "static", "static_cast", "struct", "switch", "template", "this", "throw", "true", "try", "typedef", "typeid", "typename", "union", "unsigned", "using", "virtual", "void", "volatile", "wchar_t", "while", "xor", "xor_eq"]


    def preprocess(self, code: str) -> str:
        code = re.sub(r"\/\/.*", " ", code)   
        code = re.sub(r"\s+", " ", code)   
        words = filter(lambda word: word not in JavaPreprocessor.CPP_KEYWORDS, code.split())
        return " ".join(words)
