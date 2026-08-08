# Genome Explorer Project

## Version 0.1

### Date
10 July 2026

### Objective
Create a basic DNA analyzer using Python.

### Features Completed
- Take DNA sequence as input
- Calculate DNA sequence length
- Count A nucleotides
- Count T nucleotides
- Count G nucleotides
- Count C nucleotides

### Python Concepts Learned
- input()
- print()
- len()
- count()

### Biology Concepts
- DNA consists of four nucleotides:
  - Adenine (A)
  - Thymine (T)
  - Guanine (G)
  - Cytosine (C)

### Sample Input
AATTTGGGGCCCA

### Sample Output
Length: 13
A = 3
T = 3
G = 4
C = 3

### What I Learned
Today I learned how to use Python strings to analyze a DNA sequence.---



# Version 0.2

## Date
10 July 2026

## New Feature Added
- Calculate GC Content of a DNA sequence

## Formula Used

GC Content = (G + C) / Length × 100

## Python Concepts Learned
- Variables
- Arithmetic Operators
  - +
  - /
  - *
- round() function

## Biology Concepts Learned
- GC Content
- G-C base pair has 3 hydrogen bonds
- A-T base pair has 2 hydrogen bonds
- Higher GC content generally means more stable DNA

## Sample Input

AATTGGGGCCCTTAACGGG

## Sample Output

Length: 18

A = 4

T = 4

G = 6

C = 4

GC Content = 55.56 %

## What I Learned

Today I learned how to:
- Store values in variables.
- Use mathematical formulas in Python.
- Calculate GC Content from a DNA sequence.
- Format decimal numbers using the round() function. 



# Version 0.3

## 📅 Date
10 July 2026

## 🎯 New Feature Added
- DNA Sequence Validation

---

## 🐍 Python Concepts Learned

- Boolean variables (`True` / `False`)
- `for` loop
- `if` statement
- `not in`
- `break`
- Iterating through a string one character at a time

---

## 🧬 Biology Concepts Learned

- A valid DNA sequence contains only four nucleotides:
  - Adenine (A)
  - Thymine (T)
  - Guanine (G)
  - Cytosine (C)

- Any other character (such as X, Z, 1, @) makes the DNA sequence invalid.

---

## 🧪 Sample Input

```
ATGXCCA
```

## ✅ Sample Output

```
Invalid DNA sequence
```

---

## ⚠ Challenges Faced

- Learned how to check each nucleotide one by one.
- Understood why `break` makes the program stop immediately after finding an invalid character.
- Learned how `not in` works for validation.

---

## 📚 What I Learned

- A `for` loop can process every nucleotide in a DNA sequence.
- Boolean variables (`True` and `False`) help control program logic.
- DNA validation is an important first step before any biological analysis.


# Version 0.4

## 📅 Date
12 July 2026

## 🎯 Objective
To combine all previous features into one Python application and add the Reverse DNA Sequence feature.

---

## ✅ Features Included

- DNA Sequence Validation
- DNA Length Calculation
- Nucleotide Count (A, T, G, C)
- GC Content Calculation
- Reverse DNA Sequence

---

## 🐍 Python Concepts Learned

- String slicing (`[::-1]`)
- Negative indexing
- `input()`
- `print()`
- `if-else`
- `for` loop
- `.upper()`
- `.count()`
- `len()`
- `round()`

---

## 🧬 Biology Concepts Learned

- A valid DNA sequence contains only A, T, G, and C.
- GC Content is the percentage of Guanine (G) and Cytosine (C) in a DNA sequence.
- Reverse DNA changes only the order of nucleotides.
- Reverse DNA is **different** from Reverse Complement DNA.

---

## 📝 Algorithm

1. Take DNA sequence as input.
2. Convert it to uppercase.
3. Check whether the sequence is valid.
4. Calculate DNA length.
5. Count A, T, G, and C.
6. Calculate GC Content.
7. Reverse the DNA sequence.
8. Display all results.

---

## 💡 Challenges Faced

- Renamed the project folder from **Genome Explorar** to **Genome Explorer**.
- Renamed `day1.py` to `main.py`.
- Learned that a project should keep growing in one file instead of creating a new file for every version.
- Reorganized the project structure to make it suitable for GitHub and the college report.

---

## 📚 What I Learned Today

- How to combine multiple features into one Python program.
- How string slicing (`[::-1]`) reverses a DNA sequence.
- How to organize a Python project professionally.
- The importance of documenting each project version.

---

## 📌 Current Project Version

**Version 0.4**

**Status:** ✅ Completed Successfully

---

## 🚀 Next Goal

**Version 0.5 – Reverse Complement DNA**

In the next version, I will learn:
- Python Dictionaries
- Complementary base pairing (A↔T, G↔C)
- Reverse Complement DNA generation


# Version 0.5

## 📅 Date
12 July 2026

---

## 🚀 New Feature Added
- Reverse Complement DNA

---

## 🐍 Python Concepts Learned

- Dictionary (`dict`)
- Key-value pairs
- Accessing dictionary values using keys
- `for` loop
- String concatenation
- Building a new string one character at a time
- Using an empty string (`""`) as a starting value

---

## 🧬 Biology Concepts Learned

- DNA bases pair according to complementary base pairing:
  - Adenine (A) ↔ Thymine (T)
  - Guanine (G) ↔ Cytosine (C)
- Reverse Complement DNA is obtained by:
  1. Reversing the DNA sequence.
  2. Replacing each base with its complementary base.
- Reverse complement sequences are widely used in:
  - Bioinformatics
  - DNA sequencing
  - PCR primer design
  - Genome analysis

---

## 📝 Algorithm

1. Take a DNA sequence from the user.
2. Validate the DNA sequence.
3. Reverse the DNA sequence.
4. Create a dictionary containing complementary bases.
5. Create an empty string for the reverse complement.
6. Traverse the reversed DNA sequence.
7. Replace each nucleotide with its complementary base.
8. Store the result in the new string.
9. Display the reverse complement DNA sequence.

---

## 💡 Example

### Input

```
ATGC
```

### Reverse DNA

```
CGTA
```

### Reverse Complement DNA

```
GCAT
```

---

## 🎯 What I Learned

- How dictionaries store related data.
- How to retrieve values from a dictionary using keys.
- How to generate a reverse complement DNA sequence.
- How to build a string inside a loop.
- The biological importance of complementary DNA sequences.

---

## ⚠️ Challenges Faced

- Understanding how dictionaries work.
- Learning why an empty string is needed.
- Understanding how the reverse complement is created step by step.

---

## ✅ Version Status

Completed Successfully ✔️



# Version 0.6

## 📅 Date
12 July 2026

---

## 🚀 New Feature Added
- DNA to RNA Transcription

---

## 🐍 Python Concepts Learned

- String method: `.replace()`
- Creating a new variable
- String manipulation

---

## 🧬 Biology Concepts Learned

- DNA is transcribed into RNA.
- During transcription, Thymine (T) is replaced by Uracil (U).
- RNA is an important molecule involved in protein synthesis.

---

## 📝 Algorithm

1. Take the DNA sequence.
2. Replace every `T` with `U`.
3. Store the result in a new variable called `rna`.
4. Display the RNA sequence.

---

## 💡 Example

### Input

ATGCTT

### Output

AUGCUU

---

## 🎯 What I Learned

- How to use the `.replace()` method.
- How DNA is converted into RNA.
- How Python can be used to model a biological process.

---

## ⚠️ Challenges Faced

- Understanding why `T` changes to `U`.
- Learning how `.replace()` works.

---

## ✅ Version Status

Completed Successfully ✔️


# Version 0.7

## 📅 Date
14 July 2026

---

## 🚀 New Feature Added
- Start Codon Detection

---

## 🐍 Python Concepts Learned

- `in` operator
- String searching
- `if-else` statement

---

## 🧬 Biology Concepts Learned

- A start codon marks the beginning of protein synthesis.
- The start codon in DNA is **ATG**.
- Start codons are essential for gene expression.

---

## 📝 Algorithm

1. Take the validated DNA sequence.
2. Search for the sequence "ATG".
3. If found, display that the start codon is present.
4. Otherwise, display that the start codon is not present.

---

## 💡 Example

### Input

CCCATGAAA

### Output

Start codon (ATG) found.

---

## 🎯 What I Learned

- How to search for a substring using the `in` operator.
- The biological importance of the start codon.
- How Python can detect biological patterns in DNA.

---

## ⚠️ Challenges Faced

- Understanding how the `in` operator searches inside a string.
- Connecting the Python code with the biological concept.

---

## ✅ Version Status

Completed Successfully ✔️

# Version 0.8

## 📅 Date
14 July 2026

---

## 🚀 New Feature Added

- Stop Codon Detection

---

## 🐍 Python Concepts Learned

- Logical operator (`or`)
- Multiple condition checking
- String searching using the `in` operator
- Conditional statements (`if-else`)

---

## 🧬 Biology Concepts Learned

- Stop codons signal the end of protein synthesis.
- There are three stop codons in DNA:
  - TAA
  - TAG
  - TGA
- A protein-coding gene usually begins with a start codon (ATG) and ends with one of the stop codons.

---

## 📝 Algorithm

1. Take the validated DNA sequence.
2. Search for the stop codons:
   - TAA
   - TAG
   - TGA
3. If any stop codon is found, display:
   "Stop codon found."
4. Otherwise display:
   "Stop codon not found."

---

## 💡 Example

### Input

ATGAAATAG

### Output

Start codon (ATG) found.
Stop codon found.

---

## 🎯 What I Learned

- How to check multiple conditions using the `or` operator.
- The biological role of stop codons.
- How Python can identify important DNA sequence patterns.

---

## ⚠️ Challenges Faced

- Understanding how multiple conditions work together.
- Learning the three different stop codons.

---

## ✅ Version Status

Completed Successfully ✔️

# Version 0.9

## 📅 Date
14 July 2026

---

## 🚀 New Feature Added

- Start Codon Position Detection

---

## 🐍 Python Concepts Learned

- `.find()` method
- Storing returned values in variables
- String indexing

---

## 🧬 Biology Concepts Learned

- The position of a start codon helps identify where a protein-coding sequence begins.
- Bioinformatics tools often report the location of important DNA features.

---

## 📝 Algorithm

1. Search the DNA sequence for "ATG".
2. If found, store its position using `.find()`.
3. Display that the start codon is present.
4. Display its position.
5. Otherwise, report that no start codon was found.

---

## 💡 Example

### Input

CCCATGAAATAG

### Output

Start codon (ATG) found.
Start codon position: 3

---

## 🎯 What I Learned

- How to use the `.find()` method.
- How to determine the location of a DNA pattern.
- Why sequence positions are important in bioinformatics.

---

## ⚠️ Challenges Faced

- Understanding that Python starts counting from index 0.
- Learning the difference between checking if a pattern exists and finding its position.

---

## ✅ Version Status

Completed Successfully ✔️

# Genome Explorer v0.10
Date: 14 July 2026

## Topics Learned

- Introduction to Python Functions (`def`)
- Function Calls
- Parameters
- Return Statement
- Code Refactoring

## Functions Created

1. dna_length(dna)
   - Prints the length of the DNA sequence.

2. nucleotide_count(dna)
   - Counts A, T, G and C nucleotides.

3. gc_content(dna)
   - Calculates GC percentage.

4. reverse_dna(dna)
   - Prints the reverse DNA sequence.
   - Returns the reversed sequence for later use.

## New Python Concepts

- `def` is used to create a function.
- Functions help organize code.
- Parameters allow data to be passed into a function.
- `return` sends a value back to the program.
- Variables can store returned values.

Example:

reverse_sequence = reverse_dna(dna)

Here:
- Function: reverse_dna
- Argument: dna
- Variable: reverse_sequence

## Project Status

Completed Features:
- DNA Validation
- DNA Length
- Nucleotide Count
- GC Content
- Reverse DNA
- Reverse Complement
- RNA Transcription
- Start Codon Detection
- Stop Codon Detection

Current Version:
Genome Explorer v0.10

# Version 1.0

## 📅 Date
21 July 2026

---

## 🚀 New Feature Added

- Interactive Menu System

---

## 🐍 Python Concepts Learned

- `while True` loop
- `break` statement
- `if`, `elif`, and `else`
- User input using `input()`
- Building a menu-driven program
- Organizing code into separate features

---

## 🧬 Biology Features Included

The Genome Explorer can now perform the following analyses:

- DNA Length
- Nucleotide Count
- GC Content Calculation
- Reverse DNA
- Reverse Complement DNA
- DNA to RNA Transcription
- Start Codon Detection
- Stop Codon Detection
- Start Codon Position Detection

---

## 📝 Algorithm

1. Display the Genome Explorer menu.
2. Ask the user to choose an option.
3. Execute the selected DNA analysis.
4. Display the result.
5. Return to the main menu.
6. Continue until the user selects Exit.
7. End the program using the `break` statement.

---

## 💡 Example

### Main Menu

```
========================================
         GENOME EXPLORER
========================================

1. DNA Length
2. Nucleotide Count
3. GC Content
4. Reverse DNA
5. Reverse Complement DNA
6. RNA Transcription
7. Start Codon Detection
8. Stop Codon Detection
9. Start Codon Position
0. Exit
```

### Example

Input

```
Choice: 3

DNA Sequence:
ATGC
```

Output

```
GC Content: 50.0 %
```

---

## 🎯 What I Learned

- How to design a menu-driven application.
- How to repeatedly execute a program using a `while` loop.
- How to control program flow using `if`, `elif`, and `else`.
- How to exit a loop using the `break` statement.
- How to organize multiple bioinformatics tools into one Python application.

---

## ⚠️ Challenges Faced

- Understanding how the `while True` loop works.
- Organizing multiple features inside one menu.
- Learning proper indentation inside loops and conditional statements.
- Connecting each menu option with the correct DNA analysis feature.

---

## 📈 Project Progress

Current Version: **Genome Explorer v1.0**

### Features Completed

✅ DNA Length

✅ Nucleotide Count

✅ GC Content Calculation

✅ DNA Validation

✅ Reverse DNA

✅ Reverse Complement DNA

✅ DNA to RNA Transcription

✅ Start Codon Detection

✅ Stop Codon Detection

✅ Start Codon Position Detection

✅ Interactive Menu System

---

## 🔜 Future Improvements

- Read DNA sequences from FASTA files.
- Save analysis results to a text file.
- Find multiple start and stop codons.
- Detect Open Reading Frames (ORFs).
- Improve the user interface.
- Add error handling for invalid DNA sequences in every menu option.

---

## ✅ Version Status

**Genome Explorer Version 1.0 Successfully Completed ✔️**