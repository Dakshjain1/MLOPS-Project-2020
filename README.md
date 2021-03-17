#Visualize Company Reviews Into Wordcloud Using Python – NLP Powered Module Via End-2-End Azure Devops Pipeline

<p align="center">
MLOPS-Project-2020
 </p>

![MLOPS Project Design Architecture](https://github.com/Dakshjain1/MLOPS-Project-2020/raw/main/mlops%20project.PNG)  

•	ML Developer creates an NLP powered “Word Cloud Generator” module using Python.     
•	The module is packed into an Egg file and pushed to Azure Repos (SCM provided by Microsoft Azure).      
 
   ~  Remain in the module folder, create a file `setup.py` (sample given in the repo) and use the command →  
```
$ python3 setup.py bdist_egg  
```
   ~  The Egg file is present in `dist` folder that will be created after running this command.   
     
•	When a push is made to the Azure Repos the Build Pipeline is triggered.   
•	The Build Pipeline creates Artifacts containing the requirement.txt file & the module Egg File.   
•	The Release Pipeline is triggered & takes these artifacts to Databricks cluster.  
•	In the Release Pipeline, specify the source path of artifacts, the destination in Databricks & the bearer token – which is an access token provided by Databricks to Azure Devops.  
•	The client puts the dataset containing the reviews in the Azure Blob Storage.  
•	The Blob Storage is mounted to Databricks by providing an Access Key.  
•	It is mounted to Databricks to provide the dataset (used as input by the module) & store the output image for client usage.  
•	The requirement.txt file is loaded to install required dependencies.   
•	The module (an egg file) is unzipped in Databricks node.  
•	The module can take a txt, csv, or xlsx(other variants also) as an input.  
•	Any kind of input is converted into a single string format.  
•	Using NLP functions the most frequent words are chosen & their polarity is calculated.  
•	Based on polarity the colour is decided [positive – green ; negative – red].  
•	The words in the reviews & the colour list are passed to the word cloud generator.  
•	The Word Cloud is stored in the mounted folder as a png file.
•	It is stored in the mount point so that it is also visible in Blob Storage for client access.

A Sample of our generated Wordcloud → 
![Wordcloud](https://github.com/Dakshjain1/MLOPS-Project-2020/raw/main/1.PNG)  
