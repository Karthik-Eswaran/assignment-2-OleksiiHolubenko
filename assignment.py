def read_file(file_path: str) -> str: 
    try:
         f = open(file_path, "r")
         return f.read()
    except FileNotFoundError:
         return "File not found" 


def write_file(file_path: str, content: str) -> None:
    f = open(file_path, "w")
    f.write(content)

import os

def list_files_in_directory(directory_path: str) -> list:
    try:
        return os.listdir(directory_path)
    except FileNotFoundError:
        return "File not found"


def generate_numbers(n: int) -> iter:
    return iter(range(n))
    
import importlib

def use_function_from_module(module_name: str, function_name: str, *args) -> any:
    try:
        module = importlib.import_module(module_name)  
        func = getattr(module, function_name)         
        return func(*args)                            
    except ModuleNotFoundError:
        return(f"Module '{module_name}' not found")
    except AttributeError:
        return(f"Attribute '{function_name}' not Found")
