from astronauts import fetch_astronauts
from iss_tracker import fetch_iss_location
from news_or_stock import fetch_news, fetch_stock

def menu():
    while True:
        print("\n--- Live Data Reporter ---")
        print("1. Who's in space?")
        print("2. Where is the ISS?")
        print("3. What's happening on Earth? (News or Stock)")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            astronauts = fetch_astronauts()
            for a in astronauts:
                print(f"{a['name']} aboard {a['craft']}")
        elif choice == "2":
            loc = fetch_iss_location()
            print(f"ISS is at Latitude: {loc.get('latitude')}, Longitude: {loc.get('longitude')}")
        elif choice == "3":
            print("\n1. News\n2. IBM Stock Price")
            sub = input("Choose: ")
            if sub == "1":
                for title in fetch_news():
                    print(f"- {title}")
            elif sub == "2":
                print(fetch_stock())
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    menu()
