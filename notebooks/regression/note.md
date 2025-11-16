# SCRIPT

Trước khi xây dựng một mô hình bất kì, việc hiểu và nắm bắt được xu hướng chính, các pattern trong dữ liệu là điều bắt buộc và đó là lí do mà ta sẽ tiến hành bước EDA (a.k.a phân tích khám phá dữ liệu)

## Explotoraty data analysis

### Phân tích đơn biến

- Đầu tiên là `độ nổi tiếng` của bộ phim, ta có thể thấy, phần lớn phim có độ nổi tiếng nằm trong mức 0.5-4, độ nổi tiếng không cao, nhưng trong box plot, ta có thể thấy sự tồn tại của khá nhiều điểm outliners, tức là có nhiều phim có độ nổi tiếng cực kì lớn.

- Tiếp theo là `điểm trung bình đánh giá`, nhìn vào hist plot, ta có thể thấy, phần lớn điểm đánh giá nằm trong mức 5-6, thuộc dạng chuông, hơn lệch trái, tuy nhiên boxplot cũng nói lên rằng, tồn tại những bộ phim có lượt đánh giá cực kì thấp, hoặc cực kì cao ở hai đầu.

- Bên cạnh đó, các bộ phim có xu hướng được sản xuất bởi 1-2 công ty sản xuất, mặc dù cũng tồn tại các bộ phim đa quốc gia, nhưng điều đó là rất hiếm, phù hợp với xu hướng hiện tại.

- Vậy tổng số lượng nhân viên đoàn làm phim cùng với diễn viên có xu hướng như thế nào? Nhìn vào hist, ta có thể thấy rằng, hầu hết các bộ phim có tổng nhân lực nằm trong mức 10-20 (thuộc mức trung bình), tuy nhiên boxplot cũng cho thấy rằng, có những bộ phim có nhân lực là cực kì lớn (outliners), bên cạnh đó, trong số diễn viên, ta nhận thấy được 1 xu hướng rằng, tỉ lệ diễn viên nữ không thực sự cao, nằm trong mức 0.2-0.4

- Thời lượng phim cho ta một insight khá thứ vị, ta nhận thấy rằng hầu hết các bộ phim có thời lượng đang nằm trong mức 90-100, ta nhận thấy rỡ rằng, đây đang là mức phim tiêu chuẩn đang được nhiều công ty ưa chuộng (ta sẽ thấy sự xu hướng của thời lượng phim ở phần phân tích theo chuỗi thời gian).

- Tiếp theo là hai biến vô cùng quan trọng, ngân sách và doanh thu của bộ phim. Nhìn vào 2 hist và 2 box, ta thấy hist đang có xu hướng lệch phải mạnh, hâu hết các phim có ngân sách nằm trong khoảng 150-750 triệu USD, doanh thu nằm trong khoảng 100 triệu-2 tỉ USD, box plot cho thấy sự tồn tại của outliners của cả ngân sách và doanh thu. Ta cũng có thể xem được top 10 bộ phim đắc đỏ trong dataset (có thể kể đến loạt phim Cướp biển vùng Caribbean, Tangled của Disney, Loạt phim transformer, các phim có sử dụng kỹ thuật CGI, điều đó giải thích rằng ngân sách luôn thuộc hàng top), và top 10 bộ phim có doanh thu cao nhất (Như Avatar, loạt phim StarWar hay phim Titanic, đây chính là các bộ phim đã từng gây sốt trên các phòng vé quốc tế).

- Tiếp theo là việc phân tích liên quan đến một vài biến định tính. Đầu tiên là thể loại phim, ta có thể nhận thấy một vài thể loại rất phổ biến như Drama, comedy, Thriller và Action.

- Ngoài ra khi phân tích ngày phát hành phim, ta nhận thấy một xu hướng khá là thú vị, phân lớn các phim được phát hành vào ngày thứ 6. Tại sao lại như vậy? Thật ra điều này nằm trong chiến lược kinh doanh của công ti sản xuất, đơn giản chi là thứ 6 là mở đầu của cuối tuần, phát hành phim vào thời điểm này để tối ưu hóa lợi nhuận, bởi vì người xem sẽ có nhiều thời gian rảnh để tận hưởng. Việc phát hành vào các ngày khác có tồn tại nhưng không phổ biến như thứ 6.

### Phân tích đa biến

- Sau khi đã phân tích đơn biến, ta sẽ tiến hành xem thử giữa các biến với nhau, ta có thể rút ra được nhận xét gì?

- Một bộ phim có hoặc không nằm trong một collection hoặc một series phim nào đó, vậy điều đó có ảnh hường gì đến ngân sách và doanh thu? Ta sẽ xem việc phân bố ngân sách và doanh thu trong 2 trường hợp, phim thuộc chuỗi phim và phim độc lập. Một xu hướng khá rõ ràng, các phim thuộc chuỗi phim/collection có xu hướng có ngân sách và doanh thu cao hơn hẳn, thậm chí nếu xét trung bình, phim thuộc collection có ngân sách gấp đôi và doanh thu gấp 4 lần phim độc lập. Điều này là phù hợp với thực tế khi những bộ phim trong chuỗi phim luôn được đầu tư vô cùng kỹ lưỡng (có thể kể đến Harry Potter, Star War, Chúa thể của những chiếc nhẫn), và vì phim thuộc chuỗi phim, việc người xem có xu hướng mong chờ và đón nhận hơn phim độc lập dẫn đến sự khác biệt về doanh thu nhưng trong hình minh họa.

- Bên cạnh đó, thể loại phim cũng có ảnh hướng sâu sắc đến ngân sách và doanh thu cũng phim. Các phim thuộc thể loại phiêu lưu, kỳ ảo, hành động, khoa học viễn tưởng có ngân sách cao hơn các phim thuộc các thể loại còn lại, điều này cũng có thể giải thích được do sự đầu tư về đạo cụ, hóa trang, cũng như kỹ thuật CGI trong các thể loại phim này, về doanh thu, không bất ngờ khi thể loại phiêu lưu luôn là thể loại cực kì ăn khách, theo sau với thể loại gia đình (một phát hiện khá thú vị khi ngân sách của thể loại gia đình thuộc mức khá thấp), hành động và khoa học viễn tưởng.

### Phân tích theo chuỗi thời gian

- Trở lại với thời lượng phim, ta có thể thấy thời lượng của phim có xu hướng tăng qua các năm từ các năm 1880-1940, thời gian phim tăng vọt từ vài phút lên khoàng 80-90 phút, điều này có thể giải thích bằng sự phát triển của ngành công nghiệp phim, cùng với sự phát triển của máy móc, sau đó, thời lượng phim giữ mức ổn định xung quang mức 100 phút, đây cũng chính là mức thời lượng tiêu chuẩn hiện tại mà chúng ta đã quen thuộc.

- Bên cạnh đó, sau khi được điều chỉnh lạm phát, ta có thể thấy rõ rằng ngân sách và doanh thu của các bộ phim có xu hướng tăng theo từng năm, điều này có nghĩa rằng, các bộ phim được ngày càng đầu tư, chau chuốt cùng với sự đón nhận của khán giả cũng tăng lên trong những năm gần đây.

### Insight

- Từ việc phân tích trên, ta có thể rút ra một vài key insight, để tiến hành chọn features hoặc xử lý dữ liệu khi xây dựng một model.
- _Read slide please!_

## Linear regression

Sau khi đã phân tích và nắm được các key insight của bộ dữ liệu, bước tiếp theo là làm cách nào để từ dữ liệu, ta xây dựng được một mô hình để giải quyết bài toán thực tế: `Ước lượng doanh thu của một bộ phim`? Để giải quyết bài toán trên, trong phần này, em đã quyết định lựa chọn `Mô hình hồi quy tuyến tính` để giải quyết bài toán trên.

### Tại sao lại là mô hình hồi quy tuyến tính?

- _Read slide_

### Các bước để xây dựng mô hình

- Trên slide là các bước mà em đã thực hiện để xây dựng một mô hình _Hồi quy tuyến tính_ hoàn chỉnh.
  - Data cleaning: Từ insight trong EDA
  - Feature engineering: Từ insight của EDA, một vài các feature được tạo ra như
  - Phân loại các features thành 3 cụm: numeric, boolean, categorical features
  - Sau bước tiền xử lý của feature engineering, ta có 11 đặc trưng dùng để dự đoán doanh thu cua một bộ phim
  - Data set cuối cùng được chia thành 0.8 train và 0.2 thực hiện test và model được fit sử dụng phần train của tập dữ liệu trên.

### Kết quả

- _Read slide_

### Hạn chế

- _Read slide_ with `Residual plot`

## Conclusion

- Đó chính là phần phân tích khám phá dữ liệu cùng với mô hình hồi quy tuyến tính để giải thích bài toán dự đoán doanh thu, tiếp theo là việc sử dụng các insight trong EDA để tiến hành xây dựng một classifier để phân loại liệu rằng một bộ phim có `thành công` hay `thất bại`.

## Author

- LE BUI TRUNG DUNG

## CHANGE LOG

- 11/16/2025: Write thís scipt
