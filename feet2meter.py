def main():
    v = feet2meter(input("Сколько футов:"))
    print(f"Это будет {v:.2f} метров.")

def feet2meter(v: str):
    m = float(v[:len(v)-2])
    m /= 3.281
    return m

main()