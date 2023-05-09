# Veri Madenciliği Dönem Projesi
K-Nearest Neighbor benimseyerek UCI Machine Learning
Repository’den (https://archive.ics.uci.edu/ml/index.php”) Bank Marketing  veri seti
üzerinde sınıflandırma veya kümeleme yapmayı amaçlanmıştır. 

# Adımlar
- [x] Eksik değerleri kontrol etme
- [x] Veri Ön İşleme Kısımları 
- [x] KNN sınıflandırıcısını eğitim verileriyle eğitme
- [x] Modelin doğruluğunu ve diğer metriklerini hesaplama
- [x] Görselleştirme

## Sınıflandırma veya kümeleme yaparak elde ttiğiniz sonuçlar
Classification Report:
               precision    recall  f1-score   support

           0       0.91      0.97      0.94      1205
           1       0.48      0.22      0.30       152

    accuracy                           0.89      1357
   macro avg       0.69      0.60      0.62      1357
weighted avg       0.86      0.89      0.87      1357


Confusion Matrix:
 [[1168   37]
 [ 118   34]]

- Accuracy (Doğruluk): %89

- Model, test veri kümesindeki örneklerin %89'unu doğru bir şekilde sınıflandırıyor. Bu, modelin genel başarısını gösterir.
Precision (Kesinlik):

- Sınıf 0 (y = no) için kesinlik: 0.91
Sınıf 1 (y = yes) için kesinlik: 0.48
Kesinlik, modelin pozitif olarak sınıflandırılan örneklerin ne kadarının gerçekten pozitif olduğunu gösterir. Model, "no" (0) sınıfını "yes" (1) sınıfına göre daha doğru bir şekilde tahmin etmektedir.
Recall (Duyarlılık):

- Sınıf 0 (y = no) için duyarlılık: 0.97
Sınıf 1 (y = yes) için duyarlılık: 0.22
Duyarlılık, gerçek pozitiflerin ne kadarının başarıyla tahmin edildiğini gösterir. Model, "no" (0) sınıfını "yes" (1) sınıfına göre daha iyi tespit etmektedir.

- F1-Score:

Sınıf 0 (y = no) için F1-Score: 0.94
Sınıf 1 (y = yes) için F1-Score: 0.30
F1-Score, kesinlik ve duyarlılığın harmonik ortalamasıdır ve modelin performansını daha dengeli bir şekilde değerlendirmeye yardımcı olur. Model, "no" (0) sınıfını "yes" (1) sınıfına göre daha iyi tahmin etmektedir.

- Confusion Matrix (Karmaşıklık Matrisi):
```
[[1168   37]
 [ 118   34]]   
 ```
 
 - İlk satır, gerçekte "no" (0) olan örnekleri gösterir. 1168'i doğru bir şekilde "no" (0) olarak sınıflandırmış ve 37'sini yanlışlıkla "yes" (1) olarak sınıflandırmıştır.
İkinci satır, gerçekte "yes" (1) olan örnekleri gösterir. 34'ünü doğru bir şekilde "yes" (1) olarak sınıflandırmış ve 118'ini yanlışlıkla "no" (0) olarak sınıflandırmıştır.
### Sonuç olarak,
 modelin "no" (0) sınıfını tahmin etmede iyi bir performansı varken, "yes" (1) sınıfını tahmin etmede daha düşük bir performansı vardır. Bu, dengesiz bir veri kümesinden kaynaklanabilir veya modelin eğitimi sırasında bazı önemli özelliklerin dikkate alınmamasından kaynaklanabilir. 
 ## Görselleştirme
 ### ROC Eğrisi
 ROC (Receiver Operating Characteristic) eğrisi, sınıflandırıcının performansını ölçen bir grafiktir. Eksenlerde, doğru pozitif oranı (True Positive Rate - TPR) ve yanlış pozitif oranı (False Positive Rate - FPR) bulunur. İdeal olarak, ROC eğrisi sol üst köşeye yakın olmalıdır, bu da TPR'nin yüksek ve FPR'nin düşük olduğu anlamına gelir. Bu durumda, ROC eğrisi orta seviyede bir performans göstermektedir.   
 
<img width="637" alt="Screenshot 2023-05-09 at 20 51 47" src="https://github.com/fport/data-mining-project/assets/56169582/1941de4f-56d8-423c-b5c7-7940c2280c0f">

### Confusion Matrix
Confusion matrix, sınıflandırıcı tarafından yapılan doğru ve yanlış tahminlerin sayısını gösterir. Bu durumda, matrisin sol üst köşesi "no" sınıfının doğru tahminlerini, sağ alt köşesi "yes" sınıfının doğru tahminlerini, sol alt köşesi "yes" sınıfının yanlış tahminlerini ve sağ üst köşesi "no" sınıfının yanlış tahminlerini gösterir. Bu görselleştirmede, sınıflandırıcının "no" sınıfını doğru bir şekilde tahmin ettiği görülüyor, ancak "yes" sınıfını doğru tahmin etme performansı düşük.   

<img width="636" alt="Screenshot 2023-05-09 at 20 51 44" src="https://github.com/fport/data-mining-project/assets/56169582/0a425f22-2ed4-464d-ae2e-f166e7e3cb07">
