import os

print("============ GET ALL DIR LISTS ============")
directories = os.listdir(".")

print("#")
print(f"============ {len(directories)} files are detected ============")
python_files = []

print("#")
print("============ START EXPLORE DIR  ============")
for directory in directories:
    if os.path.isdir(directory):
        print("#")
        print(f"============ CHANGE PATH TO {directory}  ============")
        os.chdir(directory)

        path = os.getcwd()

        print("#")
        print(f"============ GET ALL PYTHON FILES IN {directory}  ============")
        python_files = list(
            filter(
                lambda file: ".py" in file,
                [
                    file
                    for file in os.listdir(path)
                    if os.path.isfile(os.path.join(path, file))
                ],
            )
        )
        print("#")
        print(
            f"============ {len(python_files)} PYTHON FILES ARE DETECTED  ============"
        )

        print("#")
        print("============ STARTING FORMMATING USING BLACK FORMATTER  ============")
        for file in python_files:
            try:
                print(f"============ {file} FORMATTING IN PROGRESS  ============")
                os.system(f"black {file}")
            except Exception:
                print(f"============ {file} FORMATTING FAIL  ============")

        print("#")
        print(f"============ COMPLETE FORMMATING IN {path}  ============")

        os.chdir("..")

        print("#")
        print(f"============ CHANGE PATH TO {os.getcwd()}  ============")
