from gtts import gTTS
import os

def text_to_speech_gtts(text):
    tts = gTTS(text, lang='vi')
    tts.save("output.mp3")
    os.system("start output.mp3")  # Hoặc 'xdg-open' trên Linux

text_to_speech_gtts('''Ngày xửa ngày xưa, trong một khu rừng rậm rạp, có một chú chim sẻ nhỏ tên là Jack. Jack không phải là chú chim lớn nhất hay nhanh nhất trong đàn, nhưng cậu luôn tò mò và thích khám phá những điều mới mẻ.

Một ngày nọ, khi đang bay dạo quanh rừng, Jack tình cờ nhìn thấy một hạt giống lấp lánh dưới ánh mặt trời, nằm gọn trên một tảng đá. Hạt giống ấy khác hẳn những hạt giống mà Jack từng thấy: nó phát sáng như ngọc trai và tỏa ra một mùi thơm dịu dàng. Jack liền nhặt hạt giống ấy lên và mang về tổ.

“Chắc chắn đây là một hạt giống đặc biệt,” Jack nghĩ. Nhưng cậu không biết làm gì với nó, nên quyết định hỏi ý kiến các loài vật khác trong rừng.

Jack bay đến gặp thỏ con trước tiên. Thỏ con nhìn hạt giống, chép miệng nói: “Cậu nên trồng nó xuống đất. Biết đâu nó sẽ mọc thành cây thần kỳ!”

Jack tiếp tục bay đến gặp cụ cú già, người thông thái nhất trong khu rừng. Cụ cú nhìn hạt giống qua cặp kính của mình và trầm ngâm: “Hạt giống này hiếm lắm, Jack ạ. Nhưng nó chỉ phát triển nếu được chăm sóc bằng tình yêu và sự kiên nhẫn.”

Nghe lời khuyên, Jack mang hạt giống về, đào một cái lỗ nhỏ dưới đất và nhẹ nhàng trồng nó. Từ hôm đó, ngày nào Jack cũng bay đi tìm nước, kiếm chút phân bón từ những chiếc lá mục, và trò chuyện cùng hạt giống mỗi buổi sáng.

Thời gian trôi qua, hạt giống bắt đầu nảy mầm, lớn lên thành một cây non xinh đẹp. Nhưng điều kỳ diệu chưa dừng lại ở đó. Một buổi sáng, khi ánh bình minh đầu tiên chiếu xuống, cây mọc lên những bông hoa rực rỡ tỏa sáng như những viên kim cương. Từ mỗi bông hoa, rơi xuống những hạt giống mới lấp lánh, khiến cả khu rừng tràn ngập ánh sáng.

Nhờ sự chăm sóc của Jack, khu rừng trở nên sống động hơn bao giờ hết. Các loài vật đều tụ họp xung quanh cây thần kỳ để chiêm ngưỡng vẻ đẹp của nó. Jack không chỉ tìm thấy một hạt giống đặc biệt mà còn học được rằng, chỉ cần có tình yêu và sự kiên nhẫn, những điều nhỏ bé nhất cũng có thể trở thành phép màu.

''')
