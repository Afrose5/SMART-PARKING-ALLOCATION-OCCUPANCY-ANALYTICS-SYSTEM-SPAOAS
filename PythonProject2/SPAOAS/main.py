from parking import Slot, ParkingLot
from storage import save_slots, load_slots, log_action
from analytics import occupancy_analytics
from charts import show_chart
def main():
    lot = ParkingLot()
    lot.slots = load_slots()
    while True:
        print("\n===== SMART PARKING SYSTEM =====")
        print("1. Add Slot")
        print("2. View Slots")
        print("3. Allocate Slot")
        print("4. Free Slot")
        print("5. Analytics")
        print("6. Show Chart")
        print("7. Exit")
        try:
            choice = int(input("Enter choice: "))
        except:
            print("Invalid input")
            continue
        # ADD SLOT
        if choice == 1:
            try:
                sid = int(input("Enter Slot ID: "))
                stype = input("Enter Slot Type: ")
                status = input("Enter Status (Free/Occupied): ")
                slot = Slot(sid, stype, status)
                lot.add_slot(slot)
                save_slots(lot.slots)
                log_action(sid, "Added")
                print("Slot added successfully")
            except:
                print("Error")
        # VIEW
        elif choice == 2:
            lot.view_slots()
        # ALLOCATE
        elif choice == 3:
            vtype = input("Enter Vehicle Type: ")
            slot = lot.find_free_slot(vtype)
            if slot:
                slot.update_status("Occupied")
                save_slots(lot.slots)
                log_action(slot.slot_id, "Allocated")
                print("Allocated Slot:", slot.slot_id)
            else:
                print("No free slot available")
        # FREE SLOT
        elif choice == 4:
            try:
                sid = int(input("Enter Slot ID: "))
                slot = lot.get_slot_by_id(sid)
                if slot:
                    slot.update_status("Free")
                    save_slots(lot.slots)
                    log_action(sid, "Freed")
                    print("Slot freed")
                else:
                    print("Slot not found")
            except:
                print("Invalid input")
        # ANALYTICS
        elif choice == 5:
            occupancy_analytics(lot.slots)
        # CHART
        elif choice == 6:
            show_chart(lot.slots)
        # EXIT
        elif choice == 7:
            print("Exiting system")
            break
        else:
            print("Invalid choice")
if __name__ == "__main__":
    main()