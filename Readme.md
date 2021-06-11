## <a href="#giriş">GİRİŞ</a>


### [ALGORİTMALAR](#ALGORİTMALAR)

### [AŞAMALAR](#AŞAMALAR)

### [PERFORMANS](#PERFORMANS)

### <a href="#kullanım">GO KULLANIM</a>

***


# GİRİŞ

Fibonacci,ackermann ve factorial algoritmalarının, Flask kullanarak REST API mimarisiyle web servis oluşturulmuştur.

CProfile paketi kullanılarak programın çeşitli bölümlerinin ne sıklıkta ve ne kadar süreyle yürütüldüğü izlenmiştir.



# ALGORİTMALAR

#### **1-Fibonacci**

Fibonacci dizisi, her sayının kendinden önceki ile toplanması sonucu oluşan bir sayı dizisidir. Bu şekilde devam eden bu dizide sayılar birbirleriyle oranlandığında altın oran ortaya çıkar, yani bir sayı kendisinden önceki sayıya bölündüğünde altın orana gittikçe yaklaşan bir dizi elde edilir. 

$0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55 ...$

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

#### **3-Factorial**

Faktöriyel, matematikte, sağına ünlem işareti konulmuş sayıya verilen isim, daha genel olan Gama fonksiyonunun tam sayılarla sınırlanmış özel bir durumudur. 1'den başlayarak belirli bir sayma sayısına kadar olan sayıların çarpımına o sayının faktöriyeli denir.


# AŞAMALAR

### 1.Kısım 

Fibonacci,ackermann ve factorial algoritmaları için fibonacci.py, ackermann.py ve factorial.py script dosyalarında algoritmalar bulunmaktadır.

Ana program olan main.py dosyasında oluşturulan algoritma dosyaları import edilir.

### 2.Kısım

Yazılan algoritmaların web service mimarisini oluşturmak için Flask kullanılır. Gerekli uç noktalar oluşturularak REST API mimarisi main.py dosyasında tamamlanır.

### 3.Kısım

CProfile paketi import edilerek, oluşturulan her uç nokta için performanslar izlenir.

### 4.Kısım

Oluşturulan Flask uygulaması Docker kullanılarak kontainer haline getirilmiştir.


 # PERFORMANS


fibonacci(10) için oluşan profile çıktısı.

11 function calls in 0.000 seconds

   Ordered by: standard name
   
|ncalls | tottime | percall | cumtime|  percall | filename:lineno(function) |
| ----- | ------  | ----- | ----- |----- |----- |
| 1   | 0.000  |  0.000 |   0.000 |   0.000 |fibonacci.py:3(calculate_fibonacci)|
| 9   | 0.000   | 0.000 |   0.000  |  0.000| {method 'append' of 'list' objects}|
|1  |  0.000 |   0.000 |   0.000  |  0.000 |{method 'disable' of '_lsprof.Profiler' objects}  


# KULLANIM

* Git clone.

* Dockerfile kullanılarak 
  
  1. docker build -t <image_name> .
  2. docker run --name <container_name> -p 5000:5000 <image_name> 


  
