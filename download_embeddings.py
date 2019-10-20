import tarfile
import os
import requests
import urllib.request
import tarfile
import zipfile

def download_file_from_google_drive(id, destination):
    URL = "https://docs.google.com/uc?export=download"

    session = requests.Session()

    response = session.get(URL, params = { 'id' : id }, stream = True)
    token = get_confirm_token(response)

    if token:
        params = { 'id' : id, 'confirm' : token }
        response = session.get(URL, params = params, stream = True)

    save_response_content(response, destination)    

def get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value

    return None

def save_response_content(response, destination):
    CHUNK_SIZE = 32768

    with open(destination, "wb") as f:
        for chunk in response.iter_content(CHUNK_SIZE):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)

def use_once_func():

	urllib.request.urlretrieve('https://github.com/naver/biobert-pretrained/releases/download/v1.0-pubmed-pmc/biobert_v1.0_pubmed_pmc.tar.gz', 'BioBert.tar.gz')

	if not os.path.exists('BioBertFolder'):
	    os.makedirs('BioBertFolder')
	    
	tar = tarfile.open("BioBert.tar.gz")
	tar.extractall(path='BioBertFolder/')
	tar.close()

	file_id = '1uCXv6mQkFfpw5txGnVCsl93Db7t5Z2mp'

	download_file_from_google_drive(file_id, 'Float16EmbeddingsExpanded5-27-19.pkl')

	file_id = 'https://onedrive.live.com/download?cid=9DEDF3C1E2D7E77F&resid=9DEDF3C1E2D7E77F%2132792&authkey=AEQ8GtkcDbe3K98'
	    
	urllib.request.urlretrieve( file_id, 'DataAndCheckpoint.zip')

	if not os.path.exists('newFolder'):
	    os.makedirs('newFolder')

	zip_ref = zipfile.ZipFile('DataAndCheckpoint.zip', 'r')
	zip_ref.extractall('newFolder')
	zip_ref.close()

from docproduct.predictor import RetreiveQADoc

pretrained_path = 'BioBertFolder/biobert_v1.0_pubmed_pmc/'
# ffn_weight_file = None
bert_ffn_weight_file = 'newFolder/models/bertffn_crossentropy/bertffn'
embedding_file = 'Float16EmbeddingsExpanded5-27-19.pkl'

doc = RetreiveQADoc(pretrained_path=pretrained_path,
ffn_weight_file=None,
bert_ffn_weight_file=bert_ffn_weight_file,
embedding_file=embedding_file)