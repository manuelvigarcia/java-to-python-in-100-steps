def find_combination_all_ops(numbers, target):
    # Lista para almacenar las combinaciones válidas
    valid_combinations = []

    # Función recursiva para explorar combinaciones
    def explore_combinations(current_combination, remaining_numbers, current_result):
        if current_result == target:
            # Se encontró una combinación válida, se agrega a la lista
            valid_combinations.append(current_combination)
            return

        # Si no quedan números, no se puede continuar
        if not remaining_numbers:
            return

        for i, num in enumerate(remaining_numbers):
            # No se puede usar el mismo número en la misma rama, por lo que se genera una nueva lista
            new_remaining_numbers = remaining_numbers[:i] + remaining_numbers[i + 1:]

            # --- Operaciones a partir del resultado actual ---

            # Suma
            explore_combinations(current_combination + [(num, '+')], new_remaining_numbers, current_result + num)

            # Resta
            explore_combinations(current_combination + [(num, '-')], new_remaining_numbers, current_result - num)

            # Multiplicación
            explore_combinations(current_combination + [(num, '*')], new_remaining_numbers, current_result * num)

            # División (con chequeo)
            # 1. El número no puede ser 0
            # 2. El resultado debe ser un número entero (sin decimales)
            if num != 0 and current_result % num == 0:
                explore_combinations(current_combination + [(num, '/')], new_remaining_numbers, current_result // num)

    # Se inician las exploraciones, una por cada número como punto de partida
    # Cada número inicial será el "current_result" para su rama
    for i, start_num in enumerate(numbers):
        explore_combinations([(start_num, '')], numbers[:i] + numbers[i + 1:], start_num)

    return valid_combinations


# numbers = [25, 5, 2, 8, 3]
# target = 100

#numbers = [12, 34, 56, 78, 90, 23]
#target = 293
#   --> todos los números sumados

numbers = [5, 2, 7, 10, 2, 3]
target = 42
#   --> 5*2*7/10*2*3

combinations = find_combination_all_ops(numbers, target)

if combinations:
    print(f"Se encontraron {len(combinations)} combinaciones:")
    for comb in combinations:
        # Formateamos la combinación para que sea legible
        expression = str(comb[0][0])
        for num, op in comb[1:]:
            expression += f" {op} {num}"
        print(f"  - {expression} = {target}")
else:
    print(f"No se encontró ninguna combinación para el objetivo {target}.")
