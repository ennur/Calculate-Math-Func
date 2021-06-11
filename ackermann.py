class Ackermann:
    #ackermann hesaplanırken adımların tutulacağı step dizisi tanımlanır.
    step =[]

    def ackermann(m, n, s="% s"):
        #verilen m ve n değerleri negatif ise hata döndürür.
        try:
            m = int(m)
            n = int(n)
        except:
            raise SystemExit('Please provide a positive integer')
        #1.adımda oluşturulan m ve n değerleri step dizisine eklenir.
        Ackermann.step.append(s % ("A(% d, % d)" % (m, n)))
        #ackermann hesaplama adımları uygulanır.
        if m == 0:
            return n + 1
        if n == 0:
            return Ackermann.ackermann(m - 1, 1, s)
        #m ve n değerlerinin sıfır olmama durumunda ackermann metodu yeniden çağrılır.
        n2 = Ackermann.ackermann(m, n - 1, s % ("A(% d, %% s)" % (m - 1)))
        #m değeri 1 azaltarak kendine geri döndürülür.
        #m değeri 0 olana kadar devam eder.
        #ardından değerler hesaplanır.
        return Ackermann.ackermann(m - 1, n2, s)

    def calculate_ackermann(m, n):
        #ackermann değerinin hesaplanması için bu fonksiyon main.py den çağırılır.
        return Ackermann.ackermann(m, n)
