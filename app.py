import streamlit as st
import math

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
            circle at 50% 20%,
            #260909 0%,
            #111111 45%,
            #050505 100%
        );
}

/* THICK STATIC RED LINES */

.race-lines {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: 0;
    pointer-events: none;

    background:
        repeating-linear-gradient(
            90deg,
            transparent 0px,
            transparent 55px,
            rgba(225, 6, 0, 0.75) 55px,
            rgba(225, 6, 0, 0.75) 75px,
            transparent 75px,
            transparent 140px
        );
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

/* TOP F1 STRIPE */

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
}

/* RED BUTTONS */

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
        0 5px 15px rgba(225, 6, 0, 0.45);
}

.stButton > button:active {
    background-color: #8f0400 !important;
    transform: translateY(1px);
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
    min-height: 60px;

    font-size: 22px;
    font-weight: bold;

    border-radius: 10px;
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

</style>

<div class="f1-racing-stripes"></div>
<div class="race-lines"></div>

""", unsafe_allow_html=True)


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


# =========================================================
# PROFILE PAGE
# =========================================================

def profile_page():

    st.title("👤 My Profile")

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

            st.header(
                f"Hello! My name is {name}."
            )

            st.write(f"🎂 I am {age} years old.")
            st.write(f"🏫 I go to {school}.")
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


# =========================================================
# CALCULATOR PAGE
# =========================================================

def calculator_page():

    st.title("🧮 Calculator")

    st.markdown(
        '<div class="calculator-container">',
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


# =========================================================
# GRADE CALCULATOR
# =========================================================

def grades_page():

    st.title("📊 Grade Calculator")

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

        st.subheader(
            f"Average: {average:.1f}%"
        )

        if average >= 90:

            grade = "A"

        elif average >= 80:

            grade = "B"

        elif average >= 70:

            grade = "C"

        elif average >= 60:

            grade = "D"

        else:

            grade = "F"

        st.success(
            f"Overall Grade: {grade}"
        )

        if average >= 90:

            st.write(
                "🏆 Excellent work!"
            )

        elif average >= 80:

            st.write(
                "🔥 Great job! Keep it up!"
            )

        elif average >= 70:

            st.write(
                "👍 Good work!"
            )

        elif average >= 60:

            st.write(
                "📚 Keep practicing!"
            )

        else:

            st.write(
                "💪 Keep studying and don't give up!"
            )

        st.divider()

        st.subheader(
            "🎮 Terraria Tip"
        )

        st.info(
            "Build a safe base before exploring dangerous areas!"
        )

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

        st.subheader(
            f"Question {i + 1}"
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

        st.divider()

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

    st.subheader(
        f"Question {current + 1} of {len(questions)}"
    )

    st.write(
        question["question"]
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

    st.metric(
        "Score",
        f"{score}/{len(questions)}"
    )

    st.progress(
        percentage / 100
    )

    st.subheader(
        f"You scored {percentage:.0f}%"
    )

    st.divider()

    for i, question in enumerate(questions):

        st.write(
            f"**{i + 1}. {question['question']}**"
        )

        user_answer = answers[i]

        correct_answer = question["correct"]

        if user_answer == correct_answer:

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
