import streamlit as st
import random
import matplotlib.pyplot as plt

# 1. Create randomized cabinets
def create_filing_cabinets():
    cabinets = list(range(1, 101))
    random.shuffle(cabinets)
    return cabinets

# 2. Loop strategy for one employee
def run_employee_strategy(employee_id, cabinets, max_attempts=50):
    next_cabinet = employee_id
    for _ in range(max_attempts):
        found_id = cabinets[next_cabinet - 1]
        if found_id == employee_id:
            return True
        next_cabinet = found_id
    return False

# ❗ 3. Rename this to match the new brand
def simulate_abyssal_paper_round():
    cabinets = create_filing_cabinets()
    for employee_id in range(1, 101):
        if not run_employee_strategy(employee_id, cabinets):
            return False
    return True

# 4. Simulate multiple rounds
def run_simulations(num_simulations=1000):
    success_count = 0
    for _ in range(num_simulations):
        if simulate_abyssal_paper_round():  # match new function name
            success_count += 1
    return success_count

# 5. Streamlit UI
st.title("📎 Abyssal Paper: Folder Retrieval Protocol")

simulations = st.slider("Number of simulations to run", min_value=100, max_value=5000, step=100, value=1000)

if st.button("Run Simulation"):
    successes = run_simulations(simulations)
    failures = simulations - successes

    st.write(f"Out of {simulations} runs:")
    st.success(f"Escapes: {successes}")
    st.error(f"Back to Cubicles: {failures}")

    fig, ax = plt.subplots()
    ax.bar(['Escaped', 'Back to Cubicles'], [successes, failures], color=['green', 'gray'])
    ax.set_ylabel("Number of Runs")
    ax.set_title("Abyssal Paper — Protocol 100-P Results")
    st.pyplot(fig)

# =========================
# Single Employee + Team Follow-Up (Fixed and Enhanced)
# =========================
import time

# --- Session counters (persist across reruns) ---
if "dept_escapes" not in st.session_state:
    st.session_state.dept_escapes = 0
if "dept_failures" not in st.session_state:
    st.session_state.dept_failures = 0

# (1) Helper – render a 10x10 grid of squares with optional labels
def render_grid(box_colors, labels=None, cell_size=28, text_colors=None):
    if labels is None:
        labels = [str(i+1) for i in range(100)]
    if text_colors is None:
        text_colors = ['black'] * 100
    rows = [st.columns(10) for _ in range(10)]
    for i in range(10):
        for j in range(10):
            idx = i * 10 + j
            color = box_colors[idx]
            text = labels[idx]
            text_color = text_colors[idx]
            with rows[i][j]:
                st.markdown(
                    f"""
                    <div style="
                        width:{cell_size}px;
                        height:{cell_size}px;
                        background-color:{color};
                        color:{text_color};
                        border-radius:4px;
                        border:1px solid #888;
                        text-align:center;
                        line-height:{cell_size}px;
                        font-size:12px;
                        user-select:none;">
                        {text}
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

# (2) Loop-following strategy
def follow_employee_path(employee_id, cabinets, max_attempts=50):
    path = []
    next_cabinet = employee_id
    for _ in range(max_attempts):
        path.append(next_cabinet)
        found_id = cabinets[next_cabinet - 1]
        if found_id == employee_id:
            return True, path
        next_cabinet = found_id
    return False, path

# Divider
st.markdown("---")
st.header("👤 Try as One Employee, then Watch the Team")

# Layout: left main / right counters
left, right = st.columns([4, 1])
with right:
    stats_placeholder = st.empty()
    stats_placeholder.metric("All Escaped (lifetime)", st.session_state.dept_escapes)
    stats_placeholder.metric("Back to Work (lifetime)", st.session_state.dept_failures)

with left:
    employee_id = st.number_input(
        "Choose your Employee ID (1–100)", min_value=1, max_value=100, value=73
    )
    start_single_sim = st.button("Start Single Simulation")

    if start_single_sim:
        cabinets = create_filing_cabinets()
        st.session_state.last_cabinets = cabinets
        st.session_state.last_first_employee = employee_id

        box_colors = ["#d3d3d3"] * 100
        text_colors = ["black"] * 100
        grid_placeholder = st.empty()

        result, path = follow_employee_path(employee_id, cabinets)
        st.session_state.last_success = result  # Save for later use

        for step, cab in enumerate(path):
            if step == len(path) - 1 and result:
                box_colors[cab - 1] = "white"
                text_colors[cab - 1] = "green"
            else:
                box_colors[cab - 1] = "green"
            with grid_placeholder.container():
                render_grid(box_colors, text_colors=text_colors)
            time.sleep(0.04)

        if not result:
            box_colors[path[-1] - 1] = "red"
            with grid_placeholder.container():
                render_grid(box_colors)
            st.error(f"🟥 Employee #{employee_id} failed to find their folder. Back to work.")
        else:
            with grid_placeholder.container():
                render_grid(box_colors, text_colors=text_colors)
            st.success(f"✅ Employee #{employee_id} found their folder!")

# === Watch the Team Simulation Block ===
# Only show after solo simulation has run
if "last_cabinets" in st.session_state and "last_first_employee" in st.session_state:
    st.markdown("### 🧑‍🤝‍🧑 Now simulate the **rest of the department**")
    batch_delay = st.slider("Batch delay (seconds)", 0.0, 1.0, 0.2, 0.1, key="delay_slider")
    go_team = st.button("Run Department Simulation (99 employees in groups of 10)", key="go_team_button")

    if go_team:
        cabinets = st.session_state.last_cabinets
        employee_id = st.session_state.last_first_employee
        first_success = st.session_state.last_success

        emp_colors = ["#d3d3d3"] * 100
        emp_labels = [str(i+1) for i in range(100)]

        emp_colors[employee_id - 1] = "green" if first_success else "red"

        team_placeholder = st.empty()
        with team_placeholder.container():
            render_grid(emp_colors, labels=emp_labels, cell_size=26)

        group_failed = not first_success
        remaining = [i for i in range(1, 101) if i != employee_id]

        for start in range(0, len(remaining), 10):
            batch = remaining[start:start+10]
            for emp in batch:
                emp_success = run_employee_strategy(emp, cabinets)
                emp_colors[emp - 1] = "green" if emp_success else "red"
                if not emp_success:
                    group_failed = True
            with team_placeholder.container():
                render_grid(emp_colors, labels=emp_labels, cell_size=26)
            time.sleep(batch_delay)

        if group_failed:
            st.error("🟥 Department result: Someone failed. Back to work.")
            st.session_state.dept_failures += 1
        else:
            st.success("✅ Department result: All 100 found their folders. Freedom!")
            st.session_state.dept_escapes += 1

        # Update stats
        stats_placeholder.metric("All Escaped (lifetime)", st.session_state.dept_escapes)
        stats_placeholder.metric("Back to Work (lifetime)", st.session_state.dept_failures)
        