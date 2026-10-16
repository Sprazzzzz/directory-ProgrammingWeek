
import java.util.ArrayList;

// ==========================================
// PHYSICS SIMULATOR - INCLINED PLANE
// Processing / Java
// ==========================================

Slider angleSlider;
Slider massSlider;
Slider velocitySlider;
Slider frictionSlider;

ArrayList<Float> timeData = new ArrayList<Float>();
ArrayList<Float> positionData = new ArrayList<Float>();
ArrayList<Float> velocityData = new ArrayList<Float>();

float g = 9.81;
float simTime = 0;
float distance = 0;
float velocity = 0;
float acceleration = 0;

float startX = 335;
float startY = 415;
float rampLength = 535;
float boxSize = 34;

boolean running = false;
boolean paused = false;
boolean finished = false;
boolean dragging = false;

color bg = color(20, 28, 35);
color panel = color(30, 40, 48);
color cyan = color(65, 190, 240);
color green = color(50, 205, 125);
color orange = color(255, 175, 55);

void setup() {
  size(1200, 760);
  smooth(4);

  angleSlider = new Slider(
  "ANGLE (deg)", 0, 60, 30, 28, 130, 245
);

massSlider = new Slider(
  "MASS (kg)", 1, 20, 5, 28, 195, 245
);

velocitySlider = new Slider(
  "INITIAL VELOCITY (m/s)", 0, 10, 2,
  28, 260, 245
);

frictionSlider = new Slider(
  "FRICTION (mu)", 0, 1, 0.30,
  28, 325, 245
);

  resetSimulation();
}

void draw() {
  background(bg);

  drawHeader();
  drawControls();
  drawSimulation();
  drawResults();
  drawGraphs();

  if (running && !paused && !finished) {
    updateSimulation();
  }
}

// ==========================================
// HEADER
// ==========================================

void drawHeader() {
  fill(16, 23, 29);
  noStroke();
  rect(0, 0, width, 58);

  fill(255);
  textAlign(LEFT, CENTER);
  textSize(23);
  text("PHYSICS SIMULATOR", 25, 29);

  fill(cyan);
  textSize(13);
  text("INCLINED PLANE | MOTION & FORCES",
       310, 30);

  fill(running && !paused && !finished
       ? green : orange);
  textAlign(RIGHT, CENTER);
  textSize(14);

  String status = finished ? "FINISHED"
                 : paused ? "PAUSED"
                 : running ? "SIMULATING"
                 : "READY";

  text(status, width - 28, 29);
}

// ==========================================
// INPUT: SLIDERS AND BUTTONS
// ==========================================

void drawControls() {
  drawPanel(20, 75, 275, 415);

  fill(255);
  textAlign(LEFT, CENTER);
  textSize(18);
  text("SIMULATION CONTROLS", 35, 100);

  angleSlider.display();
  massSlider.display();
  velocitySlider.display();
  frictionSlider.display();

  drawButton(35, 390, 76, 37,
             "START", green);
  drawButton(119, 390, 76, 37,
             "PAUSE", orange);
  drawButton(203, 390, 76, 37,
             "RESET", color(100, 115, 125));

  fill(180, 200, 210);
  textSize(11);
  text("Drag sliders to change parameters",
       35, 455);
  text("Start again to apply new values",
       35, 472);
}

void drawButton(float x, float y, float w,
                float h, String label, color c) {
  noStroke();
  fill(c);
  rect(x, y, w, h, 7);

  fill(20, 27, 32);
  textAlign(CENTER, CENTER);
  textSize(12);
  text(label, x + w/2, y + h/2);
}

// ==========================================
// OUTPUT: ANIMATION
// ==========================================

void drawSimulation() {
  drawPanel(310, 75, 870, 415);

  fill(255);
  textAlign(LEFT, CENTER);
  textSize(18);
  text("MOTION SIMULATION", 330, 101);

  float theta = radians(angleSlider.value);
  float endX = startX + rampLength * cos(theta);
  float endY = startY - rampLength * sin(theta);

  // Sky
  noStroke();
  fill(100, 160, 195);
  rect(326, 120, 838, 350, 10);

  // Ground beneath the ramp
  fill(88, 70, 51);
  rect(326, 425, 838, 45, 0, 0, 10, 10);

  // Ramp body
  fill(75, 83, 90);
  beginShape();
  vertex(startX, startY);
  vertex(endX, endY);
  vertex(endX, startY + 10);
  vertex(startX, startY + 10);
  endShape(CLOSE);

  // Ramp top
  stroke(220);
  strokeWeight(3);
  line(startX, startY, endX, endY);

  // Dashed guide along ramp
  stroke(240);
  strokeWeight(1.5);
  for (float d = 15; d < rampLength - 15; d += 24) {
    float x1 = startX + d * cos(theta);
    float y1 = startY - d * sin(theta);
    float x2 = startX + (d + 12) * cos(theta);
    float y2 = startY - (d + 12) * sin(theta);
    line(x1, y1, x2, y2);
  }

  // Angle label
  fill(255);
  noStroke();
  textAlign(LEFT, CENTER);
  textSize(17);
  text(nf(angleSlider.value, 1, 1) + " deg",
       startX + 48, startY - 10);

  // Moving box
  float s = constrain(distance * 30,
                      0, rampLength - 45);

  float bx = startX + s * cos(theta);
  float by = startY - s * sin(theta);

  pushMatrix();
  translate(bx, by);
  rotate(-theta);

  rectMode(CENTER);
  stroke(255, 220, 150);
  strokeWeight(2);
  fill(205, 145, 65);
  rect(0, -boxSize/2, boxSize, boxSize, 4);

  stroke(120, 75, 30);
  line(-boxSize/2, -boxSize/2,
        boxSize/2, -boxSize/2);
  line(-boxSize/2, -boxSize/2,
        boxSize/2, boxSize/2);
  line(boxSize/2, -boxSize/2,
       -boxSize/2, boxSize/2);

  popMatrix();
  rectMode(CORNER);

  // Motion arrow
  if (running && !paused && !finished
      && velocity > 0.1) {
    float ax = bx + 40 * cos(theta);
    float ay = by - 40 * sin(theta);

    stroke(255, 80, 70);
    strokeWeight(3);
    line(ax, ay, ax + 35*cos(theta),
         ay - 35*sin(theta));

    line(ax + 35*cos(theta),
         ay - 35*sin(theta),
         ax + 25*cos(theta) - 7*sin(theta),
         ay - 25*sin(theta) - 7*cos(theta));
  }

  noStroke();
  fill(255);
  textAlign(LEFT, CENTER);
  textSize(14);
  text("Time: " + nf(simTime, 1, 2) + " s",
       950, 145);

  if (!running) {
    fill(20, 30, 40, 190);
    rect(600, 150, 300, 38, 8);
    fill(255);
    textAlign(CENTER, CENTER);
    text("Adjust parameters, then press START",
         750, 169);
  }

  if (paused) {
    fill(20, 30, 40, 200);
    rect(600, 150, 300, 38, 8);
    fill(255);
    textAlign(CENTER, CENTER);
    text("PAUSED", 750, 169);
  }

  if (finished) {
    fill(20, 30, 40, 210);
    rect(600, 150, 300, 38, 8);
    fill(255);
    textAlign(CENTER, CENTER);
    text("SIMULATION FINISHED", 750, 169);
  }
}

// ==========================================
// PHYSICS CALCULATIONS
// ==========================================

void calculateForce() {
  float theta = radians(angleSlider.value);
  float mass = massSlider.value;
  float mu = frictionSlider.value;

  float gravityAlongRamp = mass * g * sin(theta);
  float normalForce = mass * g * cos(theta);
  float frictionForce = mu * normalForce;

  // Positive direction is down the ramp.
  acceleration =
    g * (sin(theta) - mu * cos(theta));

  // If the object is stationary and gravity
  // cannot overcome friction, it stays at rest.
  if (velocity <= 0 && acceleration < 0) {
    acceleration = 0;
  }

  // Keep the mass input physically meaningful.
  // Mass affects forces, but cancels in a = F/m
  // for this idealized friction model.
}

void updateSimulation() {
  float dt = min(1.0 / max(frameRate, 30), 0.033);

  calculateForce();

  // Update velocity
  velocity += acceleration * dt;

  if (velocity < 0) {
    velocity = 0;
  }

  // Update position
  distance += velocity * dt;

  // Update elapsed time
  simTime += dt;

  saveGraphData();

  if (distance * 30 >= rampLength - 45) {
    distance = (rampLength - 45) / 30.0;
    finished = true;
    running = false;
  }
}

void saveGraphData() {
  if (timeData.size() == 0 ||
      simTime - timeData.get(timeData.size()-1) >= 0.08) {
    timeData.add(simTime);
    positionData.add(distance);
    velocityData.add(velocity);
  }
}

// ==========================================
// LIVE RESULTS
// ==========================================

void drawResults() {
  drawPanel(20, 505, 275, 230);

  fill(255);
  textAlign(LEFT, CENTER);
  textSize(18);
  text("LIVE RESULTS", 35, 530);

  calculateForce();

  float mass = massSlider.value;
  float theta = radians(angleSlider.value);

  float netForce = mass * acceleration;
  float normalForce = mass * g * cos(theta);
  float frictionForce =
    frictionSlider.value * normalForce;

  resultRow("Net force", nf(netForce, 1, 2) + " N", 565);
  resultRow("Acceleration", nf(acceleration, 1, 2) + " m/s2", 600);
  resultRow("Velocity", nf(velocity, 1, 2) + " m/s", 635);
  resultRow("Distance", nf(distance, 1, 2) + " m", 670);
  resultRow("Friction force", nf(frictionForce, 1, 2) + " N", 705);
}

void resultRow(String label, String value, float y) {
  fill(175, 195, 205);
  textAlign(LEFT, CENTER);
  textSize(13);
  text(label, 35, y);

  fill(255);
  textAlign(RIGHT, CENTER);
  text(value, 280, y);
}

// ==========================================
// GRAPHS
// ==========================================

void drawGraphs() {
  drawPanel(310, 505, 870, 230);

  fill(255);
  textAlign(LEFT, CENTER);
  textSize(18);
  text("MOTION GRAPHS", 330, 530);

  drawGraph(330, 550, 260, 155,
            "Position - Time", positionData,
            color(50, 220, 130));

  drawGraph(610, 550, 260, 155,
            "Velocity - Time", velocityData,
            color(70, 175, 255));

  // Acceleration graph: current value as a line
  stroke(255, 100, 90);
  strokeWeight(2);
  float gy = map(acceleration, -10, 10,
                 685, 585);
  line(910, gy, 1150, gy);

  drawGraphFrame(890, 550, 270, 155,
                 "Acceleration (m/s2)");
}

void drawGraph(float x, float y, float w,
               float h, String title,
               ArrayList<Float> data, color c) {
  drawGraphFrame(x, y, w, h, title);

  if (data.size() < 2) return;

  float maxValue = 1;
  for (int i = 0; i < data.size(); i++) {
    maxValue = max(maxValue, data.get(i));
  }

  stroke(c);
  strokeWeight(2);
  noFill();
  beginShape();

  for (int i = 0; i < data.size(); i++) {
    float px = map(i, 0, max(1, data.size()-1),
                   x + 25, x + w - 10);
    float py = map(data.get(i), 0, maxValue * 1.15,
                   y + h - 20, y + 35);
    vertex(px, py);
  }

  endShape();
}

void drawGraphFrame(float x, float y, float w,
                    float h, String title) {
  noStroke();
  fill(19, 26, 32);
  rect(x, y, w, h, 6);

  fill(cyan);
  textAlign(LEFT, CENTER);
  textSize(12);
  text(title, x + 10, y + 15);

  stroke(65, 78, 88);
  strokeWeight(1);
  for (int i = 1; i <= 3; i++) {
    float gy = y + 30 + i * (h - 55) / 4;
    line(x + 25, gy, x + w - 10, gy);
  }

  line(x + 25, y + 30, x + 25, y + h - 20);
  line(x + 25, y + h - 20, x + w - 10, y + h - 20);
}

// ==========================================
// UI HELPERS
// ==========================================

void drawPanel(float x, float y, float w, float h) {
  noStroke();
  fill(panel);
  rect(x, y, w, h, 10);
}

void resetSimulation() {
  simTime = 0;
  distance = 0;
  velocity = velocitySlider.value;
  acceleration = 0;

  running = false;
  paused = false;
  finished = false;

  timeData.clear();
  positionData.clear();
  velocityData.clear();

  saveGraphData();
}

// ==========================================
// MOUSE INPUT
// ==========================================

void mousePressed() {
  if (angleSlider.hit(mouseX, mouseY)) {
    angleSlider.drag(mouseX);
    return;
  }

  if (massSlider.hit(mouseX, mouseY)) {
    massSlider.drag(mouseX);
    return;
  }

  if (velocitySlider.hit(mouseX, mouseY)) {
    velocitySlider.drag(mouseX);
    return;
  }

  if (frictionSlider.hit(mouseX, mouseY)) {
    frictionSlider.drag(mouseX);
    return;
  }

  // START
  if (mouseX >= 35 && mouseX <= 111 &&
      mouseY >= 390 && mouseY <= 427) {
    if (!running || finished) {
      resetSimulation();
      running = true;
    } else if (paused) {
      paused = false;
    }
  }

  // PAUSE / RESUME
  if (mouseX >= 119 && mouseX <= 195 &&
      mouseY >= 390 && mouseY <= 427) {
    if (running) {
      paused = !paused;
    }
  }

  // RESET
  if (mouseX >= 203 && mouseX <= 279 &&
      mouseY >= 390 && mouseY <= 427) {
    resetSimulation();
  }
}

void mouseDragged() {
  if (angleSlider.dragging) angleSlider.drag(mouseX);
  if (massSlider.dragging) massSlider.drag(mouseX);
  if (velocitySlider.dragging) velocitySlider.drag(mouseX);
  if (frictionSlider.dragging) frictionSlider.drag(mouseX);
}

void mouseReleased() {
  angleSlider.dragging = false;
  massSlider.dragging = false;
  velocitySlider.dragging = false;
  frictionSlider.dragging = false;
}

// ==========================================
// SLIDER CLASS
// ==========================================

class Slider {
  String label;
  float minValue, maxValue, value;
  float x, y, w;
  boolean dragging = false;

  Slider(String label, float minValue,
         float maxValue, float value,
         float x, float y, float w) {
    this.label = label;
    this.minValue = minValue;
    this.maxValue = maxValue;
    this.value = value;
    this.x = x;
    this.y = y;
    this.w = w;
  }

  void display() {
    fill(220, 230, 235);
    textAlign(LEFT, CENTER);
    textSize(12);
    text(label, x, y);

    fill(255);
    textAlign(RIGHT, CENTER);
    text(nf(value, 1, 2), x + w, y);

    stroke(80, 95, 105);
    strokeWeight(5);
    line(x, y + 22, x + w, y + 22);

    float px = map(value, minValue, maxValue, x, x + w);

    stroke(cyan);
    line(x, y + 22, px, y + 22);

    noStroke();
    fill(cyan);
    ellipse(px, y + 22, 13, 13);
  }

  boolean hit(float mx, float my) {
    if (mx >= x - 5 && mx <= x + w + 5 &&
        my >= y + 10 && my <= y + 34) {
      dragging = true;
      return true;
    }
    return false;
  }

  void drag(float mx) {
    value = map(constrain(mx, x, x + w),
                x, x + w, minValue, maxValue);
  }
}
