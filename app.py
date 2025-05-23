import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

# Make sure the app runs locally
# To run this app locally, use: streamlit run app.py

# Configure page settings for mobile
st.set_page_config(
    page_title="My Mobile App",
    page_icon="📱",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS to make it more mobile-friendly with improved header and spacing
st.markdown("""
<style>
    /* Base styles */
    .block-container {
        padding-top: 0.5rem;
        padding-bottom: 1rem;
    }
    .st-emotion-cache-16txtl3 h1 {
        font-size: 1.8rem;
        color: #4F46E5; /* Updated to a modern indigo */
    }
    .st-emotion-cache-16txtl3 h2 {
        font-size: 1.4rem;
        color: #4F46E5; /* Matching subheader color */
    }
    button {
        width: 100%;
    }
    input {
        font-size: 1rem !important;
    }
    
    /* Header styling - updated with modernized gradient */
    .header-container {
        background: linear-gradient(135deg, #6366F1, #4F46E5);
        padding: 1.5rem 1rem;
        border-radius: 12px;
        color: white;
        margin-bottom: 1.5rem;
        box-shadow: 0 4px 12px rgba(99, 102, 241, 0.2);
    }
    .app-header {
        color: white !important;
        margin: 0;
        font-size: 1.8rem !important;
    }
    .header-date {
        color: rgba(255, 255, 255, 0.8);
        margin-top: 0.5rem;
        font-size: 0.9rem;
    }
    
    /* Link styling */
    .forgot-password {
        text-align: right;
        color: #F87171;
        text-decoration: underline;
        cursor: pointer;
        margin-bottom: 1rem;
        font-size: 0.9rem;
    }
    
    /* Main dashboard cards - updated color scheme */
    .metric-card {
        background-color: #F9FAFB; /* Light gray background */
        border-radius: 12px;
        padding: 1.2rem;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
        text-align: center;
        border-left: 4px solid #6366F1; /* Indigo border */
        margin-bottom: 0.8rem;
        transition: transform 0.2s ease;
    }
    .metric-card:hover {
        transform: translateY(-2px);
    }
    
    /* Enhanced sidebar */
    .css-1d391kg, .css-1cypcdb {
        background-color: #F3F4F6 !important;
    }
    .css-zt5igj {
        border-right-color: #E5E7EB !important;
    }
    [data-testid="stSidebar"] {
        background-color: #F3F4F6;
        border-right: 1px solid #E5E7EB;
    }
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] {
        padding-top: 1rem;
    }
    
    /* Custom sidebar navigation styles */
    .sidebar-nav {
        padding: 0.5rem;
    }
    .sidebar-nav-item {
        padding: 0.75rem 1rem;
        border-radius: 8px;
        margin-bottom: 0.5rem;
        cursor: pointer;
        transition: all 0.2s ease;
        display: flex;
        align-items: center;
        color: #4B5563;
    }
    .sidebar-nav-item:hover {
        background-color: rgba(99, 102, 241, 0.1);
    }
    .sidebar-nav-item.active {
        background-color: rgba(99, 102, 241, 0.15);
        color: #4F46E5;
        font-weight: 500;
    }
    .sidebar-nav-icon {
        margin-right: 10px;
        width: 20px;
        text-align: center;
    }
    
    /* Navigation bar - updated with modern look */
    .nav-bar {
        background-color: #FFFFFF;
        padding: 0.65rem 0.5rem 0.5rem 0.5rem;
        border-radius: 16px 16px 0 0;
        margin-top: 1rem;
        border-top: 2px solid #E5E7EB;
        position: fixed;
        bottom: 0;
        left: 0;
        right: 0;
        z-index: 1000;
        box-shadow: 0 -2px 10px rgba(0, 0, 0, 0.05);
    }
    
    /* Improved form controls */
    div[data-baseweb="select"] {
        border-radius: 8px !important;
    }
    div[data-baseweb="base-input"] {
        border-radius: 8px !important;
    }
    
    /* Improved task and note cards */
    .task-item {
        padding: 1rem;
        border-radius: 10px;
        margin-bottom: 0.8rem;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.05);
        transition: transform 0.2s ease;
    }
    .task-item:hover {
        transform: translateY(-2px);
    }
    .high-priority {
        background-color: rgba(239, 68, 68, 0.1);
        border-left: 4px solid #EF4444;
    }
    .medium-priority {
        background-color: rgba(245, 158, 11, 0.1);
        border-left: 4px solid #F59E0B;
    }
    .low-priority {
        background-color: rgba(16, 185, 129, 0.1);
        border-left: 4px solid #10B981;
    }
    
    /* Fix for very small screens */
    @media screen and (max-width: 320px) {
        .header-container {
            padding: 1rem 0.5rem;
        }
        .app-header {
            font-size: 1.5rem !important;
        }
        .metric-card {
            padding: 0.75rem;
        }
    }
    
    /* Extra padding at the bottom to prevent content being hidden by navbar */
    .content-container {
        padding-bottom: 70px;
    }
    
    /* Floating action button */
    .floating-btn {
        position: fixed;
        right: 20px;
        bottom: 80px;
        width: 56px;
        height: 56px;
        border-radius: 28px;
        background: linear-gradient(135deg, #6366F1, #4F46E5);
        color: white;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 24px;
        box-shadow: 0 4px 10px rgba(99, 102, 241, 0.3);
        cursor: pointer;
        z-index: 999;
        transition: transform 0.2s, box-shadow 0.2s;
    }
    .floating-btn:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(99, 102, 241, 0.4);
    }
</style>
""", unsafe_allow_html=True)
# Device detection without deprecated experimental_get_query_params
def get_device_type():
    # Use session state for device detection
    if "device_detected" not in st.session_state:
        st.session_state["device_detected"] = "responsive"
        
    # Let user manually set their device type
    if st.sidebar.checkbox("Override device detection", value=False):
        device_option = st.sidebar.radio(
            "Select your device type:",
            options=["Mobile", "Desktop", "Responsive"],
            index=2
        )
        st.session_state["device_detected"] = device_option.lower()
    
    return st.session_state["device_detected"]

def login_page():
    # Check if we're on mobile and adjust UI accordingly
    device = get_device_type()
    
    st.markdown('<div class="header-container"><h1 class="app-header">🐝 Taskbee </h1></div>', unsafe_allow_html=True)
    
    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submit_button = st.form_submit_button("Login")
        
        if submit_button:
            # This is a simple demo - in a real app, you'd validate against a database
            if username == "demo" and password == "password":
                st.session_state["logged_in"] = True
                st.rerun()
            else:
                st.error("Invalid username or password")
    
    # Responsive forgot password link
    st.markdown('<p class="forgot-password">Forgot Password?</p>', unsafe_allow_html=True)
    
    forgot_pwd = st.button("Reset Password")
    if forgot_pwd:
        email = st.text_input("Enter your email address")
        if st.button("Send Reset Link"):
            if email:
                st.success("Password reset link sent to your email!")
            else:
                st.warning("Please enter your email address")
    
    # Quick access for demo purposes
    if st.button("Demo Login (Skip)"):
        st.session_state["logged_in"] = True
        st.rerun()

# Define page functions
def show_dashboard():
    st.header("Dashboard")
    
    # Summary cards with improved styling
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="metric-card">
            <h3>Tasks</h3>
            <h2>5</h2>
            <p style="color: green;">+2</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="metric-card">
            <h3>Notes</h3>
            <h2>8</h2>
            <p style="color: red;">-1</p>
        </div>
        """, unsafe_allow_html=True)

    # Activity chart
    st.subheader("Weekly Activity")
    chart_data = pd.DataFrame({
        'Day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
        'Activity': [3, 1, 5, 2, 4, 6, 2]
    })
    
    # Custom color for chart - using the new warm color palette
    fig, ax = plt.subplots(figsize=(10, 4))
    bars = ax.bar(chart_data['Day'], chart_data['Activity'], color=['#FF6B6B', '#FF7B59', '#FF8E53', '#FFA14C', '#FFB347', '#FFC447', '#FFD447'])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('#DDDDDD')
    ax.spines['bottom'].set_color('#DDDDDD')
    ax.tick_params(bottom=False, left=False)
    ax.set_axisbelow(True)
    ax.yaxis.grid(True, color='#EEEEEE')
    ax.xaxis.grid(False)
    
    st.pyplot(fig)
    
    # Recent items
    st.subheader("Recent Items")
    with st.container():
        for i in range(3):
            st.info(f"Item {i+1}: Updated recently")

def show_tasks():
    st.header("Tasks")
    
    # Add new task - improved mobile UI
    with st.form("new_task", clear_on_submit=True):
        task = st.text_input("New Task")
        col1, col2 = st.columns(2)
        with col1:
            priority = st.select_slider("Priority", options=["Low", "Medium", "High"])
        with col2:
            due_date = st.date_input("Due date")
        submit = st.form_submit_button("Add Task", use_container_width=True)
    
    # Sample tasks
    tasks = [
        {"name": "Complete mobile app design", "priority": "High", "done": False},
        {"name": "Meeting with client", "priority": "Medium", "done": False},
        {"name": "Update documentation", "priority": "Low", "done": True},
        {"name": "Fix login bug", "priority": "High", "done": False}
    ]
    
    # Display tasks with improved mobile UI
    st.subheader("Task List")
    
    # Add task filter for better mobile experience
    filter_col1, filter_col2 = st.columns(2)
    with filter_col1:
        filter_option = st.selectbox("Filter by", ["All", "High Priority", "Medium Priority", "Low Priority", "Completed"])
    with filter_col2:
        sort_option = st.selectbox("Sort by", ["Priority", "Name", "Status"])
    
    # Apply filters (in a real app, this would filter the tasks)
    filtered_tasks = tasks  # Placeholder for filtered tasks
    
    # Mobile-friendly task list with swipe actions hint
    st.markdown("<p style='font-size:0.8rem; color:gray;'>Swipe task left for more options</p>", unsafe_allow_html=True)
    
    for i, task in enumerate(filtered_tasks):
        col1, col2, col3 = st.columns([0.1, 0.8, 0.1])
        with col1:
            done = st.checkbox("", task["done"], key=f"task_{i}")
        with col2:
            if task["priority"] == "High":
                st.markdown(f"""<div style="padding: 0.5rem; border-radius: 4px; background-color: rgba(255,107,107,0.1);">
                    <span style="font-weight: bold;">{task['name']}</span> <span style="color: #FF6B6B;">●</span>
                </div>""", unsafe_allow_html=True)
            elif task["priority"] == "Medium":
                st.markdown(f"""<div style="padding: 0.5rem; border-radius: 4px; background-color: rgba(255,142,83,0.1);">
                    <span style="font-weight: bold;">{task['name']}</span> <span style="color: #FF8E53;">●</span>
                </div>""", unsafe_allow_html=True)
            else:
                st.markdown(f"""<div style="padding: 0.5rem; border-radius: 4px; background-color: rgba(255,212,71,0.1);">
                    <span style="font-weight: bold;">{task['name']}</span> <span style="color: #FFD447;">●</span>
                </div>""", unsafe_allow_html=True)
        with col3:
            st.button("⋮", key=f"menu_{i}")

def show_notes():
    st.header("Notes")
    
    # Add new note with improved mobile UI
    with st.form("new_note", clear_on_submit=True):
        note_title = st.text_input("Title")
        note_content = st.text_area("Content", height=100)
        col1, col2 = st.columns(2)
        with col1:
            category = st.selectbox("Category", ["Personal", "Work", "Ideas", "Other"])
        with col2:
            color = st.color_picker("Color", "#FF6B6B")
        submit = st.form_submit_button("Save Note", use_container_width=True)
    
    # Sample notes
    notes = [
        {"title": "Meeting notes", "date": "May 20, 2025", "preview": "Discussed project timeline and...", "category": "Work"},
        {"title": "Ideas for new features", "date": "May 18, 2025", "preview": "1. Add dark mode 2. Implement...", "category": "Ideas"},
        {"title": "Bugs to fix", "date": "May 15, 2025", "preview": "Login screen on iPhone has alignment...", "category": "Work"}
    ]
    
    # Search box for notes - mobile friendly
    search = st.text_input("🔍 Search notes", placeholder="Type to search")
    
    # Filter for better mobile experience
    filter_category = st.selectbox("Filter by category", ["All", "Work", "Personal", "Ideas", "Other"])
    
    # Display notes with improved mobile UX
    for note in notes:
        # Apply filters in a real app
        if filter_category != "All" and note["category"] != filter_category:
            continue
            
        with st.expander(f"📝 {note['title']} - {note['date']}"):
            st.write(note["preview"])
            st.caption(f"Category: {note.get('category', 'Uncategorized')}")
            
            # Mobile-friendly button row
            col1, col2, col3 = st.columns(3)
            with col1:
                st.button("📝 Edit", key=f"edit_{note['title']}", use_container_width=True)
            with col2:
                st.button("🔖 Tag", key=f"tag_{note['title']}", use_container_width=True)
            with col3:
                st.button("🗑️ Delete", key=f"delete_{note['title']}", use_container_width=True)

def show_profile():
    st.header("User Profile")
    
    # Profile info with improved mobile layout
    col1, col2 = st.columns([1, 2])
    with col1:
        # Use a local placeholder instead of external URL
        st.markdown(
            """
            <div style="width:100px; height:100px; border-radius:50%; background-color:#3A0CA3; 
            display:flex; align-items:center; justify-content:center; color:white; font-size:36px;">
            DU
            </div>
            """, 
            unsafe_allow_html=True
        )
        st.button("Change Photo", use_container_width=True)
    with col2:
        st.subheader("Demo User")
        st.write("demo@example.com")
        st.write("Member since: Jan 2025")
        st.button("Edit Profile", use_container_width=True)
    
    # Settings with better organized tabs for mobile
    tab1, tab2, tab3 = st.tabs(["Account", "Notifications", "Appearance"])
    
    with tab1:
        st.subheader("Account Settings")
        st.text_input("Name", value="Demo User")
        st.text_input("Email", value="demo@example.com")
        st.button("Change Password", use_container_width=True)
        st.button("Delete Account", use_container_width=True, type="secondary")
        
    with tab2:
        st.subheader("Notification Settings")
        st.toggle("Push Notifications", value=True)
        st.toggle("Email Notifications", value=True)
        st.toggle("Task Reminders", value=True)
        st.number_input("Reminder Time (minutes before)", min_value=5, max_value=60, value=15, step=5)
        
    with tab3:
        st.subheader("Appearance")
        st.toggle("Dark Mode")
        theme = st.selectbox("Theme Color", ["Coral (Default)", "Blue", "Green", "Purple"])
        font_size = st.select_slider("Font Size", options=["Small", "Medium", "Large"])
        st.button("Apply Settings", use_container_width=True)
    
    # Mobile-optimized stats
    st.subheader("Your Activity")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Completed Tasks", "42", "+5")
    with col2:
        st.metric("Active Notes", "8", "-1")
        
    # Add space at bottom to prevent fixed navbar overlay
    st.markdown("<div style='height:60px'></div>", unsafe_allow_html=True)
    
    # Logout button
    if st.button("Logout", use_container_width=True):
        st.session_state["logged_in"] = False
        st.rerun()

# Main app interface
def main_app():
    # Sidebar navigation - collapsed by default on mobile
    with st.sidebar:
        st.title("Navigation")
        # Device selection option moved to sidebar for better access
        device_type = get_device_type()
        st.write(f"Current mode: {device_type.capitalize()}")
        
        page = st.radio("Go to", ["Dashboard", "Tasks", "Notes", "Profile"])
    
    # Header with date and notification count - improved layout
    st.markdown(
        f"""
        <div class="header-container">
            <h1 class="app-header">🐝 Taskbee</h1>
            <p class="header-date">{datetime.now().strftime('%A, %B %d, %Y')}</p>
        </div>
        """, 
        unsafe_allow_html=True
    )
    
    # Notification button
    col1, col2 = st.columns([3, 1])
    with col2:
        st.button("🔔 3")
    
    # Wrap content in container for proper spacing with fixed nav
    st.markdown('<div class="content-container">', unsafe_allow_html=True)
    
    # Pages content - handle both sidebar navigation and bottom nav bar
    current_page = st.session_state.get("current_page", "Dashboard")
    
    # Update the current page in session state based on sidebar selection
    if page != current_page:
        st.session_state["current_page"] = page
        current_page = page
        
    # Display the appropriate page content
    if current_page == "Dashboard":
        show_dashboard()
    elif current_page == "Tasks":
        show_tasks()
    elif current_page == "Notes":
        show_notes()
    elif current_page == "Profile":
        show_profile()
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Bottom navigation bar (mobile style) - fixed position
    st.markdown('<div class="nav-bar">', unsafe_allow_html=True)
    cols = st.columns(4)
    
    # Active page indicator style
    dashboard_style = "color: #4361EE; font-weight: bold;" if current_page == "Dashboard" else "color: inherit;"
    tasks_style = "color: #4361EE; font-weight: bold;" if current_page == "Tasks" else "color: inherit;"
    notes_style = "color: #4361EE; font-weight: bold;" if current_page == "Notes" else "color: inherit;"
    profile_style = "color: #4361EE; font-weight: bold;" if current_page == "Profile" else "color: inherit;"
    
    with cols[0]:
        if st.button(f"🏠", key="home_btn", help="Dashboard", use_container_width=True):
            st.session_state["current_page"] = "Dashboard"
            st.rerun()
        st.markdown(f"<div style='text-align: center; font-size: 0.7rem; {dashboard_style}'>Home</div>", unsafe_allow_html=True)
    with cols[1]:
        if st.button(f"✓", key="tasks_btn", help="Tasks", use_container_width=True):
            st.session_state["current_page"] = "Tasks"
            st.rerun()
        st.markdown(f"<div style='text-align: center; font-size: 0.7rem; {tasks_style}'>Tasks</div>", unsafe_allow_html=True)
    with cols[2]:
        if st.button(f"📝", key="notes_btn", help="Notes", use_container_width=True):
            st.session_state["current_page"] = "Notes"
            st.rerun()
        st.markdown(f"<div style='text-align: center; font-size: 0.7rem; {notes_style}'>Notes</div>", unsafe_allow_html=True)
    with cols[3]:
        if st.button(f"👤", key="profile_btn", help="Profile", use_container_width=True):
            st.session_state["current_page"] = "Profile"
            st.rerun()
        st.markdown(f"<div style='text-align: center; font-size: 0.7rem; {profile_style}'>Profile</div>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Check if the user is logged in
if __name__ == "__main__":
    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False
    
    if "current_page" not in st.session_state:
        st.session_state["current_page"] = "Dashboard"
        
    if st.session_state["logged_in"]:
        main_app()
    else:
        login_page()