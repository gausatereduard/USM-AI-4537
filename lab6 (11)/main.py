import argparse


def recognize(text: str) -> bool:
    """Проверить, состоит ли строка из одной или нескольких пар `aa`."""
    length = len(text)
    if length == 0 or length % 2 != 0:
        return False
    return all(text.startswith("aa", index) for index in range(0, length, 2))


def main():
    parser = argparse.ArgumentParser(description="Распознавание цепочек вида a^(2j), j ≥ 1")
    parser.add_argument("text", help="строка для проверки")
    args = parser.parse_args()
    print("Принята" if recognize(args.text) else "Отклонена")


if __name__ == "__main__":
    main()
