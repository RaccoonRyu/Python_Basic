import os

def rename_files_in_directory(directory_path):
    for root, _, files in os.walk(directory_path):
        for file in files:
            if file.endswith(".py") and not file.startswith("02_"):  # 이미 접두사가 붙은 파일 제외
                old_path = os.path.join(root, file)
                new_path = os.path.join(root, f"02_{file}")
                os.rename(old_path, new_path)
                print(f"Renamed: {old_path} -> {new_path}")

# CH02 디렉터리 경로
target_directory = "C:/Users/Ryu Raccoon/vscodeProjects/Python_Basic/CH02_DataType"  # 사진에 보이는 CH02 경로를 지정하세요.
rename_files_in_directory(target_directory)