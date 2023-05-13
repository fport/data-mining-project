from sklearn.cluster import KMeans
import pandas as pd

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

import numpy as np
import itertools
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import roc_curve, roc_auc_score, auc


data = pd.read_csv('./bank/bank.csv', sep=';')

# Eksik değerleri kontrol etme
print(data.isnull().sum())

# Kategorik özelliklerin isimlerini belirleyin
categorical_features = ['job', 'marital', 'education',
                        'default', 'housing', 'loan', 'contact', 'month', 'poutcome']

# Veri Ön İşleme Kısımları
# One-Hot Encoding uygulama
data_encoded = pd.get_dummies(data, columns=categorical_features)

# Ölçeklendirilecek sayısal özellikleri belirleyin
numeric_features = ['age', 'balance', 'day',
                    'duration', 'campaign', 'pdays', 'previous']

# Özellikleri ölçeklendirmek için StandardScaler'ı kullanma
scaler = StandardScaler()
data_encoded[numeric_features] = scaler.fit_transform(
    data_encoded[numeric_features])

# Veri kümesini eğitim ve test kümelerine ayırma
X = data_encoded.drop('y', axis=1)
y = data['y'].map({'yes': 1, 'no': 0})  # Hedef değişkeni sayısal hale getirin

# K-Means kümeleme
kmeans = KMeans(n_clusters=2, random_state=0).fit(X)
labels = kmeans.labels_
centers = kmeans.cluster_centers_

# Veriyi görselleştirin
plt.scatter(X.iloc[:, 0], X.iloc[:, 1], c=labels, s=50, cmap='viridis')
plt.scatter(centers[:, 0], centers[:, 1], c='black', s=200, alpha=0.5)
plt.show()

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42)

# KNN sınıflandırıcısını eğitim verileriyle eğitme
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

# Test seti üzerinde tahminler yapın:
y_pred = knn.predict(X_test)

# Modelin doğruluğunu ve diğer metriklerini hesaplayın:
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)

print("Accuracy:", accuracy)
print("\nClassification Report:\n", report)
print("\nConfusion Matrix:\n", cm)


# Görselleştirme
# Confusion matrix görselleştirme
def plot_confusion_matrix(cm, classes, normalize=False, title='Confusion Matrix', cmap=plt.cm.Blues):
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], fmt), horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')


plt.figure()
plot_confusion_matrix(cm, classes=['no', 'yes'], title='Confusion Matrix')

# ROC eğrisi ve AUC skoru
y_probs = knn.predict_proba(X_test)[:, 1]  # Sadece 'yes' olasılıklarını al
fpr, tpr, thresholds = roc_curve(y_test, y_probs)
roc_auc = auc(fpr, tpr)

plt.figure()
plt.plot(fpr, tpr, color='darkorange', lw=2,
         label='ROC curve (area = %0.2f)' % roc_auc)
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic (ROC) Curve')
plt.legend(loc="lower right")
plt.show()
