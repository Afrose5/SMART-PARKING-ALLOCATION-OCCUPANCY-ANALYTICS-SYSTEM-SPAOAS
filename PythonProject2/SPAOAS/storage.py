import csv
import datetime
from parking import Slot

SLOTS_FILE = "data/slots.csv"
LOG_FILE = "data/logs.csv"


def save_slots(slots):
    with open(SLOTS_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["SlotID", "Type", "Status", "LastUpdated"])
        for s in slots:
            writer.writerow(s.to_list())


def load_slots():
    slots = []
    try:
        with open(SLOTS_FILE, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                slot = Slot(int(row["SlotID"]), row["Type"], row["Status"])
                slots.append(slot)
    except FileNotFoundError:
        pass
    return slots
def log_action(slot_id, action):
    with open(LOG_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([slot_id, action, datetime.datetime.now()])