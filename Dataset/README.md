# Dataset Source

*The dataset is published by [Kaggle](https://www.kaggle.com/uciml/breast-cancer-wisconsin-data) and taken from the [University of California Irvine (UCI)](https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+%28Diagnostic%29) machine learning repository.*

Table of Contents :
* [Dataset Information](#1)
	* [How data is collected?](#1.1)
* [Attribute Information](#2)

##  Dataset Information<a id=1></a>

Features are computed from a digitized image of a fine needle aspirate (FNA) of a breast mass. They describe characteristics of the cell nuclei present in the image.

**How data is collected ?<a id=1.1></a>**  
To create the dataset , samples taken from the patients with solid masses and an easy-to-use graphical computer program called Xyct, which is capable of perform the analysis of cytological(exam of each single cell) features based on the digital scan.  The program computes the ten features for  each cell nucleus in the sample , then it calculates the mean value, standard error and extreme value of each feature for the image , returning 30 real-valued vector.

For example:

<p align="center">
    <img src="https://raw.githubusercontent.com/Gkchandora/Breast_Cancer_Prediction/main/Dataset/Images/Breast_Tumour_Cells.jpeg" alt="Image" width="350" height="200" />
<br>
Figure 1 :
<em>Breast Tumor Cells</em>
</p>

The above picture shows the breast tumour cells and their nuclei of one of patient. Let this picture contains 1000(in real life this number is too big) cells , and the radius(measured by taken mean of distances from center to points on the perimeter) of each cell nucleus be  <img src="https://render.githubusercontent.com/render/math?math=\large r_1,r_2,r_3,...,r_1000"> . Then :
* radius_mean attibute of the patient is the mean radius of the 1000 nuclei.
* radius_se(radius standard error) attribute of the patient is standard deviation of the radius of 1000 nuclei.
* radius_worst (or radius_largest) attribute of the patient is the mean of radius of the  three largest nuclei.
* and so on...

## Attribute Information<a id=2></a>

* Ten real-valued features are computed for each cell nucleus:
	* radius (mean of distances from center to points on the perimeter)
	* texture (standard deviation of gray-scale values)
	* perimeter
	*  area
	* smoothness (local variation in radius lengths)
	* compactness (perimeter^2 / area - 1.0)
	* concavity (severity of concave portions of the contour)
	* concave points (number of concave portions of the contour)
	* symmetry
	* fractal dimension ("coastline approximation" - 1)

* Number of instances = 569
* Number of attributes: 32 (ID, diagnosis, 30 real-valued input features)
* Name of all the  attributes
	 <details>
     <summary>Please click on it</summary>
     <p>
     
     ```text
	 (1) ID Number
     (2) Diagnosis (M = malignant, B = benign)
     (3) Radius_mean
     (4) Texture_mean 
     (5) Perimeter_mean
     (6) Area_mean
     (7) Smoothness_mean
     (8) Compactness_mean
     (9) Concavity_mean
     (10) Concave points_mean
     (11) Symmetry_mean
     (12) Fractal_dimension_mean
     (13) Radius_se
     (14) Texture_se
     (15) Perimeter_se
     (16) Area_se
     (17) Smoothness_se
     (18) Compactness_se
     (19) Concavity_se
     (20) Concave points_se
     (21) Symmetry_se
     (22) Fractal_dimension_se
     (23) Radius_worst  
     (24) Texture_worst
     (25) Perimeter_worst
     (26) Area_worst
     (27) Smoothness_worst  
     (28) Compactness_worst
     (29) Concavity_worst
     (30) Concave points_worst
     (31) Symmetry_worst
     (32) Fractal_dimension_worst
     ```
     </p>
     </details>
