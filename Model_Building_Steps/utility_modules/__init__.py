# modules
# __all__ = ["sample"] 
print("init file invoked")
def infun(s):
    print("init file executed")

url = "https://raw.githubusercontent.com/Gkchandora/Breast_Cancer_Prediction/main/Model_Building_Steps/utility_modules"

with httpimport.remote_repo(["sample","data_wrangling", "junk"], url):
    import junk
    from sample import *
    from data_wrangling import *