import bentoml

iris_clf_runner =bentoml.sklearn.get("iris_clf:latest").to_runner()
iris_clf_runner.init_local()
print(iris_clf_runner.predict.run([[5.9,3.,5.1,1.8]]))

'''
.init_local(): تشير إلى دالة تُستدعى لتهيئة النموذج أو بيئة التشغيل محليًا
، مما يعني أنه سيتم تشغيل النموذج على الجهاز المحلي بدلاً من خادم بعيد أو بيئة سحابية.
'''