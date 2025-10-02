def carica_da_file(file_path):
    """Carica i libri dal file"""
    # TODO
    try:
        input_file = open(file_path, "r")  # May throw exceptions
        biblioteca = []
        for line in input_file:
            biblioteca.append(line.strip().split(","))
    except FileNotFoundError:
        print("\nFile not found!")
        return None
    input_file.close()
    print("\nFile caricato con successo!")
    return biblioteca


def aggiungi_libro(biblioteca, titolo, autore, anno, pagine, sezione, file_path):
    """Aggiunge un libro nella biblioteca"""
    # TODO
    z=0
    for i in biblioteca:
        if i[0] == titolo:
            print("\nTitolo già presente!")
            return None
        if i[4] == str(sezione):
            z=z+1
    if z==0:
        print("\nSezione non presente!")
        return None

    try:
        output_file = open(file_path, "a")  # May throw exceptions
        output_file.write(titolo+","+autore+","+str(anno)+","+str(pagine)+","+str(sezione)+"\n")
    except FileNotFoundError:
        print("\nFile not found!")
        return None
    output_file.close()
    biblioteca.append([titolo, autore, anno, pagine, sezione])
    return True

def cerca_libro(biblioteca, titolo):
    """Cerca un libro nella biblioteca dato il titolo"""
    # TODO
    for i in biblioteca:
        if i[0] == titolo:
            return i[0]+", "+i[1]+", "+str(i[2])+", "+str(i[3])+", "+str(i[4])
    return None



def elenco_libri_sezione_per_titolo(biblioteca, sezione):
    """Ordina i titoli di una data sezione della biblioteca in ordine alfabetico"""
    # TODO
    titoli=[]
    for i in biblioteca:
        if i[4] == str(sezione):
            titoli.append(i[0])
    if len(titoli)==0:
        print("\nSezione non presente!")
        return None
    else:
        titoli.sort()
        return titoli


def main():
    biblioteca = []
    file_path = "biblioteca.csv"

    while True:
        print("\n--- MENU BIBLIOTECA ---")
        print("1. Carica biblioteca da file")
        print("2. Aggiungi un nuovo libro")
        print("3. Cerca un libro per titolo")
        print("4. Ordina titoli di una sezione")
        print("5. Esci")

        scelta = input("Scegli un'opzione >> ").strip()

        if scelta == "1":
            while True:
                file_path = input("Inserisci il path del file da caricare: ").strip()
                biblioteca = carica_da_file(file_path)
                if biblioteca is not None:
                    biblioteca.pop(0)
                    break

        elif scelta == "2":
            if not biblioteca:
                print("\nPrima carica la biblioteca da file!")
                continue

            titolo = input("Titolo del libro: ").strip()
            autore = input("Autore: ").strip()
            try:
                anno = int(input("Anno di pubblicazione: ").strip())
                pagine = int(input("Numero di pagine: ").strip())
                sezione = int(input("Sezione: ").strip())
            except ValueError:
                print("\nErrore: inserire valori numerici validi per anno, pagine e sezione!")
                continue

            libro = aggiungi_libro(biblioteca, titolo, autore, anno, pagine, sezione, file_path)
            if libro:
                print(f"\nLibro aggiunto con successo!")
            else:
                print("Non è stato possibile aggiungere il libro!")

        elif scelta == "3":
            if not biblioteca:
                print("\nLa biblioteca è vuota!")
                continue

            titolo = input("Inserisci il titolo del libro da cercare: ").strip()
            risultato = cerca_libro(biblioteca, titolo)
            if risultato:
                print(f"\nLibro trovato: {risultato}")
            else:
                print("\nLibro non trovato!")

        elif scelta == "4":
            if not biblioteca:
                print("\nLa biblioteca è vuota!")
                continue

            try:
                sezione = int(input("Inserisci numero della sezione da ordinare: ").strip())
            except ValueError:
                print("\nErrore: inserire un valore numerico valido!")
                continue

            titoli = elenco_libri_sezione_per_titolo(biblioteca, sezione)
            if titoli is not None:
                print(f'\nSezione {sezione} ordinata:')
                print("\n".join([f"- {titolo}" for titolo in titoli]))

        elif scelta == "5":
            print("\nUscita dal programma...")
            break
        else:
            print("\nOpzione non valida. Riprova!")


if __name__ == "__main__":
    main()

