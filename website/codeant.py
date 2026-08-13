import rio
import pages 

# Configure color accents matching modern agency aesthetics 
app_theme = rio.Theme.from_colors(
    primary_color=rio.Color.from_hex("#2196F3"),  # Codeant Active Blue Accent
    secondary_color=rio.Color.from_hex("#F5F5F5"), # Light Clean Minimal canvas
    mode = "light"                                  # Handles the background automatically

)

# Pass your base layout into Rio's runtime constructor
app = rio.App(
    build=pages.HomePage,
    theme=app_theme
)