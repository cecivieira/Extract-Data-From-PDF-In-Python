import os

list_ = os.listdir()

for folder in list_:    
    if '.' not in folder:        
        sub_list = os.listdir(folder)
        os.makedirs(f'{folder}_txt', exist_ok=False)
        folder_error = []
        for archive in sub_list:
            if archive.endswith('.pdf'):
                try:
                    os.system(f"pdftotext '{folder}/{archive}' '{folder}_txt/{archive[:-4]}.txt'")
                except Exception as error:
                    print(error)
            else:
                print(archive)