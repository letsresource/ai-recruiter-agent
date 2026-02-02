def load_job_description(path):
    with open(path, "r", encoding="utf-8") as file:
        return file.read()
