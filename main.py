
from flask import jsonify,Flask
from fibonacci import Fibonacci
from ackermann import Ackermann
from factorial import Factorial
import cProfile

#programın çeşitli bölümlerinin ne sıklıkta ve ne kadar süreyle yürütüldüğünü açıklamak için 
prof = cProfile.Profile()

app = Flask(__name__)

#fibonacci değerinin hesaplanması için bir uç nokta oluşturulur.
#fibonacci sınıfına parametre olarak param_n verilir.
@app.route("/fibonacci/<int:param_n>/")
def get_fibo(param_n):
    #fibonacci metriklerin hesaplanması için profile enable edilir.
    prof.enable()
    #fibonacci sınıfı kullanılarak verilen parametrenin değeri hesaplanır.
    fi=Fibonacci.calculate_fibonacci(param_n)
    #fibonacci değerinin hesaplanması bittikten sonra çalışma değerleri
    #disable edilir. Bu değerler prof değişkeninde saklanır.
    prof.disable()
    #terminal ekranına prof değerleri yazdırılır.
    prof.print_stats()
    #tarayıcı sayfasına fibonacci değeri json ile çıkartılır.
    return jsonify(fi)

#ackermann değerinin hesaplanması için bir uç nokta oluşturulur.
#ackermann sınıfına parametre olarak param_m ve param_n verilir.
@app.route("/ackermann/<int:param_m>/<int:param_n>")
def get_ackermann(param_m,param_n):
    #ackermann metriklerin hesaplanması için profile enable edilir.
    prof.enable()
    #ackermann sınıfı kullanılarak verilen parametrenin değeri hesaplanır.
    ack=Ackermann.calculate_ackermann(param_m,param_n)
    #ackermann hesaplanırken oluşan adımlar stp değişkeninde saklanır.
    stp=Ackermann.step
    #ackermann değerinin hesaplanması bittikten sonra çalışma değerleri
    #disable edilir. Bu değerler prof değişkeninde saklanır.
    prof.disable()
    #terminal ekranına prof değerleri yazdırılır.
    prof.print_stats()
    #tarayıcı sayfasına ackermann değeri ve adımlar json ile çıkartılır.
    return jsonify(stp,ack)


#factorial değerinin hesaplanması için bir uç nokta oluşturulur.
#factorial sınıfına parametre olarak param_n verilir.
@app.route("/factorial/<int:param_n>")
def get_factorial(param_n):
    #factorial metriklerin hesaplanması için profile enable edilir.
    prof.enable()
    #factorial sınıfı kullanılarak verilen parametrenin değeri hesaplanır.
    fct=Factorial.factorial(param_n)
    #factorial değerinin hesaplanması bittikten sonra çalışma değerleri
    #disable edilir. Bu değerler prof değişkeninde saklanır.
    prof.disable()
    #terminal ekranına prof değerleri yazdırılır.
    prof.print_stats()
    #tarayıcı sayfasına factorial değeri ve adımlar json ile çıkartılır.
    return jsonify(fct)



if __name__ == '__main__':
    #flask app başlar.
    app.run(debug=True,host='0.0.0.0')
    





