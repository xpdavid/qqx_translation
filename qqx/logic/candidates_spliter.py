def deduplicate_candidates(original_list):
    sorted_list = list(sorted(original_list, key=lambda t: t['pos']))
    filtered = []
    idx = 0
    while idx < len(sorted_list):
        curr_ele = sorted_list[idx]
        till_idx = idx + 1
        while till_idx < len(sorted_list):
            next_ele = sorted_list[till_idx]
            abs_w = abs(curr_ele['pos'][0] - next_ele['pos'][0])
            abs_h = abs(curr_ele['pos'][1] - next_ele['pos'][1])
            if abs_w > 3 or abs_h > 3:
                break
            till_idx += 1
        winner = None
        for k in range(idx, till_idx):
            if winner is None:
                winner = sorted_list[idx]
                continue
            if winner['score'] < sorted_list[k]['score']:
                winner = sorted_list[k]
        filtered.append(winner)
        idx = till_idx
    return filtered


def split(lst):
    if len(lst) == 1:
        return lst, []

    sorted_list = list(sorted(lst, key=lambda t: t['pos'][1]))
    idx = 0
    while idx + 1 < len(sorted_list):
        curr_ele = sorted_list[idx]
        next_ele = sorted_list[idx + 1]
        if abs(curr_ele['pos'][1] - next_ele['pos'][1]) <= 70:
            idx += 1
        else:
            break

    top_lst = sorted_list[:idx + 1]
    bottom_lst = sorted_list[idx + 1:]
    top_lst = deduplicate_candidates(sorted(top_lst, key=lambda t: t['pos']))
    bottom_lst = deduplicate_candidates(sorted(bottom_lst, key=lambda t: t['pos']))
    return top_lst, bottom_lst
