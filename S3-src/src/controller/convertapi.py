from os import getenv
import os
from dotenv import load_dotenv
import convertapi

class ConvertApi:
    
    def __init__(self):
        load_dotenv()
        self.API_KEY = getenv('API_KEY_PDF')
        convertapi.api_secret=self.API_KEY
    
    def extraer_imagenes(self, files):
        return convertapi.convert('extract-images', {'File': files})
    
    def unir_pdfs(self, files): 
        return convertapi.convert('merge',{'Files': files}, from_format='pdf')

    def convertir_archivo(self, files, convert_to): 
        return convertapi.convert(convert_to, {'File': files})

