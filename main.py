from farm import Farm


def main():
    Chernihiv = Farm(540, "Kurin", 807, 260.4, 880, 10, "Avangard")

    Cherkasy = Farm(325, "Novomaydanets'ke", 1246, 280.2, 500, 22, "Leader")

    Volodymyr = Farm(478, "Bilin", 1525, 240, 724, 19, "Progress")

    print(Chernihiv.__str__())

    print(Cherkasy.__str__())

    print(Volodymyr.__str__())


if __name__ == "__main__":
    main()
