def read_file(filename):

    try:

        with open(filename, "r") as file:

            content = file.read()

            return content

    except FileNotFoundError:

        print("File not found")

        return None


def count_words(content):

    count = len(content.split())
    return count


def count_lines(content):


    count = len(content.splitlines())
    return count


def count_characters(content):

    count = len(content)
    return count



def main():

    filename = "random_sample.txt"

    content = read_file(filename)

    if content is None:
        return

    print("Total Words:", count_words(content))

    print("Total Lines:", count_lines(content))

    print("Total Characters:", count_characters(content))


main()