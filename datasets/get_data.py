""" Get lhc datasets """

from zipfile import ZipFile
from tqdm import tqdm
import os
import wget

URL = "https://www.dropbox.com/s/4u8iu7hpjacautk/kias.zip?dl=1"
NAME = "kias.zip"
wget.download(URL, f"{NAME}")

# Re-open the newly-created file with ZipFile()
with ZipFile("kias.zip","r") as zip_ref:
     for file in tqdm(iterable=zip_ref.namelist(), total=len(zip_ref.namelist())):
          zip_ref.extract(member=file)
          
os.remove("kias.zip")