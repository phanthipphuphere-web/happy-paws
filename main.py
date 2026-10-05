from app.repositories.pet_repository import delete_pet


def main():
    print("   Happy Paws Pet Hotel")
    print("------------------------")

    rows_deleted = delete_pet(4)

    print(f"Rows deleted: {rows_deleted}")


if __name__ == "__main__":
    main()