# PromptShield: AI Prompt-Injection Firewall

A two-layer firewall (rule engine + ML classifier) that scans messages sent to a
chatbot and flags prompt-injection attacks.

## Setup
```
python -m venv venv
venv\Scripts\activate          # Windows   (Mac/Linux: source venv/bin/activate)
pip install -r requirements.txt
```

## Run (in this order)
```
python get_data.py       # downloads dataset into data/
python train.py          # trains models, saves models/ and confusion_matrix.png
python rules.py          # optional: test the rule layer
streamlit run app.py     # opens the web app at http://localhost:8501
```

## Files
- get_data.py : downloads deepset/prompt-injections from Hugging Face
- train.py    : TF-IDF + Logistic Regression / Random Forest, metrics, confusion matrix
- rules.py    : regex rule layer for known attack patterns
- app.py      : Streamlit UI (risk score, triggered rules, explainable words)
