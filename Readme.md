### <a href="#giriş">GİRİŞ</a>
### <a href="#algoritmalar">ALGORİTMALAR</a>
### <a href="#aşama">AŞAMALAR</a>
### <a href="#performanslar">PERFORMANS</a>
### <a href="#kullanım">KULLANIM</a>

***

<h3><a name="giriş">GİRİŞ</a></h3>

Fibonacci,ackermann ve factorial algoritmalarının, Flask kullanarak REST API mimarisiyle web servis oluşturulmuştur.

Flask küçük projeler için daha hızlı olduğundan ve kullanılacak bir veri tabanı olmadığından tercih edilmiştir.

JSON ile çalışmasından dolayı ise REST kullanılmıştır.

CProfile paketi kullanılarak programın çeşitli bölümlerinin ne sıklıkta ve ne kadar süreyle yürütüldüğü izlenmiştir.

Docker kullanılarak proje, işletim sistemi seviyesinde sanallaştırılmıştır.

***

<h3><a name="algoritmalar">ALGORİTMALAR</a></h3>

#### **1-Fibonacci**

Fibonacci dizisi, her sayının kendinden önceki ile toplanması sonucu oluşan bir sayı dizisidir. Bu şekilde devam eden bu dizide sayılar birbirleriyle oranlandığında altın oran ortaya çıkar, yani bir sayı kendisinden önceki sayıya bölündüğünde altın orana gittikçe yaklaşan bir dizi elde edilir. 

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55 ...

- 2, önündeki iki sayıyı (1+1) toplanarak bulunur.
- 3, önündeki iki sayıyı (1+2) toplayarak bulunur.
- 5, (2+3)

Belirli bir sayının(pozitif tam sayı) fibonacci karşılığı dizide, bu değere denk gelen sayısır. Örneğin ;
  - fibonacci(0)=0
  - fibonacci(9)=34

#### **2-Ackermann**

Ackermann işlevi, ismini Wilhelm Ackermann'dan alan oldukça hızlı büyüyen bir işlevdir. Özyinelemeli olup işlevlerin göreceli olarak en basitidir. Özellikle karmaşıklık çözümlemesinde kullanılır.
      
              n+1 , m=0;  

    A(m,n) =  A(m-1,1) , n=0;

              A(m-1,A(m,n-1)), diğer 

#### **3-Faktöriyel**

Faktöriyel, matematikte, sağına ünlem işareti konulmuş sayıya verilen isim, daha genel olan Gama fonksiyonunun tam sayılarla sınırlanmış özel bir durumudur. 1'den başlayarak belirli bir sayma sayısına kadar olan sayıların çarpımına o sayının faktöriyeli denir.


***


<h3><a name="aşama">AŞAMALAR</a></h3>

### 1.Kısım 

Fibonacci,ackermann ve factorial algoritmaları için fibonacci.py, ackermann.py ve factorial.py script dosyalarında algoritmalar bulunmaktadır.

Ana program olan main.py dosyasında oluşturulan algoritma dosyaları import edilir.

### 2.Kısım

Yazılan algoritmaların web service mimarisini oluşturmak için Flask kullanılır. Gerekli uç noktalar oluşturularak REST API mimarisi main.py dosyasında tamamlanır.

### 3.Kısım

CProfile paketi import edilerek, oluşturulan her uç nokta için performanslar izlenir.

### 4.Kısım

Oluşturulan Flask uygulaması Docker kullanılarak konteyner haline getirilmiştir.

***


<h3><a name="performanslar">PERFORMANS</a></h3>


fibonacci(10) için oluşan profile çıktısı.

11 function calls in 0.000 seconds

   Ordered by: standard name
   
|ncalls | tottime | percall | cumtime|  percall | filename:lineno(function) |
| ----- | ------  | ----- | ----- |----- |----- |
| 1   | 0.000  |  0.000 |   0.000 |   0.000 |fibonacci.py:3(calculate_fibonacci)|
| 9   | 0.000   | 0.000 |   0.000  |  0.000| {method 'append' of 'list' objects}|
|1  |  0.000 |   0.000 |   0.000  |  0.000 |{method 'disable' of '_lsprof.Profiler' objects}  

***

<h3><a name="kullanım">KULLANIM</a></h3>

Proje dosyası indirilerek main.py ya da Dockerfile ile konteyner oluşturularak çalıştırılır. 


  
