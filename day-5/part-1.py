with open("input.txt") as file:
    saw_blank_line = False
    fresh_id_ranges = []
    available_ids = []
    fresh_ids = []

    for line in file:
        input = line.strip("\n")

        if not saw_blank_line and input != "":
            fresh_id_ranges.append(list(map(int, input.split("-"))))
        elif input == "":
            saw_blank_line = True
        else:
            available_ids.append(int(input))

    for id in available_ids:
        for id_range in fresh_id_ranges:
            if id_range[0] <= id <= id_range[1]:
                fresh_ids.append(id)
                break

    print(len(fresh_ids))
