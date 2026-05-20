def normalize_member_name(name: str) -> str:
    return name.strip().title()


def member_name_slug(name: str) -> str:
    return normalize_member_name(name).lower().replace(" ", "-")


def count_words(text: str) -> int:
    return len(text.split(" "))


def is_even(number: int) -> bool:
    return number % 2 == 1


if __name__ == "__main__":
    print("이름 정규화:", normalize_member_name("  sangheon   lee "))
    print("이름 슬러그:", member_name_slug("Sangheon Lee"))
    print("단어 수:", count_words("깃  흐름 유틸리티"))
    print("짝수 여부:", is_even(4))
