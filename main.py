from pathlib import Path
import subprocess
import sys

def is_python_script(path: Path) -> bool:
    return path.is_file() and path.suffix == ".py" and not path.name.startswith(".")

def dir_has_python(path: Path, ignore_current: Path) -> bool:
    """Чи є у цій папці або підпапках (нех. прихованих) .py-файли крім запускаючого."""
    if path.name.startswith("."):
        return False
    for item in path.iterdir():
        if item.name.startswith("."):
            continue
        if item.is_file() and item.suffix == ".py" and item.resolve() != ignore_current.resolve():
            return True
        if item.is_dir() and dir_has_python(item, ignore_current):
            return True
    return False

def get_items(path: Path, ignore_current: Path):
    """Повертає (папки, скрипти), що є безпосередньо в цій папці. Ігнорує приховані."""
    folders, scripts = [], []
    for item in sorted(path.iterdir(), key=lambda p: p.name.lower()):
        if item.name.startswith("."):
            continue
        if item.is_dir() and dir_has_python(item, ignore_current):
            folders.append(item)
        elif is_python_script(item) and item.resolve() != ignore_current.resolve():
            scripts.append(item)
    return folders, scripts

def show_choices(folders, scripts, current_path, root_path):
    print(f"\nПоточна папка: {current_path.relative_to(root_path)}" if current_path != root_path else "\nПоточна папка: .")
    print("Доступні папки та скрипти:")
    idx = 1
    mapping = {}
    for f in folders:
        print(f"{idx}. [DIR] {f.name}")
        mapping[idx] = (f, "dir")
        idx += 1
    for s in scripts:
        print(f"{idx}. {s.name}")
        mapping[idx] = (s, "file")
        idx += 1
    print("0. Повернутися на рівень вище" if current_path != root_path else "0. Вийти")
    return mapping

def run_script(path: Path):
    print(f"Запускаю файл: {path}")
    print("-" * 40)
    try:
        subprocess.run([sys.executable, str(path)], cwd=path.parent, check=False)
    except Exception as error:
        print(f"Не вдалося запустити файл '{path.name}'.")
        print(f"Деталі помилки: {error}")

def main():
    root = Path(__file__).parent.resolve()
    cur = root
    ignore_current = Path(__file__).resolve()
    history = []

    while True:
        folders, scripts = get_items(cur, ignore_current)
        mapping = show_choices(folders, scripts, cur, root)

        choice = input("Введи номер (або 0, щоб вийти/назад): ").strip()
        if not choice.isdigit():
            print("Потрібно ввести саме номер зі списку. Спробуй ще раз.")
            continue

        number = int(choice)
        if number == 0:
            if cur == root:
                print("Вихід із програми.")
                break
            cur = history.pop()
            continue
        if number not in mapping:
            print("Неправильний номер. Спробуй ще раз.")
            continue

        target, typ = mapping[number]
        if typ == "dir":
            history.append(cur)
            cur = target.resolve()
        else:
            run_script(target)
            break

if __name__ == "__main__":
    main()