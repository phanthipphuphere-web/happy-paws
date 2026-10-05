from app.database.connection import get_connection


def get_all_pets():
    connection = get_connection()
    cursor = connection.cursor()

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

    cursor.close()
    connection.close()

    return pets


def get_pet_by_id(pet_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT
            id,
            name,
            type,
            breed,
            age,
            owner_name
        FROM pets
        WHERE id = ?
        """,
        (pet_id,),
    )

    pet = cursor.fetchone()

    cursor.close()
    connection.close()

    return pet


def add_pet(name, pet_type, breed, age, owner_name):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
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
        (name, pet_type, breed, age, owner_name),
    )

    connection.commit()
    new_pet_id = cursor.lastrowid

    cursor.close()
    connection.close()

    return new_pet_id


def update_pet(
    pet_id,
    name,
    pet_type,
    breed,
    age,
    owner_name,
):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        UPDATE pets
        SET
            name = ?,
            type = ?,
            breed = ?,
            age = ?,
            owner_name = ?
        WHERE id = ?
        """,
        (
            name,
            pet_type,
            breed,
            age,
            owner_name,
            pet_id,
        ),
    )

    connection.commit()
    rows_updated = cursor.rowcount

    cursor.close()
    connection.close()

    return rows_updated


def delete_pet(pet_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        DELETE FROM pets
        WHERE id = ?
        """,
        (pet_id,),
    )

    connection.commit()
    rows_deleted = cursor.rowcount

    cursor.close()
    connection.close()

    return rows_deleted