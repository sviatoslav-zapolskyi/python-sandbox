from pathlib import Path
import subprocess
import sys


def find_scripts(current_file: Path) -> list[Path]:
    directory = current_file.parent
    return sorted(
        [
            path
            for path in directory.glob("*.py")
            if path.is_file() and path.resolve() != current_file.resolve()
        ],
        key=lambda p: p.name.lower()
    )


def show_list(scripts: list[Path]) -> None:
    print("Доступні Python-файли:")
    for number, script in enumerate(scripts, start=1):
        print(f"{number}. {script.name}")


def main() -> None:
    current_file = Path(__file__).resolve()
    scripts = find_scripts(current_file)

    if not scripts:
        print("Ти ще не створив жодного скрипта.")
        return

    show_list(scripts)
    print()

    choice = input("Введи номер файлу, який потрібно запустити, і натисни Enter: ").strip()

    if not choice.isdigit():
        print("Потрібно ввести саме номер зі списку. Спробуй ще раз.")
        return

    number = int(choice)

    if number < 1 or number > len(scripts):
        print("Файлу з таким номером немає. Перевір номер і спробуй ще раз.")
        return

    selected_script = scripts[number - 1]
    print(f"Запускаю файл: {selected_script.name}")
    print("-" * 40)

    try:
        subprocess.run(
            [sys.executable, str(selected_script)],
            cwd=current_file.parent,
            check=False
        )
    except Exception as error:
        print(f"Не вдалося запустити файл '{selected_script.name}'.")
        print(f"Деталі помилки: {error}")


if __name__ == "__main__":
    main()
