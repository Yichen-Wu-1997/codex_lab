class ReadingList:
    def __init__(self) -> None:
        self._books: list[dict[str, object]] = []

    def add_book(self, title: str, author: str) -> None:
        self._books.append({"title": title, "author": author, "read": False})

    def mark_read(self, title: str) -> None:
        for book in self._books:
            if book["title"] == title:
                book["read"] = True
                return
        raise ValueError(f"unknown title: {title}")

    def unread_titles(self) -> list[str]:
        return [str(book["title"]) for book in self._books if not book["read"]]

    # Change: added title search for the feature tests task.
    def search_titles(self, keyword: str) -> list[str]:
        keyword_lower = keyword.lower()
        return [
            str(book["title"])
            for book in self._books
            if keyword_lower in str(book["title"]).lower()
        ]

    def total_books(self) -> int:
        return len(self._books)
