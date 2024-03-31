def PTArithGeo(arr):
    is_arith = all(arr[i] - arr[i-1] == arr[1] - arr[0] for i in range(2, len(arr)))
    is_geo = all(arr[i] / arr[i-1] == arr[1] / arr[0] for i in range(2, len(arr)))
    if is_arith:
        return "Arithmetic"
    elif is_geo:
        return "Geometric"
    else:
        return -1

# Mantenha esta chamada de função aqui
print(PTArithGeo(input()))
