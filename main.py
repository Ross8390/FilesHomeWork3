def sorted_files(files: list, path: str) -> None:
    file_dict = {sum(1 for _ in open(file, encoding="UTF-8")): file for file in files}
    with open(path, "w", encoding="UTF-8") as file_write:
        file_write.write("")
    with open(path, "a", encoding="UTF-8") as file_write:
        for key in sorted(file_dict.keys()):
            file_write.write(file_dict[key] + "\n")
            file_write.write(str(key) + "\n")
            file_write.writelines(line for line in open(file_dict[key], "r", encoding="UTF-8"))
            file_write.write("\n")

def main():
    files = ["1.txt", "2.txt"]
    sorted_files(files, "union file.txt")

if __name__ == "__main__":
    main()