# Person Project: Olympic medalist predictions
*Audience: Target audience for my final report is a Codeup Data Science Students

![image.png](attachment:image.png)

### Description
120 years of olympic data was pull.  Athletic information and event data is merged with medalist data to identify if athletes are able to medal in the games.  Based on the data provided by these datasets, the goal of this project is to find if there is a better way to predict if an athlete will medal.

<hr style="background-color:silver;height:3px;" />

## Project Summary

> - The purpose of this project was to identify which Olympians would medal in the olympics based on information derived from the olympics.com data. 

<hr style="background-color:silver;height:3px;" />

### Project Deliverables
> - A final report notebook (Jupyter Notebook)
> - Python modules for automation and to facilitate project reproduction
> - Notebooks that show:
> - This README file
>  - Data acquisition and preparation 
>  - exploratory analysis 
> - Trell board was used for project updates
> - Tableau was used for some visuals
  - [Link to Tableau dashboard](https://public.tableau.com/views/OlympicCountrySport/Dashboard1?:language=en-US&:display_count=n&:origin=viz_share_link)
  - [Link to Trello](https://trello.com/invite/b/MKjYvF4Y/a2ff8f44b2213759036f8c0ef947ea80/personal-project)
 
### Initial Hypothesis & Predictions
> - 1. Host country is a factor in medaling
> - 2. Team Sports have more medalists than individual events
> - 3. Overall BMI will not have effect on medaling
> - 4. Age will have an effect on medaling

### Specific requirements to document
> - Data Acquisition: Data was pulled from Kaggle, originally scrapped from Olympics.com website
> - Data Merge: Key data from CSVs were merged for all events and athletes in each event
> - Data Prep: Equestrian olympics (1956) and Intercolated Games (1906) were deleted from set due to missing values
> - Data Prep: Ages were updated to Jan 01 of that year, if only dates were available.  Weight categories and multiple weight ins took lowest amount displayed. 
> - Exploration: the interaction between independent variables and the target variable is explored using visualization and statistical testing
> - Exploration:  Looked at 4 key variables and visualizations to accompany
>   1. Effects of Being Athlete from Host nation
>   2. Team Sports
>   3. Age
>   4. BMI
> - Modeling: Decision Tree, Random Forest, K-Nearest Neighbors, and logistical regression were utilitzed
> - Best practices on data splitting are followed
> - The final notebook has a good title and the documentation within is sufficiently explanatory and of high quality
> - Decisions and judment calls are made and explained/documented


### Initial questions on the data

>  - 1. Effects of Being Athlete from Host nation
>  - 2. Team Sports
>  - 3. Age
>  - 4. BMI

---

<hr style="background-color:silver;height:3px;" />

## Executive Summary
<hr style="background-color:silver;height:3px;" />

**Project Goal:**

**Discoveries and Recommendations**


<hr style="background-color:silver;height:3px;" />

## Data Dictionary
<hr style="background-color:silver;height:3px;" />

| Variable                       | Definition                                         | Data Type |
|:-------------------------------|:--------------------------------------------------:|:---------:|
| athlete ID                          | unique identifier for athletes       | category  |
| Name                          | name of athlete             | str |
| sex                 | gender          | str   |
| height                  | height in cm        | float64 |
| weight                   | weight in kg    | float64   |
| born                   | date of birth (year) - deleted       | int |
| country                      | home country of athlete                    | string   |
| country_noc_x               |country code of athlete   | string  |
| edition  | summer/winter olympics     | string    |
| sport | sport name     | string    |
| result_id                       | key variable for events  | category  |
| medal                      | participant, bronze, silver, gold medalist                   | string   |
| isTeamSport                      | 1 is team sport, 0 is individual sport | category  |
| city                    | city of olympic event           | string  |
| country_noc_y                   | country code for olympic event             | string   |
| event year             | year of olympics      | int   |
| medalist                   | did athlete medal: 1 = yes, 0= no          | int64   |
| home                   | is althete from host country: 1=yes, 0 =no        | int64     |
| age                  | approximate age of athlete at time of games         | float64   |
| bmi                   | height times weight multiplied by 10000       | int    |


|Target Variable                 | Definition                                         | Data Type|
|:-------------------------------|:--------------------------------------------------:|:---------:|
|medalist                       | did athlete medal: 1 = yes, 0= no                    |           |
<hr style="background-color:silver;height:3px;" />

## Reproducing this project
<hr style="background-color:silver;height:3px;" />

> In order to reproduce this project you will need your own environment file and access to the database. You can reproduce this project with the following steps:
> - Read this README
> - need to download '!pip install opendatasets'
> - Acquire, Modeling, Utilities, and Wrangel_o files in .py format from the repo
> - Need Kaggle api token or you will be asked for kaggle login information
>    - ![image.png](attachment:image.png)
> - For information on kaggle api visit this [link](https://www.analyticsvidhya.com/blog/2021/04/how-to-download-kaggle-datasets-using-jupyter-notebook/ "how to download kaggle dataset using jupyter notebook")
> - Clone the repository or download all files into your working directory
> - Add your environment file to your working directory:
>  - filename should be env.py
>  - contains variables: username, password, host
> - Run the Final_Report notebook or explore the other notebooks for greater insight into the project.

### Project Plan 

<details>
  <summary><i>Click to expand</i></summary>
  <ul>
   <li><b>Acquire</b> data from Kaggle</li>
    <li>Clean and <b>prepare</b>data for the exploration. </li>
    <li>Create wrangle.py to store functions I created to automate the cleaning and preparation process.</li>
    <li>Separate train, validate, test subsets and scaled data.</li>
    <li><b>Explore</b> the data through visualizations; Document findings and takeaways.</li>
    <li>Perform <b>modeling</b>:
    <ul>
        <li>Identify model evaluation criteria</li>
        <li>Create at least three different models.</li>
        <li>Evaluate models on appropriate data subsets.</li>
    </ul>
    </li>
    <li>Create <b>Final Report</b> notebook with a curtailed version of the above steps.</li>
    <li>Create and review README. </li>
    
  </ul>
</details
