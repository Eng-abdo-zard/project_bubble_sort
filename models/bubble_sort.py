import streamlit as st


def bubble_sort_ascending(array):
    for i in range(len(array)):
        is_sorted = True
        st.write(", ".join(map(str, array)))

        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                is_sorted = False
                



        if is_sorted:
            break


def bubble_sort_descending(array):
    for i in range(len(array)):
        is_sorted = True
        st.write(", ".join(map(str, array)))

        for j in range(0, len(array) - i - 1):
            if array[j] < array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                is_sorted = False

        if is_sorted:
            break


def main() -> None:
    data = [-2, 45, 0, 11, -9]

    bubble_sort_ascending(data)
    print(data)

    data = [-2, 45, 0, 11, -9]

    bubble_sort_descending(data)
    print(data)


if __name__ == "__main__":
    main()