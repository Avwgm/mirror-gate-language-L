def h(x: str, key: str) -> str:
    return ''.join(str(int(b)^int(k)) for b, k in zip(x, key))

def r(y: str) -> str:
    return ''.join('1' if b == '0' else '0' for b in y[::-1])

def generate(key: str, n: int = 8):
    from itertools import product
    for bits in product("01", repeat=n):
        x = ''.join(bits)
        hx = h(x, key)
        if r(hx) == hx:
            yield x

if __name__ == "__main__":
    key = '11001100'
    for x in generate(key):
        print(f"Valid x: {x}")
