def main() -> None:
    max_emoji = 76
    rows = 10
    string = ""

    for emoji_idx in range(max_emoji):
        string += f'|![{emoji_idx}](scripts/tiles/tile_{emoji_idx}.png)'
        # string += f'|{str(emoji_idx).rjust(2, '0')}'
        if (emoji_idx + 1) % rows == 0:
            string += "|\n"
        if (emoji_idx + 1) == rows:
            string += ("|--" * (rows + 1))[:-2] + "\n"

    for extra_idx in range(rows - (max_emoji % rows)):
        string += '|'
        if (extra_idx + 1) == (rows - (max_emoji % rows)):
            string += '|'

    print(string)


if __name__ == "__main__":
    main()