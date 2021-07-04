# Below will print the tables from 1 to 20
# And store them as TXT file
for i in range(1, 21):
    with open(
        f"d:\\visual studio\\python practice\\advanced\\tables\\table_of_{i}.txt", "w"
    ) as f:
        heading = "Table of " + str(i) + "\n"
        f.write(heading)

        for j in range(1, 11):
            table = f"\n{i} X {j} = {i*j}"
            f.write(table)
