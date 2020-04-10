import os

main_dir = '../main'  # main directory
# extensions of files that are supposed to be deleted
unwanted_extensions = ('.exe', '.out')
# paths to directories that should be ignored. .vscode or .git are good examples.
ignored_directories = (f'{main_dir}/.git', f'{main_dir}/.vscode')


def remove_all_in_dir(path):
    for current_name in os.listdir(path):
        full_path = os.path.join(path, current_name)
        if os.path.isdir(full_path) and full_path not in ignored_directories:
            print(f'Entering: {full_path}')
            remove_all_in_dir(full_path)
        elif current_name.endswith(unwanted_extensions):
            print(f'Removed: {full_path}')
            os.remove(full_path)


remove_all_in_dir(main_dir)
