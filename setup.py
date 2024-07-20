import os

def create_project_structure(base_dir):
    # Define the directory structure
    dirs = [
        "backend/app/routes",
        "backend/app/models",
        "backend/app/utils",
        "frontend",
        "tests"
    ]
    
    # Define the files to create
    files = [
        "backend/app/__init__.py",
        "backend/app/routes/__init__.py",
        "backend/app/models/__init__.py",
        "backend/app/utils/__init__.py",
        "backend/config.py",
        "backend/run.py",
        "tests/__init__.py",
        "requirements.txt",
        "README.md"
    ]
    
    # Create the directories
    for dir in dirs:
        os.makedirs(os.path.join(base_dir, dir), exist_ok=True)
    
    # Create the files
    for file in files:
        with open(os.path.join(base_dir, file), 'w') as f:
            pass  # Create an empty file

if __name__ == "__main__":
    project_root = "project_root"  # Change this to your desired project root
    create_project_structure(project_root)
    print(f"Project structure created under '{project_root}'")
