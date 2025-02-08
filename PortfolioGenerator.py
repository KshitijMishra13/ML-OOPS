import streamlit as st


def main():
    st.title("Portfolio Generator")

    menu = ["Personal Info", "Education", "Skills", "Projects", "Portfolio Preview"]
    choice = st.sidebar.selectbox("Select a section: ", menu)

    if choice == "Personal Info":
        personal_info()
    elif choice == "Education":
        education()
    elif choice == "Skills":
        skills()
    elif choice == "Projects":
        projects()
    elif choice == "Portfolio Preview":
        preview_portfolio()


def personal_info():
    st.header("Personal Information")
    name = st.text_input("Full Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone Number")
    bio = st.text_area("Bio")

    st.session_state.name = name
    st.session_state.email = email
    st.session_state.phone = phone
    st.session_state.bio = bio


def education():
    st.header("Education")
    institution = st.text_input("Institution Name")
    degree = st.text_input("Degree")
    graduation_year = st.text_input("Graduation Year")

    st.session_state.institution = institution
    st.session_state.degree = degree
    st.session_state.graduation_year = graduation_year


def skills():
    st.header("Skills")
    skills_list = st.text_area("List your skills (separated by commas)").split(',')

    st.session_state.skills = [skill.strip() for skill in skills_list]


def projects():
    st.header("Projects")
    project_name = st.text_input("Project Name")
    description = st.text_area("Project Description")
    link = st.text_input("Link to Project (eg. GitHub, website)")

    if "projects" not in st.session_state:
        st.session_state.projects = []

    if st.button("Add Project"):
        st.session_state.projects.append({"name": project_name, "description": description, "link": link})


def preview_portfolio():
    st.header("Portfolio Preview")

    st.subheader("Personal Information")
    st.write(f"Name: {st.session_state.name}")
    st.write(f"Email: {st.session_state.email}")
    st.write(f"Phone: {st.session_state.phone}")
    st.write(f"Bio: {st.session_state.bio}")

    st.subheader("Education")
    st.write(f"Institution: {st.session_state.institution}")
    st.write(f"Degree: {st.session_state.degree}")
    st.write(f"Graduation Year: {st.session_state.graduation_year}")

    st.subheader("Skills")
    st.write(", ".join(st.session_state.skills))

    st.subheader("Projects")
    for project in st.session_state.projects:
        st.write(f"{project['name']}")
        st.write(f"{project['description']}")
        st.write(f"Link: {project['link']}")

    if st.button("Download Portfolio"):
        portfolio_text = generate_portfolio_text()
        st.download_button("Download as Text File", portfolio_text, file_name="portfolio.txt")

def generate_portfolio_text():
    portfolio = f"""
    Personal Information:
    Name: {st.session_state.name}
    Email: {st.session_state.email}
    Phone: {st.session_state.phone}
    Bio: {st.session_state.bio}

    Education:
    Institution: {st.session_state.institution}
    Degree: {st.session_state.degree}
    Graduation Year: {st.session_state.graduation_year}

    Skills:
    {', '.join(st.session_state.skills)}

    Projects:
    """
    for project in st.session_state.projects:
        portfolio += f"\nProject Name: {project['name']}\nDescription: {project['description']}\nLink: {project['link']}\n"

    return portfolio


if __name__ == "__main__":
    if 'name' not in st.session_state:
        st.session_state.name = ''
    if 'email' not in st.session_state:
        st.session_state.email = ''
    if 'phone' not in st.session_state:
        st.session_state.phone = ''
    if 'bio' not in st.session_state:
        st.session_state.bio = ''
    if 'institution' not in st.session_state:
        st.session_state.institution = ''
    if 'degree' not in st.session_state:
        st.session_state.degree = ''
    if 'graduation_year' not in st.session_state:
        st.session_state.graduation_year = ''
    if 'skills' not in st.session_state:
        st.session_state.skills = []
    if 'projects' not in st.session_state:
        st.session_state.projects = []

    main()
