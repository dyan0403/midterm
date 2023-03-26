from comparator_factory import ComparatorFactory

while True:
    try:
        language = input("Nhập ngôn ngữ lập trình của đoạn code (python/java/c++): ").lower()
        if not ComparatorFactory.is_supported_language(language):
            print(f"Ngôn ngữ {language} không được hỗ trợ.")
        else:
            break
    except Exception as e:
        print(f"Đã có lỗi xảy ra: {e}")

while True:
    try:
        code1 = input("Nhập đoạn code 1: ")
        code2 = input("Nhập đoạn code 2: ")    
        break
    except Exception as e:
        print(f"Đã có lỗi xảy ra: {e}")

try:
    comparator = ComparatorFactory.create(language, code1, code2)
    similarity = comparator.compare()
    print(f"Độ giống nhau của 2 đoạn code là: {similarity:.2f}%")
except ValueError as e:
    print(f"Lỗi: {e}")
except Exception as e:
    print(f"Đã có lỗi xảy ra: {e}")
