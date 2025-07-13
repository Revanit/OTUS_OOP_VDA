import csv
import json


def load_books(path):
    books = []
    with open(path, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            books.append(
                {
                    "title": row.get("Title", ""),
                    "author": row.get("Author", ""),
                    "genre": row.get("Genre", ""),
                    "pages": int(row.get("Pages", 0)),
                }
            )
    return books


def load_users(path):
    with open(path, encoding="utf-8") as f:
        raw_users = json.load(f)
        return [
            {
                "name": u["name"],
                "gender": u["gender"],
                "address": u["address"],
                "age": u["age"],
            }
            for u in raw_users
        ]


def assign_books(books, users):
    total_books = len(books)
    total_users = len(users)
    books_per_user = total_books // total_users
    extra_books = total_books % total_users

    index = 0
    for i, user in enumerate(users):
        count = books_per_user + (1 if i < extra_books else 0)
        user["books"] = books[index: index + count]
        index += count
    return users


def main():
    books = load_books("books.csv")
    users = load_users("users.json")
    result = assign_books(books, users)

    with open("result.json", "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    main()
