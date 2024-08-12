import os, json
from dataclasses import dataclass
from tasks.common.config import Config


@dataclass
class CronRecordDto:
    module: str
    enabled: bool | None = None
    schedule: str | None = None
    enabled_key: str | None = None
    schedule_key: str | None = None


@dataclass
class CronRecord:
    enabled: bool
    schedule: str
    module: str


def load_source() -> list[CronRecordDto]:
    with open(os.path.join(Config.MODULE_PATH, "crontab_source.json"), "r") as file:
        data = json.loads(file.read())

    return [CronRecordDto(**record) for record in data]

def parse_source(raw_data: list[CronRecordDto]) -> list[CronRecord]:
    parsed_data = []

    for record in raw_data:
        enabled = bool(int(os.getenv(record.enabled_key))) if record.enabled_key is not None else record.enabled
        schedule = os.getenv(record.schedule_key) if record.schedule_key is not None else record.schedule

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
        for entry in entries:
            file.write(f"{entry}\n")

        file.write("\n")


def main():
    raw_rows = load_source()
    parsed_rows = parse_source(raw_rows)

    save_crontab(parsed_rows)

if __name__ == "__main__":
    main()
