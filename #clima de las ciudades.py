#clima de las ciudades
temperaturas = [
    [   # Loja
        [   # Semana 1
            {"día": "Lunes", "temp": 3},
            {"día": "Martes", "temp": 12},
            {"día": "Miércoles", "temp": -5},
            {"día": "Jueves", "temp": 27},
            {"día": "Viernes", "temp": 0},
            {"día": "Sábado", "temp": 18},
            {"día": "Domingo", "temp": 8}
        ],
        [   # Semana 2
            {"día": "Lunes", "temp": -2},
            {"día": "Martes", "temp": 21},
            {"día": "Miércoles", "temp": 15},
            {"día": "Jueves", "temp": 5},
            {"día": "Viernes", "temp": -7},
            {"día": "Sábado", "temp": 32},
            {"día": "Domingo", "temp": 14}
        ],
        [   # Semana 3
            {"día": "Lunes", "temp": 10},
            {"día": "Martes", "temp": -12},
            {"día": "Miércoles", "temp": 25},
            {"día": "Jueves", "temp": 6},
            {"día": "Viernes", "temp": 30},
            {"día": "Sábado", "temp": -1},
            {"día": "Domingo", "temp": 22}
        ],
        [   # Semana 4
            {"día": "Lunes", "temp": 11},
            {"día": "Martes", "temp": 4},
            {"día": "Miércoles", "temp": -4},
            {"día": "Jueves", "temp": 28},
            {"día": "Viernes", "temp": 7},
            {"día": "Sábado", "temp": 19},
            {"día": "Domingo", "temp": 9}
        ]
    ],
    [   # Imbabura
        [   # Semana 1
            {"día": "Lunes", "temp": 2},
            {"día": "Martes", "temp": 16},
            {"día": "Miércoles", "temp": 33},
            {"día": "Jueves", "temp": -6},
            {"día": "Viernes", "temp": 9},
            {"día": "Sábado", "temp": 20},
            {"día": "Domingo", "temp": -3}
        ],
        [   # Semana 2
            {"día": "Lunes", "temp": 13},
            {"día": "Martes", "temp": 26},
            {"día": "Miércoles", "temp": 1},
            {"día": "Jueves", "temp": 24},
            {"día": "Viernes", "temp": -11},
            {"día": "Sábado", "temp": 17},
            {"día": "Domingo", "temp": 31}
        ],
        [   # Semana 3
            {"día": "Lunes", "temp": -10},
            {"día": "Martes", "temp": 23},
            {"día": "Miércoles", "temp": -9},
            {"día": "Jueves", "temp": -8},
            {"día": "Viernes", "temp": 34},
            {"día": "Sábado", "temp": 35},
            {"día": "Domingo", "temp": 15}
        ],
        [   # Semana 4
            {"día": "Lunes", "temp": 0},
            {"día": "Martes", "temp": 5},
            {"día": "Miércoles", "temp": 14},
            {"día": "Jueves", "temp": -2},
            {"día": "Viernes", "temp": 12},
            {"día": "Sábado", "temp": 7},
            {"día": "Domingo", "temp": 25}
        ]
    ],
    [   # Quito
        [   # Semana 1
            {"día": "Lunes", "temp": 3},
            {"día": "Martes", "temp": 10},
            {"día": "Miércoles", "temp": -6},
            {"día": "Jueves", "temp": 22},
            {"día": "Viernes", "temp": 18},
            {"día": "Sábado", "temp": -1},
            {"día": "Domingo", "temp": 8}
        ],
        [   # Semana 2
            {"día": "Lunes", "temp": 27},
            {"día": "Martes", "temp": 6},
            {"día": "Miércoles", "temp": 21},
            {"día": "Jueves", "temp": -4},
            {"día": "Viernes", "temp": 15},
            {"día": "Sábado", "temp": 2},
            {"día": "Domingo", "temp": 30}
        ],
        [   # Semana 3
            {"día": "Lunes", "temp": -9},
            {"día": "Martes", "temp": 9},
            {"día": "Miércoles", "temp": 19},
            {"día": "Jueves", "temp": -3},
            {"día": "Viernes", "temp": 11},
            {"día": "Sábado", "temp": 24},
            {"día": "Domingo", "temp": 1}
        ],
        [   # Semana 4
            {"día": "Lunes", "temp": 28},
            {"día": "Martes", "temp": -7},
            {"día": "Miércoles", "temp": 16},
            {"día": "Jueves", "temp": 4},
            {"día": "Viernes", "temp": 32},
            {"día": "Sábado", "temp": -12},
            {"día": "Domingo", "temp": 13}
        ]
    ]
]

# Calcular el promedio de temperaturas para cada ciudad y semana
ciudades = ["Loja", "Imababura", "Quito"]
for ciudad_idx, ciudad in enumerate(temperaturas):
    for semana_idx, semana in enumerate(ciudad):
        suma_temperaturas = sum([dia["temp"] for dia in semana])
        promedio = suma_temperaturas / len(semana)
        print(f"Promedio de temperaturas en {ciudades[ciudad_idx]}, Semana {semana_idx + 1}: {promedio:.2f} grados")