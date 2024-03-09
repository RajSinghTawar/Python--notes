import os, shutil

# NOTE: you can write every single extensions inside tuples
dict_extensions = {
    'audio_extensions' : ('.mp3','.m4a','.wav','.flac'),
    'video_extensions' : ('.mp4','.mkv','.MKV','.flv','.mpeg'),
    'document_extensions' : ('.doc','.pdf','.txt')
}

folderpath = input('Enter folder path : ')

def file_finder(folder_path, file_extensions):
    # files = []
    # for file in os.listdir(folder_path):
    #     for extensions in file_extensions:
    #         if file.endswith(extensions):
    #             files.append(file)
    # return files
    return [file for file in os.listdir(folder_path) for extensions in file_extensions if file.endswith(extensions)]
# print(file_finder(folderpath, audio_extensions))

for extensions_type, extensions_tuple in dict_extensions.items():
    folder_name = extensions_type.split('_')[0] + 'Files'
    folder_path = os.path.join(folderpath, folder_name)
    os.mkdir(folder_path)
    for item in file_finder(folderpath, extensions_tuple):
        item_path = os.path.join(folderpath, item)
        item_new_path = os.path.join(folder_path,item)
        shutil.move(item_path,item_new_path)


    # print('calling file finder')
    # print(file_finder(folderpath, extensions_tuple))
