import pandas as pd
import os

def generate_birthday_messages(names, file_paths):
    """
    Generates personalized birthday messages using given names and template files.

    Args:
        names (list): A list of names to personalize the messages with.
        file_paths (list): A list of file paths to the template files.

    Returns:
        pandas.DataFrame: A pandas DataFrame containing personalized messages.
    """
    messages = []
    for file_path in file_paths:
        try:
             with open(file_path, 'r', encoding='utf-8') as file:
                 template = file.read()
             for name in names:
                personalized_message = template.replace("[NAME]", name)
                messages.append({"file": os.path.basename(file_path), "name": name, "message": personalized_message})
        except FileNotFoundError:
             print(f"Error: File not found: {file_path}")
             continue
        except Exception as e:
            print(f"An error occurred while processing file: {file_path} - {e}")
            continue

    df = pd.DataFrame(messages)
    return df


names = ["Kosar"]


file_paths = ["card1.txt", "card2.txt", "card3.txt"]


for file_path in file_paths:
    if not os.path.exists(file_path):
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write("Dear [NAME] , \n Happy birthday! \n All the best for the year! \n\n Delaram")
        except Exception as e:
            print(f"Error creating file {file_path}: {e}")
            continue

print(names,file_paths)

df_messages = generate_birthday_messages(names,file_paths)
print(df_messages)

