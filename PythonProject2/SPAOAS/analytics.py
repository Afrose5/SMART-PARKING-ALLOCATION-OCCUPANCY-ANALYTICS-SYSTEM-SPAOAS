import numpy as np
def occupancy_analytics(slots):
    if len(slots) == 0:
        print("No slots available")
        return
    status_list = [1 if s.status == "Occupied" else 0 for s in slots]
    arr = np.array(status_list)
    total = len(arr)
    occupied = np.sum(arr)
    free = total - occupied
    percent = (occupied / total) * 100
    print("\n--- Occupancy Analytics ---")
    print("Total Slots :", total)
    print("Occupied    :", occupied)
    print("Free        :", free)
    print("Occupancy % :", round(percent, 2))