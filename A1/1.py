import pygame
import math

# =========================================================
# INITIAL SETUP
# =========================================================

pygame.init()

WIDTH = 1200
HEIGHT = 720

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Interactive Inclined Plane")

clock = pygame.time.Clock()

# =========================================================
# COLORS
# =========================================================

BG = (245, 247, 250)
PANEL = (255, 255, 255)
DARK = (35, 40, 48)
GRAY = (120, 125, 135)
LIGHT_GRAY = (220, 224, 230)

BLUE = (55, 120, 220)
BLUE_DARK = (40, 90, 175)

GREEN = (60, 170, 110)
RED = (220, 80, 80)
ORANGE = (235, 155, 55)

PLANE_COLOR = (90, 95, 105)
OBJECT_COLOR = (55, 135, 225)

# =========================================================
# FONTS
# =========================================================

title_font = pygame.font.Font(None, 42)
header_font = pygame.font.Font(None, 30)
font = pygame.font.Font(None, 25)
small_font = pygame.font.Font(None, 21)

# =========================================================
# PHYSICS
# =========================================================

g = 9.81

angle = 30.0
mass = 5.0
friction = 0.10

initial_velocity = 0.0

velocity = initial_velocity
position = 0.0
acceleration = 0.0
net_force = 0.0

simulation_running = False

# =========================================================
# SLIDER CLASS
# =========================================================

class Slider:

    def __init__(self, x, y, width, min_value, max_value, value, label):
        self.x = x
        self.y = y
        self.width = width

        self.min_value = min_value
        self.max_value = max_value

        self.value = value
        self.label = label

        self.radius = 9
        self.dragging = False

    def get_x(self):

        ratio = (
            self.value - self.min_value
        ) / (
            self.max_value - self.min_value
        )

        return self.x + ratio * self.width

    def update(self, mouse_pos, mouse_pressed):

        mouse_x, mouse_y = mouse_pos

        knob_x = self.get_x()

        # Start dragging
        if mouse_pressed[0]:

            distance = math.sqrt(
                (mouse_x - knob_x) ** 2 +
                (mouse_y - self.y) ** 2
            )

            if distance < 18 or self.dragging:

                self.dragging = True

                mouse_x = max(
                    self.x,
                    min(self.x + self.width, mouse_x)
                )

                ratio = (
                    mouse_x - self.x
                ) / self.width

                self.value = (
                    self.min_value +
                    ratio *
                    (self.max_value - self.min_value)
                )

        else:

            self.dragging = False

    def draw(self):

        # Label
        label_text = font.render(
            self.label,
            True,
            DARK
        )

        screen.blit(
            label_text,
            (self.x, self.y - 42)
        )

        # Value
        value_text = small_font.render(
            f"{self.value:.2f}",
            True,
            GRAY
        )

        screen.blit(
            value_text,
            (self.x + self.width + 15, self.y - 8)
        )

        # Track
        pygame.draw.line(
            screen,
            LIGHT_GRAY,
            (self.x, self.y),
            (self.x + self.width, self.y),
            6
        )

        # Filled track
        pygame.draw.line(
            screen,
            BLUE,
            (self.x, self.y),
            (self.get_x(), self.y),
            6
        )

        # Knob
        pygame.draw.circle(
            screen,
            BLUE,
            (int(self.get_x()), self.y),
            self.radius
        )

        pygame.draw.circle(
            screen,
            PANEL,
            (int(self.get_x()), self.y),
            4
        )


# =========================================================
# BUTTON CLASS
# =========================================================

class Button:

    def __init__(self, x, y, width, height, text, color):
        self.rect = pygame.Rect(
            x, y, width, height
        )

        self.text = text
        self.color = color

    def draw(self):

        mouse_pos = pygame.mouse.get_pos()

        color = self.color

        if self.rect.collidepoint(mouse_pos):

            color = tuple(
                min(c + 20, 255)
                for c in color
            )

        pygame.draw.rect(
            screen,
            color,
            self.rect,
            border_radius=8
        )

        text_surface = font.render(
            self.text,
            True,
            (255, 255, 255)
        )

        text_rect = text_surface.get_rect(
            center=self.rect.center
        )

        screen.blit(
            text_surface,
            text_rect
        )

    def clicked(self, mouse_pos):

        return self.rect.collidepoint(mouse_pos)


# =========================================================
# CREATE SLIDERS
# =========================================================

angle_slider = Slider(
    790,
    180,
    280,
    0,
    60,
    angle,
    "Angle (degree)"
)

mass_slider = Slider(
    790,
    280,
    280,
    1,
    20,
    mass,
    "Mass (kg)"
)

friction_slider = Slider(
    790,
    380,
    280,
    0,
    0.5,
    friction,
    "Friction coefficient"
)

# =========================================================
# BUTTONS
# =========================================================

start_button = Button(
    790,
    470,
    85,
    45,
    "START",
    GREEN
)

pause_button = Button(
    885,
    470,
    85,
    45,
    "PAUSE",
    ORANGE
)

reset_button = Button(
    980,
    470,
    85,
    45,
    "RESET",
    RED
)

# =========================================================
# PHYSICS FUNCTIONS
# =========================================================

def calculate_force(angle, mass, friction):

    theta = math.radians(angle)

    # Gravity component parallel to plane
    gravity_force = (
        mass *
        g *
        math.sin(theta)
    )

    # Normal force
    normal_force = (
        mass *
        g *
        math.cos(theta)
    )

    # Friction force
    friction_force = (
        friction *
        normal_force
    )

    # Net force
    force = (
        gravity_force -
        friction_force
    )

    return force


def calculate_acceleration(
    angle,
    mass,
    friction
):

    force = calculate_force(
        angle,
        mass,
        friction
    )

    if mass == 0:
        return 0

    return force / mass


def update_velocity(
    velocity,
    acceleration,
    dt
):

    return velocity + acceleration * dt


def update_position(
    position,
    velocity,
    dt
):

    return position + velocity * dt


# =========================================================
# DRAW PLANE
# =========================================================

def draw_plane(angle, position):

    # จุดเริ่มต้นของพื้นเอียง
    # ทำให้ด้านซ้ายเป็นด้านสูง
    start_x = 110
    start_y = 250

    plane_length = 570

    theta = math.radians(angle)

    # ปลายพื้นเอียงอยู่ด้านขวาและต่ำกว่า
    end_x = (
        start_x +
        plane_length * math.cos(theta)
    )

    end_y = (
        start_y +
        plane_length * math.sin(theta)
    )

    # -----------------------------------------------------
    # Ground
    # -----------------------------------------------------

    pygame.draw.line(
        screen,
        LIGHT_GRAY,
        (60, 575),
        (700, 575),
        4
    )

    # -----------------------------------------------------
    # Inclined plane
    # -----------------------------------------------------

    pygame.draw.line(
        screen,
        PLANE_COLOR,
        (start_x, start_y),
        (end_x, end_y),
        18
    )

    # -----------------------------------------------------
    # Object position
    # -----------------------------------------------------

    pixels_per_meter = 70

    distance = position * pixels_per_meter

    # จำกัดไม่ให้วัตถุออกจากพื้นเอียง
    distance = max(
        0,
        min(
            distance,
            plane_length - 35
        )
    )

    # ตำแหน่งวัตถุ
    # position เพิ่ม → วัตถุเคลื่อนลงทางขวา
    object_x = (
        start_x +
        distance * math.cos(theta)
    )

    object_y = (
        start_y +
        distance * math.sin(theta)
    )

    # -----------------------------------------------------
    # Object
    # -----------------------------------------------------

    box_size = 42

    # Offset ให้วัตถุอยู่บนพื้นเอียง
    offset_x = (
        math.sin(theta) *
        box_size / 2
    )

    offset_y = (
        math.cos(theta) *
        box_size / 2
    )

    object_center = (
        object_x + offset_x,
        object_y - offset_y
    )

    # สร้างกล่อง
    surface = pygame.Surface(
        (box_size, box_size),
        pygame.SRCALPHA
    )

    pygame.draw.rect(
        surface,
        OBJECT_COLOR,
        (0, 0, box_size, box_size),
        border_radius=5
    )

    # หมุนกล่องตามพื้นเอียง
    rotated = pygame.transform.rotate(
        surface,
        -angle
    )

    rect = rotated.get_rect(
        center=(
            int(object_center[0]),
            int(object_center[1])
        )
    )

    screen.blit(
        rotated,
        rect
    )

    # -----------------------------------------------------
    # Angle
    # -----------------------------------------------------

    angle_text = font.render(
        f"θ = {angle:.1f}°",
        True,
        DARK
    )

    screen.blit(
        angle_text,
        (125, 595)
    )


# =========================================================
# DRAW INFORMATION PANEL
# =========================================================

def draw_information():

    # -----------------------------------------------------
    # Panel
    # -----------------------------------------------------

    pygame.draw.rect(
        screen,
        PANEL,
        (740, 25, 410, 635),
        border_radius=15
    )

    # -----------------------------------------------------
    # Header
    # -----------------------------------------------------

    title = title_font.render(
        "INTERACTIVE INCLINED PLANE",
        True,
        DARK
    )

    screen.blit(
        title,
        (35, 30)
    )

    header = header_font.render(
        "SIMULATION CONTROL",
        True,
        DARK
    )

    screen.blit(
        header,
        (775, 65)
    )

    # -----------------------------------------------------
    # Divider
    # -----------------------------------------------------

    pygame.draw.line(
        screen,
        LIGHT_GRAY,
        (775, 105),
        (1115, 105),
        2
    )

    # -----------------------------------------------------
    # Physics information
    # -----------------------------------------------------

    info_y = 530

    information = [
        ("Net Force", f"{net_force:.2f} N"),
        ("Acceleration", f"{acceleration:.2f} m/s²"),
        ("Velocity", f"{velocity:.2f} m/s"),
        ("Position", f"{position:.2f} m")
    ]

    for label, value in information:

        label_surface = small_font.render(
            label,
            True,
            GRAY
        )

        value_surface = font.render(
            value,
            True,
            DARK
        )

        screen.blit(
            label_surface,
            (775, info_y)
        )

        screen.blit(
            value_surface,
            (970, info_y - 3)
        )

        info_y += 30


# =========================================================
# RESET SIMULATION
# =========================================================

def reset_simulation():

    global velocity
    global position
    global simulation_running

    velocity = initial_velocity
    position = 0.0

    simulation_running = False


# =========================================================
# MAIN LOOP
# =========================================================

running = True

while running:

    # Delta time
    dt = clock.tick(60) / 1000

    # -----------------------------------------------------
    # EVENTS
    # -----------------------------------------------------

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:

            mouse_pos = pygame.mouse.get_pos()

            # START
            if start_button.clicked(mouse_pos):

                simulation_running = True

            # PAUSE
            if pause_button.clicked(mouse_pos):

                simulation_running = False

            # RESET
            if reset_button.clicked(mouse_pos):

                reset_simulation()

    # -----------------------------------------------------
    # UPDATE SLIDERS
    # -----------------------------------------------------

    mouse_pos = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()

    angle_slider.update(
        mouse_pos,
        mouse_pressed
    )

    mass_slider.update(
        mouse_pos,
        mouse_pressed
    )

    friction_slider.update(
        mouse_pos,
        mouse_pressed
    )

    # -----------------------------------------------------
    # Get slider values
    # -----------------------------------------------------

    angle = angle_slider.value
    mass = mass_slider.value
    friction = friction_slider.value

    # -----------------------------------------------------
    # Physics calculation
    # -----------------------------------------------------

    net_force = calculate_force(
        angle,
        mass,
        friction
    )

    acceleration = calculate_acceleration(
        angle,
        mass,
        friction
    )

    # -----------------------------------------------------
    # Simulation
    # -----------------------------------------------------

    if simulation_running:

        velocity = update_velocity(
            velocity,
            acceleration,
            dt
        )

        position = update_position(
            position,
            velocity,
            dt
        )

        # Prevent object from moving backward
        if position < 0:

            position = 0
            velocity = 0

        # Stop at end of plane
        if position >= 7.5:

            position = 7.5
            simulation_running = False

    # -----------------------------------------------------
    # DRAW
    # -----------------------------------------------------

    screen.fill(BG)

    draw_plane(
        angle,
        position
    )

    draw_information()

    angle_slider.draw()
    mass_slider.draw()
    friction_slider.draw()

    start_button.draw()
    pause_button.draw()
    reset_button.draw()

    # -----------------------------------------------------
    # Status
    # -----------------------------------------------------

    if simulation_running:

        status = "RUNNING"
        status_color = GREEN

    else:

        status = "PAUSED"
        status_color = RED

    status_surface = small_font.render(
        f"Status: {status}",
        True,
        status_color
    )

    screen.blit(
        status_surface,
        (775, 600)
    )

    # -----------------------------------------------------
    # Update display
    # -----------------------------------------------------

    pygame.display.flip()


pygame.quit()