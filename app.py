
import streamlit as st
import math

# ============================================================
# PAGE SETTINGS
# ============================================================

st.set_page_config(
    page_title="F1 Student Hub",
    page_icon="🏎️",
    layout="centered"
)

# ============================================================
# F1 STYLE
# ============================================================

st.markdown(
    """
    <style>
    .stApp {
        background:
            linear-gradient(135deg, #050505, #151515 50%, #250000);
        color: white;
    }

    .block-container {
        max-width: 950px;
        padding-top: 2rem;
        padding-bottom: 4rem;
    }

    h1, h2, h3 {
        color: white !important;
    }

    p, label {
        color: #eeeeee !important;
    }

    .main-title {
        text-align: center;
        font-size: 48px;
        font-weight: 900;
        color: white;
        text-transform: uppercase;
        text-shadow: 4px 4px 0px #e10600;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        color: #cccccc;
        font-size: 17px;
        margin-bottom: 30px;
    }

    .section-title {
        font-size: 30px;
        font-weight: 900;
        text-transform: uppercase;
        border-left: 6px solid #e10600;
        padding-left: 12px;
        margin-top: 25px;
        margin-bottom: 20px;
    }

    .question-number {
        text-align: center;
        background: #e10600;
        color: white;
        font-weight: 900;
        padding: 10px;
        border-radius: 5px;
        margin: 20px 0;
    }

    .score-box {
        text-align: center;
        background: #181818;
        border: 3px solid #e10600;
        border-radius: 10px;
        padding: 30px;
        margin: 25px 0;
        box-shadow: 0 0 20px rgba(225, 6, 0, 0.35);
    }

    .big-score {
        font-size: 45px;
        font-weight: 900;
        color: white;
    }

    .progress-container {
        background: #171717;
        border: 2px solid #333333;
        border-radius: 7px;
        padding: 14px;
        margin: 20px 0;
    }

    .progress-label {
        font-weight: 900;
        font-size: 14px;
        margin-bottom: 8px;
        letter-spacing: 1px;
    }

    .progress-track {
        width: 100%;
        height: 18px;
        background: #333333;
        border-radius: 4px;
        overflow: hidden;
    }

    .progress-fill {
        height: 100%;
        background: linear-gradient(90deg, #e10600, #ff3b30);
        transition: width 0.6s ease;
    }

    .progress-text {
        text-align: right;
        font-size: 12px;
        margin-top: 5px;
        color: #bbbbbb;
    }

    div.stButton > button {
        width: 100%;
        min-height: 48px;
        background: #e10600;
        color: white;
        border: none;
        border-radius: 5px;
        font-weight: 900;
        font-size: 16px;
        transition: 0.2s;
    }

    div.stButton > button:hover {
        background: #ff2018;
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(225, 6, 0, 0.4);
    }

    div[data-baseweb="input"] {
        background: #202020;
    }

    .calculator-display {
        background: #090909;
        border: 3px solid #e10600;
        border-radius: 8px;
        padding: 20px;
        text-align: right;
        font-size: 38px;
        font-weight: 900;
        margin-bottom: 20px;
        overflow-x: auto;
    }

    .grade-box {
        background: #181818;
        border: 3px solid #e10600;
        border-radius: 10px;
        padding: 25px;
        text-align: center;
        margin: 20px 0;
    }

    .grade-letter {
        font-size: 55px;
        font-weight: 900;
    }

    .terrararia-tip {
        background: #142b14;
        border: 2px solid #3b8f3b;
        border-radius: 10px;
        padding: 20px;
        margin-top: 20px;
    }

    .divider {
        border-top: 2px solid #333333;
        margin: 35px 0;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ============================================================
# SESSION STATE
# ============================================================

if "page" not in st.session_state:
    st.session_state.page = "home"

if "quiz" not in st.session_state:
    st.session_state.quiz = []

if "current_question" not in st.session_state:
    st.session_state.current_question = 0

if "answers" not in st.session_state:
    st.session_state.answers = {}

if "calculator" not in st.session_state:
    st.session_state.calculator = "0"

if "calc_old_number" not in st.session_state:
    st.session_state.calc_old_number = None

if "calc_operator" not in st.session_state:
    st.session_state.calc_operator = None

if "calc_new_number" not in st.session_state:
    st.session_state.calc_new_number = True

if "subjects" not in st.session_state:
    st.session_state.subjects = [
        {"name": "Mathematics", "marks": 100},
        {"name": "Science", "marks": 100},
        {"name": "English", "marks": 100}
    ]

if "show_grade" not in st.session_state:
    st.session_state.show_grade = False


# ============================================================
# HOME
# ============================================================

def home_page():

    st.markdown(
        '<div class="main-title">🏎️ F1 Student Hub</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">Choose an application below</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:
        if st.button("🏁 Quiz Master", use_container_width=True):
            st.session_state.page = "quiz_setup"
            st.rerun()

    with col2:
        if st.button("🧮 Calculator", use_container_width=True):
            st.session_state.page = "calculator"
            st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)

    col3, col4 = st.columns(2)

    with col3:
        if st.button("🎓 Grade Calculator", use_container_width=True):
            st.session_state.page = "grade"
            st.rerun()

    with col4:
        if st.button("👤 My Profile", use_container_width=True):
            st.session_state.page = "profile"
            st.rerun()


# ============================================================
# PROFILE
# ============================================================

def profile_page():

    st.markdown(
        '<div class="main-title">👤 My Profile</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">Fill in your information below!</div>',
        unsafe_allow_html=True
    )

    name = st.text_input("Name")
    age = st.number_input(
        "Age",
        min_value=1,
        max_value=100,
        value=13,
        step=1
    )
    school = st.text_input("School")
    subject = st.text_input("Favorite subject")
    hobby = st.text_input("Favorite hobby")

    if st.button("✨ Create My Profile", use_container_width=True):

        if name and school and subject and hobby:

            st.success("Profile created!")

            st.header(f"Hello! My name is {name}.")
            st.write(f"🎂 I am {age} years old.")
            st.write(f"🏫 I go to {school}.")
            st.write(f"📚 My favorite subject is {subject}.")
            st.write(f"🎮 I enjoy {hobby}.")

        else:
            st.warning("⚠️ Please fill in all the fields!")

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("⬅️ Back to Home", use_container_width=True):
        st.session_state.page = "home"
        st.rerun()


# ============================================================
# QUIZ SETUP
# ============================================================

def quiz_setup_page():

    st.markdown(
        '<div class="main-title">🏎️ Quiz Master</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">Create your own quiz and challenge yourself!</div>',
        unsafe_allow_html=True
    )

    number_of_questions = st.number_input(
        "Number of questions",
        min_value=1,
        max_value=20,
        value=5,
        step=1
    )

    questions = []

    for i in range(number_of_questions):

        st.markdown(
            f'<div class="section-title">📝 Question {i + 1}</div>',
            unsafe_allow_html=True
        )

        question = st.text_input(
            "Question",
            placeholder="Enter your question...",
            key=f"question_{i}"
        )

        col1, col2 = st.columns(2)

        with col1:
            choice_a = st.text_input(
                "🔵 Choice A",
                placeholder="Enter choice A",
                key=f"choice_a_{i}"
            )

        with col2:
            choice_b = st.text_input(
                "🟡 Choice B",
                placeholder="Enter choice B",
                key=f"choice_b_{i}"
            )

        col3, col4 = st.columns(2)

        with col3:
            choice_c = st.text_input(
                "🟢 Choice C",
                placeholder="Enter choice C",
                key=f"choice_c_{i}"
            )

        with col4:
            choice_d = st.text_input(
                "🔴 Choice D",
                placeholder="Enter choice D",
                key=f"choice_d_{i}"
            )

        correct = st.radio(
            "Correct answer",
            ["A", "B", "C", "D"],
            horizontal=True,
            key=f"correct_{i}"
        )

        questions.append(
            {
                "question": question,
                "A": choice_a,
                "B": choice_b,
                "C": choice_c,
                "D": choice_d,
                "correct": correct
            }
        )

    if st.button("🚀 Start Quiz", use_container_width=True):

        complete = True

        for q in questions:

            if (
                q["question"].strip() == ""
                or q["A"].strip() == ""
                or q["B"].strip() == ""
                or q["C"].strip() == ""
                or q["D"].strip() == ""
            ):
                complete = False
                break

        if complete:

            st.session_state.quiz = questions
            st.session_state.current_question = 0
            st.session_state.answers = {}
            st.session_state.page = "quiz"
            st.rerun()

        else:
            st.warning(
                "⚠️ Please fill in every question and all four choices."
            )

    if st.button("⬅️ Back to Home", use_container_width=True):
        st.session_state.page = "home"
        st.rerun()


# ============================================================
# QUIZ
# ============================================================

def quiz_page():

    quiz = st.session_state.quiz

    current = st.session_state.current_question

    total = len(quiz)

    q = quiz[current]

    st.markdown(
        '<div class="main-title">🏁 Quiz Time!</div>',
        unsafe_allow_html=True
    )

    answered_count = len(st.session_state.answers)

    progress = answered_count / total

    progress_percent = int(progress * 100)

    st.markdown(
        f'<div class="progress-container">'
        f'<div class="progress-label">'
        f'🏁 QUESTIONS ANSWERED: {answered_count} / {total}'
        f'</div>'
        f'<div class="progress-track">'
        f'<div class="progress-fill" '
        f'style="width:{progress_percent}%;"></div>'
        f'</div>'
        f'<div class="progress-text">'
        f'{progress_percent}% COMPLETE'
        f'</div>'
        f'</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f'<div class="question-number">'
        f'QUESTION {current + 1} OF {total}'
        f'</div>',
        unsafe_allow_html=True
    )

    st.subheader(q["question"])

    choices = [
        f"A. {q['A']}",
        f"B. {q['B']}",
        f"C. {q['C']}",
        f"D. {q['D']}"
    ]

    previous_answer = st.session_state.answers.get(current)

    if previous_answer:
        default_index = ["A", "B", "C", "D"].index(previous_answer)
    else:
        default_index = None

    selected = st.radio(
        "Choose your answer:",
        choices,
        index=default_index,
        key=f"answer_{current}"
    )

    if selected:

        letter = selected[0]

        st.session_state.answers[current] = letter

    col1, col2 = st.columns(2)

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

                if current in st.session_state.answers:

                    st.session_state.current_question += 1
                    st.rerun()

                else:
                    st.warning("⚠️ Please choose an answer first.")

        else:

            if st.button(
                "🏁 Finish Quiz",
                use_container_width=True
            ):

                if len(st.session_state.answers) == total:

                    st.session_state.page = "quiz_complete"
                    st.rerun()

                else:
                    st.warning(
                        "⚠️ Please answer every question before finishing."
                    )

    if st.button("🏠 Home", use_container_width=True):

        st.session_state.page = "home"
        st.rerun()


# ============================================================
# QUIZ COMPLETE
# ============================================================

def quiz_complete_page():

    quiz = st.session_state.quiz

    total = len(quiz)

    score = 0

    for i, q in enumerate(quiz):

        if st.session_state.answers.get(i) == q["correct"]:
            score += 1

    st.markdown(
        '<div class="main-title">🏁 Quiz Complete!</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f'<div class="score-box">'
        f'<div>Your Score</div>'
        f'<div class="big-score">{score} / {total}</div>'
        f'</div>',
        unsafe_allow_html=True
    )

    if score == total:

        st.success(
            "🌟 Perfect score! You got every question correct!"
        )

    elif score >= total / 2:

        st.info(
            "👍 Good job! You got more than half correct."
        )

    else:

        st.warning(
            "📚 Keep practicing! You can do even better next time."
        )

    st.markdown(
        '<div class="divider"></div>',
        unsafe_allow_html=True
    )

    st.subheader("📋 Answer Review")

    for i, q in enumerate(quiz):

        user_answer = st.session_state.answers.get(i)

        correct_answer = q["correct"]

        st.markdown(f"### Question {i + 1}")

        st.write(q["question"])

        if user_answer == correct_answer:

            st.success(
                f"✅ Correct — "
                f"{user_answer}. {q[user_answer]}"
            )

        else:

            st.error(
                f"❌ Wrong — "
                f"Your answer: {user_answer}. "
                f"{q[user_answer]}"
            )

            st.info(
                f"✅ Correct answer: "
                f"{correct_answer}. "
                f"{q[correct_answer]}"
            )

    if st.button(
        "🔄 Create New Quiz",
        use_container_width=True
    ):

        st.session_state.page = "quiz_setup"
        st.session_state.current_question = 0
        st.session_state.answers = {}
        st.rerun()

    if st.button("🏠 Home", use_container_width=True):

        st.session_state.page = "home"
        st.rerun()


# ============================================================
# CALCULATOR FUNCTIONS
# ============================================================

def calculator_number(number):

    if st.session_state.calc_new_number:

        st.session_state.calculator = number

        st.session_state.calc_new_number = False

    else:

        if st.session_state.calculator == "0":

            st.session_state.calculator = number

        else:

            st.session_state.calculator += number


def calculator_decimal():

    if st.session_state.calc_new_number:

        st.session_state.calculator = "0."
        st.session_state.calc_new_number = False

    elif "." not in st.session_state.calculator:

        st.session_state.calculator += "."


def calculator_operator(operator):

    try:

        st.session_state.calc_old_number = float(
            st.session_state.calculator
        )

        st.session_state.calc_operator = operator

        st.session_state.calc_new_number = True

    except ValueError:

        st.session_state.calculator = "0"


def calculator_equals():

    if (
        st.session_state.calc_old_number is None
        or st.session_state.calc_operator is None
    ):
        return

    try:

        first = st.session_state.calc_old_number

        second = float(st.session_state.calculator)

        operator = st.session_state.calc_operator

        if operator == "+":

            answer = first + second

        elif operator == "-":

            answer = first - second

        elif operator == "*":

            answer = first * second

        elif operator == "/":

            if second == 0:

                st.session_state.calculator = "Error"

                st.session_state.calc_old_number = None
                st.session_state.calc_operator = None
                st.session_state.calc_new_number = True

                return

            answer = first / second

        else:

            return

        if answer == int(answer):

            st.session_state.calculator = str(int(answer))

        else:

            st.session_state.calculator = str(answer)

        st.session_state.calc_old_number = None
        st.session_state.calc_operator = None
        st.session_state.calc_new_number = True

    except ValueError:

        st.session_state.calculator = "Error"


def calculator_clear():

    st.session_state.calculator = "0"

    st.session_state.calc_old_number = None

    st.session_state.calc_operator = None

    st.session_state.calc_new_number = True


def calculator_delete():

    if not st.session_state.calc_new_number:

        st.session_state.calculator = (
            st.session_state.calculator[:-1]
        )

        if st.session_state.calculator in ["", "-"]:

            st.session_state.calculator = "0"


def calculator_percent():

    try:

        number = float(st.session_state.calculator)

        answer = number / 100

        if answer == int(answer):

            st.session_state.calculator = str(int(answer))

        else:

            st.session_state.calculator = str(answer)

    except ValueError:

        st.session_state.calculator = "Error"


def calculator_plus_minus():

    if st.session_state.calculator != "0":

        if st.session_state.calculator.startswith("-"):

            st.session_state.calculator = (
                st.session_state.calculator[1:]
            )

        else:

            st.session_state.calculator = (
                "-" + st.session_state.calculator
            )


# ============================================================
# CALCULATOR PAGE
# ============================================================

def calculator_page():

    st.markdown(
        '<div class="main-title">🧮 Calculator</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f'<div class="calculator-display">'
        f'{st.session_state.calculator}'
        f'</div>',
        unsafe_allow_html=True
    )

    # ROW 1

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.button(
            "AC",
            key="calc_ac",
            use_container_width=True,
            on_click=calculator_clear
        )

    with col2:
        st.button(
            "±",
            key="calc_pm",
            use_container_width=True,
            on_click=calculator_plus_minus
        )

    with col3:
        st.button(
            "%",
            key="calc_percent",
            use_container_width=True,
            on_click=calculator_percent
        )

    with col4:
        st.button(
            "÷",
            key="calc_divide",
            use_container_width=True,
            on_click=calculator_operator,
            args=("/",)
        )

    # ROW 2

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.button(
            "7",
            key="calc_7",
            use_container_width=True,
            on_click=calculator_number,
            args=("7",)
        )

    with col2:
        st.button(
            "8",
            key="calc_8",
            use_container_width=True,
            on_click=calculator_number,
            args=("8",)
        )

    with col3:
        st.button(
            "9",
            key="calc_9",
            use_container_width=True,
            on_click=calculator_number,
            args=("9",)
        )

    with col4:
        st.button(
            "×",
            key="calc_multiply",
            use_container_width=True,
            on_click=calculator_operator,
            args=("*",)
        )

    # ROW 3

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.button(
            "4",
            key="calc_4",
            use_container_width=True,
            on_click=calculator_number,
            args=("4",)
        )

    with col2:
        st.button(
            "5",
            key="calc_5",
            use_container_width=True,
            on_click=calculator_number,
            args=("5",)
        )

    with col3:
        st.button(
            "6",
            key="calc_6",
            use_container_width=True,
            on_click=calculator_number,
            args=("6",)
        )

    with col4:
        st.button(
            "−",
            key="calc_minus",
            use_container_width=True,
            on_click=calculator_operator,
            args=("-",)
        )

    # ROW 4

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.button(
            "1",
            key="calc_1",
            use_container_width=True,
            on_click=calculator_number,
            args=("1",)
        )

    with col2:
        st.button(
            "2",
            key="calc_2",
            use_container_width=True,
            on_click=calculator_number,
            args=("2",)
        )

    with col3:
        st.button(
            "3",
            key="calc_3",
            use_container_width=True,
            on_click=calculator_number,
            args=("3",)
        )

    with col4:
        st.button(
            "+",
            key="calc_plus",
            use_container_width=True,
            on_click=calculator_operator,
            args=("+",)
        )

    # ROW 5

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.button(
            "⌫",
            key="calc_delete",
            use_container_width=True,
            on_click=calculator_delete
        )

    with col2:
        st.button(
            "0",
            key="calc_0",
            use_container_width=True,
            on_click=calculator_number,
            args=("0",)
        )

    with col3:
        st.button(
            ".",
            key="calc_decimal",
            use_container_width=True,
            on_click=calculator_decimal
        )

    with col4:
        st.button(
            "=",
            key="calc_equals",
            use_container_width=True,
            on_click=calculator_equals
        )

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("🏠 Back to Home", use_container_width=True):

        st.session_state.page = "home"
        st.rerun()


# ============================================================
# GRADE CALCULATOR
# ============================================================

def get_grade(percentage):

    if percentage >= 90:
        return "A+"

    elif percentage >= 85:
        return "A"

    elif percentage >= 80:
        return "A-"

    elif percentage >= 75:
        return "B+"

    elif percentage >= 70:
        return "B"

    elif percentage >= 65:
        return "B-"

    elif percentage >= 60:
        return "C+"

    elif percentage >= 55:
        return "C"

    elif percentage >= 50:
        return "D"

    else:
        return "F"


def get_gpa(percentage):

    if percentage >= 90:
        return 4.0

    elif percentage >= 85:
        return 3.7

    elif percentage >= 80:
        return 3.3

    elif percentage >= 75:
        return 3.0

    elif percentage >= 70:
        return 2.7

    elif percentage >= 65:
        return 2.3

    elif percentage >= 60:
        return 2.0

    elif percentage >= 55:
        return 1.5

    elif percentage >= 50:
        return 1.0

    else:
        return 0.0


def reset_grade():

    st.session_state.subjects = [
        {"name": "Mathematics", "marks": 100},
        {"name": "Science", "marks": 100},
        {"name": "English", "marks": 100}
    ]

    st.session_state.show_grade = False


def grade_page():

    st.markdown(
        '<div class="main-title">🎓 Grade Calculator</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">'
        'Calculate your marks, percentage, grade and GPA'
        '</div>',
        unsafe_allow_html=True
    )

    st.subheader("📚 Your Subjects")

    for i, subject in enumerate(st.session_state.subjects):

        col1, col2 = st.columns([2, 1])

        with col1:

            name = st.text_input(
                "Subject",
                value=subject["name"],
                key=f"grade_name_{i}"
            )

        with col2:

            marks = st.number_input(
                "Marks",
                min_value=0,
                max_value=100,
                value=int(subject["marks"]),
                step=1,
                key=f"grade_marks_{i}"
            )

        st.session_state.subjects[i]["name"] = name
        st.session_state.subjects[i]["marks"] = marks

    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            "➕ Add Subject",
            use_container_width=True
        ):

            number = len(st.session_state.subjects) + 1

            st.session_state.subjects.append(
                {
                    "name": f"Subject {number}",
                    "marks": 0
                }
            )

            st.session_state.show_grade = False

            st.rerun()

    with col2:

        if st.button(
            "🗑️ Reset",
            use_container_width=True
        ):

            reset_grade()
            st.rerun()

    if st.button(
        "🎯 Calculate My Grade",
        use_container_width=True
    ):

        st.session_state.show_grade = True

    if st.session_state.show_grade:

        subjects = st.session_state.subjects

        total_marks = sum(
            subject["marks"]
            for subject in subjects
        )

        maximum_marks = len(subjects) * 100

        if maximum_marks > 0:

            percentage = (
                total_marks / maximum_marks
            ) * 100

        else:

            percentage = 0

        grade = get_grade(percentage)

        gpa = get_gpa(percentage)

        st.divider()

        st.subheader("📊 Your Results")

        col1, col2, col3 = st.columns(3)

        with col1:

            st.metric(
                "Total Marks",
                f"{total_marks}/{maximum_marks}"
            )

        with col2:

            st.metric(
                "Percentage",
                f"{percentage:.1f}%"
            )

        with col3:

            st.metric(
                "GPA",
                f"{gpa:.2f}/4.0"
            )

        st.markdown(
            f'<div class="grade-box">'
            f'<div>Overall Grade</div>'
            f'<div class="grade-letter">{grade}</div>'
            f'<div>Average: {percentage:.1f}%</div>'
            f'</div>',
            unsafe_allow_html=True
        )

        st.write("📈 Overall Performance")

        st.progress(
            min(max(percentage / 100, 0), 1)
        )

        st.subheader("📚 Subject Results")

        for subject in subjects:

            subject_grade = get_grade(
                subject["marks"]
            )

            col1, col2, col3 = st.columns(
                [2, 1, 1]
            )

            with col1:
                st.write(
                    f"**{subject['name']}**"
                )

            with col2:
                st.write(
                    f"{subject['marks']}/100"
                )

            with col3:
                st.write(
                    f"**{subject_grade}**"
                )

        if percentage >= 90:

            st.success(
                "🏆 Outstanding! You're doing amazing!"
            )

        elif percentage >= 75:

            st.success(
                "👏 Great job! Keep it up!"
            )

        elif percentage >= 60:

            st.info(
                "📘 Good effort! Keep improving!"
            )

        elif percentage >= 50:

            st.warning(
                "💪 You're passing, but there's room to improve!"
            )

        else:

            st.error(
                "📚 Keep practicing. You can improve!"
            )

        # Terraria tip

        st.markdown(
            '<div class="terrararia-tip">'
            '<h3>🌲 Terraria Tip</h3>'
            '<p>'
            'Explore underground areas and collect useful '
            'materials early. Building a good base and '
            'preparing your equipment will make your '
            'adventures much easier!'
            '</p>'
            '</div>',
            unsafe_allow_html=True
        )

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("🏠 Back to Home", use_container_width=True):

        st.session_state.page = "home"
        st.rerun()


# ============================================================
# PAGE ROUTER
# ============================================================

if st.session_state.page == "home":

    home_page()

elif st.session_state.page == "profile":

    profile_page()

elif st.session_state.page == "quiz_setup":

    quiz_setup_page()

elif st.session_state.page == "quiz":

    quiz_page()

elif st.session_state.page == "quiz_complete":

    quiz_complete_page()

elif st.session_state.page == "calculator":

    calculator_page()

elif st.session_state.page == "grade":

    grade_page()