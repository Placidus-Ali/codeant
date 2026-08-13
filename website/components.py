import rio

class NavigationBar(rio.Component):
    def build(self) -> rio.Component:
        return rio.Row(
            # Brand Logo text
            rio.Text("Codeant Technology Hub", style="heading2"),
            rio.Spacer(),
            # Navigation links mapping to Rio pages
            rio.Link(rio.Button("Home", style="plain-text"), target_url="/"),
            rio.Link(rio.Button("About Us", style="plain-text"), target_url="/about"),
            rio.Link(rio.Button("Courses", style="plain-text"), target_url="/courses"),
            rio.Link(rio.Button("Register", style="major"), target_url="/register"),
            spacing=2,
            margin=1.5,
        )

class FeatureCard(rio.Component):
    title: str
    description: str
    icon: str

    def build(self) -> rio.Component:
        return rio.Card(
            content=rio.Column(
                rio.Icon(self.icon, min_width=3, min_height=3),
                rio.Text(self.title, style="heading3"),
                rio.Text(self.description, justify="center"),
                spacing=1,
                margin=2,
                align_x=0.5
            )
        )

class FooterSection(rio.Component):
    def build(self) -> rio.Component:
        return rio.Container(
            content=rio.Column(
                rio.Row(
                    rio.Column(
                        rio.Text("Codeant Hub", style="heading3"),
                        rio.Text("Empowering kids through computational thinking."),
                    ),
                    rio.Spacer(),
                    rio.Column(
                        rio.Text("Contact Us", style="heading3"),
                        rio.Text("Email: info@codeant.org"),
                        rio.Text("Phone: +1 234 567 890"),
                    ),
                    spacing=4,
                ),
                rio.Separator(),
                rio.Text("© 2026 Codeant Technology Hub. All rights reserved.", align_x=0.5),
                spacing=2,
                margin=2,
            ),
            margin_top=5
        )
