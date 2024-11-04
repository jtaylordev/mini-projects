# main.py
from file_management_system import FileManagementSystem


def command_line_interface():
    fms = FileManagementSystem()
    while True:
        cmd = input(f"{fms.get_current_path()}$ ").strip().split()
        if not cmd:
            continue
        command = cmd[0]
        args = cmd[1:]

        if command == 'mkdir':
            if args:
                fms.create_folder(args[0])
            else:
                print("Usage: mkdir folder_name")
        elif command == 'touch':
            if args:
                fms.create_file(args[0])
            else:
                print("Usage: touch file_name")
        elif command == 'cd':
            if args:
                fms.change_directory(args[0])
            else:
                print("Usage: cd folder_name")
        elif command == 'ls':
            fms.list_directory()
        elif command == 'pwd':
            print(fms.get_current_path())
        elif command == 'save':
            if args:
                fms.save_file_system(args[0])
            else:
                print("Usage: save filename")
        elif command == 'load':
            if args:
                fms.load_file_system(args[0])
            else:
                print("Usage: load filename")
        elif command == 'exit':
            print("Exiting the file management system.")
            break
        else:
            print(f"Unknown command: {command}")

if __name__ == "__main__":
    command_line_interface()
