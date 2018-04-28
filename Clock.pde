float sRadius;
float mRadius;
float hRadius;

void setup(){
  size(400, 400);
}  

void draw(){
  background(125);
  fill(80);
  ellipse(width/2, height/2, 200, 200);
  
  float sec = map(second(), 0, 60, 0, TWO_PI) - HALF_PI;
  float min = map(minute() + norm(second(), 0, 60), 0, 60, 0, TWO_PI) - HALF_PI;
  float hou = map(hour() + norm(minute(), 0, 60), 0, 24, 0, TWO_PI * 2) - HALF_PI;
  text(hour(), 10, 10);
  
  strokeWeight(1);  
  line(width/2, height/2, width/2 + cos(sec) * (100 * 0.9), height/2 + sin(sec) * (100 * 0.9));
  strokeWeight(2); 
  line(width/2, height/2, width/2 + cos(min) * (100 * 0.9), height/2 + sin(min) * (100 * 0.9));
  strokeWeight(3); 
  line(width/2, height/2, width/2 + cos(hou) * (100 * 0.5), height/2 + sin(hou) * (100 * 0.5));
  
  strokeWeight(2);
  beginShape(POINTS);
  int count = 0;
  for (int a = 0; a <= 360; a+=6) {
    float angle = radians(a);
    if(a%15!=0){
      float x = width/2 + cos(angle - HALF_PI) * 100 * 0.9;
      float y = height/2 + sin(angle - HALF_PI) * 100 * 0.9;
    vertex(x, y);
    }else{
      textSize(5);
      text(count, width/2 + cos(angle - HALF_PI) * 100 * 0.9, height/2 + sin(angle - HALF_PI) * 100 * 0.9);
      fill(250);
      count++;
    }
  }
  endShape();
}