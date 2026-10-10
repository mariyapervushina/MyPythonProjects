def chunked(items, n):
    chunks = []
    for i in range(0, len(items), n):
        chunks.append(items[i:i + n])
    return chunks


s = input().split()
n = int(input())
print(chunked(s, n))
