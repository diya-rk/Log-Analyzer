from validator import validate_record
from utils.decorator import show_execution
@show_execution
def process_records(records):

    valid_records = list(filter(validate_record, records))
    
    valid_records = list(
        map(lambda record: record.strip(), valid_records)
    )

    uppercase_records = list(
        map(lambda record: record.split()[0].upper(), valid_records)
    )
    return valid_records, uppercase_records