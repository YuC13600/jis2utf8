import os

failed = []
def convert_encoding(folder_path):
    global failed
    for dir_path, dirnames, filenames in os.walk(folder_path):
        for filename in filenames:
            full_path = os.path.join(dir_path, filename)
            if full_path.endswith('.x'):
                try:
                    with open(full_path, 'r', encoding='shift-jis') as file:
                        content = file.read()
                    with open(full_path, 'w', encoding='utf-8') as file:
                        file.write(content)

                        print(f"Successed converting {full_path} to utf-8")
                except Exception as e:
                    print(f"Failed to convert {full_path} : {e}")
                    failed.append(full_path)

        for dirname in dirnames:
            full_path = os.path.join(dir_path, dirname)
            convert_encoding(full_path)

        break

if __name__ == '__main__':
    convert_encoding("C:\\Users\\a0985\\OneDrive\\Desktop\\temp\\GeibiLineProject")
    convert_encoding("C:\\Users\\a0985\\OneDrive\\Desktop\\temp\\Hckh_common")

    print("==========Failed==========")
    for fail in failed:
        print(f"Failed to convert {fail}")
