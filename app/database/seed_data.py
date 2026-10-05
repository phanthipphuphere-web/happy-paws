from app.database.connection import get_connection


def seed_data():
    # 1. Connect to MariaDB
    connection = get_connection()
    cursor = connection.cursor()

    # --------------------------------------------------
    # 2. Insert pets
    # --------------------------------------------------
    pets = [
        ("Milo", "Dog", "Golden Retriever", 3, "Somchai"),
        ("Luna", "Cat", "British Shorthair", 2, "Nok"),
        ("Coco", "Dog", "Poodle", 4, "Mali"),
    ]

    cursor.executemany(
        """
        INSERT INTO pets (
            name,
            type,
            breed,
            age,
            owner_name
        )
        VALUES (?, ?, ?, ?, ?)
        """,
        pets,
    )

    # --------------------------------------------------
    # 3. Insert rooms
    # --------------------------------------------------
    rooms = [
        ("101", "Standard", 500.00, "available"),
        ("102", "Deluxe", 800.00, "occupied"),
        ("103", "Deluxe", 800.00, "available"),
    ]

    cursor.executemany(
        """
        INSERT INTO rooms (
            room_number,
            room_type,
            daily_rate,
            status
        )
        VALUES (?, ?, ?, ?)
        """,
        rooms,
    )

    # --------------------------------------------------
    # 4. Get IDs we need for bookings
    # --------------------------------------------------
    cursor.execute(
        "SELECT id FROM pets WHERE name = ?",
        ("Milo",),
    )
    milo_id = cursor.fetchone()[0]

    cursor.execute(
        "SELECT id FROM pets WHERE name = ?",
        ("Luna",),
    )
    luna_id = cursor.fetchone()[0]

    cursor.execute(
        "SELECT id FROM rooms WHERE room_number = ?",
        ("102",),
    )
    room_102_id = cursor.fetchone()[0]

    cursor.execute(
        "SELECT id FROM rooms WHERE room_number = ?",
        ("101",),
    )
    room_101_id = cursor.fetchone()[0]

    # --------------------------------------------------
    # 5. Insert bookings
    # --------------------------------------------------
    bookings = [
        (
            milo_id,
            room_102_id,
            "2026-09-27",
            "2026-09-30",
            "confirmed",
        ),
        (
            luna_id,
            room_101_id,
            "2026-10-01",
            "2026-10-03",
            "confirmed",
        ),
    ]

    cursor.executemany(
        """
        INSERT INTO bookings (
            pet_id,
            room_id,
            check_in,
            check_out,
            status
        )
        VALUES (?, ?, ?, ?, ?)
        """,
        bookings,
    )

    # 6. Save everything
    connection.commit()

    # 7. Close resources
    cursor.close()
    connection.close()

    print("Sample data inserted successfully!")


if __name__ == "__main__":
    seed_data()