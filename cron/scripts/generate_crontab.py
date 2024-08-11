import os, json
from dataclasses import dataclass
from tasks.config import Config


@dataclass
class RawCronRecord:
    enabled_key: str
    schedule_key: str
    module: str


@dataclass
class CronRecord:
    enabled: bool
    schedule: str
    module: str


def load_source() -> list[RawCronRecord]:
    with open(os.path.join(Config.MODULE_PATH, "crontab_source.json"), "r") as file:
        data = json.loads(file.read())

    return [RawCronRecord(**record) for record in data]

def parse_source(raw_data: list[RawCronRecord]) -> list[CronRecord]:
    parsed_data = []

    for record in raw_data:
        enabled = bool(int(os.getenv(record.enabled_key)))
        schedule = os.getenv(record.schedule_key)
        module = record.module

        parsed_data.append(CronRecord(enabled, schedule, module))

    return parsed_data


def record_to_row(record: CronRecord) -> str:
    return f"{record.schedule} python3 {Config.TASKS_PATH}/{record.module}"


def save_crontab(records: list[CronRecord]):
    filename = os.path.join(Config.MODULE_PATH, "jobs.txt")
    entries = []

    for record in records:
        if record.enabled:
            entries.append(record_to_row(record))

    with open(filename, "w") as file:
        file.writelines(entries)
        file.write("\n")


def main():
    raw_rows = load_source()
    parsed_rows = parse_source(raw_rows)

    save_crontab(parsed_rows)

if __name__ == "__main__":
    main()
