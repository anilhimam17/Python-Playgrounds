inp = float(input("Enter the cash to be owed: "))
deno_count = 0

while inp >= 0.25:
    inp -= 0.25
    deno_count += 1
    inp = round(inp, 2)
    print(inp)

while inp >= 0.10:
    inp -= 0.10
    deno_count += 1
    inp = round(inp, 2)
    print(inp)

while inp >= 0.05:
    inp -= 0.05
    deno_count += 1
    inp = round(inp, 2)
    print(inp)

while inp >= 0.01:
    inp -= 0.01
    deno_count += 1
    inp = round(inp, 2)
    print(inp)

print("The minimum no of deno = {}".format(deno_count))
    
