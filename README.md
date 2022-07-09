# CORE-SG: Efficient Computation of Multiple MSTs for Density-Based Methods

# Overview
This repository contains artifacts for predicting the Software Reusability rate project. We plan to study the usefulness of machine learning techniques in predicting the reusability rate of a software component in both class and library levels to answer the following research questions:

* What are the most useful static analysis metrics for predicting reusability rate using machine learning?

* What are the optimal models for predicting the reusability rate of software components?

* Are Deep Neural Networks efficient in predicting reusability rate?

## Table of Content
* [Abstract of report](#abstract)
* [Content](#content)
* [Instructions](#instructions)
  * [Using Docker image](#docker)
  * [Dependencies](#dependencies)
* [Contributors](#contributors)

## Abstract
In the modern industry, software developers rely on using software components from online platforms to increase efficiency in a limited time. This practice has gained popularity over time with the rapid evolution of open-source platforms. The context of reusing a software component relies completely on the selection as it is necessary to use a component that is suitable for reuse. The naïve way to determine the degree of reusability of any software component involves the opinion of experts in the field who makes their decision by evaluating the static analysis metrics. The application of an automated machine learning approach was illustrated in this context that involved a polynomial regression approach to determine the frequency of reuse of any component. The purpose of our paper is to empirically find the best model and static analysis metric that gives users the optimal reusability prediction for a software component. Our experiments are designed at both package and class levels of 65 selected Java projects.

The final report is available on: **LINK** 

## Content

This repository contains the source code and Jupyter notebooks for data preprocessing, data correlation, and ML method evaluation parts. We use data provided by  Papamichail et al. (2019) for this work.

* `DataSets` directory contains all datasets that we used in this work. It also contains some intermediate data that we needed for the evaluation part.
* `Results` direcorty contains all our findings and experiments' results.
* `*.ipynb`:
  * `best_classifier_model_selection.ipynb`: This notebook gets the classifier that is giving the best accuracy and the metric (when used for training) that is giving the best avg overall accuracy.
  * `best_regression_model_selection.ipynb`: Same as previous, but also presents a bar plot that depicts the number of times a model has been found as the optimal when trained with different static analysis metric.
  * `classifier_pred_reusibility.ipynb`: Returns the accuracy, prec and rec of each classifier for every static analysis metric.
  * `no_cls_pkg_dataset_generation.ipynb`: This notebook is for creating a dataset. Each row of the dataset contains the number of classes/ number of packages in a project, `Xtrain`, and the average reuse rate of that project, `Ytrain`. The class level results can be found at `ReusabilityRate_ML/Results/class_frequencyRes_TraditionalModels.xlsx` and the package level results can be found at `ReusabilityRate_ML/Results/package_frequencyRes_TraditionalModels.xlsx`.
  * `correlation_analysis.ipynb`: This notebook is related to the correlation analysis experiment. 
  * `dnn_data_normalization.ipynb`: To use the dataset as the feed for the DNN model, we should normalize all columns individually; otherwise, the model would consider some inputs as white noise.
  * `all_input_dnn.ipynb`: Compute and evaluate the result for DNN Classifier and Regression models.
# Instructions
The program is written in Python 3.8 using Jupyter notebooks. First, you need to install Jupyter lab:
* Using conda:
```
conda install -c conda-forge jupyterlab
```
* or using pip:
```
pip install jupyterlab
```

Then, it would help if you cloned this directory on your local machine's working directory. Also, you can open each of the notebooks in Google collab and use their resources.
## Docker
We also provide a docker version of our artifact that you can be sure of runtime environment compatibility!
To use our docker image, clone the docker branch:
```
git clone -b docker https://github.com/NeuralClassifier/ReusabilityRate_ML.git
```
Go to Docker directory:
```
cd ReusabilityRate_ML/Docekr/
```
build image:
```
docker build -t rrml:v0.1 --force-rm --no-cache -f Dockerfile .
```
Finally you can run it:
```
docker run -p 8888:8888 rrrml:v0.1
```
A url will be provided on the last line of the output. You can check the docker branch [here](https://github.com/NeuralClassifier/ReusabilityRate_ML/tree/docker).


## Dependencies
The program requires the following Python libraries:
* scikit-learn v1.0.1
* tensorflow v2.7.0
* seaborn v0.11.2
* matplotlib v3.5.0
* pandas v1.3.4

# Contributors

* Kushankur Ghosh, [kushanku@ualberta.ca](mailto:kushanku@ualberta.ca)
* Mehdi Akbarian Rastaghi, [makbaria@ualberta.ca](mailto:makbaria@ualberta.ca)
