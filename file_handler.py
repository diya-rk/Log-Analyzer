import pickle


def read_log_file(filename):
    try:
        with open(filename, "r") as file:
            return file.readlines()

    except FileNotFoundError:
        print("Error: log.txt file was not found.")
        return []

    except Exception as e:
        print("Error while reading file:", e)
        return []


def write_invalid_records(filename, records):
    try:
        with open(filename, "w") as file:
            for record in records:
                file.write(record + "\n")

        print("Invalid records saved to", filename)

    except Exception as e:
        print("Error while writing invalid records:", e)


def save_pickle(filename, data):
    try:
        with open(filename, "wb") as file:
            pickle.dump(data, file)

        print("Valid records saved successfully.")

    except Exception as e:
        print("Error while saving pickle file:", e)


def load_pickle(filename):
    try:
        with open(filename, "rb") as file:
            return pickle.load(file)

    except FileNotFoundError:
        print("Pickle file was not found.")
        return []

    except Exception as e:
        print("Error while loading pickle file:", e)
        return []