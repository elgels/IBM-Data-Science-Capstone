<h1>IBM Data Science Capstone Project</h1>

<h2>Project Overview</h2>
<p>
This repository contains my capstone project for the <strong>IBM Data Science Professional Certificate (Coursera)</strong>, completed in April 2024, prior to beginning my Master’s in Data Science.
</p>

<p>
The project demonstrates a complete <strong>end-to-end data science workflow</strong>, including data collection, preprocessing, exploratory analysis, and machine learning modeling.
</p>

<p>
While the dataset is relatively small, this project establishes a strong foundation and serves as a baseline for more advanced work developed during my graduate studies.
</p>

<hr>

<h2>Objective</h2>
<p>
The goal of this project is to <strong>predict whether the first stage of a Falcon 9 rocket will land successfully</strong>, which has direct implications for <strong>launch cost estimation</strong>.
</p>

<hr>

<h2>Key Skills Demonstrated</h2>
<ul>
  <li>Data collection (API &amp; web scraping)</li>
  <li>Data wrangling and preprocessing</li>
  <li>Exploratory Data Analysis (EDA)</li>
  <li>Data visualization</li>
  <li>Geospatial analysis (Folium)</li>
  <li>Interactive dashboards (Dash)</li>
  <li>Machine learning modeling and evaluation</li>
</ul>

<hr>

<h2>Project Presentation</h2>
<p>
  <a href="./reports/IBM_Capstone_Presentation_Report.pdf">View Project Presentation (PDF)</a>
</p>

<hr>

<h2>Important Note About the Notebooks</h2>
<p>
The Jupyter notebooks in this repository were provided as <strong>guided lab assignments by IBM</strong> as part of the capstone project.
</p>

<ul>
  <li>The structure and instructions were provided by IBM</li>
  <li>All code implementations, analysis, and answers were completed by me</li>
  <li>The notebooks were submitted for grading as part of the certification</li>
</ul>

<p>
The final presentation included in this repository was <strong>fully created by me</strong> and summarizes the complete analysis and results.
</p>

<hr>

<h2>Repository Structure</h2>

<pre><code>.
├── data/
│   ├── dataset_part_1.csv
│   ├── dataset_part_2.csv
│   ├── dataset_part_3.csv
│   ├── spacex_launch_dash.csv
│   └── spacex_launch_geo.csv
│
├── notebooks/
│   ├── Collecting_the_Data_API.ipynb
│   ├── Webscraping_Records_from_Wikipedia.ipynb
│   ├── Data_Wrangling.ipynb
│   ├── EDA_using_SQL.ipynb
│   ├── Data_Visualization.ipynb
│   ├── Launch_Sites_Locations_Analysis_with_Folium.ipynb
│   ├── Machine_Learning_Prediction.ipynb
│   └── Dashboard_Application_with_Dash.ipynb
│
├── reports/
│   └── IBM_Capstone_Presentation_Report.pdf
│
├── requirements.txt
└── README.md
</code></pre>

<hr>

<h2>Notebooks Description</h2>
<ul>
  <li><strong>Collecting the Data (API)</strong><br>Data collection using the SpaceX API</li>
  <li><strong>Web Scraping Records from Wikipedia</strong><br>Data extraction using web scraping</li>
  <li><strong>Data Wrangling</strong><br>Data cleaning and preprocessing</li>
  <li><strong>EDA using SQL</strong><br>Exploratory analysis using SQL queries</li>
  <li><strong>Data Visualization</strong><br>Visual analysis using matplotlib, seaborn, and plotly</li>
  <li><strong>Launch Sites Location Analysis (Folium)</strong><br>Geospatial visualization and mapping</li>
  <li><strong>Dashboard Application with Dash</strong><br>Interactive dashboard for data exploration</li>
  <li><strong>Machine Learning Prediction</strong><br>Model training, tuning, and evaluation</li>
</ul>

<hr>

<h2>Technologies &amp; Libraries</h2>

<h3>Python Libraries</h3>
<ul>
  <li>pandas</li>
  <li>numpy</li>
  <li>matplotlib</li>
  <li>seaborn</li>
  <li>plotly</li>
  <li>sqlite3</li>
  <li>dash</li>
  <li>folium</li>
  <li>requests</li>
  <li>datetime</li>
  <li>os</li>
</ul>

<h3>Machine Learning (scikit-learn)</h3>
<ul>
  <li>train_test_split</li>
  <li>GridSearchCV</li>
  <li>LogisticRegression</li>
  <li>SVC</li>
  <li>DecisionTreeClassifier</li>
  <li>KNeighborsClassifier</li>
</ul>

<hr>

<h2>Setup</h2>
<p>Install dependencies:</p>
<pre><code>pip install -r requirements.txt
</code></pre>

<hr>

<h2>Key Takeaways</h2>
<ul>
  <li>Built a complete data science pipeline from raw data to predictive modeling</li>
  <li>Developed interactive visualizations and dashboards for insights</li>
  <li>Applied geospatial analysis to understand launch site behavior</li>
   <li>Compared multiple machine learning models for classification performance</li>
</ul>

<hr>

<h2>Future Improvements</h2>
<ul>
  <li>Apply ensemble methods such as Random Forest and Gradient Boosting</li>
  <li>Use larger and more recent datasets</li>
  <li>Deploy the dashboard as a live web application</li>
</ul>
