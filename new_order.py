import sys
import numpy as np

def is_integer_header(tokens):
    try:
        ints = [int(t) for t in tokens]
        return ints[0] == 0
    except ValueError:
        return False


def read_ezfcf_matrix(filename):
    with open(filename, "r") as f:
        lines = f.readlines()

    marker = "=== Reading the parallel approximation job parameters ==="
    start = None
    for i, line in enumerate(lines):
        if marker in line:
            start = i
            break
    if start is None:
        raise RuntimeError("Marker line not found")

    # Find the column header line dynamically
    header_idx = None
    for i in range(start, len(lines)):
        tokens = lines[i].split()
        if tokens and is_integer_header(tokens):
            header_idx = i
            break

    if header_idx is None:
        raise RuntimeError("Column index header not found")

    # Read header → determine N
    header = lines[header_idx].split()
    cols = [int(x) for x in header]
    N = max(cols) + 1

    # Read matrix
    M = np.zeros((N, N), dtype=float)

    for r in range(N):
        line = lines[header_idx + 1 + r].split()
        row_idx = int(line[0])
        values = line[1:]

        for c, v in enumerate(values):
            if v == "--":
                M[row_idx, c] = 0.0
            else:
                M[row_idx, c] = float(v)

    return M


def get_new_order(M):
    return np.argmax(np.abs(M), axis=0)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python new_order.py <ezfcf_output.txt>")
        sys.exit(1)

    filename = sys.argv[1]

    M = read_ezfcf_matrix(filename)
    new_order = get_new_order(M)

    print("New mode order:")
    print(" ".join(str(i) for i in new_order))
