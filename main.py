import os

def convert_bytes(num):
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0


from datetime import datetime
 # Recursively scans all subfolders and files within the given folder_path
def categorize_files_by_type(directory_path, method):
    result = {}
    
    
    for root, dirs, files in os.walk(directory_path):

        for file_name in files:
            f, file_extension = os.path.splitext(f'{root}\{file_name}')

            if(file_extension not in result):
                result[file_extension] = []

            result[file_extension].append(f'{root}\{file_name}')
            logger.info('Добаваления файла:' + f'{root}\{file_name}')
            
    if method != None:
        logger.info('Сортировака по дате')
        if method.lower() == 'time':
            for key, value in result.items():
                ## Sort list of file names by date
                files_with_dates = [(file, os.path.getmtime(file)) for file in value]
                sorted_files = sorted(files_with_dates, key=lambda x: x[1])
                result[key] = []
                for file in sorted_files:
                    result[key].append(file[0])

                    
        elif method.lower() == 'size':
            logger.info('Сортировака по Размеру')
            for key, value in result.items():
                # Sort list of file names by size  
                result[key] = sorted(value, key=lambda x: os.stat(x).st_size) 

        elif method.lower() == 'filename':
            logger.info('Сортировака по Названию')
            for key, value in result.items():
                # Sort list of file names by filename 
                result[key].sort()
        
    return result
    


import argparse

def main():
    parser = argparse.ArgumentParser(description="Пример обработки аргумента -path")
    
    # Add argument -path
    parser.add_argument('-path', type=str, help='Путь к файлу или директории', required=True)
    parser.add_argument('-sorted', type=str, help='size - сортировка по размеру, time - сортировка по времени, filename - сортировка по названия файла \nExample: \n-sorted [size, time,filename]', required=False)
    
    # Parse args
    args = parser.parse_args()
    # Write logs
    logging.basicConfig(filename='myapp.log', level=logging.INFO)
    logger.info('Started')
    print(categorize_files_by_type(args.path, args.sorted))
    logger.info('Finished')



import argparse
import logging
logger = logging.getLogger(__name__)

if __name__ == '__main__':
    main()