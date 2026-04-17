import matplotlib.pyplot as plt
def show_chart(slots):
    if len(slots) == 0:
        print("No data to display")
        return
    free = sum(1 for s in slots if s.status == "Free")
    occupied = sum(1 for s in slots if s.status == "Occupied")
    plt.bar(["Free", "Occupied"], [free, occupied])
    plt.title("Parking Slot Occupancy")
    plt.xlabel("Status")
    plt.ylabel("Count")
    plt.show()