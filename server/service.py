def gs_calculator(first_elem: int, coefficient: int, n: int) -> list[int]:
    gs_list = [first_elem]

    current_elem = first_elem
    for _ in range(n - 1):
        current_elem = current_elem * coefficient
        
        gs_list.append(current_elem)

    return gs_list
