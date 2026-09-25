import streamlit as st
import math

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="F1 Student Hub",
    page_icon="🏎️",
    layout="centered"
)

# ============================================================
# F1 BACKGROUND - RACE LINES ONLY
# ============================================================

st.markdown("""
<style>

/* DARK F1 BACKGROUND */
.stApp {
    background:
        radial-gradient(
            circle at 45% 25%,
            #351010 0%,
            #181818 45%,
            #050505 100%
        );
}
/* RED SPEED LINES */
.speed-lines {
    position: fixed;

    top: 0;
    left: 0;

    width: 100%;
    height: 100%;

    z-index: 0;
    pointer-events: none;

    background:
        repeating-linear-gradient(
            0deg,
            transparent 0px,
            transparent 85px,
            rgba(225,6,0,0.08) 85px,
            rgba(225,6,0,0.08) 87px
        );

    animation:
        speedBackground 2s linear infinite;
}

@keyframes speedBackground {

    0% {
        background-position: 0 0;
    }

    100% {
        background-position: 0 170px;
    }
}

/* MOVING RED LIGHT */
.red-light {

    position: fixed;

    top: 0;
    left: -40%;

    width: 30%;
    height: 100%;

    z-index: 0;
    pointer-events: none;

    background:
        linear-gradient(
            90deg,
            transparent,
            rgba(225,6,0,0.08),
            rgba(225,6,0,0.18),
            transparent
        );

    transform: skewX(-20deg);

    animation:
        lightSweep 4s li    near infinite;
}

@keyframes lightSweep {

    0% {
        left: -40%;
    }

    100% {
        left: 140%;
    }
}

/* F1 TOP STRIPE */
.f1-racing-stripes {

    position: fixed;

    top: 0;
    left: 0;

    width: 100%;
    height: 7px;

    z-index: 9999;
    pointer-events: none;

    background:
        repeating-linear-gradient(
            90deg,
            #e10600 0px,
            #e10600 35px,
            white 35px,
            white 50px,
            #e10600 50px,
            #e10600 85px
        );

    background-size: 170px 100%;

    animation:
        stripeMove 1s linear infinite;
}

@keyframes stripeMove {

    0% {
        background-position: 0 0;
    }

    100% {
        background-position: 170px 0;
    }
}

/* CHECKERED FINISH PATTERN */
.finish-line {

    position: fixed;

    right: 0;
    top: 0;

    width: 60px;
    height: 100%;

    opacity: 0.04;

    z-index: 0;
    pointer-events: none;

    background:
        conic-gradient(
            white 25%,
            transparent 0 50%,
            white 0 75%,
            transparent 0
        )
        0 0 / 30px 30px;
}

/* KEEP CONTENT ABOVE BACKGROUND */
[data-testid="stAppViewContainer"] {
    position: relative;
    z-index: 3;
}

/* ============================================================
   RED F1 BUTTONS
   ============================================================ */

.stButton > button {

    background-color: #e10600 !important;

    color: white !important;

    border: 2px solid #ff3b30 !important;

    border-radius: 10px !important;

    font-weight: bold !important;

    min-height: 48px;

    transition:
        background-color 0.15s,
        transform 0.15s,
        box-shadow 0.15s;
}

.stButton > button:hover {

    background-color: #b80500 !important;

    color: white !important;

    border-color: #ff4d45 !important;

    transform: translateY(-2px);

    box-shadow:
        0 5px 15px rgba(225,6,0,0.45);
}

.stButton > button:active {

    background-color: #8f0400 !important;

    transform: translateY(1px);
}

/* ============================================================
   CALCULATOR
   ============================================================ */

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

    min-height: 58px;

    font-size: 22px;

    font-weight: bold;

    border-radius: 10px;
}

/* PHONE */
@media (max-width: 600px) {

    .race-lines {
        height: 120px;
    }

    .finish-line {
        width: 40px;
    }

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

</style>

<div class="f1-racing-stripes"></div>

<div class="race-lines"></div>

<div class="speed-lines"></div>

<div class="red-light"></div>

<div class="finish-line"></div>

""", unsafe_allow_html=True)


# ============================================================
# SESSION STATE
# ============================================================

if "page" not in st.session_state:
    st.session_state.page = "home"


# ============================================================
# HOME PAGE
# ============================================================

def home_page():

    st.title("🏎️ F1 Student Hub")

    st.write(
        "Welcome to the F1 Student Hub! "
        "Choose an application below."
    )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            "🏁 Quiz Master",
            use_container_width=True
        ):

            st.session_state.page = "quiz_setup"

            st.rerun()

    with col2:

        if st.button(
            "🧮 Calculator",
            use_container_width=True
        ):

            st.session_state.page = "calculator"

            st.rerun()

    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            "🎓 Grade Calculator",
            use_container_width=True
        ):

            st.session_state.page = "grades"

            st.rerun()

    with col2:

        if st.button(
            "👤 My Profile",
            use_container_width=True
        ):

            st.session_state.page = "profile"

            st.rerun()


# ============================================================
# PROFILE
# ============================================================

def profile_page():

    st.title("👤 My Profile")

    st.write(
        "Fill in your information below!"
    )

    name = st.text_input("Name")

    age = st.number_input(
        "Age",
        min_value=1,
        max_value=100,
        step=1
    )

    school = st.text_input("School")

    subject = st.text_input(
        "Favorite subject"
    )

    hobby = st.text_input(
        "Favorite hobby"
    )

    if st.button(
        "✨ Create My Profile",
        use_container_width=True
    ):

        if name and school and subject and hobby:

            st.success("Profile created!")

            st.subheader(
                f"Hello! My name is {name}."
            )

            st.write(
                f"🎂 I am {age} years old."
            )

            st.write(
                f"🏫 I go to {school}."
            )

            st.write(
                f"📚 My favorite subject is {subject}."
            )

            st.write(
                f"🎮 I enjoy {hobby}."
            )

        else:

            st.warning(
                "Please fill in all the information."
            )

    st.divider()

    if st.button(
        "⬅️ Back to Home",
        use_container_width=True
    ):

        st.session_state.page = "home"

        st.rerun()


# ============================================================
# QUIZ SETUP
# ============================================================

def quiz_setup_page():

    st.title("🏁 F1 Quiz Master")

    st.write(
        "Create your own quiz and test yourself!"
    )

    number_of_questions = st.number_input(
        "Number of questions",
        min_value=1,
        max_value=20,
        value=5,
        step=1
    )

    questions = []

    st.divider()

    for i in range(
        int(number_of_questions)
    ):

        st.subheader(
            f"Question {i + 1}"
        )

        question = st.text_input(
            "Question",
            key=f"question_{i}"
        )

        choice_a = st.text_input(
            "A",
            key=f"choice_a_{i}"
        )

        choice_b = st.text_input(
            "B",
            key=f"choice_b_{i}"
        )

        choice_c = st.text_input(
            "C",
            key=f"choice_c_{i}"
        )

        choice_d = st.text_input(
            "D",
            key=f"choice_d_{i}"
        )

        correct = st.selectbox(
            "Correct answer",
            ["A", "B", "C", "D"],
            key=f"correct_{i}"
        )

        questions.append({

            "question": question,

            "A": choice_a,

            "B": choice_b,

            "C": choice_c,

            "D": choice_d,

            "correct": correct
        })

    st.divider()

    if st.button(
        "🏎️ Start Quiz",
        use_container_width=True
    ):

        valid = True

        for q in questions:

            if not q["question"]:
                valid = False

            if not q["A"]:
                valid = False

            if not q["B"]:
                valid = False

            if not q["C"]:
                valid = False

            if not q["D"]:
                valid = False

        if valid:

            st.session_state.questions = questions

            st.session_state.current_question = 0

            st.session_state.answers = {}

            st.session_state.page = "quiz"

            st.rerun()

        else:

            st.error(
                "Please fill in every question "
                "and every answer choice."
            )

    if st.button(
        "⬅️ Back to Home",
        use_container_width=True
    ):

        st.session_state.page = "home"

        st.rerun()


# ============================================================
# QUIZ
# ============================================================

def quiz_page():

    questions = st.session_state.questions

    current = st.session_state.current_question

    total = len(questions)

    q = questions[current]

    st.title("🏁 F1 Quiz Master")

    answered_count = len(
        st.session_state.answers
    )

    progress = answered_count / total

    st.progress(
        progress,
        text=(
            f"🏁 {answered_count} / "
            f"{total} questions answered"
        )
    )

    st.caption(
        f"Question {current + 1} of {total}"
    )

    st.divider()

    st.subheader(
        q["question"]
    )

    choices = [

        f"A. {q['A']}",

        f"B. {q['B']}",

        f"C. {q['C']}",

        f"D. {q['D']}"
    ]

    previous_answer = (
        st.session_state.answers.get(current)
    )

    if previous_answer:

        default_index = [
            "A",
            "B",
            "C",
            "D"
        ].index(previous_answer)

    else:

        default_index = None

    selected = st.radio(
        "Choose your answer:",
        choices,
        index=default_index,
        key=f"answer_{current}"
    )

    if selected:

        st.session_state.answers[current] = (
            selected[0]
        )

    st.divider()

    col1, col2, col3 = st.columns(3)

    with col1:

        if current > 0:

            if st.button(
                "⬅️ Previous",
                use_container_width=True
            ):

                st.session_state.current_question -= 1

                st.rerun()

    with col2:

        if current < total - 1:

            if st.button(
                "Next ➡️",
                use_container_width=True
            ):

                st.session_state.current_question += 1

                st.rerun()

    with col3:

        if current == total - 1:

            if st.button(
                "🏁 Finish",
                use_container_width=True
            ):

                if (
                    len(st.session_state.answers)
                    == total
                ):

                    st.session_state.page = (
                        "quiz_results"
                    )

                    st.rerun()

                else:

                    st.warning(
                        "Please answer every "
                        "question first."
                    )

    if st.button(
        "🏠 Quit Quiz",
        use_container_width=True
    ):

        st.session_state.page = "home"

        st.rerun()


# ============================================================
# QUIZ RESULTS
# ============================================================

def quiz_results_page():

    questions = st.session_state.questions

    answers = st.session_state.answers

    total = len(questions)

    score = 0

    for i, q in enumerate(questions):

        if answers.get(i) == q["correct"]:

            score += 1

    percentage = (
        score / total
    ) * 100

    st.title("🏆 Quiz Complete!")

    st.metric(
        "Score",
        f"{score} / {total}"
    )

    st.progress(
        percentage / 100
    )

    st.write(
        f"You scored {percentage:.0f}%."
    )

    st.divider()

    st.subheader(
        "📋 Answer Review"
    )

    for i, q in enumerate(questions):

        user_answer = answers.get(i)

        correct_answer = q["correct"]

        if user_answer == correct_answer:

            st.success(
                f"Question {i + 1}: Correct ✅"
            )

        else:

            st.error(
                f"Question {i + 1}: "
                f"Incorrect ❌ — "
                f"Correct answer: "
                f"{correct_answer}"
            )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            "🔄 Take Quiz Again",
            use_container_width=True
        ):

            st.session_state.page = (
                "quiz_setup"
            )

            st.rerun()

    with col2:

        if st.button(
            "🏠 Home",
            use_container_width=True
        ):

            st.session_state.page = "home"

            st.rerun()


# ============================================================
# CALCULATOR
# ============================================================

def calculator_page():

    st.markdown(
        '<div class="calculator-container">',
        unsafe_allow_html=True
    )

    st.title("🧮 Calculator")

    # -----------------------------
    # Calculator state
    # -----------------------------

    if "calc_display" not in st.session_state:

        st.session_state.calc_display = "0"

    if "calc_first_number" not in st.session_state:

        st.session_state.calc_first_number = None

    if "calc_operator" not in st.session_state:

        st.session_state.calc_operator = None

    if "calc_new_number" not in st.session_state:

        st.session_state.calc_new_number = True

    # -----------------------------
    # Calculator functions
    # -----------------------------

    def format_result(number):

        if number is None:

            return "Error"

        if not math.isfinite(number):

            return "Error"

        if number == int(number):

            return str(int(number))

        return str(
            round(number, 10)
        )

    def calculate_result(
        first,
        second,
        operator
    ):

        if operator == "+":

            return first + second

        elif operator == "-":

            return first - second

        elif operator == "×":

            return first * second

        elif operator == "÷":

            if second == 0:

                return None

            return first / second

        return second

    def press_number(number):

        if st.session_state.calc_new_number:

            st.session_state.calc_display = number

            st.session_state.calc_new_number = False

        else:

            if (
                st.session_state.calc_display
                == "0"
            ):

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

        try:

            current = float(
                st.session_state.calc_display
            )

            if (
                st.session_state.calc_first_number
                is not None
                and
                st.session_state.calc_operator
                is not None
                and
                not st.session_state.calc_new_number
            ):

                result = calculate_result(

                    st.session_state.calc_first_number,

                    current,

                    st.session_state.calc_operator
                )

                if result is None:

                    st.session_state.calc_display = (
                        "Error"
                    )

                    return

                st.session_state.calc_display = (
                    format_result(result)
                )

                current = result

            st.session_state.calc_first_number = current

            st.session_state.calc_operator = operator

            st.session_state.calc_new_number = True

        except:

            st.session_state.calc_display = "Error"

    def press_equals():

        if (
            st.session_state.calc_first_number
            is None
            or
            st.session_state.calc_operator
            is None
        ):

            return

        try:

            first = (
                st.session_state.calc_first_number
            )

            second = float(
                st.session_state.calc_display
            )

            operator = (
                st.session_state.calc_operator
            )

            result = calculate_result(
                first,
                second,
                operator
            )

            if result is None:

                st.session_state.calc_display = (
                    "Error"
                )

            else:

                st.session_state.calc_display = (
                    format_result(result)
                )

            st.session_state.calc_first_number = None

            st.session_state.calc_operator = None

            st.session_state.calc_new_number = True

        except:

            st.session_state.calc_display = "Error"

    def clear_calculator():

        st.session_state.calc_display = "0"

        st.session_state.calc_first_number = None

        st.session_state.calc_operator = None

        st.session_state.calc_new_number = True

    def delete_number():

        if st.session_state.calc_new_number:

            return

        current = (
            st.session_state.calc_display
        )

        if len(current) <= 1:

            st.session_state.calc_display = "0"

        else:

            st.session_state.calc_display = (
                current[:-1]
            )

    def plus_minus():

        if (
            st.session_state.calc_display
            == "0"
        ):

            return

        if st.session_state.calc_display.startswith("-"):

            st.session_state.calc_display = (
                st.session_state.calc_display[1:]
            )

        else:

            st.session_state.calc_display = (
                "-" +
                st.session_state.calc_display
            )

    def percentage():

        try:

            number = float(
                st.session_state.calc_display
            )

            st.session_state.calc_display = (
                format_result(
                    number / 100
                )
            )

        except:

            st.session_state.calc_display = "Error"

    # -----------------------------
    # Display
    # -----------------------------

    st.markdown(
        f"""
        <div class="calculator-display">
            {st.session_state.calc_display}
        </div>
        """,
        unsafe_allow_html=True
    )

    # ========================================================
    # ROW 1
    # AC | ± | % | ÷
    # ========================================================

    col1, col2, col3, col4 = st.columns(
        4,
        gap="small"
    )

    with col1:

        if st.button(
            "AC",
            key="calc_ac",
            use_container_width=True
        ):

            clear_calculator()

            st.rerun()

    with col2:

        if st.button(
            "±",
            key="calc_plus_minus",
            use_container_width=True
        ):

            plus_minus()

            st.rerun()

    with col3:

        if st.button(
            "%",
            key="calc_percent",
            use_container_width=True
        ):

            percentage()

            st.rerun()

    with col4:

        if st.button(
            "÷",
            key="calc_divide",
            use_container_width=True
        ):

            press_operator("÷")

            st.rerun()

    # ========================================================
    # ROW 2
    # 7 | 8 | 9 | ×
    # ========================================================

    col1, col2, col3, col4 = st.columns(
        4,
        gap="small"
    )

    with col1:

        if st.button(
            "7",
            key="calc_7",
            use_container_width=True
        ):

            press_number("7")

            st.rerun()

    with col2:

        if st.button(
            "8",
            key="calc_8",
            use_container_width=True
        ):

            press_number("8")

            st.rerun()

    with col3:

        if st.button(
            "9",
            key="calc_9",
            use_container_width=True
        ):

            press_number("9")

            st.rerun()

    with col4:

        if st.button(
            "×",
            key="calc_multiply",
            use_container_width=True
        ):

            press_operator("×")

            st.rerun()

    # ========================================================
    # ROW 3
    # 4 | 5 | 6 | -
    # ========================================================

    col1, col2, col3, col4 = st.columns(
        4,
        gap="small"
    )

    with col1:

        if st.button(
            "4",
            key="calc_4",
            use_container_width=True
        ):

            press_number("4")

            st.rerun()

    with col2:

        if st.button(
            "5",
            key="calc_5",
            use_container_width=True
        ):

            press_number("5")

            st.rerun()

    with col3:

        if st.button(
            "6",
            key="calc_6",
            use_container_width=True
        ):

            press_number("6")

            st.rerun()

    with col4:

        if st.button(
            "−",
            key="calc_minus",
            use_container_width=True
        ):

            press_operator("-")

            st.rerun()

    # ========================================================
    # ROW 4
    # 1 | 2 | 3 | +
    # ========================================================

    col1, col2, col3, col4 = st.columns(
        4,
        gap="small"
    )

    with col1:

        if st.button(
            "1",
            key="calc_1",
            use_container_width=True
        ):

            press_number("1")

            st.rerun()

    with col2:

        if st.button(
            "2",
            key="calc_2",
            use_container_width=True
        ):

            press_number("2")

            st.rerun()

    with col3:

        if st.button(
            "3",
            key="calc_3",
            use_container_width=True
        ):

            press_number("3")

            st.rerun()

    with col4:

        if st.button(
            "+",
            key="calc_plus",
            use_container_width=True
        ):

            press_operator("+")

            st.rerun()

    # ========================================================
    # ROW 5
    # 0 | . | DELETE | =
    # ========================================================

    col1, col2, col3, col4 = st.columns(
        4,
        gap="small"
    )

    with col1:

        if st.button(
            "0",
            key="calc_0",
            use_container_width=True
        ):

            press_number("0")

            st.rerun()

    with col2:

        if st.button(
            ".",
            key="calc_decimal",
            use_container_width=True
        ):

            press_decimal()

            st.rerun()

    with col3:

        if st.button(
            "⌫",
            key="calc_delete",
            use_container_width=True
        ):

            delete_number()

            st.rerun()

    with col4:

        if st.button(
            "=",
            key="calc_equals",
            use_container_width=True
        ):

            press_equals()

            st.rerun()

    st.markdown(
        "</div>",
        unsafe_allow_html=True
    )

    st.divider()

    if st.button(
        "⬅️ Back to Home",
        use_container_width=True
    ):

        st.session_state.page = "home"

        st.rerun()


# ============================================================
# GRADE CALCULATOR
# ============================================================

def grades_page():

    st.title("🎓 Grade Calculator")

    st.write(
        "Enter your subjects and marks."
    )

    number_of_subjects = st.number_input(
        "Number of subjects",
        min_value=1,
        max_value=12,
        value=5,
        step=1
    )

    subjects = []

    for i in range(
        int(number_of_subjects)
    ):

        col1, col2 = st.columns(2)

        with col1:

            name = st.text_input(
                f"Subject {i + 1}",
                key=f"grade_subject_{i}"
            )

        with col2:

            mark = st.number_input(
                f"Mark {i + 1}",
                min_value=0.0,
                max_value=100.0,
                value=0.0,
                step=1.0,
                key=f"grade_mark_{i}"
            )

        subjects.append({

            "name": name,

            "mark": mark
        })

    if st.button(
        "📊 Calculate Grades",
        use_container_width=True
    ):

        valid_subjects = [
            s
            for s in subjects
            if s["name"]
        ]

        if not valid_subjects:

            st.warning(
                "Please enter at least one subject."
            )

        else:

            total = sum(
                s["mark"]
                for s in valid_subjects
            )

            average = (
                total /
                len(valid_subjects)
            )

            st.divider()

            st.subheader(
                f"Average: {average:.2f}%"
            )

            if average >= 90:

                performance = (
                    "Excellent 🌟"
                )

            elif average >= 80:

                performance = (
                    "Very Good 🏆"
                )

            elif average >= 70:

                performance = (
                    "Good 👍"
                )

            elif average >= 60:

                performance = (
                    "Passing 🙂"
                )

            else:

                performance = (
                    "Keep Practicing 💪"
                )

            st.info(
                f"Overall performance: "
                f"{performance}"
            )

            st.divider()

            for subject in valid_subjects:

                mark = subject["mark"]

                if mark >= 90:

                    grade = "A"

                elif mark >= 80:

                    grade = "B"

                elif mark >= 70:

                    grade = "C"

                elif mark >= 60:

                    grade = "D"

                else:

                    grade = "F"

                st.write(
                    f"**{subject['name']}** — "
                    f"{mark:.0f}% — "
                    f"Grade **{grade}**"
                )

            st.divider()

            if average >= 90:

                gpa = 4.0

            elif average >= 80:

                gpa = 3.0

            elif average >= 70:

                gpa = 2.0

            elif average >= 60:

                gpa = 1.0

            else:

                gpa = 0.0

            st.metric(
                "Estimated GPA",
                f"{gpa:.1f}"
            )

            st.divider()

            st.subheader(
                "🎮 Terraria Tip"
            )

            tips = [

                "Build a small arena before fighting a boss.",

                "Keep healing potions in your hotbar.",

                "Explore underground areas for useful ores and accessories.",

                "Make several NPC houses early in the game.",

                "Always keep some blocks and a grappling hook with you.",

                "Upgrade your equipment before taking on a difficult boss."
            ]

            tip_number = (
                int(average)
                % len(tips)
            )

            st.success(
                tips[tip_number]
            )

    st.divider()

    if st.button(
        "⬅️ Back to Home",
        use_container_width=True
    ):

        st.session_state.page = "home"

        st.rerun()


# ============================================================
# PAGE ROUTER
# ============================================================

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

else:

    st.session_state.page = "home"

    st.rerun()
