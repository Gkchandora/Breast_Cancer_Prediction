# %%
"""
# *Exploratory Data Analysis*

*Table of Contents :*
* *Previous Notebook References*  
    * [*Data Wrangling*](https://nbviewer.jupyter.org/github/Gkchandora/Breast_Cancer_Prediction/blob/main/Model_Building_Steps/NB_1_Data_Wrangling.ipynb)
* [*Import libraries and Utility Modules*](#1)
* [*Descriptive Statistics*](#2)
* [*Data Visualization*](#3)
    * [*Response Variable*](#3.1)
    * [*Box Plot*](#3.2)
    * [*Histogram and Density Plot*](#3.3)
    * [*Correlation Matrix*](#3.4)
    * [*Features Scatter Plot Matrix*](#3.5)



*Uptil now we have a good intuitive sense of data, lets take a step further to get a closer look of attributes and data values. This will provide useful knowledge for data pre-processing.*
"""

# %%
"""
## *Import libraries and Utility Modules*<a id=1></a>
"""

# %%
# import the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
from tabulate import tabulate
import shutil

# graph styles 
mpl.style.use("ggplot")

# %%
# import utility modules(i.e. previous notebook variables, methods etc) via Url
import httpimport

address = "https://raw.githubusercontent.com/Gkchandora/Breast_Cancer_Prediction/main/Codes/Model_Building_Steps/utility_modules"

with httpimport.remote_repo(["data_wrangling"], address):
    from data_wrangling import *

# %%
# cleaned data preview
df.head()

# %%
"""
## *Descriptive Statistics*<a id=2></a>
"""

# %%
# Types of Features : Discrete(in Categorical sense) and Continuous 

features_description = {"Discrete_Features":[],
                        "Continuous_Features": []}

if __name__ == "__main__":
    for column in df.columns:

        # setting threshold to 5% of total observations to decide discrete vs categorical

        if df[column].nunique()/df[column].count() < 0.05 :
            # store it in Discrete Features list
            features_description["Discrete_Features"].append(column)

        else :
            # store it in Continuos Features list
            features_description["Continuous_Features"].append(column)

    # print the features descriptions
    for key, value in features_description.items() :
        print(f"{key} are : {value}\n")

# %%
"""
*So the `target` valriable is only discrete while all the other features are continous.*

"""

# %%
# statistical summary of the data
if __name__ == "__main__":
    print("The Statistical summary of the data : \n")
df.describe() 

# %%
"""
*Insights*
* ***Normalisation*** *of the data is required as scale varies for the features* : 
    * *most of the features values lies between*
$[0, 1]$
    * *`area_mean`features has exceptionally high range values which lies between*
$[143, 2501]$
* *some features have large standard deviations : `area_mean`, `perimeter_mean`, `area_se`, `area_worst`*
"""

# %%
# features with high standard deviations > 20(set threshold)
if __name__ =="__main__":

    # satandard deviation of featues
    std_dev = df.describe().loc["std"]
    std_dev = std_dev[std_dev > 20]
    std_dev.index.name = "Features"
    std_dev = std_dev.reset_index( name  = "Standard Deviations(std)")
    print(f" Features with higher standard deviations are :\n \n{tabulate(std_dev, headers = 'keys', tablefmt = 'psql')}")

# %%
"""
## *Data Visualization*<a id=3></a>  
"""

# %%
"""
#### *Distribution of Dependent Variable(i.e. Target)*<a id=3.1></a>
"""

# %%
if __name__ == "__main__":
    # Plot the bar graph to visulaize the distribution of patients having : Benign vs Malignant Tumor

    # figure
    x,y = 7,5
    plt.figure(figsize = (x,y))

    # bar graph
    target_distn = df["target"].value_counts().sort_index() 
    target_distn.plot(kind ="bar", color = ['green', 'red'], alpha = 0.6, width = 0.5, )

    # categories percentage
    categories = ["Benign", "Malignant"]
    categories_percent = [100*(value/target_distn.sum()) for value in target_distn ]

    # to get coordinates for annotations
    ax = plt.gca() # current axes
    rects = ax.patches # axes of each bars in bar graph

    # categories annotations
    for i in range(len(categories)):
        txt = f"{categories[i]} -{categories_percent[i] : 0.2f}%"
        plt.annotate(s = txt,
                    xy = (rects[i].get_x() + rects[i].get_width()/2, 
                        rects[i].get_y()+ (ax.get_yticks()[1] - ax.get_yticks()[0])*.2, # chose 2% of y axis scale for positon of y coordinate.
                        ),
                    fontsize = (rects[i].get_height())*y*.28/len(txt),
                    color = "white",
                    ha = "center", # horizontal alignment of text at given x,y coordinate
                    rotation = 90,
                    )
    plt.ylabel("# Patients", fontsize = 20,)
    plt.title("Distn. of Tumor Patients", fontsize = 25, fontname = "Monospace", alpha = .6, y = 1.05)
    plt.xticks([])
    plt.tight_layout(rect=[0, 0, 1, 1])
    # plt.savefig("1_EDA_Dist_of_Tumor_Patients.png", bbox_inches = "tight", dpi = 120)
    plt.show()

# %%
"""
*Insights :*  
*The percentage of patients with Benign and Malignant tumor are 62.74 and 37.26 . So, its not a case a of imbalanced class data.* 
"""

# %%
"""
#### *Box Plot*<a id=3.2></a>
"""

# %%
# In Dataframe set B : Benign  and M : Malignant 
df["target"] = df['target'].map(lambda x: 'Benign' if x == 'B' else "Malignant")

if __name__ == "__main__":
    ############################ box plot ######################################

    # figure and axes objets
    fig, axes = plt.subplots(nrows = 3, ncols = 10, figsize = (25, 6), dpi = 150)
    axes = axes.flatten()

    # loop for creating box plot for each feature
    for i, column in enumerate(list(df.columns)[1:]):

        # box plot
        sns.boxplot(ax = axes[i],                            # axes for drawing the graph
                    x = "target",                            # Respond Variable on x-axis
                    y = column,                              # Feature on y-axis 
                    data = df,                               # dataframe
                    orient = "v",                            # orientation of box plot
                    hue = "target",                          # categorical variable
                    dodge = False,                           # alignment of box plot with categorical axis, here x-axis
                    hue_order = ["Benign", "Malignant"],     # order for names of categories in legend box
                    order = ["Benign", "Malignant"],         # order of plotting categories
                    palette=['#5ba85b', '#f45b5b'],          # earlier used color hex vlaues for "green" and "red" in Distribution of Tumor's Patient
                    saturation = 1.5,                        # color brightness adjustment
                    )
        
        axes[i].get_xaxis().set_visible(False)               # x-axiss set to invisible mode
        axes[i].set_ylabel("")                               # y axis label empty
        axes[i].set_title(column.capitalize(), alpha = 0.7)  # title for present box plot  
        axes[i].legend("", frameon = False)                  # set empty legend for present subplot

    # single legend for all boxplots i.e, subplots
    handles, labels = plt.gca().get_legend_handles_labels()  # returns a list of Artists and labels(i.e. strings) 
    fig.legend(handles = handles,                            # artist list
            labels = labels,                                 # labels(i.e. list of string )
            loc ='center',                                   # positon of legend 
            fontsize = 15 ,                                  # labels font size 
            bbox_to_anchor=(0.5, 1.1),                       # coordintes of boundind box point wrt loc parameter 
            ncol = 2,                                        # to put labels in column vector,
            frameon = False                                  # bounding box frame on/off 
            )

    # Single title for all boxplots or subplots
    plt.suptitle(t = r"Box Plot Visualization of Tumour's",  # title 
                x = 0.5, y = 1.3,                           # coordinates for title 
                fontsize = 35,                              # fontsize
                alpha = .6,                                 # opacity of title font color
                fontname = "Monospace",                     # font style
                color = "black"                             # font color
                )               

    plt.tight_layout(rect=[0, 0, 1, 1])
    # plt.savefig("2_EDA_1_Box_Plot_Tumor_Viz.png", bbox_inches='tight', dpi = 150)
    plt.show()

# %%
if __name__ == "__main__":
    # Alternate BoxPlots Graph
    # All box plots in one graph with a standardized data.
    stdz_df = df[df.columns[1:]].apply(lambda x : (x - x.mean())/x.std(), axis = 0) 
    stdz_df["target"] = df["target"] 

    # metled dataframe of standardize data
    melted_stdz_df = pd.melt(stdz_df, id_vars = ["target"], value_vars = list(stdz_df.columns[:-1]), var_name = "features", value_name = "values" )

    # figure size and dpi
    plt.figure(figsize = (30,8),dpi = 120)

    # single graph
    sns.boxplot(data = melted_stdz_df,
                x = "features",
                y = "values",
                hue = "target",
                hue_order = ["Benign", "Malignant"],
                order = sorted(melted_stdz_df.features.unique()), # sorted list of all the features
                palette = ['#5ba85b', '#f45b5b'],                 # previous used colors 
                saturation = 1.5,                                 # color brightness
                )

    # legend 
    plt.legend(title = "", frameon = False, bbox_to_anchor = (0.5, 1.1), loc = "center", ncol = 2)

    # graph labeling
    plt.xticks(rotation = 90,)
    plt.title("Box plots of features for Standardized Data", y = 1.2, alpha = 0.6, fontname = "Monospace", fontsize = 25)
    plt.tight_layout(rect=[0, 0, 1, 1])
    # plt.savefig("3_EDA_Boxplots_for_Standardized_data.png", bbox_inches='tight')
    plt.show()

# %%
"""
*From the above box plot visualization, the features that could be useful for classification are as follows:*  
> *`area_mean`, `area_worst`   
`concave points_mean`, `concave points_worst`   
`concavity_mean`, `concavity_worst`  
`perimeter_mean`, `perimeter_worst`  
`radius_mean`, `radius_worst`*  

*Rule Used : Considering a quiet separation between boxes.*

"""

# %%
"""
#### *Histogram and Denisty Plot*<a id=3.3></a>
"""

# %%
if __name__ == "__main__":

    # Histogram : Distributions of Malignant and Benign Tumour for each features. 

    fig, axes = plt.subplots( nrows = 3, ncols = 10, figsize = (25, 6), dpi = 150)
    axes = axes.flatten()

    # loop for creating histogram of each feature

    for i, column in enumerate(list(df.columns)[1:]):

        # histogram
        sns.histplot( data = df,                                  # data
                    x = column,                                   # x axis 
                    hue = "target",                               # categorical variable
                    kde = True,                                   # density plot
                    ax = axes[i],                                 # axes object
                    hue_order = ["Benign", "Malignant"],          # order of names in Legend box
                    palette=['#5ba85b', '#f45b5b'],               # color of histograms
                    alpha = 0.7                                   # color opacity             
                    )
        
        axes[i].set_ylabel("# Patients")                          # y-axis label
        axes[i].set_title(column.capitalize(), alpha = 0.7)       # set title for each histogram
        axes[i].set_xlabel("")                                    # x axis label
        axes[i].get_legend().set_visible(False)                   # hide legend visibility in individual plot

    # single legend for all histograms i.e, subplots
    handles = axes[-1].legend_.get_patches()                      # plt.gca().get_legend_handles_labels returns empty list for sns.histplot, so extract from the handles and labels from ground
    labels = plt.gca().legend_.get_texts()                        # labels values
    fig.legend(handles = handles,
            labels = [category.get_text() for category in labels ],
            loc ='center',                                        # positon of legend 
            fontsize = 15 ,                                       # labels font size 
            bbox_to_anchor=(0.5, 1.1),                            # coordintes of boundind box point wrt loc parameter 
            ncol = 2,                                             # to put labels in column vector,
            frameon = False                                       # bounding box frame on/off 
            )

    # Single title for all subplots
    plt.suptitle(t = r"Distribution of Malignant and Benign Tumor for each Features ",      # title 
                x = 0.5, y = 1.3,                                 # coordinates for title 
                fontsize = 35,                                    # fontsize
                alpha = .6,                                       # opacity of title font color
                fontname = "Monospace",                           # font style
                color = "black"                                   # font color
                )               

    plt.tight_layout(rect=[0, 0, 1, 1])
    # plt.savefig("4_EDA_Distn_of_Malignant_and_Benign_Tumors_for_each_Features.png", bbox_inches = 'tight')
    plt.show()

# %%
"""
*Insights:*  
*Features that could be useful for classification are as follows :*  
> *`area_mean`, `area_worst`   
`concave points_mean`, `concave points_worst`   
`concavity_mean`, `concavity_worst`  
`perimeter_mean`, `perimeter_worst`  
`radius_mean`, `radius_worst`*  
  
*Note: Use either box plot(prefer) or pdf to get this insight.* 

"""

# %%
if __name__ == "__main__":

    # Distributions of Features

    # colors for each graph
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
            '#66CDAA', '#e377c2', '#7B68EE', '#bcbd22', '#17becf']

    fig, axes = plt.subplots(nrows = 3, ncols = 10, figsize = (25, 6), dpi = 150)
    axes = axes.flatten()

    for i, column in enumerate(df.columns[1:]):
        sns.histplot( ax = axes[i],                                    # axes object
                    data = df,                                         # data set
                    x = column,                                        # x axis
                    color = colors[i%10],                              # color of histogram
                    kde = True,                                        # density plot
                    alpha = [0.8, 0.6, 0.4][i//10],                    # histogram opacity
                    line_kws = {"alpha" : [0.8, 0.6, 0.4][i//10]}      # kde line opacity
                    )
        
        axes[i].set_ylabel("# Patients")                               # y-axis label
        axes[i].set_title(column.capitalize(), alpha = 0.7)            # set title for each histogram
        axes[i].set_xlabel("")                                         # x axis label

    # Single title for all subplots
    plt.suptitle(t = r"Distribution of Features ",                     # title 
                x = 0.5, y = 1.1,                                      # coordinates for title 
                fontsize = 35,                                         # fontsize
                alpha = .6,                                            # opacity of title font color
                fontname = "Monospace",                                # font style
                color = "black"                                        # font color
                )               

    plt.tight_layout(rect=[0, 0, 1, 1])
    # plt.savefig("5_EDA_Distn_of_Features.png", bbox_inches = 'tight')
    plt.show()

# %%
"""
*Insights*
* *Postively Skewed (Useful for Outlier Detection )*
    > *`Radius_mean`, `Radius_se`, `Radius_worst`  
     `Texture_se`  
     `Perimeter_mean`, `Perimeter_se`, `Perimeter_worst`   
     `Compactness_mean`, `Compactness_se`, `Compactness_worst`  
     `Area_mean`, `Area_se`, `Area_worst`  
     `Concave points_mean`, `Concave points_se`  
     `Concavity_mean`, `Concavity_se`, `Concavity_worst`*  

*Most of the distributions are skewed and outlier detection is required*
"""

# %%
"""
#### *Correlation Matrix*<a id=3.4></a>
"""

# %%
if __name__ == "__main__":
    # Multicollinearity : Lets see the collinearity between variables and collinearity threshold |x| > 0.7

    # figure size
    plt.figure( figsize = (15, 15), dpi = 120)

    # heatmap
    sns.heatmap(data = df.corr(),                 # data
                cmap = 'coolwarm',                # colormap
                vmin = -1.0,                      # anchor the colormap
                vmax = 1.0,                       # anchor the colormap
                annot = True,                     # data vlaues in cell
                fmt = "0.1f",                     # string formatting annotations
                mask = np.triu(df.corr()),        # Data will not seen where mask is true
                linewidths = 0.5
                )

    # annotate only highly correlated variables
    ax = plt.gca()

    for t in ax.texts:
        if float(t.get_text()) > 0.7 or float(t.get_text()) < -0.7 :
            t.set_text(t.get_text()) #if the value is greater than 0.7 then set the text 
        else:
            t.set_text("") # if not it sets an empty text

    plt.title("Collinearity between Features",
            x = 0.5, y = 1.1,
            fontsize = 35,
            alpha = .6,
            fontname = "Monospace",
            color = "black"
            )

    plt.tight_layout(rect=[0, 0, 1, 1])
    # plt.savefig("6_Features_Corr_Matrix.png", bbox_inches = 'tight' )
    plt.show()

# %%
"""
*Insights : From the above heatmap, the highly correlated features are-* 
> *`Radius_mean`, `Perimeter_mean`, `Area_mean`, `Radius_worst`, `Perimeter_worst`  
 `Texture_mean`, `Texture_worst`  
 `Smoothness_mean`, `Smoothness_worst`  
 `Compactness_mean`, `Compactness_worst`, `Concavity_mean`  
 `Fractal_dimension_mean`, `Fractal_dimension_worst`  
 `Radius_se`, `Perimeter_se`, `Area_se`  
 `Compactness_se`, `Fractal_dimension_se`, `Concavity_se`  
 `Concavity_worst`, `Concave_points_worst`*   

<details>
<summary></summary>

*Rule Used : Consider those features which have high correlated values in a heatmap column. Example:*  
* *`Radius_mean` has correaltion value of `1.0` with all these features- `Perimeter_mean`, `Area_mean`, `Radius_worst`, `Perimeter_worst` and dont go for correlations of these features with rest of other features i.e. drop all here *  
* *`corr(Radius_mean, concave_points_mean) = 0.8`, look correlations of `concave_point_mean` with all others features in its column.*
* *`corr(Radius_mean, area_worst) = 0.9`, same as above*  


</details>
"""

# %%
"""
#### *Features Scatter Plot Matrix*<a id=3.5></a>
"""

# %%
if __name__ == "__main__":
    # Overview of Features Scatter Plot Matrix

    # pairplot
    g = sns.pairplot(df[df.columns[:11]], 
                    hue = "target", 
                    palette=['#5ba85b', '#f45b5b'], 
                    hue_order = ["Benign", "Malignant"])

    # remove legend from original postion
    g._legend.remove()

    # legends handles and labels
    handles = g._legend_data.values()
    labels = g._legend_data.keys()

    # legend set
    g.fig.legend(handles = handles,
            labels = labels,
            loc ='center',                                             # positon of legend 
            fontsize = 15 ,                                            # labels font size 
            bbox_to_anchor=(0.5, 1.02),                                # coordintes of boundind box point wrt loc parameter 
            ncol = 2,                                                  # to put labels in column vector,
            frameon = False                                            # bounding box frame on/off 
            )

    # title of graph
    plt.suptitle("Features Scatter Plot Matrix",                       # title name
                x = 0.5, y = 1.08,                                     # coordinates for title 
                fontsize = 30,                                         # fontsize
                alpha = .6,                                            # opacity of title font color
                fontname = "Monospace",                                # font style
                color = "black"                                        # font color
                )

    plt.tight_layout(rect=[0, 0, 1, 1])
    # plt.savefig("7_Features_Scatter_Matrix_Plot.png", bbox_inches = 'tight', dpi = 120)
    plt.show()

# %%
"""
*Insights -   
As from the above features scatter plot matrix, we can see that : The malignant and begin tumors are separable in most of the pair plots, so taking more than two features for model building is really helpful for classification.*
"""

