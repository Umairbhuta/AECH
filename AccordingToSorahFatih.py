def ayah_needs():
    needs = {
        "Spiritual Need": {
            "description": "Worship, gratitude, and seeking guidance for spiritual growth.",
            "ayat": ["Alhamdulillahi Rabbil Alameen", "Iyyaka Na'budu wa Iyyaka Nasta'een", "Ihdinas Siratal Mustaqeem"],
            "action": [
                "Be grateful for Allah's blessings.",
                "Develop sincerity in worship.",
                "Pray to Allah for guidance."
            ]
        },
        "Moral Need": {
            "description": "Guidance to follow the right path and avoid misguidance.",
            "ayat": ["Siratal Lazeena An'amta Alaihim", "Ghairil Maghdoobi Alaihim Walad Dalleen"],
            "action": [
                "Follow the path of righteous people.",
                "Avoid false beliefs and bad deeds.",
                "Obey to stay away from Allah's wrath."
            ]
        },
        "Establishment of Justice": {
            "description": "Mention of accountability, reward, and punishment on the Day of Judgment.",
            "ayat": ["Maliki Yawmid Deen"],
            "action": [
                "Do good deeds and avoid sins.",
                "Pray for success on the Day of Judgment.",
                "Keep the sense of accountability to Allah."
            ]
        }
    }

    return needs


def display_needs():
    needs = ayah_needs()
    for need_type, details in needs.items():
        print(f"\nNeed: {need_type}")
        print(f"Description: {details['description']}")
        print("Ayahs:")
        for ayah in details['ayat']:
            print(f"- {ayah}")
        print("Actions:")
        for action in details['action']:
            print(f"- {action}")


def check_need(need_type):
    needs = ayah_needs()
    if need_type in needs:
        details = needs[need_type]
        print(f"\nYou selected: {need_type}")
        print(f"Description: {details['description']}")
        print("Ayahs:")
        for ayah in details['ayat']:
            print(f"- {ayah}")
        print("Actions:")
        for action in details['action']:
            print(f"- {action}")
    else:
        print("\nThis need does not exist. Please check again.")


if __name__ == "__main__":
    print("Welcome to the program on the needs derived from Surah Al-Fatihah!")
    print("1. Display all needs.")
    print("2. Check a specific need.")
    try:
        choice = input("Enter your choice (1 or 2): ").strip()

        if choice == "1":
            display_needs()
        elif choice == "2":
            need_type = input("Enter the name of the need to check (Spiritual Need, Moral Need, Establishment of Justice): ").strip()
            check_need(need_type)
        else:
            print("\nInvalid choice. Please try again.")
    except KeyboardInterrupt:
        print("\nProgram interrupted. Goodbye!")
    except IOError as io_err:
        print(f"\nInput/Output error: {io_err}")
    except Exception as e:
        print(f"\nAn error occurred in the program: {e}")
