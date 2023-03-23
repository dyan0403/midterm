from comparator_factory import ComparatorFactory

while True:
    try:
        language = input("Bạn cần nhập ngôn ngữ lập trình của 2 đoạn code cần so sánhsánh để sự so sánh được chính xác hơn (python/java/c++): ").lower()
        if ComparatorFactory.is_supported_language(language):
            break
        else:
            print(f"Ngôn ngữ {language} không được hỗ trợ.")   #Yêu cầu người dùng nhập ngôn ngữ lập trình để so sánh
    except:                                                 #kiểm tra xem ngôn ngữ đã nhập có được hỗ trợ bởi factory pattern hay không bằng cách gọi hàm is_supported_language. 
        print("Đã có lỗi xảy ra, vui lòng thử lại.")


while True:
    try:
        code1 = input("Nhập đoạn code 1: ")
        code2 = input("Nhập đoạn code 2: ")    #tạo ra một đối tượng comparator từ factory bằng cách gọi hàm create và truyền vào ngôn ngữ, đoạn code thứ nhất và thứ hai.
        break
    except:
        print("Đã có lỗi xảy ra, vui lòng thử lại.")

#Chương trình gọi phương thức compare của đối tượng comparator để so sánh hai đoạn code.
comparator = ComparatorFactory.create(language, code1, code2)
similarity = comparator.compare()
print(f"Độ giống nhau của 2 đoạn code là: {similarity:.2f}%")
