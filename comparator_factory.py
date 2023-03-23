from preprocess import PythonPreprocessor, JavaPreprocessor, CppPreprocessor, Preprocessor
from comparator import CodeComparator


class ComparatorFactory:   #Factory Pattern (Mẫu Factory), được sử dụng để tạo ra các đối tượng tùy theo điều kiện đầu vào
    SUPPORTED_LANGUAGES = {"python", "java", "cpp"}

    @staticmethod 
    def is_supported_language(language: str) -> bool:     #nhận vào một string language và trả về True nếu language được hỗ trợ và False nếu ngược lại. Để kiểm tra xem một ngôn ngữ có được hỗ trợ hay không, method này so sánh language với tập hợp các ngôn ngữ được hỗ trợ đã được định nghĩa trong SUPPORTED_LANGUAGES
        return language.lower() in ComparatorFactory.SUPPORTED_LANGUAGES

    @staticmethod     
    def create(language: str, code1: str, code2: str) -> CodeComparator:     # Tạo hàm create để tạo ra instance của CodeComparator với ngôn ngữ và đoạn code đầu vào
        if not ComparatorFactory.is_supported_language(language):
            raise ValueError(f"Unsupported language: {language}")      # Nếu ngôn ngữ lập trình không được hỗ trợ ném ra lỗi ValueError

        if language == "python":
            preprocessor = PythonPreprocessor()
        elif language == "java":
            preprocessor = JavaPreprocessor()   #tạo instance tương ứng mỗi class ngôn ngữ
        elif language == "cpp":
            preprocessor = CppPreprocessor()

        return CodeComparator(code1, code2, preprocessor)     # Trả về instance của CodeComparator với đoạn code và preprocessor đã được tiền xử lí
