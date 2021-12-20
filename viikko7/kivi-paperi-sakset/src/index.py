from peli import Peli


def main():
    while True:
        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )

        vastaus = input()
        
        print("Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s")

        if vastaus.endswith("a"):
            Peli.kaksinpeli().pelaa()
        elif vastaus.endswith("b"):
            Peli.yksinpeli().pelaa()
        elif vastaus.endswith("c"):
            Peli.haastava_yksinpeli().pelaa()
        else:
            break


if __name__ == "__main__":
    main()
