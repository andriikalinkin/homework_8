from .models import Log


def write_to_file(dictionary):
    try:
        with open("log_middleware/log.txt", "a") as file:
            for key, value in dictionary.items():
                file.write(f"{key}: {value}\n")
            file.write("\n")
        print(f"Dictionary has been written to \"project/school/log_middleware/log.txt\"")
    except Exception as e:
        print(f"An error occurred: {e}")


def write_to_db(dictionary):
    log = Log.objects.create(
        request_path=dictionary["request_path"],
        request_method=dictionary["request_method"],
        execution_time=dictionary["execution_time"],
        date_and_time=dictionary["date_and_time"]
    )

    log.save()
    print(f"Dictionary has been written to student_log sheet in DB")
