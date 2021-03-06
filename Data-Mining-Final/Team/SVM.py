import csv
import random
import car
import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.cluster import KMeans
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import mean_squared_error
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.preprocessing import label_binarize

# Load Data
[data, target]  = car.preprocess()

# Split Data into Train and Test
SPLIT_THRESHOLD = int(len(data) * 4 / 10)
x_train, x_test	= data	[0 : SPLIT_THRESHOLD], data	 [SPLIT_THRESHOLD:]
y_train, y_test	= target[0 : SPLIT_THRESHOLD], target[SPLIT_THRESHOLD:]

print "SVM"
# SVM
clf = svm.SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,
			decision_function_shape='ovo', degree=3, gamma='auto', kernel='rbf',
			max_iter=-1, probability=False, random_state=False, shrinking=True,
			tol=0.001, verbose=False)
			
y_score = clf.fit(x_train, y_train).decision_function(x_test)

<<<<<<< HEAD
print "mean_squared_error"
print mean_squared_error(y_test, clf.predict(x_test))
print

print "accuracy_score"
print accuracy_score(y_test, clf.predict(x_test))
=======
print ("mean_squared_error")
print (mean_squared_error(y_test, clf.predict(x_test)))
print

print "accuracy_score"
print (accuracy_score(y_test, clf.predict(x_test)))
>>>>>>> ee6e13c82c4ada2554f2cba204c1f9290c34429f
print

print "confusion_matrix"
print (confusion_matrix(y_test, clf.predict(x_test)))
print

print "classification_report"
print (classification_report(y_test, clf.predict(x_test)))
print

<<<<<<< HEAD
import plot_precision_recall
'''
# Compute Precision-Recall and plot curve
precision = dict()
recall = dict()
average_precision = dict()
for i in range(n_classes):
    precision[i], recall[i], _ = precision_recall_curve(y_test[:, i],
                                                        y_score[:, i])
    average_precision[i] = average_precision_score(y_test[:, i], y_score[:, i])

# Compute micro-average ROC curve and ROC area
precision["micro"], recall["micro"], _ = precision_recall_curve(y_test.ravel(),
    y_score.ravel())
average_precision["micro"] = average_precision_score(y_test, y_score,
                                                     average="micro")


# Plot Precision-Recall curve
plt.clf()
plt.plot(recall[0], precision[0], lw=lw, color='navy',
         label='Precision-Recall curve')
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.ylim([0.0, 1.05])
plt.xlim([0.0, 1.0])
plt.title('Precision-Recall example: AUC={0:0.2f}'.format(average_precision[0]))
plt.legend(loc="lower left")
plt.show()

# Plot Precision-Recall curve for each class
plt.clf()
plt.plot(recall["micro"], precision["micro"], color='gold', lw=lw,
         label='micro-average Precision-recall curve (area = {0:0.2f})'
               ''.format(average_precision["micro"]))
for i, color in zip(range(n_classes), colors):
    plt.plot(recall[i], precision[i], color=color, lw=lw,
             label='Precision-recall curve of class {0} (area = {1:0.2f})'
                   ''.format(i, average_precision[i]))

plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.title('Extension of Precision-Recall curve to multi-class')
plt.legend(loc="lower right")
plt.show()
'''
'''
print "KMeans"
kmeans = KMeans(n_clusters=4, random_state=0).fit(x_train + x_test)
print kmeans.labels_
print kmeans.cluster_centers_
'''
	
	
=======
import plot_precision_recall
>>>>>>> ee6e13c82c4ada2554f2cba204c1f9290c34429f
