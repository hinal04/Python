import os
import shutil

def archive_logs(log_directory, archive_directory):
    if not os.path.exists(archive_directory):
        os.makedirs(archive_directory)
    for file_name in os.listdir(log_directory):
        if file_name.endswith(".log"):
            shutil.move(os.path.join(log_directory, file_name),
                        os.path.join(archive_directory, file_name))
            print(f"Archived: {file_name}")

if __name__ == "__main__":
    archive_logs("/var/log", "/var/log/archived_logs")