# IBM Data Science Capstone

## Project Overview
This repository contains a capstone portfolio project for IBM Data Science Professional Certificate, including data collection, wrangling, EDA, visualization, and machine learning modeling tasks. It covers a complete end-to-end analysis workflow using real-world datasets and modern Python data science libraries.

## Repository Structure
- `Collecting the Data API-api.ipynb`: API data collection and extraction
- `Data Wrangling.ipynb`: data cleaning and transformation
- `EDA using SQL.ipynb`: exploratory data analysis with SQL queries
- `Data Visualization.ipynb`: charts and insights with matplotlib/seaborn/plotly
- `Launch Sites Locations Analysis with Folium.ipynb`: geospatial visualization in Folium
- `Machine Learning Prediction.ipynb`: model training, evaluation, and prediction pipeline
- `Build a Dashboard Application with Plotly Dash.py`: interactive web dashboard implementation
- `Webscraping Records from Wikipedia.ipynb`: web scraping demonstration from Wikipedia
- `Capstone Project Presentation.pdf`: final presentation slides

## Objectives
1. Acquire data from APIs and web sources
2. Clean and preprocess datasets for analysis
3. Perform exploratory data analysis (EDA) to generate actionable insights
4. Develop and evaluate machine learning models
5. Build a user-facing dashboard for reporting results

## Getting Started
1. Clone the repository
   ```bash
   git clone https://github.com/elgels/IBM-Data-Science-Capstone.git
   cd IBM-Data-Science-Capstone
   ```
2. Create and activate a virtual environment
   ```bash
   python -m venv venv
   venv\Scripts\activate   # Windows
   source venv/bin/activate  # macOS/Linux
   ```
3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```
4. Open notebooks in Jupyter
   ```bash
   jupyter notebook
   ```

## Key Dependencies
- pandas
- numpy
- scikit-learn
- matplotlib
- seaborn
- plotly
- folium
- dash
- jupyter
- requests

## Usage Notes
- Run notebooks sequentially: data collection -> wrangling -> EDA -> modeling -> dashboard.
- Save intermediate clean data to avoid repeating long preprocessing steps.
- Customize the dashboard script with your local file path or data exports.

## Author
- Project by: IBM Data Science Capstone student
- GitHub: https://github.com/elgels

## License
This project is provided for educational purposes. Feel free to adapt and reuse the notebooks for learning and portfolio development.
