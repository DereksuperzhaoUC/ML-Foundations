# Environment
env: vol
Python 3.11 (micromamba)
packages: requirements.txt
Core packages:
- numpy
- pandas
- scikit-learn
- lightgbm
- xgboost
- matplotlib
- statsmodels
- yfinance
Editor:
- VS Code (remote SSH)
Run:
- `micromamba activate vol`
- `python main.py`
Or:
- `micromamba run -n vol python main.py`
