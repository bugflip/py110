def find_dup(lst):
    holder = set()
    for item in lst:
        if item in holder:
            return item
        holder.add(item)