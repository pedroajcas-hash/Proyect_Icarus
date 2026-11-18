#!/usr/bin/env python3
"""Genera un PDF unificado con portadas, índices y guía de estudio."""

from __future__ import annotations

from pathlib import Path

from pypdf import PdfReader, PdfWriter
from reportlab.lib.colors import HexColor, white, black
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm, mm
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    PageTemplate,
    Paragraph,
    Spacer,
    PageBreak,
    KeepTogether,
    ListFlowable,
    ListItem,
    Table,
    TableStyle,
    HRFlowable,
)

UPLOADS = Path("/home/ubuntu/.cursor/projects/agent-repos-Proyect-Icarus/uploads")
OUT_DIR = Path(__file__).resolve().parent
OUT_PDF = OUT_DIR / "Computacion_Apuntes_Unificados.pdf"
GUIDE_PDF = OUT_DIR / "_guia_y_portadas.pdf"

# Colores (no purple / cream tropes)
NAVY = HexColor("#0B3A4A")
TEAL = HexColor("#1F7A6C")
SAND = HexColor("#F3F0E8")
INK = HexColor("#1A1A1A")
ACCENT = HexColor("#C45C26")
LIGHT = HexColor("#E8F2F0")
LINE = HexColor("#B8C5C2")

SOURCES = [
    {
        "key": "gen12",
        "title": "De la 1ª a la 2ª generación",
        "subtitle": "La era electrónica y el transistor (1940–1963)",
        "file": UPLOADS / "De_la_1__a_la_2__generaci_n_7aef.pdf",
        "color": HexColor("#0B3A4A"),
        "index": [
            (1, "1ª generación: válvulas de vacío y WWII"),
            (1, "Z3 (1941) — primer ordenador programable"),
            (2, "ABC (1942) — electrónica digital y memoria regenerativa"),
            (3, "Colossus (1943) — lógica y criptografía"),
            (3, "ENIAC (1943–1946) — cálculo masivo y cables"),
            (4, "Cuello de botella físico de la 1ª generación"),
            (5, "Arquitectura de Von Neumann (1945)"),
            (6, "Buses, cuello de botella y arquitectura Harvard"),
            (7, "Problemas de las válvulas de vacío"),
            (8, "2ª generación: el transistor (1956–1963)"),
            (9, "IBM 1401 y nacimiento del software moderno"),
            (10, "FORTRAN, COBOL y memoria de ferrita"),
            (11, "Batch processing y tiranía de los números"),
        ],
    },
    {
        "key": "gen36",
        "title": "De la 3ª a la 6ª generación",
        "subtitle": "Del chip a la inteligencia artificial (1964–hoy)",
        "file": UPLOADS / "De_la_3__a_la_6__generaci_n_0d2a.pdf",
        "color": HexColor("#1F7A6C"),
        "index": [
            (1, "3ª generación: circuito integrado y multitarea"),
            (2, "Entrada, SO, discos y monitores CRT"),
            (3, "RAM: de ferrita a DRAM Intel 1103"),
            (3, "Familia IBM System/360"),
            (4, "CDC 6600 y UNIVAC 1108"),
            (5, "PDP-8, System/370 y Apollo"),
            (6, "Transición a la 4ª: LSI/VLSI e Intel 4004"),
            (7, "4ª generación: microprocesador y PC"),
            (8, "Flujo de datos del PC y diagrama Von Neumann"),
            (9, "Trinidad de 1977, GUI y Macintosh"),
            (10, "Importancia de la 4ª generación"),
            (11, "5ª generación: GUI, Internet y redes"),
            (12, "Windows, SSD, nube y multimedia"),
            (13, "6ª generación: Big Data e IA"),
            (14, "CPU, GPU, NPU, IoT y nube"),
            (15, "Glosario"),
        ],
    },
    {
        "key": "hw",
        "title": "Fundamentos de Hardware",
        "subtitle": "Componentes físicos del ordenador",
        "file": UPLOADS / "Fundamentos_de_Hardware_1990.pdf",
        "color": HexColor("#8B4513"),
        "index": [
            (2, "Procesador (CPU): definición y características"),
            (3, "Mononúcleo vs multinúcleo y caché L1"),
            (4, "Caché L2/L3 y refrigeración"),
            (5, "Memoria RAM: definición y módulos DIMM/DDR"),
            (6, "Canales de memoria (single/dual/quad)"),
            (7, "Placa base, BIOS, zócalo y chipset"),
            (8, "Formatos ATX, microATX e ITX"),
            (10, "Conectores externos y USB"),
            (11, "Almacenamiento: HDD, óptico, flash"),
            (12, "Interfaces IDE/SATA/SCSI y partes del HDD"),
            (13, "SSD, ópticos y flash"),
            (14, "Tarjeta gráfica (GPU y VRAM)"),
            (15, "Tarjetas de sonido y de red"),
            (16, "Caja y fuente de alimentación"),
            (18, "Periféricos: monitor, teclado y ratón"),
        ],
    },
    {
        "key": "nieves",
        "title": "Computación — Nieves",
        "subtitle": "Sistemas de numeración, generaciones y hardware",
        "file": UPLOADS / "Computaci_n_-_Nieves_ad3f.pdf",
        "color": HexColor("#C45C26"),
        "index": [
            (1, "Sistemas decimal, binario y octal"),
            (2, "Hexadecimal y conversiones bin↔oct/hex"),
            (2, "1ª generación y primeros ordenadores"),
            (3, "Von Neumann, Harvard y válvulas"),
            (4, "2ª generación: transistor y software"),
            (5, "Batch processing y tiranía de los números"),
            (5, "3ª generación: chips y multitarea"),
            (6, "IBM 360, CDC 6600, PDP-8 e Intel 4004"),
            (6, "4ª generación: microprocesador y PC"),
            (7, "Trinidad de 1977 y GUI"),
            (7, "5ª generación: redes e interfaces"),
            (8, "6ª generación: Big Data e IA"),
            (8, "Impacto social de la tecnología"),
            (8, "Hardware: CPU, caché y refrigeración"),
            (10, "RAM, placa base y almacenamiento"),
            (12, "GPU, sonido, red, caja y fuente"),
            (13, "Periféricos básicos"),
        ],
    },
]


def make_styles():
    styles = getSampleStyleSheet()
    styles.add(
        ParagraphStyle(
            name="CoverTitle",
            fontName="Helvetica-Bold",
            fontSize=28,
            leading=34,
            textColor=white,
            alignment=TA_CENTER,
            spaceAfter=12,
        )
    )
    styles.add(
        ParagraphStyle(
            name="CoverSub",
            fontName="Helvetica",
            fontSize=14,
            leading=20,
            textColor=HexColor("#E8F2F0"),
            alignment=TA_CENTER,
            spaceAfter=8,
        )
    )
    styles.add(
        ParagraphStyle(
            name="H1",
            fontName="Helvetica-Bold",
            fontSize=18,
            leading=24,
            textColor=NAVY,
            spaceBefore=10,
            spaceAfter=8,
        )
    )
    styles.add(
        ParagraphStyle(
            name="H2",
            fontName="Helvetica-Bold",
            fontSize=14,
            leading=18,
            textColor=TEAL,
            spaceBefore=12,
            spaceAfter=6,
        )
    )
    styles.add(
        ParagraphStyle(
            name="H3",
            fontName="Helvetica-Bold",
            fontSize=12,
            leading=16,
            textColor=ACCENT,
            spaceBefore=10,
            spaceAfter=4,
        )
    )
    styles.add(
        ParagraphStyle(
            name="Body",
            fontName="Helvetica",
            fontSize=10.5,
            leading=15,
            textColor=INK,
            alignment=TA_JUSTIFY,
            spaceAfter=6,
        )
    )
    styles.add(
        ParagraphStyle(
            name="BulletBody",
            fontName="Helvetica",
            fontSize=10.5,
            leading=14,
            textColor=INK,
            leftIndent=8,
            spaceAfter=3,
        )
    )
    styles.add(
        ParagraphStyle(
            name="Trick",
            fontName="Helvetica-Oblique",
            fontSize=10.5,
            leading=14,
            textColor=NAVY,
            backColor=LIGHT,
            borderPadding=6,
            spaceBefore=4,
            spaceAfter=8,
        )
    )
    styles.add(
        ParagraphStyle(
            name="Mono",
            fontName="Courier",
            fontSize=10,
            leading=13,
            textColor=INK,
            leftIndent=10,
            spaceAfter=4,
        )
    )
    styles.add(
        ParagraphStyle(
            name="IndexItem",
            fontName="Helvetica",
            fontSize=11,
            leading=16,
            textColor=INK,
            spaceAfter=4,
        )
    )
    styles.add(
        ParagraphStyle(
            name="Footer",
            fontName="Helvetica",
            fontSize=8,
            textColor=HexColor("#666666"),
            alignment=TA_CENTER,
        )
    )
    styles.add(
        ParagraphStyle(
            name="SmallCenter",
            fontName="Helvetica",
            fontSize=10,
            leading=13,
            textColor=HexColor("#444444"),
            alignment=TA_CENTER,
        )
    )
    return styles


STYLES = make_styles()


def draw_header_footer(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(LINE)
    canvas.setLineWidth(0.5)
    canvas.line(2 * cm, A4[1] - 1.4 * cm, A4[0] - 2 * cm, A4[1] - 1.4 * cm)
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(HexColor("#666666"))
    canvas.drawString(2 * cm, A4[1] - 1.2 * cm, "Apuntes unificados de Computación")
    canvas.drawRightString(A4[0] - 2 * cm, A4[1] - 1.2 * cm, "Guía de estudio")
    canvas.line(2 * cm, 1.4 * cm, A4[0] - 2 * cm, 1.4 * cm)
    canvas.drawCentredString(A4[0] / 2, 0.9 * cm, f"Página {doc.page}")
    canvas.restoreState()


def draw_cover_bg(canvas, color):
    canvas.saveState()
    canvas.setFillColor(color)
    canvas.rect(0, 0, A4[0], A4[1], fill=1, stroke=0)
    # atmospheric band
    canvas.setFillColor(HexColor("#000000"))
    canvas.setFillAlpha(0.12)
    canvas.rect(0, A4[1] * 0.55, A4[0], A4[1] * 0.45, fill=1, stroke=0)
    canvas.setFillAlpha(1)
    # accent bar
    canvas.setFillColor(ACCENT)
    canvas.rect(0, A4[1] * 0.42, A4[0], 8, fill=1, stroke=0)
    canvas.restoreState()


def build_guide_pdf() -> Path:
    doc = BaseDocTemplate(
        str(GUIDE_PDF),
        pagesize=A4,
        leftMargin=2 * cm,
        rightMargin=2 * cm,
        topMargin=2 * cm,
        bottomMargin=2 * cm,
    )
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="normal")
    doc.addPageTemplates(
        [
            PageTemplate(id="content", frames=[frame], onPage=draw_header_footer),
        ]
    )

    story = []

    # ---- Portada general (custom canvas page via flowables + spacer) ----
    # We'll generate covers separately with canvas for better control.
    # Here we only build the textual guide + index pages; covers appended first via merge.

    story.extend(build_master_index())
    story.append(PageBreak())
    story.extend(build_study_guide())

    # Section covers + indexes as separate pages with colored headers
    for src in SOURCES:
        story.append(PageBreak())
        story.extend(build_section_cover_flow(src))
        story.append(PageBreak())
        story.extend(build_section_index(src))

    doc.build(story)
    return GUIDE_PDF


def build_master_index():
    s = []
    s.append(Paragraph("Índice general", STYLES["H1"]))
    s.append(
        Paragraph(
            "Este documento une los 4 apuntes originales y añade una guía final "
            "para entender y memorizar todo el contenido con explicaciones simples, "
            "trucos y ejemplos paso a paso.",
            STYLES["Body"],
        )
    )
    s.append(Spacer(1, 8))
    items = [
        "<b>PARTE A — Documentos originales</b>",
        "1. De la 1ª a la 2ª generación (portada + índice + PDF original)",
        "2. De la 3ª a la 6ª generación (portada + índice + PDF original)",
        "3. Fundamentos de Hardware (portada + índice + PDF original)",
        "4. Computación — Nieves (portada + índice + PDF original)",
        "<b>PARTE B — Guía para tontos (al final del PDF)</b>",
        "5. Mapa mental: cómo recordar todo",
        "6. Generaciones 1ª–6ª explicadas fácil + trucos",
        "7. Sistemas de numeración (decimal, binario, octal, hex)",
        "8. Conversiones paso a paso (sobre todo decimal ↔ binario ↔ hex)",
        "9. Hardware explicado fácil + ejemplos",
        "10. Mini-cheat sheet final",
    ]
    for it in items:
        s.append(Paragraph("• " + it, STYLES["IndexItem"]))
    s.append(Spacer(1, 12))
    s.append(
        Paragraph(
            "<b>Truco general:</b> estudia en este orden: "
            "<i>generaciones → flujo de datos (E/P/A/S) → hardware → numeración</i>. "
            "Las generaciones te dan el “por qué”; el hardware el “qué piezas”; "
            "la numeración el “idioma de la máquina”.",
            STYLES["Trick"],
        )
    )
    return s


def build_section_cover_flow(src):
    # Textual section divider (actual colored covers created with canvas later)
    s = []
    s.append(Spacer(1, 4 * cm))
    s.append(Paragraph(f"PORTADA — {src['title']}", STYLES["H1"]))
    s.append(Paragraph(src["subtitle"], STYLES["Body"]))
    s.append(Spacer(1, 1 * cm))
    s.append(
        Paragraph(
            "A continuación: índice del documento y después las páginas originales.",
            STYLES["Body"],
        )
    )
    return s


def build_section_index(src):
    s = []
    s.append(Paragraph(f"Índice — {src['title']}", STYLES["H1"]))
    s.append(
        Paragraph(
            "Números de página referidos al PDF original (no a este documento unificado).",
            STYLES["SmallCenter"],
        )
    )
    s.append(Spacer(1, 8))
    data = [[Paragraph("<b>Pág.</b>", STYLES["IndexItem"]), Paragraph("<b>Contenido</b>", STYLES["IndexItem"])]]
    for page, title in src["index"]:
        data.append(
            [
                Paragraph(str(page), STYLES["IndexItem"]),
                Paragraph(title, STYLES["IndexItem"]),
            ]
        )
    table = Table(data, colWidths=[2.2 * cm, 14 * cm])
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), LIGHT),
                ("TEXTCOLOR", (0, 0), (-1, -1), INK),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("GRID", (0, 0), (-1, -1), 0.4, LINE),
                ("LEFTPADDING", (0, 0), (-1, -1), 6),
                ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                ("TOPPADDING", (0, 0), (-1, -1), 4),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1), [white, HexColor("#FAFAFA")]),
            ]
        )
    )
    s.append(table)
    return s


def p(text):
    return Paragraph(text, STYLES["Body"])


def h2(text):
    return Paragraph(text, STYLES["H2"])


def h3(text):
    return Paragraph(text, STYLES["H3"])


def trick(text):
    return Paragraph(f"<b>TRUCO:</b> {text}", STYLES["Trick"])


def mono(text):
    return Paragraph(text.replace(" ", "&nbsp;"), STYLES["Mono"])


def bullets(items):
    return [
        Paragraph(f"• {item}", STYLES["BulletBody"]) for item in items
    ]


def build_study_guide():
    s = []
    s.append(Paragraph("PARTE B — Guía para tontos: entender y recordar TODO", STYLES["H1"]))
    s.append(
        p(
            "Esta guía resume la información de los 4 PDFs con lenguaje simple. "
            "Primero te doy el mapa mental, luego cada tema con truco + explicación + ejemplos."
        )
    )

    # ========== MAPA MENTAL ==========
    s.append(h2("1. Mapa mental: 3 ideas para no perderte"))
    s.extend(
        bullets(
            [
                "<b>Historia</b> = generaciones 1ª→6ª (cómo evolucionó el ordenador).",
                "<b>Idioma</b> = sistemas de numeración (binario/octal/hex) porque la máquina solo entiende 0 y 1.",
                "<b>Piezas</b> = hardware (CPU, RAM, placa, disco, GPU, fuente, periféricos).",
            ]
        )
    )
    s.append(
        trick(
            "Recuerda el flujo de datos en 4 letras: <b>E-P-A-S</b> = "
            "<b>E</b>ntrada → <b>P</b>rocesamiento → <b>A</b>lmacenamiento → <b>S</b>alida. "
            "En cada generación cambia E-P-A-S."
        )
    )

    # ========== GENERACIONES ==========
    s.append(h2("2. Generaciones explicadas para tontos"))
    s.append(
        p(
            "Piensa en cada generación como “el material estrella” del ordenador. "
            "Cuando cambia el material, cambia todo lo demás."
        )
    )

    gens = [
        (
            "1ª (1940–1956) — Válvulas de vacío",
            "Como bombillas gigantes que encienden/apagan corriente muy rápido. "
            "Máquinas enormes, caras, se calientan y se funden.",
            "Válvula = bombilla inteligente. Muchas bombillas = mucho calor y averías.",
            [
                "Z3: relés + binario (Konrad Zuse).",
                "ABC: electrónica digital + memoria con condensadores (antepasado de la RAM).",
                "Colossus: puertas lógicas para descifrar mensajes (AND/OR/XOR).",
                "ENIAC: cálculo numérico; se programaba moviendo cables físicos.",
                "Von Neumann (1945): datos + programa en la misma memoria → base de los PC actuales.",
                "Harvard: dos memorias separadas (instrucciones / datos).",
            ],
        ),
        (
            "2ª (1956–1963) — Transistor",
            "El transistor es un interruptor minúsculo de silicio. Sustituye a las “bombillas”.",
            "Transistor = interruptor pequeño, frío y fiable.",
            [
                "IBM 1401: éxito comercial (empresas/bancos).",
                "Lenguajes: FORTRAN (ciencia), COBOL (empresas).",
                "Memoria de núcleos de ferrita (anillos magnéticos, no volátil).",
                "Batch processing: varios programas en cola sin intervención humana.",
                "Problema: “tiranía de los números” (demasiadas soldaduras/cables).",
            ],
        ),
        (
            "3ª (1964–1971) — Circuito integrado (chip)",
            "Meten cientos de transistores en una pastilla de silicio. Menos cables, más velocidad.",
            "Chip = ciudad de interruptores en una uña.",
            [
                "IBM System/360: familia compatible (mismo software en varios modelos).",
                "Multitarea / multiprogramación + sistemas operativos modernos.",
                "Discos magnéticos (acceso aleatorio) vs cintas (acceso secuencial).",
                "Teclado + monitores CRT.",
                "Intel 1103 (1970): DRAM comercial (volátil).",
                "CDC 6600, UNIVAC 1108, PDP-8.",
            ],
        ),
        (
            "4ª (1971–1981) — Microprocesador / PC",
            "Toda la CPU cabe en un chip. Nace el ordenador personal.",
            "Microprocesador = cerebro entero en un chip.",
            [
                "Intel 4004 (1971) inicia la generación.",
                "Altair 8800, Apple I/II, IBM PC, Trinidad 1977 (Apple II, TRS-80, PET).",
                "Disquete, MS-DOS, VisiCalc, WordStar.",
                "Xerox Alto y Macintosh popularizan ratón + GUI.",
            ],
        ),
        (
            "5ª (1982–2010) — GUI + Internet",
            "El ordenador se conecta al mundo y se usa con ventanas e iconos.",
            "5ª = pantallas bonitas + red global.",
            [
                "Windows / macOS, ratón, multimedia.",
                "CD/DVD, HDD→SSD, Wi-Fi, fibra, smartphones.",
                "Internet y WWW cambian comunicación, trabajo y ocio.",
            ],
        ),
        (
            "6ª (2010–hoy) — Big Data e IA",
            "Muchos núcleos, nube, sensores e inteligencia artificial.",
            "6ª = datos masivos + máquinas que aprenden.",
            [
                "CPU (general), GPU (paralelo/gráficos), NPU (IA).",
                "IoT, voz, VR/AR, vehículos autónomos, nube.",
                "Beneficios: acceso, eficiencia, automatización.",
                "Riesgos: brecha digital, empleo, dependencia/ciberseguridad.",
            ],
        ),
    ]

    for title, simple, tip, points in gens:
        s.append(h3(title))
        s.append(p(simple))
        s.append(trick(tip))
        s.extend(bullets(points))

    s.append(h3("Ejemplo paso a paso: E-P-A-S en 3 generaciones"))
    s.append(p("<b>Problema:</b> ¿cómo introduce, calcula, guarda y muestra datos cada generación?"))
    s.append(mono("2ª gen:  tarjeta perforada → transistor → cinta/ferrita → impresora"))
    s.append(mono("3ª gen:  teclado         → chip+SO   → disco duro  → monitor CRT"))
    s.append(mono("4ª gen:  teclado         → microCPU  → disquete    → monitor + impresora"))
    s.append(
        trick(
            "Si te preguntan “¿qué cambió en la generación X?”, responde siempre con E-P-A-S "
            "y el material estrella (válvula / transistor / chip / microprocesador / redes / IA)."
        )
    )

    s.append(h3("Tabla exprés de generaciones"))
    gen_table = Table(
        [
            [
                Paragraph("<b>Gen</b>", STYLES["BulletBody"]),
                Paragraph("<b>Material</b>", STYLES["BulletBody"]),
                Paragraph("<b>Idea clave</b>", STYLES["BulletBody"]),
            ],
            ["1ª", "Válvulas", "Cálculo electrónico + cables"],
            ["2ª", "Transistor", "Más fiable + software (FORTRAN/COBOL)"],
            ["3ª", "Chip IC", "Familia 360 + multitarea + discos"],
            ["4ª", "MicroCPU", "PC en casa"],
            ["5ª", "ULSI + red", "GUI + Internet"],
            ["6ª", "Multinúcleo", "Nube + Big Data + IA"],
        ],
        colWidths=[2 * cm, 3.5 * cm, 11 * cm],
    )
    gen_table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), LIGHT),
                ("GRID", (0, 0), (-1, -1), 0.4, LINE),
                ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),
                ("FONTSIZE", (0, 0), (-1, -1), 9),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("LEFTPADDING", (0, 0), (-1, -1), 5),
                ("TOPPADDING", (0, 0), (-1, -1), 4),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
            ]
        )
    )
    s.append(gen_table)

    # ========== VON NEUMANN ==========
    s.append(h2("3. Arquitectura Von Neumann vs Harvard (fácil)"))
    s.append(
        p(
            "<b>Von Neumann:</b> una sola memoria para datos e instrucciones. "
            "Es como una cocina con un solo pasillo: comida y recetas pasan por el mismo sitio "
            "(cuello de botella). Se mitiga con caché."
        )
    )
    s.append(
        p(
            "<b>Harvard:</b> dos memorias (y buses) separados para datos e instrucciones. "
            "Dos pasillos: más rápido, más caro/complejo."
        )
    )
    s.append(
        trick(
            "Hoy: híbrido. Memoria principal tipo Von Neumann; cachés internas tipo Harvard."
        )
    )
    s.append(h3("Ejemplo: ejecutar “suma 3+5” en Von Neumann"))
    s.extend(
        bullets(
            [
                "1. La instrucción “SUMAR” está en RAM.",
                "2. La UC la lee por el bus.",
                "3. La ALU suma 3+5 = 8.",
                "4. El 8 se guarda otra vez en RAM por el mismo bus.",
                "5. Mientras viaja una cosa, la otra espera → cuello de botella.",
            ]
        )
    )

    # ========== NUMERACIÓN ==========
    s.append(PageBreak())
    s.append(h2("4. Sistemas de numeración (explicación para tontos)"))
    s.append(
        p(
            "Un sistema de numeración es un “alfabeto de números”. "
            "Son <b>posicionales</b>: el valor de una cifra depende de su sitio "
            "(como las unidades, decenas y centenas, pero con otra base)."
        )
    )
    s.append(
        trick(
            "Fórmula universal: valor = dígito × base^posición (posiciones desde la derecha, empezando en 0)."
        )
    )

    s.append(h3("4.1 Decimal (base 10) — el de siempre"))
    s.append(p("Dígitos: 0–9. Ejemplo: 253 = 2×100 + 5×10 + 3×1."))
    s.append(mono("253 = 2×10² + 5×10¹ + 3×10⁰"))

    s.append(h3("4.2 Binario (base 2) — el idioma de la máquina"))
    s.append(p("Solo 0 y 1 (bits). Cada posición vale el doble que la de la derecha: 1, 2, 4, 8, 16, 32, 64, 128…"))
    s.append(
        trick(
            "Aprende de memoria las potencias de 2 hasta 256: "
            "1, 2, 4, 8, 16, 32, 64, 128, 256. Con eso haces casi todo a ojo."
        )
    )
    s.append(p("Con n bits: hay 2ⁿ números posibles; el máximo es 2ⁿ−1. Ejemplo: 8 bits → 256 valores (0–255)."))

    s.append(h3("4.3 Octal (base 8) — atajo del binario"))
    s.append(p("Dígitos 0–7. Cada cifra octal = 3 bits. Sirve para acortar binarios."))
    s.append(trick("Agrupa bits de 3 en 3 desde la derecha → octal."))

    s.append(h3("4.4 Hexadecimal (base 16) — el favorito de la informática"))
    s.append(p("Dígitos 0–9 y letras A=10, B=11, C=12, D=13, E=14, F=15. Cada cifra hex = 4 bits (un nibble)."))
    s.append(
        trick(
            "Tabla mágica 0–F en 4 bits: "
            "0=0000, 1=0001, 2=0010, 3=0011, 4=0100, 5=0101, 6=0110, 7=0111, "
            "8=1000, 9=1001, A=1010, B=1011, C=1100, D=1101, E=1110, F=1111."
        )
    )

    # ========== CONVERSIONES ==========
    s.append(h2("5. Conversiones paso a paso (lo más importante)"))

    s.append(h3("5.1 Decimal → Binario (divisiones entre 2)"))
    s.append(
        p(
            "<b>Método:</b> divide el número entre 2 una y otra vez. "
            "Anota el resto (0 o 1). Cuando llegues a cociente 0, lee los restos "
            "<b>de abajo hacia arriba</b>."
        )
    )
    s.append(trick("Los restos son los bits. El primer resto es el bit menos significativo (derecha)."))

    s.append(p("<b>Ejemplo A:</b> convertir <b>13</b> a binario"))
    s.append(mono("13 ÷ 2 = 6  resto 1"))
    s.append(mono(" 6 ÷ 2 = 3  resto 0"))
    s.append(mono(" 3 ÷ 2 = 1  resto 1"))
    s.append(mono(" 1 ÷ 2 = 0  resto 1"))
    s.append(p("Leemos restos de abajo a arriba → <b>1101₂</b>"))
    s.append(p("Comprobación: 1×8 + 1×4 + 0×2 + 1×1 = 8+4+1 = 13. Correcto."))

    s.append(p("<b>Ejemplo B (más grande):</b> convertir <b>156</b> a binario"))
    s.append(mono("156 ÷ 2 = 78  resto 0"))
    s.append(mono(" 78 ÷ 2 = 39  resto 0"))
    s.append(mono(" 39 ÷ 2 = 19  resto 1"))
    s.append(mono(" 19 ÷ 2 =  9  resto 1"))
    s.append(mono("  9 ÷ 2 =  4  resto 1"))
    s.append(mono("  4 ÷ 2 =  2  resto 0"))
    s.append(mono("  2 ÷ 2 =  1  resto 0"))
    s.append(mono("  1 ÷ 2 =  0  resto 1"))
    s.append(p("Resultado: <b>10011100₂</b>"))
    s.append(
        p(
            "Comprobación con potencias: 128+0+0+16+8+4+0+0 = 156. "
            "(bits: 1 0 0 1 1 1 0 0 → 128+16+8+4)"
        )
    )

    s.append(p("<b>Método alternativo (resta de potencias)</b> para 156:"))
    s.extend(
        bullets(
            [
                "Mayor potencia ≤ 156 → 128 → bit 1. Queda 156−128=28.",
                "64 > 28 → bit 0. 32 > 28 → bit 0.",
                "16 ≤ 28 → bit 1. Queda 12.",
                "8 ≤ 12 → bit 1. Queda 4.",
                "4 ≤ 4 → bit 1. Queda 0.",
                "2 y 1 → bits 0 0.",
                "Misma respuesta: 10011100₂.",
            ]
        )
    )

    s.append(h3("5.2 Binario → Decimal (suma de potencias)"))
    s.append(p("<b>Método:</b> escribe debajo de cada bit su peso (1,2,4,8…) desde la derecha y suma donde haya 1."))
    s.append(p("<b>Ejemplo:</b> 101101₂"))
    s.append(mono("bits:     1  0  1  1  0  1"))
    s.append(mono("pesos:   32 16  8  4  2  1"))
    s.append(p("Suma: 32 + 8 + 4 + 1 = <b>45₁₀</b>"))

    s.append(h3("5.3 Decimal → Hexadecimal (divisiones entre 16)"))
    s.append(
        p(
            "<b>Método:</b> igual que al binario, pero divides entre 16. "
            "Si el resto es 10–15, escribe A–F."
        )
    )
    s.append(trick("10=A, 11=B, 12=C, 13=D, 14=E, 15=F. Memorízalo como “A de once… no: A=10”."))

    s.append(p("<b>Ejemplo A:</b> 156 a hexadecimal"))
    s.append(mono("156 ÷ 16 = 9  resto 12 → C"))
    s.append(mono("  9 ÷ 16 = 0  resto 9  → 9"))
    s.append(p("De abajo a arriba → <b>9C₁₆</b>"))
    s.append(p("Comprobación: 9×16 + 12 = 144 + 12 = 156."))

    s.append(p("<b>Ejemplo B:</b> 255 a hexadecimal"))
    s.append(mono("255 ÷ 16 = 15 resto 15 → F"))
    s.append(mono(" 15 ÷ 16 =  0 resto 15 → F"))
    s.append(p("Resultado: <b>FF₁₆</b> (el máximo de 1 byte)."))

    s.append(p("<b>Ejemplo C:</b> 4095 a hexadecimal"))
    s.append(mono("4095 ÷ 16 = 255 resto 15 → F"))
    s.append(mono(" 255 ÷ 16 =  15 resto 15 → F"))
    s.append(mono("  15 ÷ 16 =   0 resto 15 → F"))
    s.append(p("Resultado: <b>FFF₁₆</b>"))

    s.append(h3("5.4 Hexadecimal → Decimal"))
    s.append(p("<b>Ejemplo:</b> 2F₁₆"))
    s.append(mono("2F = 2×16¹ + 15×16⁰ = 32 + 15 = 47₁₀"))
    s.append(p("<b>Ejemplo:</b> A3₁₆"))
    s.append(mono("A3 = 10×16 + 3 = 160 + 3 = 163₁₀"))

    s.append(h3("5.5 Binario ↔ Hexadecimal (el atajo estrella)"))
    s.append(
        p(
            "Como 16 = 2⁴, <b>cada dígito hex = exactamente 4 bits</b>. "
            "No hace falta pasar por decimal."
        )
    )
    s.append(
        trick(
            "De binario a hex: agrupa de 4 en 4 desde la derecha (completa con ceros a la izquierda). "
            "De hex a binario: sustituye cada símbolo por sus 4 bits."
        )
    )

    s.append(p("<b>Ejemplo: binario → hex</b> — 10011100₂"))
    s.append(mono("1001 1100"))
    s.append(mono("1001 = 9"))
    s.append(mono("1100 = 12 = C"))
    s.append(p("Resultado: <b>9C₁₆</b> (coincide con el ejemplo decimal 156)."))

    s.append(p("<b>Ejemplo: hex → binario</b> — 3FA₁₆"))
    s.append(mono("3 = 0011"))
    s.append(mono("F = 1111"))
    s.append(mono("A = 1010"))
    s.append(p("Resultado: <b>0011 1111 1010₂</b> (o 1111111010₂ sin ceros iniciales)."))

    s.append(h3("5.6 Binario ↔ Octal"))
    s.append(p("Igual que hex, pero grupos de <b>3 bits</b> (porque 8=2³)."))
    s.append(p("<b>Ejemplo:</b> 10011100₂ → octal"))
    s.append(mono("010 011 100   (añadimos un 0 a la izquierda)"))
    s.append(mono(" 2   3   4"))
    s.append(p("Resultado: <b>234₈</b>"))
    s.append(p("Comprobación: 2×64 + 3×8 + 4 = 128 + 24 + 4 = 156."))

    s.append(h3("5.7 Decimal → Octal"))
    s.append(p("<b>Ejemplo:</b> 156 a octal"))
    s.append(mono("156 ÷ 8 = 19 resto 4"))
    s.append(mono(" 19 ÷ 8 =  2 resto 3"))
    s.append(mono("  2 ÷ 8 =  0 resto 2"))
    s.append(p("Resultado: <b>234₈</b>"))

    s.append(h3("Ruta recomendada en un examen"))
    s.extend(
        bullets(
            [
                "¿Decimal ↔ binario? → divisiones / potencias de 2.",
                "¿Decimal ↔ hex? → divisiones entre 16 (o pasa a binario y agrupa de 4).",
                "¿Binario ↔ hex/octal? → agrupación 4 o 3 bits (más rápido y menos errores).",
                "Siempre comprueba reconvirtiendo al final.",
            ]
        )
    )

    # Más ejemplos prácticos
    s.append(PageBreak())
    s.append(h2("6. Más ejemplos guiados (práctica)"))

    s.append(h3("Ejemplo completo 1: 42 en todas las bases"))
    s.append(p("<b>Decimal → binario</b>"))
    s.append(mono("42÷2=21 r0 | 21÷2=10 r1 | 10÷2=5 r0 | 5÷2=2 r1 | 2÷2=1 r0 | 1÷2=0 r1"))
    s.append(p("→ <b>101010₂</b> (32+8+2=42)"))
    s.append(p("<b>Decimal → hex</b>"))
    s.append(mono("42÷16=2 r10→A | 2÷16=0 r2 → 2A₁₆"))
    s.append(p("<b>Binario → hex</b> (atajo): 0010 1010 → 2 A → 2A₁₆"))
    s.append(p("<b>Decimal → octal</b>: 42÷8=5 r2; 5÷8=0 r5 → <b>52₈</b>"))

    s.append(h3("Ejemplo completo 2: color web #FF8800"))
    s.append(
        p(
            "En diseño web, los colores RGB se escriben en hex. "
            "FF=255 (rojo máximo), 88=8×16+8=136 (verde), 00=0 (azul)."
        )
    )
    s.append(mono("F=1111 → FF = 1111 1111₂ = 255"))
    s.append(mono("8=1000 → 88 = 1000 1000₂ = 136"))
    s.append(p("Así ves por qué hex es práctico: 2 dígitos = 1 byte exacto."))

    s.append(h3("Ejemplo completo 3: de hex a decimal grande — BEEF₁₆"))
    s.append(mono("B=11, E=14, E=14, F=15"))
    s.append(mono("11×16³ + 14×16² + 14×16¹ + 15×16⁰"))
    s.append(mono("11×4096 + 14×256 + 14×16 + 15"))
    s.append(mono("45056 + 3584 + 224 + 15 = 48879₁₀"))

    # ========== HARDWARE ==========
    s.append(h2("7. Hardware explicado fácil"))
    s.append(
        trick(
            "Imagina el PC como una oficina: "
            "CPU=jefe que decide, RAM=mesa de trabajo, disco=archivador, "
            "placa=suelo con cables, GPU=artista, fuente=electricidad, "
            "monitor/teclado/ratón=ventanilla de atención."
        )
    )

    hw_points = [
        (
            "CPU (procesador)",
            "Cerebro: descodifica y ejecuta instrucciones; coordina el resto. "
            "GHz = ritmo del reloj (no es lo único que importa). "
            "nm = tamaño del transistor (más pequeño → más en el chip). "
            "TDP = calor a disipar. Multinúcleo = varios “cerebros” en uno. "
            "Caché L1/L2/L3 = notas adhesivas súper rápidas cerca del jefe.",
        ),
        (
            "RAM",
            "Mesa de trabajo volátil: al apagar, se borra. Acceso aleatorio. "
            "Módulos DIMM DDR/DDR2/DDR3/DDR4 (no intercambiables). "
            "Dual/Quad channel = varios pasillos a la mesa a la vez.",
        ),
        (
            "Placa base",
            "El tablero donde enchufas todo. BIOS/UEFI arranca y reconoce piezas. "
            "Zócalo LGA/ZIF para la CPU. Chipset gestiona el tráfico "
            "(antes northbridge/southbridge). Formatos: ATX, microATX, ITX.",
        ),
        (
            "Almacenamiento",
            "Archivador permanente (no volátil). HDD magnético (platos/pistas/sectores), "
            "óptico (CD/DVD/Blu-ray), flash (SSD/pendrive). "
            "Interfaces: IDE (viejo), SATA (común), SCSI (servidores). "
            "SSD más rápido y silencioso; HDD más €/GB.",
        ),
        (
            "Tarjeta gráfica",
            "GPU = cálculos en paralelo para imágenes. VRAM propia si es dedicada. "
            "Conexión moderna: PCIe x16. Salidas: HDMI, DisplayPort (VGA/DVI antiguas).",
        ),
        (
            "Sonido y red",
            "Sonido: verde=altavoces, rosa=mic, azul=line-in, etc. "
            "Red (NIC): Ethernet RJ-45 o Wi-Fi; cada tarjeta tiene MAC única de 48 bits.",
        ),
        (
            "Caja y fuente",
            "Fuente: 220 V AC → voltajes DC bajos. Conectores ATX 24pin, EPS CPU, "
            "PCIe GPU, SATA, Molex. PFC mejora eficiencia. Modulares = menos cables.",
        ),
        (
            "Periféricos",
            "Monitor: pulgadas, 16:9, resolución, Hz, LCD/LED/OLED. "
            "Teclado: matriz de contactos. Ratón: óptico/láser; en portátil touchpad.",
        ),
    ]
    for title, text in hw_points:
        s.append(h3(title))
        s.append(p(text))

    s.append(h3("Ejemplo paso a paso: ¿qué pasa al abrir un PDF?"))
    s.extend(
        bullets(
            [
                "1. Disco (SSD/HDD) tiene el archivo guardado.",
                "2. Se copia a RAM (mesa de trabajo).",
                "3. CPU ejecuta el programa lector.",
                "4. GPU prepara los píxeles de las páginas.",
                "5. Monitor (salida) te muestra el documento.",
                "6. Teclado/ratón (entrada) te dejan hacer scroll.",
            ]
        )
    )

    # ========== CHEAT SHEET ==========
    s.append(h2("8. Mini-cheat sheet para memorizar en 5 minutos"))
    s.extend(
        bullets(
            [
                "Generaciones: Válvula → Transistor → Chip → MicroCPU → Internet/GUI → IA/Nube.",
                "E-P-A-S cambia en cada generación.",
                "Von Neumann = memoria compartida; Harvard = separada.",
                "Binario: ÷2 y restos abajo→arriba; o restar potencias de 2.",
                "Hex: ÷16; A–F = 10–15; 1 hex = 4 bits.",
                "Octal: 1 octal = 3 bits.",
                "Hardware: CPU piensa, RAM trabaja, disco guarda, placa conecta, fuente alimenta.",
                "Caché: L1 más rápida/pequeña; L3 más grande/lenta.",
                "RAM volátil; SSD/HDD no volátiles.",
            ]
        )
    )

    s.append(Spacer(1, 10))
    s.append(
        Paragraph(
            "Fin de la guía. Los documentos originales están incluidos antes de esta sección "
            "en el PDF unificado, cada uno con su portada e índice.",
            STYLES["SmallCenter"],
        )
    )
    return s


def make_colored_cover(path: Path, title: str, subtitle: str, color, badge: str):
    from reportlab.pdfgen import canvas as pdfcanvas

    c = pdfcanvas.Canvas(str(path), pagesize=A4)
    draw_cover_bg(c, color)
    c.setFillColor(white)
    c.setFont("Helvetica", 12)
    c.drawCentredString(A4[0] / 2, A4[1] - 3 * cm, badge)
    c.setFont("Helvetica-Bold", 26)
    # wrap title roughly
    y = A4[1] * 0.62
    for line in _wrap(title, 28):
        c.drawCentredString(A4[0] / 2, y, line)
        y -= 32
    c.setFont("Helvetica", 13)
    c.setFillColor(HexColor("#E8F2F0"))
    y -= 10
    for line in _wrap(subtitle, 50):
        c.drawCentredString(A4[0] / 2, y, line)
        y -= 18
    c.setFillColor(white)
    c.setFont("Helvetica", 11)
    c.drawCentredString(A4[0] / 2, 3.2 * cm, "Apuntes unificados de Computación")
    c.drawCentredString(A4[0] / 2, 2.5 * cm, "Portada de sección · incluye índice propio")
    c.showPage()
    c.save()


def make_main_cover(path: Path):
    from reportlab.pdfgen import canvas as pdfcanvas

    c = pdfcanvas.Canvas(str(path), pagesize=A4)
    draw_cover_bg(c, NAVY)
    c.setFillColor(white)
    c.setFont("Helvetica", 12)
    c.drawCentredString(A4[0] / 2, A4[1] - 3 * cm, "COMPUTACIÓN · DOCUMENTO ÚNICO")
    c.setFont("Helvetica-Bold", 30)
    y = A4[1] * 0.60
    for line in ["Apuntes unificados", "de Computación"]:
        c.drawCentredString(A4[0] / 2, y, line)
        y -= 36
    c.setFont("Helvetica", 12)
    c.setFillColor(HexColor("#E8F2F0"))
    y -= 8
    lines = [
        "1ª–2ª generación  ·  3ª–6ª generación",
        "Fundamentos de Hardware  ·  Computación Nieves",
        "",
        "Incluye: portada e índice por documento",
        "Guía simple con trucos y ejemplos paso a paso",
        "(especial énfasis decimal ↔ binario ↔ hexadecimal)",
    ]
    for line in lines:
        c.drawCentredString(A4[0] / 2, y, line)
        y -= 18
    c.setFillColor(white)
    c.setFont("Helvetica", 10)
    c.drawCentredString(A4[0] / 2, 2.8 * cm, "Material de estudio · explicación clara + práctica")
    c.showPage()
    c.save()


def make_guide_cover(path: Path):
    from reportlab.pdfgen import canvas as pdfcanvas

    c = pdfcanvas.Canvas(str(path), pagesize=A4)
    draw_cover_bg(c, TEAL)
    c.setFillColor(white)
    c.setFont("Helvetica", 12)
    c.drawCentredString(A4[0] / 2, A4[1] - 3 * cm, "PARTE B")
    c.setFont("Helvetica-Bold", 26)
    y = A4[1] * 0.60
    for line in ["Guía para tontos:", "trucos, explicación", "simple y ejemplos"]:
        c.drawCentredString(A4[0] / 2, y, line)
        y -= 34
    c.setFont("Helvetica", 12)
    c.setFillColor(HexColor("#E8F2F0"))
    y -= 10
    for line in [
        "Resumen de los 4 documentos",
        "Trucos de memoria por tema",
        "Conversiones decimal / binario / hex paso a paso",
    ]:
        c.drawCentredString(A4[0] / 2, y, line)
        y -= 18
    c.showPage()
    c.save()


def _wrap(text: str, width: int):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if len(trial) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines or [text]


def make_index_pdf(path: Path, src: dict):
    """Standalone index pages for a source PDF."""
    doc = BaseDocTemplate(
        str(path),
        pagesize=A4,
        leftMargin=2 * cm,
        rightMargin=2 * cm,
        topMargin=2 * cm,
        bottomMargin=2 * cm,
    )
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="normal")
    doc.addPageTemplates([PageTemplate(id="content", frames=[frame], onPage=draw_header_footer)])
    story = build_section_index(src)
    doc.build(story)


def append_pdf(writer: PdfWriter, path: Path):
    reader = PdfReader(str(path))
    for page in reader.pages:
        writer.add_page(page)


def main():
    tmp = OUT_DIR / "_tmp_parts"
    tmp.mkdir(exist_ok=True)

    # Covers
    main_cover = tmp / "main_cover.pdf"
    guide_cover = tmp / "guide_cover.pdf"
    make_main_cover(main_cover)
    make_guide_cover(guide_cover)

    section_covers = {}
    section_indexes = {}
    for src in SOURCES:
        cpath = tmp / f"cover_{src['key']}.pdf"
        ipath = tmp / f"index_{src['key']}.pdf"
        make_colored_cover(
            cpath,
            src["title"],
            src["subtitle"],
            src["color"],
            "DOCUMENTO ORIGINAL",
        )
        make_index_pdf(ipath, src)
        section_covers[src["key"]] = cpath
        section_indexes[src["key"]] = ipath

    # Study guide body (without the duplicated section covers/indexes)
    guide_body = tmp / "guide_body.pdf"
    doc = BaseDocTemplate(
        str(guide_body),
        pagesize=A4,
        leftMargin=2 * cm,
        rightMargin=2 * cm,
        topMargin=2.2 * cm,
        bottomMargin=2 * cm,
    )
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="normal")
    doc.addPageTemplates([PageTemplate(id="content", frames=[frame], onPage=draw_header_footer)])
    story = []
    story.extend(build_master_index())
    story.append(PageBreak())
    story.extend(build_study_guide())
    doc.build(story)

    # Merge final
    writer = PdfWriter()
    append_pdf(writer, main_cover)
    # master index is first pages of guide_body — we'll split: put index after cover,
    # originals in middle, then guide cover + rest.

    guide_reader = PdfReader(str(guide_body))
    # Page 0 of guide_body is master index (may be 1 page). Detect by building: master index is short.
    # We put: main cover, master index pages until "PARTE B", then sections, then guide.
    # Simpler approach: rebuild two small PDFs.
    master_index_pdf = tmp / "master_index.pdf"
    doc2 = BaseDocTemplate(
        str(master_index_pdf),
        pagesize=A4,
        leftMargin=2 * cm,
        rightMargin=2 * cm,
        topMargin=2.2 * cm,
        bottomMargin=2 * cm,
    )
    frame2 = Frame(doc2.leftMargin, doc2.bottomMargin, doc2.width, doc2.height, id="normal")
    doc2.addPageTemplates([PageTemplate(id="content", frames=[frame2], onPage=draw_header_footer)])
    doc2.build(build_master_index())

    guide_only = tmp / "guide_only.pdf"
    doc3 = BaseDocTemplate(
        str(guide_only),
        pagesize=A4,
        leftMargin=2 * cm,
        rightMargin=2 * cm,
        topMargin=2.2 * cm,
        bottomMargin=2 * cm,
    )
    frame3 = Frame(doc3.leftMargin, doc3.bottomMargin, doc3.width, doc3.height, id="normal")
    doc3.addPageTemplates([PageTemplate(id="content", frames=[frame3], onPage=draw_header_footer)])
    doc3.build(build_study_guide())

    writer = PdfWriter()
    append_pdf(writer, main_cover)
    append_pdf(writer, master_index_pdf)

    for src in SOURCES:
        append_pdf(writer, section_covers[src["key"]])
        append_pdf(writer, section_indexes[src["key"]])
        append_pdf(writer, src["file"])

    append_pdf(writer, guide_cover)
    append_pdf(writer, guide_only)

    writer.add_metadata(
        {
            "/Title": "Apuntes unificados de Computación",
            "/Author": "Apuntes de estudio",
            "/Subject": "Generaciones, hardware y sistemas de numeración",
        }
    )
    with open(OUT_PDF, "wb") as f:
        writer.write(f)

    # cleanup temp textual helpers left around
    for p in [GUIDE_PDF]:
        if p.exists():
            p.unlink()

    n = len(writer.pages)
    print(f"OK -> {OUT_PDF} ({n} pages)")


if __name__ == "__main__":
    main()
