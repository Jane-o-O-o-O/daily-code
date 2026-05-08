"""List ops for 2026-05-08"""

def second_largest(lst):
    unique = sorted(set(lst), reverse=True)
    return unique[1] if len(unique) > 1 else None

def remove_dupes(lst):
    seen = set()
    result = []
    for x in lst:
        if x not in seen:
            seen.add(x)
            result.append(x)
    return result

if __name__ == "__main__":
    data = [3,1,4,1,5,9,2,6,5]
    print(f"second largest: {second_largest(data)}")
    print(f"no dupes: {remove_dupes(data)}")
