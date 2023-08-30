##Data Science project on automating the process of determining the cuisine of a food recipe
# download library to read data into dataframe
import pandas as pd 
pd.set_option('display.max_columns', None)

# Download data from IBM server and read into pandas dataframe
recipes = pd.read_csv("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DS0103EN-SkillsNetwork/labs/Module%202/recipes.csv")

# check first few rows
# print(recipes.head()) 
# get dimension of the data frame
# print(recipes.shape) 

# the dataset consists of 57,961 recipes. From initial EDA, each row represents a recipe, and for each recipe, the cuisine is documented as well as whether 384 ingredients exist in the recipe or not, beginning with almond ending with zucchini.

# checking if the ingredients of a sushi (i.e., rice, soy sauce, wasabi, fish/vegetables) exist in dataframe
ingredients = list(recipes.columns.values) 

print([match.group(0) for ingredient in ingredients for match in [(re.compile(".*(rice).*")).search(ingredient)] if match])
print([match.group(0) for ingredient in ingredients for match in [(re.compile(".*(wasabi).*")).search(ingredient)] if match])

