# Simple ETL Process - Learning Project

## 📚 For Complete Beginners

This is a beginner-friendly guide to understanding ETL (Extract, Transform, Load) processes in Python. Each section includes input/output examples, visual diagrams, and step-by-step instructions.

## Overview
This project demonstrates a simple ETL (Extract, Transform, Load) pipeline implementation in Python. Created as a learning exercise to understand the fundamentals of data processing workflows.

## What is ETL?
ETL stands for:
- **Extract**: Reading data from a source (text file)
- **Transform**: Processing/modifying the data (converting to uppercase)
- **Load**: Writing the transformed data to a destination (another text file)

### Real-World Analogy
Think of ETL like cooking:
1. **Extract** = Getting ingredients from the fridge
2. **Transform** = Cooking/preparing the ingredients
3. **Load** = Plating the finished dish

## 🚀 Quick Start Guide for Beginners

### Step 1: Set Up Your Files

First, create a file called `data/raw.txt` with some sample text:

**File: data/raw.txt**
```
hello world
```

### Step 2: Run the ETL Pipeline

Run the script:
```bash
python etl.py
```

### Step 3: Check the Output

After running, you'll see a new file called `data/processed.txt`:

**File: data/processed.txt**
```
HELLO WORLD
```
(Note: "HELLO WORLD" appears on ONE line because it's one line in the input file)

**What just happened?**
- ✅ Extracted: Read "hello world" from `data/raw.txt`
- ✅ Transformed: Converted to "HELLO WORLD"
- ✅ Loaded: Wrote to `data/processed.txt`

## Project Structure

### Core Functions

#### 1. `read_and_print_file(filename)` - EXTRACT

**Purpose**: Extracts (reads) data from a text file

**Type Information:**
- **Input Type**: `str` (string) - filename/path to the file
- **Output Type**: `list[str]` (list of strings) - each item is a line from the file

**Input/Output Example:**

```python
# If you have a file called "sample.txt" with this content:
# sample.txt:
# Hello Python

content = read_and_print_file("sample.txt")
print(content)  # Output: ["Hello Python\n"]
```

**Visual Representation:**
```
📄 sample.txt        →  Function  →  ["Hello Python\n"]
(file on disk)          (reads)       (Python list)
```

---

#### 2. `transform(lines)` - TRANSFORM

**Purpose**: Transforms text data to uppercase

**Type Information:**
- **Input Type**: `list[str]` (list of strings) - list of text to transform
- **Output Type**: `list[str]` (list of strings) - same list but in UPPERCASE

**Input/Output Example:**

```python
# Input: List of lowercase strings
input_data = ["hello", "world", "python"]

# Call the function
output_data = transform(input_data)

# Output: List of uppercase strings
print(output_data)  # ["HELLO", "WORLD", "PYTHON"]
```

**Visual Representation:**
```
INPUT                    TRANSFORM                OUTPUT
["hello", "world"]   →   .upper() applied   →   ["HELLO", "WORLD"]
(lowercase)              (to each item)          (UPPERCASE)
```

**More Examples:**
| Input | Output |
|-------|--------|
| `["hi"]` | `["HI"]` |
| `["Good Morning"]` | `["GOOD MORNING"]` |
| `["123abc"]` | `["123ABC"]` |

---

#### 3. `load(filename, transformed_content)` - LOAD

**Purpose**: Loads (writes) transformed data into a new file

**Type Information:**
- **Input Type 1**: `str` (string) - filename where data will be saved
- **Input Type 2**: `list[str]` (list of strings) - data to write to file
- **Output Type**: `bool` (boolean) - `True` if file created, `False` if failed

**Input/Output Example:**

```python
# Input: filename and data to write
data = ["HELLO", "WORLD"]
success = load("output.txt", data)

# Output: Returns True if file was created
print(success)  # True
```

**File: output.txt** (each item on a NEW line)
```
HELLO
WORLD
```

**Visual Representation:**
```
INPUT                           LOAD FUNCTION              OUTPUT
filename: "output.txt"     →    writes to disk       →    📄 output.txt
data: ["HELLO", "WORLD"]        (creates file)            ✅ File created
                                                          Returns: True
```

**What happens inside the file:**
```
Before: (file doesn't exist)

After running load("output.txt", ["HELLO", "WORLD"]):
📄 output.txt:
HELLO    ← First item on line 1
WORLD    ← Second item on line 2

(Each item from the list gets its own line!)
```

---

#### 4. `my_etl()` - COMPLETE PIPELINE

**Purpose**: Orchestrates the complete ETL workflow

**Complete Example with Files:**

**BEFORE ETL:**
```
📁 Your Directory:
  � data/
    �📄 raw.txt (contains: "hello world")
```

**RUNNING ETL:**
```python
my_etl()
# Console output: ETL :: True
```

**AFTER ETL:**
```
📁 Your Directory:
  � data/
    📄 raw.txt (contains: "hello world")                    ← Original file unchanged
    📄 processed.txt (contains: "HELLO WORLD" on one line)  ← New file created!
  📁 testcases/ (for test temp files)
```

**Step-by-Step Data Flow:**

| Step | Action | Data State | File |
|------|--------|------------|------|
| 1 | Extract | `["hello world\n"]` | Read from data/raw.txt |
| 2 | Transform | `["HELLO WORLD\n"]` | In memory |
| 3 | Load | File created | Written to data/processed.txt |
| 4 | Verify | Returns `True` | Success! |

## 🎯 Hands-On Practice Examples

### Example 1: Simple Text Transformation

**Create a file: `greeting.txt`**
```
good morning
```

**Run in Python:**
```python
# Extract
data = read_and_print_file("greeting.txt")
print(f"Extracted: {data}")  # Output: ['good morning\n']

# Transform
transformed = transform(data)
print(f"Transformed: {transformed}")  # Output: ['GOOD MORNING\n']

# Load
success = load("greeting_upper.txt", transformed)
print(f"Loaded: {success}")  # Output: True
```

**Result: `greeting_upper.txt`**
```
GOOD MORNING
```
(One line because input file has one line)

---

### Example 2: Multiple Lines (IMPORTANT!)

**Create a file: `names.txt`** (3 lines)
```
alice
bob
charlie
```

**Run in Python:**
```python
# Read the file
names = []
with open("names.txt", "r") as f:
    for line in f:
        names.append(line.strip())  
        
# After reading, names = ['alice', 'bob', 'charlie']
# Type: list[str] with 3 items

# Transform to uppercase
upper_names = transform(names)  
# Result: ['ALICE', 'BOB', 'CHARLIE']
# Type: list[str] with 3 items (all uppercase)

# Save to new file
success = load("names_upper.txt", upper_names)
# Returns: True (file created successfully)
```

**Result: `names_upper.txt`** (each name on its own line)
```
ALICE    ← Line 1
BOB      ← Line 2
CHARLIE  ← Line 3
```

**KEY POINT:** Since the input list has 3 items, the output file has 3 lines!

---

### Example 3: Testing Individual Functions

**Test the Transform Function:**
```python
# Test 1: Basic transformation
result1 = transform(["apple"])
print(result1)  # Output: ['APPLE']

# Test 2: Multiple items
result2 = transform(["cat", "dog", "bird"])
print(result2)  # Output: ['CAT', 'DOG', 'BIRD']

# Test 3: Mixed case
result3 = transform(["HeLLo", "WoRLd"])
print(result3)  # Output: ['HELLO', 'WORLD']
```

**Test the Load Function:**
```python
# Create a test file
test_passed = load("test.txt", ["TEST", "DATA"])
print(f"File created: {test_passed}")  # Output: True

# Verify the file exists
import os
print(f"File exists: {os.path.exists('test.txt')}")  # Output: True

# Read it back to verify content
content = read_and_print_file("test.txt")
print(f"Content: {content}")  # Output: ['TEST\n']
```

**File: test.txt** (after load)
```
TEST    ← Line 1
DATA    ← Line 2
```

---

## Running the Project

### Execute the main script:
```bash
python word.py
```

**Expected Console Output:**
```
True
True
```

These `True` values indicate that:
1. First `True`: File was created successfully (test_load)
2. Second `True`: Transformation worked correctly (test_transform)

### Run specific ETL pipeline:
```python
from word import my_etl
my_etl()
```

**Expected Console Output:**
```
ETL :: True
```

This means the entire ETL process completed successfully!

## Testing

The project includes comprehensive unit tests for each function:

### Test Functions Overview

| Test Function | What It Tests | Expected Result |
|---------------|---------------|-----------------|
| `test_read_and_print_file()` | File reading works correctly | `True` |
| `test_transform()` | Text converts to uppercase | `True` |
| `test_load()` | File creation and writing | `True` |

### Detailed Test Explanations

#### Test 1: `test_load()`

**What it does:**
```python
def test_load():
    # Creates a file with ["hello", "world"]
    # Checks if file was created (should return True)
    # Reads the file back to verify content
```

**Example Run:**
```
Input Type: list[str] = ["hello", "world"]
Action: Creates new_file.txt
Output Type: bool = True (file created)
```

**File: new_file.txt**
```
hello    ← Item 1 on line 1
world    ← Item 2 on line 2
```
(Each item in the list becomes a separate line in the file!)

---

#### Test 2: `test_transform()`

**What it does:**
```python
def test_transform():
    # Tests if ["hello", "world"] becomes ["HELLO", "WORLD"]
```

**Example Run:**
```
Input Type:  list[str] = ["hello", "world"]
Expected Output Type: list[str] = ["HELLO", "WORLD"]
Actual Output: ["HELLO", "WORLD"]
Result: True ✅
```

---

#### Test 3: `test_read_and_print_file()`

**What it does:**
```python
def test_read_and_print_file():
    # Creates temp.txt with "hello world"
    # Reads it back
    # Checks if content matches
```

**Example Run:**
```
Step 1: Write "hello world" to temp.txt
Step 2: Read temp.txt → ["hello world"]
Step 3: Compare: "hello world" == "hello world"
Result: True ✅
```

### Run Tests

**Option 1: Run built-in tests**
```bash
python etl.py
```
Expected output:
```
True    ← test_load passed
True    ← test_transform passed
```

----------------------------------------------------------------------
Ran 2 tests in 0.001s

OK
```

### Understanding Test Output

When you see `True` printed:
- ✅ **Good!** The test passed
- The function works as expected

When you see `False` printed:
- ❌ **Problem!** The test failed
- Check your code for errors

## Example Workflow

```python
# 1. Extract: Read from source file
data = read_and_print_file("input.txt")

# 2. Transform: Convert to uppercase
transformed_data = transform(data)

# 3. Load: Write to destination file
success = load("output.txt", transformed_data)
```

## Learning Outcomes
- ✅ Understanding ETL pipeline components
- ✅ File I/O operations in Python
- ✅ Data transformation techniques
- ✅ Writing unit tests for validation
- ✅ Code organization and documentation

## Files
- `etl.py`: Main ETL implementation with tests
- `data/raw.txt`: Raw input files
- `data/processed.txt`: Processed output files
- `testcases/`: Folder for test temporary files

## Step-by-Step Code Explanation

### 1. Import Statement
```python
import os
```
- **What it does**: Imports the `os` module to interact with the operating system
- **Why we need it**: Used to check if files exist using `os.path.exists()`

---

### 2. Extract Function: `read_and_print_file(filename)`

**Two Methods to Read Files:**

The project demonstrates TWO different approaches to read all lines from a file. Both methods produce the same result!

---

#### **METHOD 1: Using `readlines()` - Recommended**

```python
def read_and_print_file_method1(filename: str) -> list[str]:
    """METHOD 1: Using readlines() to read all lines at once."""
    with open(filename, "r") as file:
        lines = file.readlines()  # Read ALL lines at once into a list
    # lines = ["hello\n", "world\n"]
    
    # Remove \n from each line using list comprehension
    return [line.strip() for line in lines]
    # Result: ["hello", "world"]
```

**Step-by-step breakdown:**
1. **Line 1**: Opens the file in read mode (`"r"`)
2. **Line 2**: `file.readlines()` reads ALL lines at once
   - Returns a list where each item is one line
   - Each line includes `\n` at the end: `["hello\n", "world\n"]`
3. **Line 3**: List comprehension removes `\n` from each line
   - `line.strip()` removes whitespace and newline characters
   - Final result: `["hello", "world"]`

**Input/Output Example:**
```python
# Given a file "message.txt" containing:
# hello
# world

result = read_and_print_file_method1("message.txt")
print(result)
# Output: ['hello', 'world']
```

**Pros of readlines():**
- ✅ More concise code
- ✅ Faster for small to medium files
- ✅ Easier to understand

---

#### **METHOD 2: Using `for` loop**

```python
def read_and_print_file_method2(filename: str) -> list[str]:
    """METHOD 2: Using for loop to read lines one by one."""
    lines = []
    with open(filename, "r") as file:
        for line in file:  # Loop through each line
            lines.append(line.strip())  # Add stripped line to list
    return lines
    # Result: ["hello", "world"]
```

**Step-by-step breakdown:**
1. **Line 1**: Creates an empty list called `lines` to hold file content
2. **Line 2**: Opens the file with the given filename in read mode (`"r"`)
   - `with` ensures file is automatically closed after reading
3. **Line 3**: Loop iterates through the file, line by line
   - Each iteration, `line` contains one line from the file (with `\n`)
4. **Line 4**: `.strip()` removes `\n`, then appends to the list
5. **Line 5**: Returns the list containing all lines

**Input/Output Example:**
```python
# Given a file "message.txt" containing:
# hello
# world

result = read_and_print_file_method2("message.txt")
print(result)
# Output: ['hello', 'world']
```

**Pros of for loop:**
- ✅ More memory efficient for large files
- ✅ Processes one line at a time
- ✅ More explicit and readable for beginners

---

#### **Comparison of Both Methods**

| Feature | `readlines()` | `for` loop |
|---------|---------------|------------|
| **Speed** | Faster for small files | Slightly slower |
| **Memory** | Loads all at once | Processes one at a time |
| **Code Length** | More concise | More lines |
| **Best For** | Small/medium files | Very large files |
| **Result** | `["hello", "world"]` | `["hello", "world"]` |

**Both produce identical output!**

---

**What `\n` means:** The `\n` is a special character representing a new line (like pressing Enter). We use `.strip()` to remove it.

**Visual Flow (Both Methods):**
```
📄 message.txt              Function Process                 Result
┌──────────┐              ┌────────────────┐          ┌─────────────────┐
│hello     │              │1. Open file    │          │["hello",        │
│world     │         →    │2. Read lines   │    →     │ "world"]        │
└──────────┘              │3. Strip \n     │          └─────────────────┘
(2 lines)                 │4. Return list  │          (list with 2 items)
                          └────────────────┘
```

---

### 3. Transform Function: `transform(lines)`

```python
def transform(lines: list[str]) -> list[str]:
    transformed_content = []                # Step 1: Create empty list for results
    for line in lines:                      # Step 2: Loop through each line
        transformed_content.append(line.upper())  # Step 3: Convert to uppercase & add
    return transformed_content              # Step 4: Return transformed list
```

**Step-by-step breakdown:**
1. **Line 1**: Creates an empty list `transformed_content` to store uppercase text
2. **Line 2**: Starts a loop that goes through each `line` in the input `lines` list
3. **Line 3**: For each line:
   - `.upper()` converts the text to UPPERCASE
   - `.append()` adds the uppercase text to our result list
4. **Line 4**: Returns the list with all transformed (uppercase) content

**Input/Output Examples:**

Example 1:
```python
input_data = ["hello", "world"]
output_data = transform(input_data)
print(output_data)  # ['HELLO', 'WORLD']
```

Example 2:
```python
input_data = ["Python is fun", "I love coding"]
output_data = transform(input_data)
print(output_data)  # ['PYTHON IS FUN', 'I LOVE CODING']
```

**Loop Visualization:**
```
Loop Iteration 1:
  Input: "hello"  →  .upper()  →  "HELLO"  →  Add to list

Loop Iteration 2:
  Input: "world"  →  .upper()  →  "WORLD"  →  Add to list

Final Result: ["HELLO", "WORLD"]
```

---

### 4. Load Function: `load(filename, transformed_content)`

```python
def load(filename: str, transformed_content: list[str]) -> bool:
    with open(filename, "w") as file:       # Step 1: Open file in write mode
        for content in transformed_content:  # Step 2: Loop through each item
            file.write(content + "\n")       # Step 3: Write item with newline
    
    return os.path.exists(filename)         # Step 4: Check if file was created
```

**Step-by-step breakdown:**
1. **Line 1**: Opens (or creates) a file in write mode (`"w"`)
   - Write mode creates a new file or overwrites existing one
2. **Line 2**: Loops through each item in `transformed_content`
3. **Line 3**: For each item:
   - `content + "\n"` adds a newline character so each item is on a separate line
   - `file.write()` writes the content to the file
4. **Line 4**: Uses `os.path.exists()` to verify the file was created successfully
   - Returns `True` if file exists, `False` otherwise

**Input/Output Example:**

```python
# Input
data_to_write = ["HELLO", "WORLD", "PYTHON"]
result = load("output.txt", data_to_write)

# What gets written to output.txt:
# HELLO
# WORLD
# PYTHON

print(result)  # True (file was created successfully)
```

**Visual Flow:**
```
Input List              Writing Process           output.txt
┌─────────┐            ┌──────────────┐          ┌────────┐
│"HELLO"  │  →  Loop 1 │Write "HELLO" │    →     │HELLO   │
│"WORLD"  │  →  Loop 2 │Write "WORLD" │    →     │WORLD   │
│"PYTHON" │  →  Loop 3 │Write "PYTHON"│    →     │PYTHON  │
└─────────┘            └──────────────┘          └────────┘
                       Add \n after each          Each on
                                                  new line!
```

**Why `+ "\n"` is important:**
```
Without \n:          With \n:
HELLOWORLDPYTHON    HELLO
                    WORLD
                    PYTHON
```

---

### 5. ETL Pipeline: `my_etl()`

```python
def my_etl():
    # EXTRACT
    src_file_content = read_and_print_file("data/raw.txt")     # Step 1
    
    # TRANSFORM
    transformed_content = transform(src_file_content)           # Step 2
    
    # LOAD
    success = load("data/processed.txt", transformed_content)   # Step 3
    
    print(f"ETL :: {success}")                                  # Step 4
```

**Step-by-step breakdown:**
1. **Extract**: Calls `read_and_print_file()` to read data from `data/raw.txt`
   - Returns a list of lines from the file
2. **Transform**: Calls `transform()` to convert all text to uppercase
   - Takes the extracted content and transforms it
3. **Load**: Calls `load()` to write transformed data to `data/processed.txt`
   - Returns `True` if successful, `False` if failed
4. **Report**: Prints the result (`True` or `False`) to show if ETL succeeded

**Complete Flow with Real Data:**
```
Step 1: EXTRACT
📄 data/raw.txt contains: "hello python"
  ↓ read_and_print_file("data/raw.txt")
["hello python\n"]

Step 2: TRANSFORM
["hello python\n"]
  ↓ transform()
["HELLO PYTHON\n"]

Step 3: LOAD
["HELLO PYTHON\n"]
  ↓ load("data/processed.txt", ...)
📄 data/processed.txt created with: "HELLO PYTHON"
Returns: True

Step 4: REPORT
Console prints: ETL :: True
```

**File Changes Visualization:**
```
BEFORE my_etl():
📁 Directory
  ├── 📄 raw.txt         (contains: "hello python")
  └── 📄 word.py

AFTER my_etl():
📁 Directory
  ├── 📄 raw.txt         (contains: "hello python")  ← Unchanged
  ├── 📄 processed.txt   (contains: "HELLO PYTHON") ← NEW!
  └── 📄 word.py
```

---

### 6. Test Functions

#### `test_load()`
```python
def test_load():
    # Test 1: Check if file is created
    expected_1 = True
    actual_1 = load("new_file.txt", ["hello", "world"])
    print(expected_1 == actual_1)  # Should print: True
    
    # Test 2: Check if content is correct
    expected_2 = ["hello", "world"]
    actual_2 = read_and_print_file("new_file.txt")
    print(expected_2 == actual_2)  # Should print: True
```

**What it tests:**
- **Test 1**: Verifies that `load()` creates a file and returns `True`
- **Test 2**: Verifies the file contains the correct content

#### `test_transform()`
```python
def test_transform():
    expected_1 = ["HELLO", "WORLD"]
    actual_1 = transform(["hello", "world"])
    print(expected_1 == actual_1)  # Should print: True
```

**What it tests:**
- Checks if lowercase text is correctly transformed to uppercase
- Compares expected result with actual result

#### `test_read_and_print_file()`
```python
def test_read_and_print_file():
    # Test 1
    expected_1 = "hello world"
    with open("temp.txt", "w") as file:
        file.write(expected_1)                    # Create test file
    
    actual_1 = read_and_print_file("temp.txt")   # Read it back
    print("hello world" == actual_1[0])          # Compare
    
    # Test 2 (similar process with different text)
    expected_2 = "hello Didi"
    with open("temp.txt", "w") as file:
        file.write(expected_2)
    
    actual_2 = read_and_print_file("temp.txt")
    print("hello Didi" == actual_2[0])
```

**What it tests:**
- Creates a temporary file with known content
- Reads it back using our function
- Verifies the content matches what we wrote

---

### 7. Main Execution Block

```python
if __name__ == "__main__":
    test_load()
    test_transform()
```

**What it does:**
- `if __name__ == "__main__":` checks if this file is being run directly (not imported)
- If true, it runs the test functions to validate our code
- This prevents tests from running when the file is imported as a module

---

## Key Python Concepts Used

1. **File I/O Operations**
   - `open()`: Opens files
   - `"r"` mode: Read only
   - `"w"` mode: Write (creates or overwrites)
   - `with` statement: Automatically closes files

2. **Lists**
   - `[]`: Creates empty list
   - `.append()`: Adds items to list
   - `for item in list`: Loops through items

3. **String Methods**
   - `.upper()`: Converts text to uppercase
   - `.readline()`: Reads one line from file
   - `.write()`: Writes to file

4. **Type Hints**
   - `-> list[str]`: Function returns a list of strings
   - `filename: str`: Parameter should be a string
   - `-> bool`: Function returns True/False

5. **Testing**
   - Compare expected vs actual results
   - Use `print()` to display test results
   - Create temporary files for testing

---

## 🔍 Common Mistakes and Troubleshooting

### Problem 1: File Not Found Error
```
Error: FileNotFoundError: [Errno 2] No such file or directory: 'raw.txt'
```
**Solution:** Create the input file first!
```python
# Create raw.txt before running ETL
with open("raw.txt", "w") as f:
    f.write("hello world")
```

### Problem 2: Empty Output
```
processed.txt is empty or contains nothing
```
**Solution:** Check if raw.txt has content:
```python
# Verify raw.txt has data
with open("raw.txt", "r") as f:
    content = f.read()
    print(f"File contains: {content}")
```

### Problem 3: Understanding the Output
```
Why do I see \n in my output?
```
**Answer:** `\n` is a newline character (invisible in files, visible in Python strings)
- In the file: Each item appears on a new line
- In Python print: You see `\n` explicitly

---

## 📝 Practice Exercises for Beginners

### Exercise 1: Modify the Transform
Change the `transform` function to convert text to lowercase instead of uppercase.

**Hint:**
```python
def transform(lines: list[str]) -> list[str]:
    transformed_content = []
    for line in lines:
        transformed_content.append(line.lower())  # Changed .upper() to .lower()
    return transformed_content
```

**Test it:**
```
Input: "HELLO WORLD"
Expected Output: "hello world"
```

---

### Exercise 2: Add a New Transformation
Create a function that adds "Hello, " before each line.

**Hint:**
```python
def add_greeting(lines: list[str]) -> list[str]:
    result = []
    for line in lines:
        result.append("Hello, " + line)
    return result
```

**Test it:**
```python
data = ["Alice", "Bob"]
output = add_greeting(data)
print(output)  # ['Hello, Alice', 'Hello, Bob']
```

---

### Exercise 3: Chain Multiple Transformations
Apply both uppercase AND add greeting.

**Solution:**
```python
# Read file
data = read_and_print_file("names.txt")

# Transform 1: Uppercase
uppercase_data = transform(data)

# Transform 2: Add greeting
greeting_data = add_greeting(uppercase_data)

# Load result
load("final.txt", greeting_data)
```

**Example Flow:**
```
names.txt: "alice"
  ↓ transform()
"ALICE"
  ↓ add_greeting()
"Hello, ALICE"
  ↓ load()
final.txt: "Hello, ALICE"
```

---

## 🎓 What You've Learned

After completing this project, you now understand:

1. ✅ **ETL Basics**: What Extract, Transform, Load means
2. ✅ **File Reading**: How to open and read files in Python
3. ✅ **File Writing**: How to create and write to files
4. ✅ **Data Transformation**: How to process and modify data
5. ✅ **Lists**: How to work with Python lists
6. ✅ **Loops**: How to iterate through data
7. ✅ **Functions**: How to organize code into reusable functions
8. ✅ **Testing**: How to verify your code works correctly
9. ✅ **Type Hints**: What `-> list[str]` means
10. ✅ **Context Managers**: What `with open()` does

---

## 📚 Next Steps

Ready to level up? Try these challenges:

1. **Read Multiple Lines**: Modify to read ALL lines from a file (not just one)
2. **CSV Files**: Work with comma-separated values
3. **Error Handling**: Add try/except blocks for better error messages
4. **Command Line**: Accept filenames from command line arguments
5. **Data Validation**: Check if file is empty before processing

---

## 📖 Additional Resources

### Python Concepts to Study Next:
- List comprehensions (shorter way to write loops)
- Exception handling (try/except)
- Working with CSV files
- Regular expressions for text processing
- Pandas library for data manipulation

---

## Date
December 31, 2025

---

*This is a learning project focused on understanding basic ETL processes and Python file handling. Created for complete beginners with step-by-step examples and clear input/output demonstrations.*
