public class Time {
    public static void main(String[] args) {
        int hour = 15;
        int min = 30;
        int sec = 15;
        System.out.println("Seconds since midnight: " + (hour * 3600 + min *60 +sec));
        System.out.println("Seconds left till midnight: "+ (86400 - hour * 3600 + min *60 +sec));
        System.out.println("% of day that have passed "+ ((hour * 3600 + min *60 +sec)/864));
    }
}
