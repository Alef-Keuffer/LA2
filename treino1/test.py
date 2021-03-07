import treino1


def test_factoriza():
    inp = [1, 3 * 5, 1000003 * 1000033]
    out = [0, 8, 2000036]
    for inp, out in zip(inp, out):
        assert treino1.factoriza(inp) == out


def test_cruzamentos():
    in1 = [
        "central",
        "liberdade",
        "chaos",
        "saovictor",
        "saovicente",
        "saodomingos",
        "souto",
        "capelistas",
        "anjo",
        "raio",
        "taxa",
    ]
    out1 = [
        ("t", 1),
        ("a", 2),
        ("e", 2),
        ("l", 2),
        ("r", 2),
        ("c", 3),
        ("o", 3),
        ("s", 6),
    ]

    in2 = ["ab", "bc", "bd", "cd"]
    out2 = [("a", 1), ("c", 2), ("d", 2), ("b", 3)]

    assert treino1.cruzamentos(in1) == out1
    assert treino1.cruzamentos(in2) == out2


def test_aloca():
    in1 = {10885: [1, 5], 40000: [5], 10000: [1, 2]}
    out1 = [40000]
    in2 = {30000: [1], 20000: [2], 10000: [3]}
    out2 = []
    in3 = {10885: [1, 5], 40000: [5], 10000: [1, 2, 3], 30000: [1], 20000: [2]}
    out3 = [30000, 40000]
    assert treino1.aloca(in1) == out1
    assert treino1.aloca(in2) == out2
    assert treino1.aloca(in3) == out3


def test_frequencia2(f):
    in1 = "o tempo perguntou ao tempo quanto tempo o tempo tem"
    out1 = ["tempo", "o", "ao", "perguntou", "quanto", "tem"]
    int2 = "ola"
    out2 = ["ola"]
    assert f(in1) == out1
    assert f(int2) == out2


def test_frequencia():
    test_frequencia2(treino1.frequencia)


def test_repete():
    in1 = ("amanha", 2)
    out1 = "amanhamanha"
    in2 = ("ola", 3)
    out2 = "olaolaola"
    in3 = ("aabcaa", 2)
    out3 = "aabcaabcaa"
    in4 = ('gg', 4)
    out4 = 'ggggg'
    in5 = ('g', 2)
    out5 = 'gg'
    in6 = ('ggg', 5)
    out6 = 'ggggggg'
    in7 = ('gag', 4)
    out7 = 'gagagagag'

    assert treino1.repete(*in1) == out1
    assert treino1.repete(*in2) == out2
    assert treino1.repete(*in3) == out3
    assert treino1.repete(*in4) == out4
    assert treino1.repete(*in5) == out5
    assert treino1.repete(*in6) == out6
    assert treino1.repete(*in7) == out7


def test_hacker():

    in1 = [
        ("****1234********", "maria@mail.pt"),
        ("0000************", "ze@gmail.com"),
        ("****1111****3333", "ze@gmail.com"),
    ]

    out1 = [("00001111****3333", "ze@gmail.com"),
            ("****1234********", "maria@mail.pt")]

    in2 = [("0000************", "ze@gmail.com"),
           ("****1234********", "maria@mail.pt")]

    out2 = [("****1234********", "maria@mail.pt"),
            ("0000************", "ze@gmail.com")]

    assert treino1.hacker(in1) == out1
    assert treino1.hacker(in2) == out2


def test_tabela():
    in0 = [
        ("A", 2, "B", 0),
        ("A", 1, "C", 0),
        ("B", 2, "C", 0),
        ("B", 1, "A", 0),
        ("C", 2, "A", 0),
        ("C", 1, "B", 0),
    ]

    out0 = [("A", 6), ("B", 6), ("C", 6)]

    in1 = [
        ("Benfica", 3, "Porto", 2),
        ("Benfica", 0, "Sporting", 0),
        ("Porto", 4, "Benfica", 1),
        ("Sporting", 2, "Porto", 2),
    ]

    out1 = [("Porto", 4), ("Benfica", 4), ("Sporting", 2)]

    in2 = [
        ("Benfica", 3, "Porto", 2),
        ("Benfica", 0, "Sporting", 0),
        ("Porto", 2, "Benfica", 1),
        ("Sporting", 2, "Porto", 2),
    ]

    out2 = [("Benfica", 4), ("Porto", 4), ("Sporting", 2)]

    assert treino1.tabela(in0) == out0
    assert treino1.tabela(in1) == out1
    assert treino1.tabela(in2) == out2


def test_isbn():
    in1 = {
        "Todos os nomes": "9789720047572",
        "Ensaio sobre a cegueira": "9789896604011",
        "Memorial do convento": "9789720046711",
        "Os cus de Judas": "9789722036757",
    }
    out1 = ["Memorial do convento", "Todos os nomes"]
    in2 = {"Ola mundo": "0000000000001"}
    out2 = ["Ola mundo"]

    assert treino1.isbn(in1) == out1
    assert treino1.isbn(in2) == out2


def test_robot():
    in1 = "EEAADAAAAAADAAAADDDAAAHAAAH"
    out1 = [(-9, -2, 0, 2), (0, 0, 0, 3)]
    in2 = "H"
    out2 = [(0, 0, 0, 0)]

    assert treino1.robot(in1) == out1
    assert treino1.robot(in2) == out2


def test():
    test_aloca()
    test_cruzamentos()
    test_factoriza()
    test_frequencia()
    test_hacker()
    test_isbn()
    test_repete()
    test_tabela()
    test_robot()


test()
