import os
import glob
import nltk
import pandas as pd

nltk.download('punkt')
from collections import Counter
from nltk.tokenize.casual import casual_tokenize

def process_xml_files_in_folder(folder):
    word_count = Counter()

    for root, dirs, files in os.walk(folder):
        # Encuentra todos los archivos XML en la carpeta actual
        xml_files = glob.glob(os.path.join(root, "*.xml"))

        for xml_file in xml_files:
            # Imprime la ruta del archivo actual
            print("Procesando archivo:", xml_file)

            # Analiza el archivo XML
            with open(xml_file, "r") as f:
                xml_data = f.read()

            # Remueve todas las etiquetas XML del texto
            import re
            clean_data = re.sub('<.*?>', '', xml_data)

            # Extrae el texto de los subtítulos y cuenta las palabras (sin distinción de mayúsculas y minúsculas)
            words = casual_tokenize(clean_data.lower())
            word_count.update(words)

    return word_count

def save_to_csv(word_count, output_file):
    df = pd.DataFrame(word_count.items(), columns=['word', 'count'])
    df = df.sort_values('count', ascending=False)
    df.to_csv(output_file, index=False)

# Directorio principal que contiene las carpetas
parent_folder = "/Users/alejandroasor/Documents/en/"
output_file = "all_words_raw.csv"

total_word_count = process_xml_files_in_folder(parent_folder)

# Muestra el recuento total de palabras
print(total_word_count)

# Guarda el recuento de palabras en un archivo CSV
save_to_csv(total_word_count, output_file)
