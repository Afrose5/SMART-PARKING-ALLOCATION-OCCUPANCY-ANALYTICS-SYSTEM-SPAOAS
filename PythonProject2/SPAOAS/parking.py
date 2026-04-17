import datetime
class Slot:
    def __init__(self, slot_id, slot_type, status):
        self.slot_id = slot_id
        self.slot_type = slot_type
        self.status = status
        self.last_updated = datetime.datetime.now()
    def update_status(self, new_status):
        self.status = new_status
        self.last_updated = datetime.datetime.now()
    def to_list(self):
        return [self.slot_id, self.slot_type, self.status, self.last_updated]
class ParkingLot:
    def __init__(self):
        self.slots = []
    def add_slot(self, slot):
        self.slots.append(slot)
    def find_free_slot(self, vehicle_type):
        for s in self.slots:
            if s.slot_type.lower() == vehicle_type.lower() and s.status == "Free":
                return s
        return None
    def get_slot_by_id(self, sid):
        for s in self.slots:
            if s.slot_id == sid:
                return s
        return None
    def view_slots(self):
        if not self.slots:
            print("No slots available")
            return
        print("\nSlotID | Type | Status | Last Updated")
        print("-------------------------------------")
        for s in self.slots:
            print(s.slot_id, "|", s.slot_type, "|", s.status, "|", s.last_updated)