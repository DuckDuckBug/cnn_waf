Web Attacks Detection based on CNN

用卷积神经网络在CSIC2012数据集进行训练，准确率达99.3%，可以实现对8种Web攻击以及异常请求的检测。

主要内容描述：

1. 训练和测试的结果请看cnn_train_test.ipynb。

2. 要应用该模型进行检测请使用detector.py。其中训练好模型保存在model目录下，将URL向量化的模型保存在tokenizer目录下，若要使用detector.py，请自行更改路径。

   ```python
   # for example
   from detector import Detector
   
   url_test = "GET /tienda1/publico/caracteristicas.jsp?id=d%27z%220"
   detector = Detector()
   label_test = detector.predict(url_test)
   print(url_test)
   # out SQLI
   ```

参考：

1. [Torpeda CSIC 2012 datasets](<http://www.tic.itefi.csic.es/torpeda/datasets.html>)

2. [Detecting Malicious Requests with Keras & Tensorflow](<https://medium.com/slalom-engineering/detecting-malicious-requests-with-keras-tensorflow-5d5db06b4f28>)
3. [Fwaf-Machine-Learning-Driven-Web-Application-Firewall](<https://github.com/faizann24/Fwaf-Machine-Learning-driven-Web-Application-Firewall>)
4. [Deep Learning with Python](<https://www.manning.com/books/deep-learning-with-python>)