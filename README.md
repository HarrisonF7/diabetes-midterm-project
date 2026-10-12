# Diabetes 130-US Hospitals: Midterm Project

## Group Members
- Harrison Furman
- Serban Negoita
- Thomas Raulerson

## Project Overview
This project examines the relationship between the number of medications administered during a hospital encounter and the length of hospital stay among patients with diabetes. We also investigate whether this relationship differs depending on insulin treatment status.

## Research Question
Among hospitalized patients with diabetes, how does the number of medications administered relate to length of hospital stay, and does this relationship differ by insulin treatment status?

## Dataset
We use the Diabetes 130-US Hospitals dataset, which contains 101,766 hospital encounters from 130 U.S. hospitals between 1999 and 2008.

The dataset was provided by our instructor and is also available through the UCI Machine Learning Repository.

Our analysis focuses on three variables:
- `num_medications`: Number of different medications administered during an encounter.
- `time_in_hospital`: Length of hospital stay in days.
- `insulin`: Insulin treatment status during the encounter.

## Analysis
We use Python, pandas, matplotlib, and Marimo to:
- Filter, sort, and group hospital encounters.
- Create a new column identifying insulin and no-insulin groups.
- Calculate correlations and group averages.
- Create a histogram, boxplot, scatter plot, and bar chart.

## How to Run the Notebook

1. Download or clone this GitHub repository.
2. Install Python and the required packages:

   `pip install marimo pandas matplotlib`

3. Open a terminal in the downloaded project folder.
4. Run:

   `marimo edit diabetes_analysis-2.py`

5. Open the Marimo notebook in your browser and explore the analysis.

The `diabetic_data.csv` file must remain in the same folder as the notebook.

## Key Findings
- Overall correlation between medication count and hospital stay length: **0.466**
- Correlation for encounters involving insulin: **0.488**
- Correlation for encounters without insulin: **0.416**
- Average hospital stay with insulin: **4.67 days**
- Average hospital stay without insulin: **4.08 days**

The results suggest a moderate positive relationship between medication count and hospital stay length, with a somewhat stronger relationship among encounters involving insulin. These findings describe associations and do not establish causation.
