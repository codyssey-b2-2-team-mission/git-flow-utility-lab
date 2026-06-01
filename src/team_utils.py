def normalize_member_name(name: str) -> str:
    return " ".join(part.capitalize() for part in name.strip().split())


def member_name_slug(name: str) -> str:
    return normalize_member_name(name).lower().replace(" ", "-")


def member_initials(name: str) -> str:
    return "".join(part[0] for part in normalize_member_name(name).split())


def count_words(text: str) -> int:
    return len(text.split())


def is_even(number: int) -> bool:
    return number % 2 == 0


if __name__ == "__main__":
    print("normalize_member_name:", normalize_member_name("  sangheon   lee "))
    print("member_name_slug:", member_name_slug("  sangheon   lee "))
    print("member_initials:", member_initials("  sangheon   lee "))
    print("count_words:", count_words("Git  flow utility"))
    print("is_even:", is_even(4))
