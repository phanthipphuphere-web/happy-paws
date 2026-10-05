from app.repositories.pet_repository import (
    get_all_pets,
    get_pet_by_id,
    add_pet,
    update_pet,
    delete_pet,
)

print("=== CREATE ===")

pet_id = add_pet(
    name="Mochi",
    pet_type="Dog",
    breed="Shiba Inu",
    age=3,
    owner_name="Alongkot",
)

print("Created pet ID:", pet_id)

print("\n=== READ ONE ===")

pet = get_pet_by_id(pet_id)

print(pet)

print("\n=== UPDATE ===")

rows_updated = update_pet(
    pet_id,
    name="Mochi",
    pet_type="Dog",
    breed="Shiba Inu",
    age=4,
    owner_name="Alongkot",
)

print("Rows updated:", rows_updated)

print("\n=== READ AFTER UPDATE ===")

pet = get_pet_by_id(pet_id)

print(pet)

print("\n=== READ ALL ===")

pets = get_all_pets()

for pet in pets:
    print(pet)

print("\n=== DELETE ===")

rows_deleted = delete_pet(pet_id)

print("Rows deleted:", rows_deleted)

print("\n=== VERIFY DELETE ===")

pet = get_pet_by_id(pet_id)

print("Pet after delete:", pet)