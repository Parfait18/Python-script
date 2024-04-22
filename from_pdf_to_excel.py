import tabula
import pandas as pd

def convert_pdf_to_excel(input_pdf, output_excel):
    # Lire les tables du fichier PDF
    # Vous pouvez spécifier les pages à lire avec `pages='all'` ou une plage spécifique
    tables = tabula.read_pdf(input_pdf, pages='all')
    
    # Créez un Excel writer pour écrire les tables dans un fichier Excel
    with pd.ExcelWriter(output_excel) as writer:
        # Pour chaque table trouvée dans le PDF
        for i, table in enumerate(tables):
            # Écrivez la table en tant que feuille dans l'Excel
            sheet_name = f"Sheet_{i+1}"
            table.to_excel(writer, sheet_name=sheet_name, index=False)
    
    print(f"Le fichier Excel a été enregistré sous le nom de {output_excel}")

# Utilisation de la fonction
input_pdf = "Bénin-e-repertoire-des-prix-de-reference-2023.pdf"
output_excel = "fichier.xlsx"

convert_pdf_to_excel(input_pdf, output_excel)
