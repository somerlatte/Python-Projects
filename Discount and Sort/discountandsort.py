def VTEXDiscountandSort(arr):
    total = sum(arr)

    if total > 1000:
        for i in range(len(arr)):
            if arr[i] > 10:
                arr[i] -= 30
                total -= 30
                if arr[i] < 10:
                    arr[i] = 10
                    total += 20

    elif total <= 1000:
        for i in range(len(arr)):
            if arr[i] > 100:
                arr[i] -= 10
                total -= 10
                if arr[i] < 10:
                    arr[i] = 10
                    total += 10
    arr.sort()

    output = " + ".join(["${}".format(price) for price in arr]) + " = ${}".format(total)

    return output

# Mantenha esta chamada de função aqui
print(VTEXDiscountandSort(input()))
