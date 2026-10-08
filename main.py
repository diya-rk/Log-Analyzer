from file_handler import (
    read_log_file,
    write_invalid_records,
    save_pickle,
    load_pickle
)
from processor import process_records
from validator import validate_record
print("\n\nSECURE LOG ANALYZER & BACKUP SYSTEM")
# read the records from log.txt
records = read_log_file("log.txt")
if records:
    records = [record.strip() for record in records if record.strip()]

    invalid_records = list(
        filter(lambda record: not validate_record(record), records)
    )

    valid_records, uppercase_names = process_records(records)

    print("\nValid Login Records:")

    for record in valid_records:
        print(record)

    print("\nUsernames in Uppercase:")

    for name in uppercase_names:
        print(name)
#saving invalid records to a file
    write_invalid_records(
        "invalid_log.txt",
        invalid_records
    )


#valid records are saved to a pickle file
    save_pickle(
        "valid_records.pkl",
        valid_records
    )


#load data from pickle
    print("\nData Loaded From Pickle:")


    stored_records = load_pickle("valid_records.pkl")

    for record in stored_records:
        print(record)
else:
    print("No records found.")

print("\n\nPROGRAM IS COMPLETED")
