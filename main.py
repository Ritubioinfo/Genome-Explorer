# ============================================
# Genome Explorer v1.0
# Author: Ritu Tiwari
# Date: 29 July 2026
# Language: Python
# ============================================

while True:

    print("\n" + "=" * 40)
    print("         GENOME EXPLORER")
    print("=" * 40)

    print("1. DNA Length")
    print("2. Nucleotide Count")
    print("3. GC Content")
    print("4. Reverse DNA")
    print("5. Reverse Complement DNA")
    print("6. RNA Transcription")
    print("7. Start Codon Detection")
    print("8. Stop Codon Detection")
    print("9. Start Codon Position")
    print("0. Exit")

    choice = input("\nEnter your choice: ")

    # ------------------------------
    # Option 1 : DNA Length
    # ------------------------------
    if choice == "1":

        dna = input("Enter DNA sequence: ").upper()

        print("Length of DNA:", len(dna))

    # ------------------------------
    # Option 2 : Nucleotide Count
    # ------------------------------
    elif choice == "2":

        dna = input("Enter DNA sequence: ").upper()

        print("A:", dna.count("A"))
        print("T:", dna.count("T"))
        print("G:", dna.count("G"))
        print("C:", dna.count("C"))

    # ------------------------------
    # Option 3 : GC Content
    # ------------------------------
    elif choice == "3":

        dna = input("Enter DNA sequence: ").upper()

        gc_count = dna.count("G") + dna.count("C")
        gc_content = (gc_count / len(dna)) * 100

        print("GC Content:", round(gc_content, 2), "%")

    # ------------------------------
    # Option 4 : Reverse DNA
    # ------------------------------
    elif choice == "4":

        dna = input("Enter DNA sequence: ").upper()

        reverse_dna = dna[::-1]

        print("Reverse DNA:", reverse_dna)

    # ------------------------------
    # Option 5 : Reverse Complement DNA
    # ------------------------------
    elif choice == "5":

        dna = input("Enter DNA sequence: ").upper()

        reverse_dna = dna[::-1]

        complement = {
            "A": "T",
            "T": "A",
            "G": "C",
            "C": "G"
        }

        reverse_complement = ""

        for base in reverse_dna:
            reverse_complement += complement[base]

        print("Reverse Complement DNA:", reverse_complement)

    # ------------------------------
    # Option 6 : RNA Transcription
    # ------------------------------
    elif choice == "6":

        dna = input("Enter DNA sequence: ").upper()

        rna = dna.replace("T", "U")

        print("RNA Sequence:", rna)

    # ------------------------------
    # Option 7 : Start Codon Detection
    # ------------------------------
    elif choice == "7":

        dna = input("Enter DNA sequence: ").upper()

        if "ATG" in dna:
            print("Start codon (ATG) found.")
        else:
            print("Start codon (ATG) not found.")

    # ------------------------------
    # Option 8 : Stop Codon Detection
    # ------------------------------
    elif choice == "8":

        dna = input("Enter DNA sequence: ").upper()

        if "TAA" in dna or "TAG" in dna or "TGA" in dna:
            print("Stop codon found.")
        else:
            print("Stop codon not found.")

    # ------------------------------
    # Option 9 : Start Codon Position
    # ------------------------------
    elif choice == "9":

        dna = input("Enter DNA sequence: ").upper()

        if "ATG" in dna:
            position = dna.find("ATG")
            print("Start codon position:", position)
        else:
            print("Start codon not found.")

    # ------------------------------
    # Exit
    # ------------------------------
    elif choice == "0":

        print("Thank you for using Genome Explorer!")
        break

    # ------------------------------
    # Invalid Choice
    # ------------------------------
    else:

        print("Invalid choice! Please enter a number between 0 and 9.")
