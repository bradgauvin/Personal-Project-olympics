# Person Project: Olympic medalist predictions
*Audience: Target audience for my final report is a Codeup Data Science Students


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
| acres                          | grouped bins, based upon lot square footage        | category  |
| age                            | grouped bins, based upon year built.               | category  |
| assessed_value                 | total tax assessed value of the property           | float64   |
| bathroom_bins                  | grouped bins, based upon number of bedrooms        | category  |
| bathrooms                      | number of bathrooms and half-bathrooms in home     | float64   |
| bedroom_bins                   | grouped bins, based upon number of bedrooms        | category  |
| bedrooms                       | number of bedrooms in the home                     | float64   |
| county_code_bin                | name of county as assigned by state_county_code    | category  |
| county_code_bin_Orange County  | numeric variable representing county_code_bin      | uint8     |
| county_code_bin_Ventura County | numeric variable representing county_code_bin      | uint8     |
| latitude                       | Latitude of the middle of the parcel multiplied by 10e6  | category  |
| logerror                       | Residual Error in Home Valuation                   | float64   |
| longitude                      | Longitude of the middle of the parcel multiplied by 10e6 | category  |
| home_sizes                     | grouped bins, based upon square footage            | category  |
| square_feet                    | total finished living area of the home             | float64   |
| state_county_code              | federal information processing standards code      | object    |
| total_rooms                    | combined number of bedrooms and bathrooms          | float64   |
| year_built                     | year the primary residence was constructed         | int64     |

|Target Variable                 | Definition                                         | Data Type|
|:-------------------------------|:--------------------------------------------------:|:---------:|
|logerror                        | Residual Error in Home Valuation                   |           |
<hr style="background-color:silver;height:3px;" />

## Reproducing this project
<hr style="background-color:silver;height:3px;" />

> In order to reproduce this project you will need your own environment file and access to the database. You can reproduce this project with the following steps:
> - Read this README
> - Clone the repository or download all files into your working directory
> - Add your environment file to your working directory:
>  - filename should be env.py
>  - contains variables: username, password, host
> - Run the Final_Report notebook or explore the other notebooks for greater insight into the project.

### Project Plan 

<details>
  <summary><i>Click to expand</i></summary>
  <ul>
   <li><b>Acquire</b> data from XXXX</li>
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
