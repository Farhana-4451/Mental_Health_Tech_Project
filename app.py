import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Mental Health in Technology",
    page_icon="🧠",
    layout="wide"
)

# Title
st.title("🧠 Mental Health in Technology")
st.subheader("Exploratory Data Analysis Dashboard")

st.write(
    "This dashboard explores mental health treatment patterns "
    "among employees in technology workplaces."
)

# Load cleaned dataset
df = pd.read_csv("data/cleaned_mental_health.csv")

# Sidebar Filters
st.sidebar.header("🔎 Filters")

selected_country = st.sidebar.selectbox(
    "Select Country",
    ["All"] + sorted(df["Country"].dropna().unique().tolist())
)

selected_gender = st.sidebar.selectbox(
    "Select Gender",
    ["All"] + sorted(df["Gender"].dropna().unique().tolist())
)

selected_remote = st.sidebar.selectbox(
    "Remote Work",
    ["All"] + sorted(df["remote_work"].dropna().unique().tolist())
)

selected_treatment = st.sidebar.selectbox(
    "Treatment",
    ["All"] + sorted(df["treatment"].dropna().unique().tolist())
)

# Apply Filters
filtered_df = df.copy()

if selected_country != "All":
    filtered_df = filtered_df[
        filtered_df["Country"] == selected_country
    ]

if selected_gender != "All":
    filtered_df = filtered_df[
        filtered_df["Gender"] == selected_gender
    ]

if selected_remote != "All":
    filtered_df = filtered_df[
        filtered_df["remote_work"] == selected_remote
    ]

if selected_treatment != "All":
    filtered_df = filtered_df[
        filtered_df["treatment"] == selected_treatment
    ]

# Dashboard Metrics
total_employees = len(filtered_df)

treated_employees = (
    filtered_df["treatment"] == "Yes"
).sum()

not_treated_employees = (
    filtered_df["treatment"] == "No"
).sum()

treatment_rate = (
    (treated_employees / total_employees) * 100
    if total_employees > 0
    else 0
)

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Employees",
    total_employees
)

col2.metric(
    "Received Treatment",
    treated_employees
)

col3.metric(
    "Did Not Receive Treatment",
    not_treated_employees
)

col4.metric(
    "Treatment Rate",
    f"{treatment_rate:.1f}%"
)

# --------------------------------------------------
# Treatment Distribution
# --------------------------------------------------

st.subheader("Mental Health Treatment Distribution")

treatment_chart = (
    filtered_df["treatment"]
    .value_counts()
    .rename_axis("Treatment")
    .to_frame("Count")
)

st.bar_chart(treatment_chart)


# --------------------------------------------------
# Family History vs Treatment
# --------------------------------------------------

st.subheader("Family History and Mental Health Treatment")

family_chart = (
    filtered_df
    .groupby(["family_history", "treatment"])
    .size()
    .unstack(fill_value=0)
)

st.bar_chart(family_chart)


# --------------------------------------------------
# Work Interference vs Treatment
# --------------------------------------------------

st.subheader("Work Interference and Mental Health Treatment")

work_chart = (
    filtered_df
    .groupby(["work_interfere", "treatment"])
    .size()
    .unstack(fill_value=0)
)

st.bar_chart(work_chart)


# --------------------------------------------------
# Remote Work vs Treatment
# --------------------------------------------------

st.subheader("Remote Work and Mental Health Treatment")

remote_chart = (
    filtered_df
    .groupby(["remote_work", "treatment"])
    .size()
    .unstack(fill_value=0)
)

st.bar_chart(remote_chart)


# --------------------------------------------------
# Workplace Benefits vs Treatment
# --------------------------------------------------

st.subheader("Workplace Benefits and Mental Health Treatment")

benefits_chart = (
    filtered_df
    .groupby(["benefits", "treatment"])
    .size()
    .unstack(fill_value=0)
)

st.bar_chart(benefits_chart)


# --------------------------------------------------
# Care Options vs Treatment
# --------------------------------------------------

st.subheader("Mental Health Care Options and Treatment")

care_chart = (
    filtered_df
    .groupby(["care_options", "treatment"])
    .size()
    .unstack(fill_value=0)
)

st.bar_chart(care_chart)


# --------------------------------------------------
# Wellness Program vs Treatment
# --------------------------------------------------

st.subheader("Workplace Wellness Program and Mental Health Treatment")

wellness_chart = (
    filtered_df
    .groupby(["wellness_program", "treatment"])
    .size()
    .unstack(fill_value=0)
)

st.bar_chart(wellness_chart)


# --------------------------------------------------
# Country-wise Treatment Analysis
# --------------------------------------------------

st.subheader("Treatment Patterns by Country")

top_countries = (
    filtered_df["Country"]
    .value_counts()
    .head(10)
    .index
)

country_chart = (
    filtered_df[
        filtered_df["Country"].isin(top_countries)
    ]
    .groupby(["Country", "treatment"])
    .size()
    .unstack(fill_value=0)
)

st.bar_chart(country_chart)


# --------------------------------------------------
# Age Group vs Treatment
# --------------------------------------------------

st.subheader("Age Group and Mental Health Treatment")

age_chart = (
    filtered_df
    .groupby(["Age_Group", "treatment"], observed=False)
    .size()
    .unstack(fill_value=0)
)

st.bar_chart(age_chart)


# --------------------------------------------------
# Key Insights
# --------------------------------------------------

st.subheader("💡 Key Insights")

st.markdown("""
### 1. Mental Health Treatment
The dashboard shows the overall distribution of employees who received mental health treatment.

### 2. Family History
Treatment patterns can be compared between employees with and without a family history of mental health conditions.

### 3. Work Interference
The analysis helps identify differences in treatment patterns across different levels of mental health interference with work.

### 4. Workplace Support
Benefits, care options, wellness programs, and help-seeking support provide an overview of the mental health support available in the workplace.

### 5. Demographic Patterns
Age-group and country-wise analysis helps explore how treatment patterns vary across different employee groups.
""")


# Footer
st.markdown("---")

st.caption(
    "Mental Health in Technology | Exploratory Data Analysis Project"
)

st.caption(
    "Data-driven analysis of mental health treatment patterns "
    "in technology workplaces."
)