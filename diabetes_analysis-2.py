import marimo

__generated_with = "0.25.1"
app = marimo.App(width="medium")


@app.cell
def _():
    return


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Diabetes 130-US Hospitals: Midterm Project

    ## Group Members

    - Harrison Furman
    - Serban Negoita
    - Thomas Raulerson

    ## Research Question

    Among hospitalized patients with diabetes, how does the number of medications administered relate to length of hospital stay, and does this relationship differ by insulin treatment status?

    ## Dataset

    This project uses the Diabetes 130-US Hospitals dataset, which contains hospital encounters involving patients with diabetes from 130 U.S. hospitals between 1999 and 2008.

    We will examine three variables:
    - **num_medications:** Number of different medications administered during a hospital encounter.
    - **time_in_hospital:** Length of the hospital stay in days.
    - **insulin:** Whether insulin was administered during the encounter.
    """)
    return


@app.cell
def _():
    # GitHub Repository: https://github.com/HarrisonF7/diabetes-midterm-project

    # Import pandas to work with our hospital dataset
    import pandas as pd

    return (pd,)


@app.cell
def _(pd):
    # Load the diabetes dataset and display the first five rows
    df = pd.read_csv("diabetic_data.csv")
    df.head()
    return (df,)


@app.cell
def _(df):
    # Check the number of hospital encounters and columns in our dataset
    df.shape
    return


@app.cell
def _(df):
    # Display the first five rows of the three variables used in our research question
    df[["num_medications", "time_in_hospital", "insulin"]].head()
    return


@app.cell
def _(df):
    # Check for missing values in the three variables used in our research question
    df[["num_medications", "time_in_hospital", "insulin"]].isna().sum()
    return


@app.cell
def _(df):
    # Count how many hospital encounters belong to each insulin category
    df["insulin"].value_counts()
    return


@app.cell
def _(df):
    # Create a new column to classify encounters by insulin treatment status
    df_with_groups = df.assign(
        insulin_group=df["insulin"].apply(
            lambda x: "No Insulin" if x == "No" else "Insulin"
        )
    )

    # Count encounters in each new group
    df_with_groups["insulin_group"].value_counts()
    return (df_with_groups,)


@app.cell
def _(df):
    # Calculate the correlation between medication count and hospital stay
    overall_corr = df["num_medications"].corr(df["time_in_hospital"])

    round(overall_corr, 3)
    return


@app.cell
def _(df_with_groups):
    # Calculate the correlation separately for insulin and no-insulin encounters
    insulin_corr = df_with_groups[df_with_groups["insulin_group"] == "Insulin"]["num_medications"].corr(
        df_with_groups[df_with_groups["insulin_group"] == "Insulin"]["time_in_hospital"]
    )

    no_insulin_corr = df_with_groups[df_with_groups["insulin_group"] == "No Insulin"]["num_medications"].corr(
        df_with_groups[df_with_groups["insulin_group"] == "No Insulin"]["time_in_hospital"]
    )

    print("Insulin:", round(insulin_corr, 3))
    print("No Insulin:", round(no_insulin_corr, 3))
    return


@app.cell
def _(df_with_groups):
    # Compare average medication counts and hospital stays by insulin group
    group_averages = df_with_groups.groupby("insulin_group")[
        ["num_medications", "time_in_hospital"]
    ].mean()

    group_averages.round(2)
    return (group_averages,)


@app.cell
def _(df_with_groups):
    # Sort hospital encounters from highest to lowest medication count
    sorted_df = df_with_groups.sort_values(by="num_medications", ascending=False)

    # Display the first five encounters using our three research variables
    sorted_df[["num_medications", "time_in_hospital", "insulin_group"]].head()
    return


@app.cell
def _():
    # Import matplotlib to create visualizations for our research project
    import matplotlib.pyplot as plt

    return (plt,)


@app.cell
def _(df, plt):
    # Create a histogram to show the distribution of hospital stay lengths
    fig_hist, ax_hist = plt.subplots(figsize=(8, 5))

    ax_hist.hist(df["time_in_hospital"], bins=range(1, 16), edgecolor="black")

    ax_hist.set_title("Distribution of Hospital Stay Lengths")
    ax_hist.set_xlabel("Length of Hospital Stay (Days)")
    ax_hist.set_ylabel("Number of Hospital Encounters")

    fig_hist
    return


@app.cell
def _(df_with_groups, plt):
    # Compare hospital stay lengths between insulin and no-insulin groups
    fig_box, ax_box = plt.subplots(figsize=(8, 5))

    ax_box.boxplot([
        df_with_groups[df_with_groups["insulin_group"] == "No Insulin"]["time_in_hospital"],
        df_with_groups[df_with_groups["insulin_group"] == "Insulin"]["time_in_hospital"]
    ], tick_labels=["No Insulin", "Insulin"])

    ax_box.set_title("Hospital Stay Length by Insulin Treatment Status")
    ax_box.set_xlabel("Insulin Treatment Status")
    ax_box.set_ylabel("Length of Hospital Stay (Days)")

    fig_box
    return


@app.cell
def _(df, plt):
    # Create a scatter plot to examine the relationship between medication count and hospital stay length
    fig_scatter, ax_scatter = plt.subplots(figsize=(8, 5))

    ax_scatter.scatter(
        df["num_medications"],
        df["time_in_hospital"],
        alpha=0.1
    )

    ax_scatter.set_title("Number of Medications vs. Hospital Stay Length")
    ax_scatter.set_xlabel("Number of Medications")
    ax_scatter.set_ylabel("Length of Hospital Stay (Days)")

    fig_scatter
    return


@app.cell
def _(group_averages, plt):
    # Compare average hospital stay lengths between insulin treatment groups
    fig_bar, ax_bar = plt.subplots(figsize=(8, 5))

    ax_bar.bar(
        group_averages.index,
        group_averages["time_in_hospital"]
    )

    ax_bar.set_title("Average Hospital Stay Length by Insulin Treatment Status")
    ax_bar.set_xlabel("Insulin Treatment Status")
    ax_bar.set_ylabel("Average Hospital Stay Length (Days)")

    fig_bar
    return


if __name__ == "__main__":
    app.run()
