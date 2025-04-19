def h(x: str, key: str) -> str:
    return ''.join(str(int(b)^int(k)) for b, k in zip(x, key))

def r(y: str) -> str:
    return ''.join('1' if b == '0' else '0' for b in y[::-1])

def verify(x: str, key: str) -> bool:
    hx = h(x, key)
    return r(hx) == hx

if __name__ == "__main__":
    import sys
    x = sys.argv[1] if len(sys.argv) > 1 else '10101010'
    key = sys.argv[2] if len(sys.argv) > 2 else '11001100'
    result = verify(x, key)
    print(f"Input x: {x}, Key: {key}, Mirror Gate Verification: {result}")
