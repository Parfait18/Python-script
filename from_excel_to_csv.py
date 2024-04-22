import pandas as pd


def convert_excel_to_csv(input_file, output_file):
    # Read the Excel file
    df = pd.read_excel(input_file)

    # Filter the desired columns
    columns_to_keep = ["CODE", "FAMILLE", "DESIGNATIONS", "UNITE DE MESURE", "BI", "BS"]
    df_filtered = df[columns_to_keep]

    # Remove spaces in the last two columns (BI and BS)
    df_filtered["BI"] = df_filtered["BI"].str.replace(" ", "")
    df_filtered["BS"] = df_filtered["BS"].str.replace(" ", "")
    df_filtered["DESIGNATIONS"] = df_filtered["DESIGNATIONS"].str.replace(
        "", "•"
    )  # Replace with a dot
    # Replace 'nan' values with empty string
    df_filtered.fillna("", inplace=True)

    # Remove line breaks in all text columns
    df_filtered = df_filtered.applymap(lambda x: str(x).replace("\n", " "))

    # Write the filtered data to a CSV file
    df_filtered.to_csv(output_file, index=False)

    print(f"The CSV file has been saved as {output_file}")


# Replace 'input.xlsx' with the path to the input Excel file
# Replace 'output.csv' with the path to the output CSV file
convert_excel_to_csv("book2.xlsx", "book2.csv")
