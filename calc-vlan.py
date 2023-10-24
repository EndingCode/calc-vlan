import argparse


def expand_range_input(input_str):
    output_list = []
    for part in input_str.split(','):
        if 'to' in part:
            start, end = part.split('to')
            start = int(start)
            end = int(end)
            output_list.extend(range(start, end + 1))
        else:
            output_list.append(int(part))

    return output_list


def main():
    parser = argparse.ArgumentParser(description="列出交换机所有的vlan batch中的vlan信息")
    parser.add_argument("batch", help="输入交换机vlan batch。示例： python calc-vlan '1 20 to 30 40'")
    args = parser.parse_args()
    result = expand_range_input(" ".join(args.batch.split()).replace(" ", ",").replace(",to,", "to"))
    print("列出所有vlan：", ' '.join(str(num) for num in result))
    print("vlan个数：", len(result))


if __name__ == "__main__":
    main()
