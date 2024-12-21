from utils import File


def elections(states_result: list[str]):
    voices_sum = {}
    for data in states_result:
        name, score = data.split(" ")
        if name in voices_sum.keys():
            voices_sum[name] += int(score)
        else:
            voices_sum[name] = int(score)

    sorted_v_sum = sorted(voices_sum.items())
    str_sorted_v_sum = [f'{s[0]} {s[1]}' for s in sorted_v_sum]
    return str_sorted_v_sum


def elections_txt():
    f = File(__file__)
    arguments = f.read()
    states_result = arguments
    answer = elections(states_result)
    f.write('\n'.join(answer))


if __name__ == "__main__":
    elections_txt()
