# car_brand_detection
Car Brand Detection, Python 3.6 ve OpenCV kullanılarak geliştirildi. Local olarak alınan resimler kullanılarak haarcascade veri seti oluşturuldu.

## Training Cascade oluşturmak için gerekli işlemler:

`opencv_createsamples -img example.jpg -bg bg.txt -info info/info.lst -pngoutput info -maxxangle 0.5 -maxyangle -0.5 -maxzangle 0.5 -num 880`

**Arkaplan Resmi kullanılarak Pozitif Resim üretmek için gerekli info.lst oluşturulur.**

* -img [image] -> Pozitif resim oluşturmak için kullanacağı ana resim.

* -bg bg.txt -> Resmin dosya konumu ve ismini içeren txt.(Örneğin: neg/1.jpg)

* -info info/info.lst -> İşlem sonucu oluşacak resimlerin (obje sayısı, x koordinat, y koordinat, genişlik, yükseklik) bilgilerini içerecek olan dosya.

* -maxyangle, maxyangle, maxzangle -> Maksimum dönüş açıları radyan olarak veilmelidir.

* -num [number] -> Negatif resim sayısı.

-----------------------------------------------------------------------------------------------

`opencv_createsamples -info info/info.lst -num 880 -w 20 -h 20 -vec positives.vec`

**Pozitif resimlerin bilgilerinin oluşmasını sağlar.**

* -num [number] -> Oluşacak pozitif resim sayısı.

-----------------------------------------------------------------------------------------------

`opencv_traincascade -data data -vec positives.vec -bg bg.txt -numPos 880 -numNeg 880 -numStages 1 -w 20 -h 20`

**Burada önceden oluşturuğumuz negatif, pozitif, bg dosyalarını kullanarak antreman yaptırılıyor.**
* -featureType LBP -> Normal cascade'den daha hızlı.

* -maxFalseAlarmRate [number] -> Varsayılan değeri 0.5'tir. Varsayılan olarak düşünürsek; antreman sırasında 1000 adet pozitif hatalı örnekten 5 tanesine izin verir.

* -minHitRate [number] -> Varsayılan değeri 0.995'tir. Bu değerin 0.998'e çıkması hedeflere ulaşmayı zorlaştırır. Ancak bu en iyi yaklaşım değil, antreman verisini overfit(antreman verisini ezberlemesi)'e zorlayana kadar.

* -numPos [number] -> Pozitif resim sayısı.

* -numNeg [number] -> Negatif resim sayısı.

* -numStages [number] -> Yapılacak işlem sayısı.PS:Ne kadar fazla olursa o kadar uzun sürecektir.
