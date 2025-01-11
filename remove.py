import os

def remove_lines_from_file(file_path, line_to_remove):
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
            lines = file.readlines()
        
        with open(file_path, 'w', encoding='utf-8', errors='ignore') as file:
            for line in lines:
                if line.strip() != line_to_remove:
                    file.write(line)
        print(f"Processed: {file_path}")

    except Exception as e:
        print(f"Error processing {file_path}: {e}")

def process_directory(directory, line_to_remove):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.txt'):
                file_path = os.path.join(root, file)
                remove_lines_from_file(file_path, line_to_remove)

if __name__ == "__main__":
    directory_path = os.path.expanduser("~/Desktop") 
    line_to_remove = '==================Blank Grabber==================='
    
    process_directory(directory_path, line_to_remove)



