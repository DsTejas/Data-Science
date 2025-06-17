#rent vehicle pricing model
def calculate_fare(distance_km, time_min, surge_multiplier=1.0):

    BASE_FARE = 50
    RATE_PER_KM = 10
    RATE_PER_MIN = 2
    BOOKING_FEE = 10

    total = (BASE_FARE + (distance_km * RATE_PER_KM) + (time_min * RATE_PER_MIN) + BOOKING_FEE) * surge_multiplier
    return round(total, 2)


def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ Invalid input! Please enter a valid number.")


def main():
    print("\n🛺 Rent Fare Calculator\n")

    distance = get_float_input("📏 Enter distance (in km): ")
    time = get_float_input("⏱  Enter time (in minutes): ")
    surge_multiplier = 1.0

    surge_input = input("⚡ Is surge pricing active? (yes/no): ").strip().lower()
    if surge_input == "yes":
        surge_multiplier = get_float_input("🔁 Enter surge multiplier (e.g. 1.5): ")

    fare = calculate_fare(distance, time, surge_multiplier)
    print(f"\n✅ Estimated Fare: ₹{fare:.2f}")


if __name__ == "__main__":
    main()
