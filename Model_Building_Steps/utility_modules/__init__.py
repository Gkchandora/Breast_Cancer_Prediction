# __all__ = ["data_wrangling"]

# Alternate approach to get rid from invoking by module.method

# url of the packages
url = "https://raw.githubusercontent.com/Gkchandora/Breast_Cancer_Prediction/main/Model_Building_Steps/utility_modules"

# import libraries
import httpimport 

# import modules
with httpimport.remote_repo(["data_wrangling", url]):
    from data_wrangling import *
