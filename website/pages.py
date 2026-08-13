import rio
from components import NavigationBar, FeatureCard, FooterSection

@rio.page(name="Home", url_segment="")
class HomePage(rio.Component):
    def build(self) -> rio.Component:
        return rio.Column(
            NavigationBar(),
            
            # Hero Section
            rio.Column(
                rio.Text("Your Child Can Code!", style="heading1"),
                rio.Text("Codeant is the leading online code learning platform for kids.", style="text"),
                rio.Link(rio.Button("Get Started Today", style="major"), target_url="/register"),
                spacing=1.5,
                margin_top=6,
                margin_bottom=6,
                align_x=0.5,
            ),
            
            # Stats Counter Row
            rio.Row(
                rio.Column(
                    rio.Text("500+", style="heading2"), 
                    rio.Text("Students Taught")
                ),
                rio.Column(
                    rio.Text("15+", style="heading2"), 
                    rio.Text("Expert Mentors")
                ),
                rio.Column(
                    rio.Text("98%", style="heading2"), 
                    rio.Text("Success Rate")
                ),
                spacing=8,
                align_x=0.5,
                margin_bottom=5,
            ),
            
            # Feature Grid Section
            rio.Text("What We Offer", style="heading2", align_x=0.5, margin_bottom=2),
            rio.Grid(
                FeatureCard("Visual Coding", "Block-based learning logic perfect for absolute beginners.", "material/grid-on"),
                FeatureCard("Python for Kids", "Transitioning young minds into real text-based software engineering.", "material/code"),
                FeatureCard("Robotics & AI", "Hands-on projects building smart algorithms and physical automation.", "material/memory"),
                row_spacing=2,
                column_spacing=2,
                margin=2,
            ),

            
            FooterSection(),
            spacing=2,
        )

@rio.page(name="About Us", url_segment="about")
class AboutPage(rio.Component):
    def build(self) -> rio.Component:
        return rio.Column(
            NavigationBar(),
            rio.Column(
                rio.Text("Our Mission", style="heading1"),
                rio.Text(
                    "At Codeant, we believe programming is a core modern literacy. "
                    "Our curriculum focuses on project-driven learning, critical thinking, "
                    "and problem-solving over simple rote memorization.",
                    justify="left"
                ),
                margin=4,
                spacing=2
            ),
            FooterSection()
        )

@rio.page(name="Courses", url_segment="courses")
class CoursesPage(rio.Component):
    def build(self) -> rio.Component:
        return rio.Column(
            NavigationBar(),
            rio.Text("Available Tracks", style="heading1", margin=2),
            rio.Grid(
                rio.Card(content=rio.Column(rio.Text("Scratch Essentials", style="heading3"), rio.Text("Ages 6-9 | 12 Weeks"), margin=1.5)),
                rio.Card(content=rio.Column(rio.Text("Python Core Mastery", style="heading3"), rio.Text("Ages 10-15 | 16 Weeks"), margin=1.5)),
                rio.Card(content=rio.Column(rio.Text("Web Dev Basics", style="heading3"), rio.Text("Ages 12+ | 12 Weeks"), margin=1.5)),
                row_spacing=2,
                column_spacing=2,
                margin=2
            ),
            FooterSection()
        )

@rio.page(name="Register", url_segment="register")
class RegisterPage(rio.Component):
    # Setup full-stack inputs variables directly in Python
    student_name: str = ""
    parent_email: str = ""
    status_message: str = ""

    def on_submit(self) -> None:
        if self.student_name and self.parent_email:
            # Backend process logic runs directly here
            self.status_message = f"Success! Registered {self.student_name}. Check your email at {self.parent_email}."
        else:
            self.status_message = "Please fill out all fields before submitting."

    def build(self) -> rio.Component:
        return rio.Column(
            NavigationBar(),
            rio.Card(
                content=rio.Column(
                    rio.Text("Student Registration", style="heading2"),
                    rio.TextInput(text=self.bind().student_name, label="Student Name"),
                    rio.TextInput(text=self.bind().parent_email, label="Parent Email"),
                    rio.Button("Submit Registration", on_press=self.on_submit, style="major"),
                    rio.Text(self.bind().status_message, color=rio.Color.from_hex("#4CAF50")),
                    spacing=2,
                    margin=3
                ),
                align_x=0.5,
                margin_top=4,
                margin_bottom=4
            ),
            FooterSection()
        )
