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
        # Find all XML files in the current folder
        xml_files = glob.glob(os.path.join(root, "*.xml"))

        for xml_file in xml_files:
            # Print the path of the current file
            print("Procesando archivo:", xml_file)

            # Parse the XML file
            with open(xml_file, "r") as f:
                xml_data = f.read()

            # Remove all XML tags from the text
            import re
            clean_data = re.sub('<.*?>', '', xml_data)

            # Extract the text from the subtitles and count the words (case-insensitive)
            words = casual_tokenize(clean_data.lower())
            word_count.update(words)

    return word_count

def save_to_csv(word_count, output_file):
    df = pd.DataFrame(word_count.items(), columns=['word', 'count'])
    df = df.sort_values('count', ascending=False)
    df.to_csv(output_file, index=False)

# Main directory containing the folders
parent_folder = "/path/to/main/directory"
output_file = "word_count.csv"

total_word_count = process_xml_files_in_folder(parent_folder)

# Display the total word count
print(total_word_count)

# Save the word count to a CSV file
save_to_csv(total_word_count, output_file)
