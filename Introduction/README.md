# Introduction to Machine Learning(ML) 

Machine Learning (ML) emerged out of an urge to impart human like learning ability to machines.

Inspired by nature, having it’s foundations in statistics and mathematics, backed up by today’s state of the art hardware and software technologies, continually being explored by
several domain experts, applications of ML sytems are growing faster and faster day by day.

## Glance at applications of ML

### Checkers game by Arthur Samuel
Initial application of ML was developed by Arthur Samuel himself for learning and playing checkers game. The best player of that time was beaten
once by the machine.

### ALVINN (Autonomous Land Vehicle In Neural Network)
ALVINN is an early effort in development of self driving vehicle using ANN. ALVINN took road images from a camera and a laser range finder as input. It produced output as the direction the vehicle should travel in order to follow the road. The vehicle was able to travel upto 70 miles per hour. ALVINN learned driving in far less time (matter of minutes or hours). It would have definitely consumed several months of effort in terms of algorithm development using conventional programming approach to achieve the similar results. The best part was that ALVINN improved its performance after recovering it from the mistakes.

### MNIST handwritten digit recognition
Yann LeCun, Corinna Cortes and Christopher Burges developed MNIST (Modified National Institute of Standards and Technology) dataset by re-mixing the NIST’s original dataset. This dataset consists of 60,000 training images of handwritten digits and 10,000 testing images. These images were developed in order to evalu- ate machine learning models on handwritten digit recognition. Several people, teams, organizations provided solutions to this problem. The error rates achieved were 12%, 0.42% (2004), 0.27% (2011), 0.21% (2013).

### Spam email flitering
Several millions of malware are detected everyday using ML approach. Rule based spam filtering fails to detect latest tricks by spammers. Whereas security programs powered by machine learning can understand the pattern and detects new malware and hence offering protection against them. 

### Image recognition, object detection and classification
Computer vision technology is improved to such as extent that it can detect thousands of different types of objects in an image & video, spot the location of multiple objects in the image. This is possible because of the development in deep learning technology using Convolutional Neural Networks (CNN).

## Definitions

The term Machine Learning was coined by Arthur Samuel in 1959, an American pioneer in the field of computer gaming and artificial intelligence and stated:

”It gives computers the ability to learn without being explicitly programmed.”

According to Arthur Samuel, ML algorithms enable the computers to learn from data, and even improve themselves, without being explicitly programmed.

And in 1997, Tom Mitchell gave a “well-posed” mathematical and relational definition:
“A computer program is said to learn from experience E with respect to some task T and some performance measure P, if its performance on T, as measured by P, improves with experience E”.

## ML approach
There are some classes of problems, for which, conventional programming approach is very hard to develop and maintain. For example, hand written digit recognition, speech recognition, autonomous driving systems, text classification etc. For all these classes of problems, it is very hard to come up with logic or algorithm to solve the problem. Even if some algorithm seems to work fine for some cases, but it is very hard to make it work in general. Hence the conventional programming approach does not work very well to solve such problems.

It has been observed that Machine Learning can solve above mentioned classes of problems very well. The Machine Learning approach consists of development of software systems that can learn from data and improve its performance with experience. They can be trained by providing examples or data.

Successful training results in ML Model with optimum set of parameter values that help achieve the desired level of performance. The sole difference between trained ML Model and untrained ML Model is simply the difference in values of the model parameters. So by updating the ML Model parameters with proper values, the performance of ML system can be improved. The performance of ML system depends on the model parameter values. The structure of the ML Model and the execution algorithm remains same. This is the distinguishing feature of ML approach.

In case of ML systems, both software and hardware are probably not that important compared to the training data and optimum set of model parameters.

## Toy example illustrating ML approach
This section presents a very simple example to illustrate ML approach. 

Let us consider we are given several objects with their weight value. All these objects fall into lighter or heavier group. Our task is to develop and train ML Model using training examples that contains objects with their weight value along with their class i.e. whether it belongs to lighter or heavier group. After successful training, this ML Model can be used to classify new object as lighter or heavier.

Model for this particular case consists of a single real value that represents the threshold weight w. An object is be considered as lighter if its weight is less than or equal to this threshold value, otherwise it is considered as heavier.

Training Algorithm determines the value of model parameter : w as follows:
  w = [ max (all weights from light weight category objects) + min (all weights from heavy weight category objects) ] / 2
  
After model parameter: w is determined using above simple training algorithm, this trained model can be used to categorize the object into light or heavry given its weight value as follows:

if given weight <= w, then, the object is light owtherwise it is heavy.

Here are the python files for this simple toy example:
[WeightClassifier.py](WeightClassifier.py)
[TestWeights.py](TestWeights.py)

The result of execution for above python code is as follows:
w = 6.6
12 class = WeightType.HEAVY
2.5 class = WeightType.LIGHT
