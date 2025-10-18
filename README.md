# Movie Recommender System

## Project Setup Instructions

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)
- Virtual environment tool (e.g., `venv` or `conda`)

### Setup Steps

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd movie_recommend
   ```

2. **Create a Virtual Environment**
   ```bash
   python -m venv movie-recommend
   # Activate the virtual environment
   # On Windows:
   .\movie-recommend\Scripts\activate
   # On macOS/Linux:
   source movie-recommend/bin/activate
   ```

3. **Install Required Libraries**
   ```bash
   pip install -r requirements.txt
   ```

4. **Download the Dataset**
   - Place the following files in the `data/` directory:
     - `movies_metadata.csv`
     - `credits.csv`
     - `ratings.csv`
     - `keywords.csv`

5. **Run Jupyter Notebooks**
   ```bash
   jupyter notebook
   ```

6. **Project Structure**
   ```
   movie_recommender/
   ├── data/                    # Datasets
   ├── notebooks/               # Jupyter notebooks
   ├── models/                  # Saved models
   ├── README.md                # Documentation
   └── requirements.txt         # Dependencies
   ```

### Notes
- Ensure all datasets are verified before proceeding.
- Use the `notebooks/` directory for exploratory and modeling tasks.
- Save all trained models in the `models/` directory.
