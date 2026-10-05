from app.database.connection import get_connection


def show_data():
    # 1. Connect to MariaDB
    connection = get_connection()
    cursor = connection.cursor()

    # --------------------------------------------------
    # 2. Show pets
    # --------------------------------------------------
    print("\n=== PETS ===")

    cursor.execute("""
        SELECT
            id,
            name,
            type,
            breed,
            age,
            owner_name
        FROM pets
        ORDER BY id
    """)

    pets = cursor.fetchall()

    for pet in pets:
        print(pet)

    # --------------------------------------------------
    # 3. Show rooms
    # --------------------------------------------------
    print("\n=== ROOMS ===")

    cursor.execute("""
        SELECT
            id,
            room_number,
            room_type,
            daily_rate,
            status
        FROM rooms
        ORDER BY id
    """)

    rooms = cursor.fetchall()

    for room in rooms:
        print(room)

    # --------------------------------------------------
    # 4. Show bookings with pet and room information
    # --------------------------------------------------
    print("\n=== BOOKINGS ===")

    cursor.execute("""
        SELECT
            bookings.id,
            pets.name,
            rooms.room_number,
            bookings.check_in,
            bookings.check_out,
            bookings.status
        FROM bookings
        JOIN pets
            ON bookings.pet_id = pets.id
        JOIN rooms
            ON bookings.room_id = rooms.id
        ORDER BY bookings.id
    """)

    bookings = cursor.fetchall()

    for booking in bookings:
        print(booking)

    # 5. Close resources
    cursor.close()
    connection.close()


if __name__ == "__main__":
    show_data()