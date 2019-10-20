# Usage

1. Install the requirements
```
pip install -r requirements.txt
```

2. Download the trained weights, vocabulary, and other requirements. This can be done by simply running `download_embeddings.py`:
```
python3 download_embeddings.py
```
**Disclaimer:** The size of download is approximately 500 mb.

3. Run the flask server and connect to backend database. This is done by running `app.py`:
```
python3 app.py
``` 
#
Detailed R&D can be found inside [inout-bert.ipynb](inout-bert.ipynb)

