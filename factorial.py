class Factorial:

    def range_fac(lo, hi):
        #bu metot low ve high olmak üzere iki parametre alır.
        if lo + 1 < hi:
            #iki değerin orta noktası bulunur.
            mid = (hi + lo) // 2
            #low dan mid'e ve mid'den high'a olan değerler recusive bir şekilde hesaplanır.
            #bu şekilde olan yaklaşım hesaplamalara hız kazandırır.
            return Factorial.range_fac(lo, mid) * Factorial.range_fac(mid + 1, hi)
        #iki değer birbirne eşit ise fonksiyona direkt döner.
        if lo == hi:
            return lo
        #iki değer birbirine eşit değilse çarpımları döndürülür.
        return lo * hi

    def factorial(self):
        #verilen n değeri negatif ise hata döndürülür.
        try:
            n = int(self)
        except:
            raise SystemExit('Please provide a positive integer')
        # 0 ve 1 faktöriyel, 1 olduğu için hesaplama olmadan 1 döndürülür. 
        if n < 2:
            return 1
        #0 ve 1 den farklıysa range_fac metodu döner.
        return Factorial.range_fac(1, n)

