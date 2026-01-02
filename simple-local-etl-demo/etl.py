import os


# ============= Core Functions =============

def read_and_print_file(filename: str) -> list[str]:
    """Read a file and return its content as a list of lines/strings.
    
    This function shows TWO methods to read all lines from a file.
    """
    
    # METHOD 1: Using readlines() - Reads all lines at once
    with open(filename, "r") as file:
        lines = file.readlines()  # Returns ["hello\n", "world\n"]
    return [line.strip() for line in lines]  # Remove \n from each line
    
    # METHOD 2: Using for loop - Reads lines one by one
    # Uncomment below and comment METHOD 1 to use this approach
    # lines = []
    # with open(filename, "r") as file:
    #     for line in file:
    #         lines.append(line.strip())  # Read and strip each line
    # return lines


def read_and_print_file_method1(filename: str) -> list[str]:
    """METHOD 1: Using readlines() to read all lines at once."""
    with open(filename, "r") as file:
        lines = file.readlines()  # Read ALL lines at once into a list
    # lines = ["hello\n", "world\n"]
    
    # Remove \n from each line using list comprehension
    return [line.strip() for line in lines]
    # Result: ["hello", "world"]


def read_and_print_file_method2(filename: str) -> list[str]:
    """METHOD 2: Using for loop to read lines one by one."""
    lines = []
    with open(filename, "r") as file:
        for line in file:  # Loop through each line
            lines.append(line.strip())  # Add stripped line to list
    return lines
    # Result: ["hello", "world"]


def transform(lines: list[str]) -> list[str]:
    """Transform list of strings to uppercase."""
    transformed_content = []
    for line in lines:
        transformed_content.append(line.upper())
    return transformed_content


def load(filename: str, transformed_content: list[str]) -> bool:
    """Write content to a file and return whether the file exists."""
    with open(filename, "w") as file:
        for content in transformed_content:
            file.write(content + "\n")
    
    return os.path.exists(filename)


def my_etl():
    """ETL pipeline: Extract, Transform, Load."""
    # Extract from one file
    src_file_content = read_and_print_file("data/raw.txt")
    
    # Transform -> capitalize
    transformed_content = transform(src_file_content)
    
    # Load
    success = load("data/processed.txt", transformed_content)
    
    print(f"ETL :: {success}")


# ============= Test Functions =============

def test_read_and_print_file():
    """Test the read_and_print_file function."""
    expected_1 = "hello world\n happy new year  "
    with open("testcases/temp.txt", "w") as file:
        file.write(expected_1)
    
    actual_1 = read_and_print_file("testcases/temp.txt")
    print("hello world" == actual_1[0])
    
    expected_2 = "hello Didi"
    with open("testcases/temp.txt", "w") as file:
        file.write(expected_2)
    
    actual_2 = read_and_print_file("testcases/temp.txt")
    print("hello Didi" == actual_2[0])


def test_transform():
    """Test the transform function."""
    expected_1 = ["HELLO", "WORLD"]
    actual_1 = transform(["hello", "world"])
    print(expected_1 == actual_1)


def test_load():
    """Test the load function."""
    # Prove file existence
    expected_1 = True
    actual_1 = load("testcases/new_file.txt", ["hello", "world"])
    print(expected_1 == actual_1)
    
    # Validate file content
    expected_2 = ["hello", "world"]
    actual_2 = read_and_print_file("testcases/new_file.txt")
    print(expected_2 == actual_2)


# ============= Main Execution =============

if __name__ == "__main__":
    my_etl()
    test_read_and_print_file()
    test_load()
    test_transform()

