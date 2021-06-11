class Fibonacci:

    def calculate_fibonacci(n):
        #try except bloğuyla hata yakama yapılır.
        try:
            #verilen n değeri negatif olup olmadığı kontrol edilir.
            n = int(n)
            #fibs değişkenine fibonacci dizisinin ilk iki değeri atılır.
            fibs = [0, 1]
            #ilk iki değer fibs değişkeninde olduğu için 2'den n+1'e kadar 
            #n değerinin bir öncesi ve iki öncesi değerleri hesaplanarak
            #tekrar fibs dizisine atılır.
            #recursive yapı kullanmak yüksek parametreler için yavaşlama problemi doğurur.
            #çünkü aynı değer birden fazla hesaplanır. 
            for i in range(2, n + 1):
                fibs.append(fibs[-1] + fibs[-2])
            #fibs dizisi döndürülür.
            return fibs[n]
        except:
            raise SystemExit('Please provide a positive integer')
