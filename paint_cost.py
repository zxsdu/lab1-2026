# Лабораторна робота, Варіант 5
# Програма для розрахунку вартості фарбування стін кімнати

# Витрата фарби: 1 літр на 10 м² за один шар (середнє значення)
CONSUMPTION_PER_M2 = 0.1


def read_positive_number(prompt, allow_zero=False):
    """Зчитує додатне число з клавіатури з перевіркою коректності."""
    while True:
        text = input(prompt).replace(",", ".").strip()
        try:
            value = float(text)
        except ValueError:
            print("Помилка: введіть число (наприклад, 3.5).")
            continue
        if value < 0 or (value == 0 and not allow_zero):
            print("Помилка: значення має бути більшим за нуль.")
            continue
        return value


def read_coats(prompt):
    """Зчитує кількість шарів фарби (ціле число >= 1)."""
    while True:
        text = input(prompt).strip()
        if text.isdigit() and int(text) >= 1:
            return int(text)
        print("Помилка: введіть ціле число, не менше 1.")


def main():
    print("=== Розрахунок вартості фарбування стін ===")

    # Введення даних користувачем
    length = read_positive_number("Довжина кімнати (м): ")
    width = read_positive_number("Ширина кімнати (м): ")
    height = read_positive_number("Висота кімнати (м): ")
    openings = read_positive_number(
        "Площа вікон і дверей, які не фарбуються (м², 0 якщо немає): ",
        allow_zero=True,
    )
    price_per_liter = read_positive_number("Вартість фарби за літр (грн): ")
    coats = read_coats("Кількість шарів фарби: ")

    # Площа чотирьох стін: периметр * висота
    walls_area = 2 * (length + width) * height

    # Перевірка: вікна й двері не можуть бути більшими за стіни
    if openings >= walls_area:
        print("Помилка: площа вікон і дверей більша або дорівнює площі стін.")
        return

    paint_area = walls_area - openings           # площа для фарбування
    liters = paint_area * CONSUMPTION_PER_M2 * coats  # потрібна кількість фарби
    total_cost = liters * price_per_liter        # загальна вартість

    # Виведення результату у форматованому вигляді
    print("\n--- Результат ---")
    print(f"Площа стін:               {walls_area:.2f} м²")
    print(f"Площа для фарбування:     {paint_area:.2f} м²")
    print(f"Потрібно фарби:           {liters:.2f} л")
    print(f"Вартість фарбування:      {total_cost:.2f} грн")


if __name__ == "__main__":
    main()
