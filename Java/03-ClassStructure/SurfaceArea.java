public class SurfaceArea {
    public static double circleArea(float radius){
        return radius * radius * 3.14;
    }
    public static double rectangleArea(float a, float b){
        return a*b;
    }
    public static double triangleArea(float a,float h){
        return a*h*0.5;
    }
    public static void main(String[] args){
        System.out.println(SurfaceArea.circleArea(3));
        System.out.println(SurfaceArea.rectangleArea(3,4));
        System.out.println(SurfaceArea.triangleArea(3,5));

    }
}
