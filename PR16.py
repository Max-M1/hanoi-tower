def tower_of_hanoi(disks, start_pole, end_pole, temp_pole):
    if disks == 1:
        print(f"Move disk 1 from {start_pole} to {end_pole}")
        return
    tower_of_hanoi(disks - 1, start_pole, temp_pole, end_pole)
    print(f"Move disk {disks} from {start_pole} to {end_pole}")
    tower_of_hanoi(disks - 1, temp_pole, end_pole, start_pole)


if __name__ == "__main__":
    total_disks = int(input("Enter the number of disks: "))
    print("Solving Tower of Hanoi...")
    tower_of_hanoi(total_disks, "A", "C", "B")
