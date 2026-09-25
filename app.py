import streamlit as st
import streamlit.components.v1 as components
import math
import random

# =========================================================
# PAGE SETUP
# =========================================================

st.set_page_config(
    page_title="F1 Student Hub",
    page_icon="🏎️",
    layout="centered"
)

# =========================================================
# F1 BACKGROUND
# =========================================================

st.markdown("""
<style>

.stApp {
    background:
        radial-gradient(
            circle at 50% 15%,
            #1a1a1a 0%,
            #0d0d0d 45%,
            #030303 100%
        );
}

/* NEON CITY GRID FLOOR */

.neon-grid {
    position: fixed;
    bottom: 0;
    left: 0;
    width: 100%;
    height: 32%;
    z-index: 0;
    pointer-events: none;
    opacity: 0.22;

    background-image:
        linear-gradient(rgba(225, 6, 0, 0.6) 1px, transparent 1px),
        linear-gradient(90deg, rgba(255, 255, 255, 0.35) 1px, transparent 1px);

    background-size: 42px 42px;

    transform: perspective(220px) rotateX(58deg);
    transform-origin: bottom;

    mask-image: linear-gradient(to top, black 0%, transparent 90%);
    -webkit-mask-image: linear-gradient(to top, black 0%, transparent 90%);
}

/* NEON CITY SKYLINE SILHOUETTE */

.neon-skyline {
    position: fixed;
    bottom: 0;
    left: 0;
    width: 100%;
    height: 20%;
    z-index: 0;
    pointer-events: none;
    opacity: 0.55;

    background-repeat: repeat-x;
    background-position: bottom;
    background-size: 768px 100%;

    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 768 260'%3E%3Crect x='0' y='170' width='50' height='90' fill='%23000000' opacity='0.7'/%3E%3Crect x='64' y='110' width='50' height='150' fill='%23000000' opacity='0.7'/%3E%3Crect x='128' y='190' width='50' height='70' fill='%23000000' opacity='0.7'/%3E%3Crect x='192' y='80' width='50' height='180' fill='%23000000' opacity='0.7'/%3E%3Crect x='256' y='140' width='50' height='120' fill='%23000000' opacity='0.7'/%3E%3Crect x='320' y='60' width='50' height='200' fill='%23000000' opacity='0.7'/%3E%3Crect x='384' y='170' width='50' height='90' fill='%23000000' opacity='0.7'/%3E%3Crect x='448' y='100' width='50' height='160' fill='%23000000' opacity='0.7'/%3E%3Crect x='512' y='150' width='50' height='110' fill='%23000000' opacity='0.7'/%3E%3Crect x='576' y='80' width='50' height='180' fill='%23000000' opacity='0.7'/%3E%3Crect x='640' y='160' width='50' height='100' fill='%23000000' opacity='0.7'/%3E%3Crect x='704' y='110' width='50' height='150' fill='%23000000' opacity='0.7'/%3E%3Crect x='78' y='130' width='4' height='6' fill='%23e10600' opacity='0.6'/%3E%3Crect x='78' y='160' width='4' height='6' fill='%23ffffff' opacity='0.35'/%3E%3Crect x='100' y='140' width='4' height='6' fill='%23e10600' opacity='0.5'/%3E%3Crect x='206' y='100' width='4' height='6' fill='%23ffffff' opacity='0.4'/%3E%3Crect x='206' y='130' width='4' height='6' fill='%23e10600' opacity='0.6'/%3E%3Crect x='228' y='110' width='4' height='6' fill='%23e10600' opacity='0.5'/%3E%3Crect x='334' y='80' width='4' height='6' fill='%23e10600' opacity='0.6'/%3E%3Crect x='334' y='110' width='4' height='6' fill='%23ffffff' opacity='0.35'/%3E%3Crect x='356' y='95' width='4' height='6' fill='%23e10600' opacity='0.5'/%3E%3Crect x='356' y='140' width='4' height='6' fill='%23ffffff' opacity='0.4'/%3E%3Crect x='462' y='115' width='4' height='6' fill='%23ffffff' opacity='0.4'/%3E%3Crect x='462' y='145' width='4' height='6' fill='%23e10600' opacity='0.6'/%3E%3Crect x='484' y='130' width='4' height='6' fill='%23e10600' opacity='0.5'/%3E%3Crect x='590' y='95' width='4' height='6' fill='%23e10600' opacity='0.6'/%3E%3Crect x='590' y='125' width='4' height='6' fill='%23ffffff' opacity='0.35'/%3E%3Crect x='612' y='110' width='4' height='6' fill='%23e10600' opacity='0.5'/%3E%3Crect x='718' y='125' width='4' height='6' fill='%23ffffff' opacity='0.4'/%3E%3Crect x='718' y='155' width='4' height='6' fill='%23e10600' opacity='0.6'/%3E%3C/svg%3E");
}

/* SOFT MOVING SPEED STREAKS */

@keyframes speedStreakMove {
    0% {
        background-position: 0 0;
    }
    100% {
        background-position: -600px 300px;
    }
}

.speed-streaks {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: 0;
    pointer-events: none;

    background:
        repeating-linear-gradient(
            115deg,
            transparent 0px,
            transparent 160px,
            rgba(225, 6, 0, 0.18) 160px,
            rgba(225, 6, 0, 0.18) 163px,
            transparent 163px,
            transparent 320px,
            rgba(255, 255, 255, 0.04) 320px,
            rgba(255, 255, 255, 0.04) 322px,
            transparent 322px,
            transparent 480px
        );

    background-size: 600px 300px;
    animation: speedStreakMove 6s linear infinite;
}

/* SOFT RED CITY GLOW ON THE HORIZON */

.glow-accent {
    position: fixed;
    bottom: -5%;
    left: 50%;
    transform: translateX(-50%);
    width: 140%;
    height: 26%;
    z-index: 0;
    pointer-events: none;

    background: radial-gradient(
        ellipse at center,
        rgba(225, 6, 0, 0.20) 0%,
        rgba(225, 6, 0, 0) 70%
    );

    filter: blur(10px);
}

/* Keep Streamlit content above background */

[data-testid="stAppViewContainer"] {
    position: relative;
    z-index: 10;
}

[data-testid="stMain"] {
    position: relative;
    z-index: 10;
}

/* TOP CHEQUERED FLAG STRIPE (ANIMATED) */

@keyframes checkerMove {
    0% {
        background-position: 0 0, 0 9px, 9px -9px, -9px 0px;
    }
    100% {
        background-position: 180px 0, 180px 9px, 189px -9px, 171px 0px;
    }
}

.f1-racing-stripes {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 10px;
    z-index: 9999;
    pointer-events: none;

    background-color: #1a1a1a;
    background-image:
        linear-gradient(45deg, #e8e8e8 25%, transparent 25%),
        linear-gradient(-45deg, #e8e8e8 25%, transparent 25%),
        linear-gradient(45deg, transparent 75%, #e8e8e8 75%),
        linear-gradient(-45deg, transparent 75%, #e8e8e8 75%);

    background-size: 18px 18px;
    background-position: 0 0, 0 9px, 9px -9px, -9px 0px;

    animation: checkerMove 3s linear infinite;

    box-shadow: 0 0 12px rgba(225, 6, 0, 0.5);
    border-bottom: 1px solid #e10600;
}

/* RED BUTTONS — BIG, GLOSSY, WITH A SHINE SWEEP */

@keyframes idleGlow {
    0%, 100% {
        box-shadow:
            0 4px 0 #6e0300,
            0 10px 22px rgba(225, 6, 0, 0.4);
    }
    50% {
        box-shadow:
            0 4px 0 #6e0300,
            0 12px 30px rgba(225, 6, 0, 0.7),
            0 0 16px rgba(255, 255, 255, 0.18);
    }
}

.stButton > button {
    background: linear-gradient(135deg, #ff2200 0%, #b80500 100%) !important;
    color: white !important;

    border: 2px solid #ff5c48 !important;
    border-radius: 14px !important;

    font-weight: 800 !important;
    font-size: 18px !important;
    letter-spacing: 1.2px;
    text-transform: uppercase;

    min-height: 66px;
    padding: 0 24px;

    position: relative;
    overflow: hidden;

    animation: idleGlow 2.6s ease-in-out infinite;

    transition:
        transform 0.15s ease,
        box-shadow 0.15s ease,
        background 0.3s ease,
        border-color 0.2s ease;
}

/* diagonal shine that sweeps across on hover */

.stButton > button::before {
    content: "";
    position: absolute;
    top: 0;
    left: -75%;
    width: 45%;
    height: 100%;

    background: linear-gradient(
        120deg,
        transparent,
        rgba(255, 255, 255, 0.45),
        transparent
    );

    transform: skewX(-25deg);
    transition: left 0.6s ease;

    border-radius: inherit;
    overflow: hidden;
}

.stButton > button:hover::before {
    left: 130%;
}

/* little checkered-flag badge that pops in on hover */

.stButton > button::after {
    content: "";
    position: absolute;
    top: 6px;
    right: 6px;
    width: 16px;
    height: 16px;

    background-image:
        linear-gradient(45deg, #fff 25%, transparent 25%),
        linear-gradient(-45deg, #fff 25%, transparent 25%),
        linear-gradient(45deg, transparent 75%, #fff 75%),
        linear-gradient(-45deg, transparent 75%, #fff 75%);

    background-color: #000;
    background-size: 4px 4px;
    background-position: 0 0, 0 2px, 2px -2px, -2px 0px;

    border-radius: 50%;
    border: 1px solid rgba(255, 255, 255, 0.5);

    opacity: 0;
    transform: scale(0.4) rotate(-25deg);

    transition: opacity 0.2s ease, transform 0.2s ease;
    pointer-events: none;

    box-shadow: 0 0 8px rgba(0, 0, 0, 0.6);
}

.stButton > button:hover::after {
    opacity: 1;
    transform: scale(1) rotate(0deg);
}

.stButton > button:hover {
    background: linear-gradient(135deg, #ff4326 0%, #d40600 100%) !important;
    color: white !important;

    border-color: #ffffff !important;

    animation: none;

    transform: translateY(-4px) scale(1.03);

    box-shadow:
        0 6px 0 #6e0300,
        0 16px 30px rgba(225, 6, 0, 0.55),
        0 0 20px rgba(255, 255, 255, 0.18);
}

.stButton > button:active {
    animation: none;

    transform: translateY(1px) scale(0.98);

    box-shadow:
        0 2px 0 #6e0300,
        0 5px 12px rgba(225, 6, 0, 0.4);
}

/* CALCULATOR */

.calculator-container {
    max-width: 430px;
    margin: auto;
}

.calculator-display {
    background: #111111;

    border: 2px solid #e10600;
    border-radius: 12px;

    padding: 18px 15px;
    margin-bottom: 12px;

    text-align: right;

    color: white;

    font-size: 38px;
    font-weight: bold;

    min-height: 55px;

    overflow: hidden;
    word-break: break-all;
}

.calculator-container .stButton > button {
    width: 100%;
    min-height: 70px;

    font-size: 26px;
    font-weight: 800;

    border-radius: 12px;

    animation: none;
}

/* MOBILE */

@media (max-width: 600px) {

    .calculator-container {
        width: 100%;
        padding: 0 3px;
    }

    .calculator-display {
        font-size: 31px;
        min-height: 48px;
        padding: 14px 12px;
    }

    .calculator-container .stButton > button {
        min-height: 55px;
        font-size: 20px;
    }
}

/* =========================================================
   SHARED "PANEL" LOOK FOR EVERY APP PAGE
   ========================================================= */

.f1-card {
    background: linear-gradient(
        160deg,
        rgba(30, 30, 30, 0.75) 0%,
        rgba(10, 10, 10, 0.85) 100%
    );

    border: 1px solid rgba(225, 6, 0, 0.35);
    border-radius: 16px;

    padding: 22px 24px;
    margin-bottom: 18px;

    backdrop-filter: blur(6px);

    box-shadow:
        0 10px 24px rgba(0, 0, 0, 0.45),
        inset 0 1px 0 rgba(255, 255, 255, 0.04);

    position: relative;
    overflow: hidden;
}

.f1-card::before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 4px;

    background: linear-gradient(
        90deg,
        #e10600 0%,
        #ffffff 50%,
        #e10600 100%
    );

    opacity: 0.85;
}

.f1-flag-divider {
    height: 6px;
    margin: 18px 0;
    border-radius: 3px;

    background-image:
        linear-gradient(45deg, #fff 25%, transparent 25%),
        linear-gradient(-45deg, #fff 25%, transparent 25%),
        linear-gradient(45deg, transparent 75%, #fff 75%),
        linear-gradient(-45deg, transparent 75%, #fff 75%);

    background-color: #1a1a1a;
    background-size: 12px 12px;
    background-position: 0 0, 0 6px, 6px -6px, -6px 0px;
}

/* GLOWING PAGE TITLES */

h1, h2, h3 {
    text-shadow: 0 0 14px rgba(225, 6, 0, 0.35);
}

/* LABEL CHIPS (used on the profile card) */

.chip-row {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    margin-top: 6px;
}

.chip {
    background: rgba(225, 6, 0, 0.14);
    border: 1px solid rgba(225, 6, 0, 0.55);
    border-radius: 999px;

    padding: 8px 16px;

    color: #fff;
    font-weight: 700;
    font-size: 14px;

    white-space: nowrap;
}

/* DRIVER-CARD HEADER (profile) */

.driver-card-header {
    display: flex;
    align-items: center;
    gap: 16px;
    margin-bottom: 8px;
}

.driver-number {
    font-size: 46px;
    font-weight: 900;
    color: #e10600;
    text-shadow: 0 0 18px rgba(225, 6, 0, 0.6);
    line-height: 1;
}

.driver-name {
    font-size: 26px;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 1px;
}

/* GRADE BADGE (grade calculator) */

.grade-badge-wrap {
    display: flex;
    justify-content: center;
    margin: 10px 0 4px 0;
}

.grade-badge {
    width: 110px;
    height: 110px;
    border-radius: 50%;

    display: flex;
    align-items: center;
    justify-content: center;

    font-size: 46px;
    font-weight: 900;

    color: #0a0a0a;

    box-shadow:
        0 0 0 4px rgba(255, 255, 255, 0.15) inset,
        0 8px 22px rgba(0, 0, 0, 0.5);
}

.grade-gold {
    background: radial-gradient(circle at 35% 30%, #fff4c2, #d9a400 70%);
}

.grade-silver {
    background: radial-gradient(circle at 35% 30%, #f5f5f5, #9a9a9a 70%);
}

.grade-bronze {
    background: radial-gradient(circle at 35% 30%, #f0c090, #a15c2b 70%);
}

.grade-red {
    background: radial-gradient(circle at 35% 30%, #ff8a80, #b80500 70%);
    color: #fff;
}

/* FUEL-GAUGE STYLE PROGRESS BARS */

[data-testid="stProgress"] > div > div {
    background: linear-gradient(90deg, #6e0300, #e10600 60%, #ff6a4d) !important;
    box-shadow: 0 0 10px rgba(225, 6, 0, 0.6);
}

[data-testid="stProgress"] {
    background: rgba(255, 255, 255, 0.06);
    border-radius: 8px;
    padding: 2px;
}

/* METRIC CARD (quiz score) */

[data-testid="stMetric"] {
    background: rgba(225, 6, 0, 0.10);
    border: 1px solid rgba(225, 6, 0, 0.4);
    border-radius: 14px;
    padding: 14px 18px;
    text-align: center;
}

[data-testid="stMetricValue"] {
    color: #ffffff !important;
    text-shadow: 0 0 16px rgba(225, 6, 0, 0.6);
}

/* QUIZ ANSWER OPTIONS AS CLICKABLE CARDS */

[data-testid="stRadio"] > div {
    gap: 10px;
}

[data-testid="stRadio"] label {
    background: rgba(255, 255, 255, 0.04);
    border: 1px solid rgba(255, 255, 255, 0.15);
    border-radius: 12px;

    padding: 12px 16px !important;
    margin: 0 !important;
    width: 100%;

    transition: background 0.15s, border-color 0.15s, transform 0.15s;
}

[data-testid="stRadio"] label:hover {
    background: rgba(225, 6, 0, 0.14);
    border-color: rgba(225, 6, 0, 0.6);
    transform: translateX(3px);
}

[data-testid="stRadio"] label:has(input:checked) {
    background: rgba(225, 6, 0, 0.28);
    border-color: #e10600;
    box-shadow: 0 0 12px rgba(225, 6, 0, 0.4);
}

/* TEXT / NUMBER INPUTS TO MATCH THE THEME */

.stTextInput input,
.stNumberInput input,
.stSelectbox [data-baseweb="select"] {
    background-color: #141414 !important;
    color: #fff !important;
    border: 1px solid rgba(225, 6, 0, 0.4) !important;
    border-radius: 10px !important;
}

.stTextInput input:focus,
.stNumberInput input:focus {
    border-color: #e10600 !important;
    box-shadow: 0 0 0 2px rgba(225, 6, 0, 0.25) !important;
}

/* SIDEBAR (TETRIS PIT-STOP PANEL) */

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #141414 0%, #0a0a0a 100%);
    border-right: 1px solid rgba(225, 6, 0, 0.35);
}

</style>

<div class="f1-racing-stripes"></div>
<div class="neon-grid"></div>
<div class="glow-accent"></div>
<div class="neon-skyline"></div>
<div class="speed-streaks"></div>

""", unsafe_allow_html=True)


# =========================================================
# F1 DRIVER FUN FACTS
# =========================================================

FUN_FACTS = [
    "Lewis Hamilton holds the record for the most pole positions "
    "in Formula 1 history.",

    "Michael Schumacher won seven Formula 1 World Championships "
    "over his career.",

    "Max Verstappen became the youngest driver ever to start an "
    "F1 race, at just 17 years old.",

    "Niki Lauda survived a horrific fiery crash in 1976 and "
    "returned to racing only six weeks later.",

    "Juan Manuel Fangio won five World Championships in the "
    "1950s, a record that stood for decades.",

    "Kimi Räikkönen earned the nickname 'The Iceman' for his "
    "famously cool, unbothered radio messages.",

    "Sebastian Vettel won four consecutive World Championships "
    "with Red Bull from 2010 to 2013.",

    "Nigel Mansell is one of the only drivers in history to hold "
    "the F1 and IndyCar titles back to back.",

    "Alain Prost was nicknamed 'The Professor' for his precise, "
    "calculated approach to racing.",

    "Daniel Ricciardo is famous for celebrating race wins by "
    "drinking champagne out of his own shoe — the 'shoey'.",

    "Ayrton Senna and Alain Prost's rivalry in the late 1980s is "
    "considered one of the fiercest in F1 history.",

    "Jenson Button won the 2009 World Championship driving for "
    "Brawn GP, a team that only existed for one season.",

    "Fernando Alonso won back-to-back World Championships in "
    "2005 and 2006 with Renault.",

    "The number '1' is reserved for the reigning World Champion, "
    "though most choose to keep their permanent number instead.",

    "Charles Leclerc secured his first F1 pole position at the "
    "circuit named after his hometown, Monaco.",
]

if "fun_fact_index" not in st.session_state:
    st.session_state.fun_fact_index = random.randrange(len(FUN_FACTS))


# =========================================================
# SIDEBAR — PIT STOP TETRIS
# =========================================================

TETRIS_HTML = """
<div style="text-align:center; font-family:Arial, sans-serif;
     background:#0a0a0a; padding:10px; border-radius:12px;
     border:1px solid rgba(225,6,0,0.45);
     box-shadow:0 0 18px rgba(225,6,0,0.15);">

    <div style="color:#e10600; font-weight:800; letter-spacing:1px;
         margin-bottom:4px; text-transform:uppercase; font-size:13px;">
        🏁 Pit Stop Tetris
    </div>

    <div id="tetris-score" style="color:#fff; font-weight:700;
         margin-bottom:8px; font-size:13px;">
        Score: 0
    </div>

    <canvas id="tetris-canvas" style="background:#000;
        border:2px solid #e10600; border-radius:8px;
        outline:none; cursor:pointer;"></canvas>

    <div style="color:#aaa; font-size:10px; margin-top:8px; line-height:1.5;">
        Click the board, then:<br>
        ⬅️➡️ move &nbsp; ⬆️ rotate<br>
        ⬇️ soft drop &nbsp; Space hard drop
    </div>

    <button id="tetris-restart" style="margin-top:8px;
        background:linear-gradient(135deg,#ff2200,#b80500); color:#fff;
        border:1px solid #ff5c48; border-radius:8px; padding:6px 14px;
        font-weight:700; cursor:pointer;">
        🔄 Restart
    </button>
</div>

<script>
(function () {

    class BlockGame {

        constructor(canvasId, scoreId) {

            this.canvas = document.getElementById(canvasId);
            this.ctx = this.canvas.getContext('2d');

            this.cols = 10;
            this.rows = 20;
            this.cell = 16;

            this.canvas.width = this.cols * this.cell;
            this.canvas.height = this.rows * this.cell;

            this.scoreEl = document.getElementById(scoreId);

            this.palette = [
                null, '#e10600', '#ffffff', '#ff6a4d',
                '#7a0000', '#e6e6e6', '#b0b0b0', '#ff3b1f'
            ];

            this.shapes = {
                I: [[0,0,0,0],[1,1,1,1],[0,0,0,0],[0,0,0,0]],
                O: [[2,2],[2,2]],
                T: [[0,3,0],[3,3,3],[0,0,0]],
                S: [[0,4,4],[4,4,0],[0,0,0]],
                Z: [[5,5,0],[0,5,5],[0,0,0]],
                J: [[6,0,0],[6,6,6],[0,0,0]],
                L: [[0,0,7],[7,7,7],[0,0,0]]
            };

            this.dropTimer = 0;
            this.dropDelay = 550;
            this.lastTick = 0;
            this.started = false;

            this.reset();
            this.bindKeys();

            requestAnimationFrame(this.loop.bind(this));
        }

        reset() {
            this.grid = Array.from(
                {length: this.rows},
                () => new Array(this.cols).fill(0)
            );
            this.score = 0;
            this.gameOver = false;
            this.updateScore();
            this.spawn();
        }

        spawn() {
            const keys = Object.keys(this.shapes);
            const key = keys[(Math.random() * keys.length) | 0];

            this.shape = this.shapes[key].map(row => row.slice());
            this.pos = {
                x: ((this.cols / 2) | 0) - ((this.shape[0].length / 2) | 0),
                y: -1
            };

            if (this.collides(this.shape, this.pos)) {
                this.gameOver = true;
            }
        }

        collides(shape, pos) {
            for (let y = 0; y < shape.length; y++) {
                for (let x = 0; x < shape[y].length; x++) {
                    if (!shape[y][x]) continue;

                    const gx = pos.x + x;
                    const gy = pos.y + y;

                    if (gx < 0 || gx >= this.cols || gy >= this.rows) {
                        return true;
                    }

                    if (gy >= 0 && this.grid[gy][gx]) {
                        return true;
                    }
                }
            }
            return false;
        }

        lock() {
            this.shape.forEach((row, y) => {
                row.forEach((val, x) => {
                    if (val) {
                        const gy = this.pos.y + y;
                        const gx = this.pos.x + x;
                        if (gy >= 0) this.grid[gy][gx] = val;
                    }
                });
            });

            this.clearRows();
            this.spawn();
        }

        clearRows() {
            let cleared = 0;

            for (let y = this.rows - 1; y >= 0; y--) {
                if (this.grid[y].every(v => v !== 0)) {
                    this.grid.splice(y, 1);
                    this.grid.unshift(new Array(this.cols).fill(0));
                    cleared++;
                    y++;
                }
            }

            if (cleared > 0) {
                const table = [0, 10, 30, 50, 80];
                this.score += table[cleared] || cleared * 20;
                this.updateScore();
            }
        }

        move(dx) {
            const next = {x: this.pos.x + dx, y: this.pos.y};
            if (!this.collides(this.shape, next)) this.pos = next;
        }

        softDrop() {
            const next = {x: this.pos.x, y: this.pos.y + 1};

            if (!this.collides(this.shape, next)) {
                this.pos = next;
            } else {
                this.lock();
            }

            this.dropTimer = 0;
        }

        hardDrop() {
            while (!this.collides(this.shape, {x: this.pos.x, y: this.pos.y + 1})) {
                this.pos.y++;
            }
            this.lock();
            this.dropTimer = 0;
        }

        rotate() {
            const rotated = this.shape[0].map(
                (_, i) => this.shape.map(row => row[i]).reverse()
            );

            if (!this.collides(rotated, this.pos)) {
                this.shape = rotated;
                return;
            }

            for (const shift of [1, -1, 2, -2]) {
                const test = {x: this.pos.x + shift, y: this.pos.y};
                if (!this.collides(rotated, test)) {
                    this.shape = rotated;
                    this.pos = test;
                    return;
                }
            }
        }

        bindKeys() {
            this.canvas.setAttribute('tabindex', '0');

            this.canvas.addEventListener('click', () => {
                this.canvas.focus();
                this.started = true;
            });

            this.canvas.addEventListener('keydown', (e) => {
                if (this.gameOver) return;

                this.started = true;

                if (e.code === 'ArrowLeft') { e.preventDefault(); this.move(-1); }
                else if (e.code === 'ArrowRight') { e.preventDefault(); this.move(1); }
                else if (e.code === 'ArrowDown') { e.preventDefault(); this.softDrop(); }
                else if (e.code === 'ArrowUp') { e.preventDefault(); this.rotate(); }
                else if (e.code === 'Space') { e.preventDefault(); this.hardDrop(); }
            });
        }

        updateScore() {
            this.scoreEl.innerText = 'Score: ' + this.score;
        }

        drawCell(x, y, color) {
            const c = this.cell;
            this.ctx.fillStyle = color;
            this.ctx.fillRect(x * c, y * c, c, c);
            this.ctx.strokeStyle = 'rgba(0,0,0,0.5)';
            this.ctx.strokeRect(x * c, y * c, c, c);
        }

        render() {
            this.ctx.fillStyle = '#0a0a0a';
            this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);

            for (let y = 0; y < this.rows; y++) {
                for (let x = 0; x < this.cols; x++) {
                    if (this.grid[y][x]) {
                        this.drawCell(x, y, this.palette[this.grid[y][x]]);
                    }
                }
            }

            this.shape.forEach((row, y) => {
                row.forEach((val, x) => {
                    if (val && this.pos.y + y >= 0) {
                        this.drawCell(
                            this.pos.x + x,
                            this.pos.y + y,
                            this.palette[val]
                        );
                    }
                });
            });

            if (!this.started && !this.gameOver) {
                this.ctx.fillStyle = 'rgba(0,0,0,0.55)';
                this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);
                this.ctx.fillStyle = '#ffffff';
                this.ctx.font = 'bold 12px Arial';
                this.ctx.textAlign = 'center';
                this.ctx.fillText(
                    'CLICK TO START',
                    this.canvas.width / 2,
                    this.canvas.height / 2
                );
            }

            if (this.gameOver) {
                this.ctx.fillStyle = 'rgba(0,0,0,0.7)';
                this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);
                this.ctx.fillStyle = '#e10600';
                this.ctx.font = 'bold 13px Arial';
                this.ctx.textAlign = 'center';
                this.ctx.fillText(
                    'GAME OVER',
                    this.canvas.width / 2,
                    this.canvas.height / 2
                );
            }
        }

        loop(ts) {
            if (this.started && !this.gameOver) {
                const delta = ts - this.lastTick;
                this.lastTick = ts;
                this.dropTimer += delta;

                if (this.dropTimer > this.dropDelay) {
                    this.softDrop();
                }
            } else {
                this.lastTick = ts;
            }

            this.render();
            requestAnimationFrame(this.loop.bind(this));
        }
    }

    const game = new BlockGame('tetris-canvas', 'tetris-score');

    document.getElementById('tetris-restart').addEventListener(
        'click',
        function () { game.reset(); }
    );

})();
</script>
"""

with st.sidebar:

    st.markdown(
        '<div style="color:#e10600; font-weight:800; '
        'text-transform:uppercase; letter-spacing:1px; '
        'font-size:15px; margin-bottom:8px;">🎮 Pit Lane Arcade</div>',
        unsafe_allow_html=True
    )

    components.html(TETRIS_HTML, height=460, scrolling=False)


# =========================================================
# SESSION STATE
# =========================================================

if "page" not in st.session_state:
    st.session_state.page = "home"

# =========================================================
# CALCULATOR STATE
# =========================================================

if "calc_display" not in st.session_state:
    st.session_state.calc_display = "0"

if "calc_first_number" not in st.session_state:
    st.session_state.calc_first_number = None

if "calc_operator" not in st.session_state:
    st.session_state.calc_operator = None

if "calc_new_number" not in st.session_state:
    st.session_state.calc_new_number = True


# =========================================================
# CALCULATOR FUNCTIONS
# =========================================================

def format_result(number):

    if number is None:
        return "0"

    if math.isfinite(number) and number.is_integer():
        return str(int(number))

    return str(round(number, 10))


def calculate_result(first, second, operator):

    if operator == "+":
        return first + second

    if operator == "−":
        return first - second

    if operator == "×":
        return first * second

    if operator == "÷":

        if second == 0:
            return None

        return first / second

    return second


def press_number(number):

    if st.session_state.calc_new_number:

        st.session_state.calc_display = number
        st.session_state.calc_new_number = False

    else:

        if st.session_state.calc_display == "0":
            st.session_state.calc_display = number

        else:
            st.session_state.calc_display += number


def press_decimal():

    if st.session_state.calc_new_number:

        st.session_state.calc_display = "0."
        st.session_state.calc_new_number = False

    elif "." not in st.session_state.calc_display:

        st.session_state.calc_display += "."


def press_operator(operator):

    current = float(st.session_state.calc_display)

    if st.session_state.calc_first_number is not None:

        result = calculate_result(
            st.session_state.calc_first_number,
            current,
            st.session_state.calc_operator
        )

        if result is None:

            st.session_state.calc_display = "Error"
            st.session_state.calc_first_number = None
            st.session_state.calc_operator = None
            st.session_state.calc_new_number = True

            return

        st.session_state.calc_display = format_result(result)
        st.session_state.calc_first_number = result

    else:

        st.session_state.calc_first_number = current

    st.session_state.calc_operator = operator
    st.session_state.calc_new_number = True


def press_equals():

    if (
        st.session_state.calc_first_number is None
        or st.session_state.calc_operator is None
    ):
        return

    second = float(st.session_state.calc_display)

    result = calculate_result(
        st.session_state.calc_first_number,
        second,
        st.session_state.calc_operator
    )

    if result is None:

        st.session_state.calc_display = "Error"

    else:

        st.session_state.calc_display = format_result(result)

    st.session_state.calc_first_number = None
    st.session_state.calc_operator = None
    st.session_state.calc_new_number = True


def clear_calculator():

    st.session_state.calc_display = "0"
    st.session_state.calc_first_number = None
    st.session_state.calc_operator = None
    st.session_state.calc_new_number = True


def delete_number():

    if st.session_state.calc_display == "Error":
        clear_calculator()
        return

    if len(st.session_state.calc_display) <= 1:

        st.session_state.calc_display = "0"

    else:

        st.session_state.calc_display = (
            st.session_state.calc_display[:-1]
        )

        if st.session_state.calc_display == "-":
            st.session_state.calc_display = "0"


def plus_minus():

    if st.session_state.calc_display == "0":
        return

    if st.session_state.calc_display.startswith("-"):

        st.session_state.calc_display = (
            st.session_state.calc_display[1:]
        )

    else:

        st.session_state.calc_display = (
            "-" + st.session_state.calc_display
        )


def percentage():

    try:

        number = float(st.session_state.calc_display)

        number = number / 100

        st.session_state.calc_display = format_result(number)

    except:

        st.session_state.calc_display = "Error"


# =========================================================
# HOME PAGE
# =========================================================

def home_page():

    st.title("🏎️ F1 Student Hub")

    st.write(
        "Your F1-themed student website for quizzes, "
        "calculations, grades and your profile."
    )

    st.divider()

    st.subheader("🏁 Choose an App")

    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            "🏆 Quiz Master",
            use_container_width=True
        ):
            st.session_state.page = "quiz_setup"
            st.rerun()

        if st.button(
            "🧮 Calculator",
            use_container_width=True
        ):
            st.session_state.page = "calculator"
            st.rerun()

    with col2:

        if st.button(
            "📊 Grade Calculator",
            use_container_width=True
        ):
            st.session_state.page = "grades"
            st.rerun()

        if st.button(
            "👤 My Profile",
            use_container_width=True
        ):
            st.session_state.page = "profile"
            st.rerun()

    st.markdown('<div class="f1-flag-divider"></div>', unsafe_allow_html=True)

    fact = FUN_FACTS[st.session_state.fun_fact_index]

    st.markdown(
        f"""
        <div class="f1-card">
            <div style="letter-spacing:2px; opacity:0.75;
                 text-transform:uppercase; font-size:12px;
                 color:#e10600; font-weight:800;">
                🏎️ F1 Driver Fun Fact
            </div>
            <div style="font-size:16px; margin-top:8px;">
                {fact}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    if st.button(
        "🎲 New Fact",
        use_container_width=True
    ):
        st.session_state.fun_fact_index = random.randrange(
            len(FUN_FACTS)
        )
        st.rerun()


# =========================================================
# PROFILE PAGE
# =========================================================

def profile_page():

    st.title("👤 My Profile")

    st.markdown('<div class="f1-card">', unsafe_allow_html=True)

    st.write("Fill in your information below!")

    name = st.text_input("Name")
    age = st.number_input(
        "Age",
        min_value=1,
        max_value=100,
        step=1
    )

    school = st.text_input("School")
    subject = st.text_input("Favorite subject")
    hobby = st.text_input("Favorite hobby")

    if st.button(
        "✨ Create My Profile",
        use_container_width=True
    ):

        if name and school and subject and hobby:

            st.success("Profile created!")

            st.markdown(
                f"""
                <div class="f1-card">
                    <div class="driver-card-header">
                        <div class="driver-number">#{int(age):02d}</div>
                        <div class="driver-name">{name}</div>
                    </div>
                    <div class="f1-flag-divider"></div>
                    <div class="chip-row">
                        <div class="chip">🏫 {school}</div>
                        <div class="chip">📚 {subject}</div>
                        <div class="chip">🎮 {hobby}</div>
                        <div class="chip">🎂 Age {age}</div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

        else:

            st.warning(
                "Please fill in all the information."
            )

    st.markdown('</div>', unsafe_allow_html=True)

    st.divider()

    if st.button(
        "⬅️ Back to Home",
        use_container_width=True
    ):

        st.session_state.page = "home"
        st.rerun()


# =========================================================
# CALCULATOR PAGE
# =========================================================

def calculator_page():

    st.title("🧮 Pit Lane Calculator")

    st.markdown(
        '<div class="f1-card"><div class="calculator-container">',
        unsafe_allow_html=True
    )

    # OPERATOR STATUS BADGE

    if st.session_state.calc_operator is not None:

        st.markdown(
            f"""
            <div class="chip-row" style="margin-bottom: 10px;">
                <div class="chip">
                    {format_result(st.session_state.calc_first_number)}
                    {st.session_state.calc_operator}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    # DISPLAY

    st.markdown(
        f"""
        <div class="calculator-display">
            {st.session_state.calc_display}
        </div>
        """,
        unsafe_allow_html=True
    )

    # NORMAL CALCULATOR GRID

    rows = [

        ["AC", "±", "%", "÷"],

        ["7", "8", "9", "×"],

        ["4", "5", "6", "−"],

        ["1", "2", "3", "+"],

        ["0", ".", "⌫", "="]

    ]

    for row_number, row in enumerate(rows):

        cols = st.columns(4)

        for column_number, button in enumerate(row):

            with cols[column_number]:

                clicked = st.button(
                    button,
                    key=f"calc_{row_number}_{column_number}",
                    use_container_width=True
                )

                if clicked:

                    if button.isdigit():

                        press_number(button)

                    elif button == ".":

                        press_decimal()

                    elif button in [
                        "+",
                        "−",
                        "×",
                        "÷"
                    ]:

                        press_operator(button)

                    elif button == "=":

                        press_equals()

                    elif button == "AC":

                        clear_calculator()

                    elif button == "⌫":

                        delete_number()

                    elif button == "±":

                        plus_minus()

                    elif button == "%":

                        percentage()

                    st.rerun()

    st.markdown(
        "</div></div>",
        unsafe_allow_html=True
    )

    st.divider()

    if st.button(
        "⬅️ Back to Home",
        use_container_width=True
    ):

        st.session_state.page = "home"
        st.rerun()


# =========================================================
# GRADE CALCULATOR
# =========================================================

def grades_page():

    st.title("📊 Grade Calculator")

    st.markdown('<div class="f1-card">', unsafe_allow_html=True)

    st.write(
        "Enter your subjects and marks."
    )

    number_of_subjects = st.number_input(
        "Number of subjects",
        min_value=1,
        max_value=10,
        value=5,
        step=1
    )

    subjects = []

    total = 0

    for i in range(int(number_of_subjects)):

        col1, col2 = st.columns(2)

        with col1:

            subject_name = st.text_input(
                f"Subject {i + 1}",
                key=f"subject_{i}"
            )

        with col2:

            mark = st.number_input(
                f"Mark {i + 1}",
                min_value=0,
                max_value=100,
                value=0,
                key=f"mark_{i}"
            )

        subjects.append(
            (subject_name, mark)
        )

        total += mark

    if st.button(
        "📈 Calculate Grades",
        use_container_width=True
    ):

        average = total / number_of_subjects

        if average >= 90:

            grade = "A"
            badge_class = "grade-gold"
            podium = "🥇"
            message = "Excellent work! Pole position!"

        elif average >= 80:

            grade = "B"
            badge_class = "grade-silver"
            podium = "🥈"
            message = "Great job! Solid podium finish!"

        elif average >= 70:

            grade = "C"
            badge_class = "grade-bronze"
            podium = "🥉"
            message = "Good work! Points finish!"

        elif average >= 60:

            grade = "D"
            badge_class = "grade-red"
            podium = "🏁"
            message = "Keep practicing! Just outside the points."

        else:

            grade = "F"
            badge_class = "grade-red"
            podium = "🔧"
            message = "Back to the garage — keep studying, don't give up!"

        st.markdown(
            f"""
            <div class="f1-card">
                <div style="text-align:center;">
                    <div style="font-size:15px; letter-spacing:2px; opacity:0.75; text-transform:uppercase;">
                        Race Result
                    </div>
                    <div class="grade-badge-wrap">
                        <div class="grade-badge {badge_class}">{grade}</div>
                    </div>
                    <div style="font-size:22px; font-weight:800; margin-top:6px;">
                        {podium} {average:.1f}% average
                    </div>
                    <div style="opacity:0.85; margin-top:4px;">
                        {message}
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.progress(min(average / 100, 1.0))

        st.divider()

        st.subheader(
            "🎮 Terraria Tip"
        )

        st.info(
            "Build a safe base before exploring dangerous areas!"
        )

    st.markdown('</div>', unsafe_allow_html=True)

    st.divider()

    if st.button(
        "⬅️ Back to Home",
        use_container_width=True
    ):

        st.session_state.page = "home"
        st.rerun()


# =========================================================
# QUIZ SETUP
# =========================================================

def quiz_setup_page():

    st.title("🏆 F1 Quiz Master")

    st.write(
        "Create your own quiz!"
    )

    number_of_questions = st.number_input(
        "Number of questions",
        min_value=1,
        max_value=20,
        value=5,
        step=1
    )

    if "quiz_questions" not in st.session_state:

        st.session_state.quiz_questions = []

    questions = []

    for i in range(int(number_of_questions)):

        st.markdown(f'<div class="f1-card">', unsafe_allow_html=True)

        st.markdown(
            f'<div style="font-weight:800; font-size:18px; '
            f'color:#e10600; text-transform:uppercase; '
            f'letter-spacing:1px;">🏁 Question {i + 1}</div>',
            unsafe_allow_html=True
        )

        question = st.text_input(
            "Question",
            key=f"quiz_question_{i}"
        )

        choices = []

        for j in range(4):

            choice = st.text_input(
                f"Choice {j + 1}",
                key=f"quiz_choice_{i}_{j}"
            )

            choices.append(choice)

        correct = st.selectbox(
            "Correct answer",
            [1, 2, 3, 4],
            key=f"quiz_correct_{i}"
        )

        questions.append({
            "question": question,
            "choices": choices,
            "correct": correct - 1
        })

        st.markdown('</div>', unsafe_allow_html=True)

    if st.button(
        "🏁 Start Quiz",
        use_container_width=True
    ):

        valid = True

        for q in questions:

            if not q["question"]:

                valid = False

            if any(
                choice == ""
                for choice in q["choices"]
            ):

                valid = False

        if valid:

            st.session_state.quiz_questions = questions

            st.session_state.quiz_answers = [
                None
                for _ in questions
            ]

            st.session_state.quiz_current = 0

            st.session_state.quiz_finished = False

            st.session_state.page = "quiz"

            st.rerun()

        else:

            st.warning(
                "Please fill in every question and choice."
            )

    if st.button(
        "⬅️ Back to Home",
        use_container_width=True
    ):

        st.session_state.page = "home"
        st.rerun()


# =========================================================
# QUIZ PAGE
# =========================================================

def quiz_page():

    questions = st.session_state.quiz_questions

    current = st.session_state.quiz_current

    question = questions[current]

    st.title("🏎️ F1 Quiz")

    st.progress(
        (current + 1) / len(questions)
    )

    st.markdown('<div class="f1-card">', unsafe_allow_html=True)

    st.markdown(
        f'<div style="letter-spacing:2px; opacity:0.7; '
        f'text-transform:uppercase; font-size:13px;">'
        f'Lap {current + 1} of {len(questions)}</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f'<div style="font-size:22px; font-weight:800; margin:6px 0 16px 0;">'
        f'{question["question"]}</div>',
        unsafe_allow_html=True
    )

    current_answer = st.session_state.quiz_answers[current]

    selected = st.radio(
        "Choose an answer:",
        question["choices"],
        index=current_answer
        if current_answer is not None
        else None,
        key=f"answer_{current}"
    )

    if selected is not None:

        st.session_state.quiz_answers[current] = (
            question["choices"].index(selected)
        )

    st.markdown('</div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:

        if current > 0:

            if st.button(
                "⬅️ Previous",
                use_container_width=True
            ):

                st.session_state.quiz_current -= 1
                st.rerun()

    with col2:

        if current < len(questions) - 1:

            if st.button(
                "Next ➡️",
                use_container_width=True
            ):

                st.session_state.quiz_current += 1
                st.rerun()

    with col3:

        if current == len(questions) - 1:

            if st.button(
                "🏁 Finish",
                use_container_width=True
            ):

                st.session_state.quiz_finished = True
                st.session_state.page = "quiz_results"
                st.rerun()


# =========================================================
# QUIZ RESULTS
# =========================================================

def quiz_results_page():

    st.title("🏆 Quiz Results")

    questions = st.session_state.quiz_questions

    answers = st.session_state.quiz_answers

    score = 0

    for i, question in enumerate(questions):

        if answers[i] == question["correct"]:

            score += 1

    percentage = (
        score / len(questions)
    ) * 100

    if percentage >= 90:

        podium = "🥇"
        podium_msg = "P1! A flawless race!"

    elif percentage >= 70:

        podium = "🥈"
        podium_msg = "P2! A strong result!"

    elif percentage >= 50:

        podium = "🥉"
        podium_msg = "P3! On the podium!"

    else:

        podium = "🏁"
        podium_msg = "You crossed the finish line — try again for a better time!"

    st.markdown(
        f"""
        <div class="f1-card" style="text-align:center;">
            <div style="font-size:52px;">{podium}</div>
            <div style="font-size:22px; font-weight:800; margin-top:4px;">
                {podium_msg}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Score",
            f"{score}/{len(questions)}"
        )

    with col2:

        st.metric(
            "Accuracy",
            f"{percentage:.0f}%"
        )

    st.progress(
        percentage / 100
    )

    st.markdown('<div class="f1-flag-divider"></div>', unsafe_allow_html=True)

    for i, question in enumerate(questions):

        user_answer = answers[i]

        correct_answer = question["correct"]

        is_correct = user_answer == correct_answer

        st.markdown('<div class="f1-card">', unsafe_allow_html=True)

        st.write(
            f"**{i + 1}. {question['question']}**"
        )

        if is_correct:

            st.success(
                f"Correct: {question['choices'][correct_answer]}"
            )

        else:

            st.error(
                f"Correct answer: "
                f"{question['choices'][correct_answer]}"
            )

            if user_answer is not None:

                st.write(
                    f"Your answer: "
                    f"{question['choices'][user_answer]}"
                )

        st.markdown('</div>', unsafe_allow_html=True)

    st.divider()

    if st.button(
        "🔄 Take Another Quiz",
        use_container_width=True
    ):

        st.session_state.page = "quiz_setup"
        st.rerun()

    if st.button(
        "🏠 Back to Home",
        use_container_width=True
    ):

        st.session_state.page = "home"
        st.rerun()


# =========================================================
# PAGE ROUTER
# =========================================================

if st.session_state.page == "home":

    home_page()

elif st.session_state.page == "profile":

    profile_page()

elif st.session_state.page == "calculator":

    calculator_page()

elif st.session_state.page == "grades":

    grades_page()

elif st.session_state.page == "quiz_setup":

    quiz_setup_page()

elif st.session_state.page == "quiz":

    quiz_page()

elif st.session_state.page == "quiz_results":

    quiz_results_page()
