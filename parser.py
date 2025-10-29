from frontmatter import Frontmatter







def parse_markdown(file_path):
    d = Frontmatter.read_file(file_path)
    if __name__ == "__main__":
        print(d["attributes"])
    return d["attributes"]






if __name__ == "__main__":
    parse_markdown("야채볶음밥.md")
