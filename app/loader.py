from langchain_community.document_loaders import PyMuPDFLoader,TextLoader, DirectoryLoader

def load_document(file_path:str):
    if file_path.endswith(".pdf"):
        loader=PyMuPDFLoader(file_path)
    else:
        loader=TextLoader(file_path,encoding="utf-8")
    return loader.load()
def load_directory(dir_path:str, glob_pattern:str="**/*.*"):
    loader=DirectoryLoader(dir_path,glob=glob_pattern)
    return loader.load()    