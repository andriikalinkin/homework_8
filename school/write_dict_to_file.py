from datetime import datetime


def write(dictionary):
    try:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("log_middleware/log.txt", "a") as file:
            file.write(f"{current_time}\n")
            for key, value in dictionary.items():
                file.write(f"{key}: {value}\n")
            file.write("\n")
        print(f"Dictionary has been written to \"project/school/log_middleware/log.txt\"")
    except Exception as e:
        print(f"An error occurred: {e}")
