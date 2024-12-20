import java.util.*;

public class Main {
    public static void bai1() {
        Scanner scanner = new Scanner(System.in);
        String x = scanner.nextLine();

        int getting = 0;
        for (char i : x.toCharArray()) {
            getting += Character.getNumericValue(i);
        }
        System.out.println(x.length());
        System.out.println(getting);
        System.out.println(Collections.max(Arrays.asList(x.split(""))));
    }

    public static void bai2() {
        Scanner scanner = new Scanner(System.in);
        System.out.print("dài ");
        int x = scanner.nextInt();
        System.out.print("rộng ");
        int y = scanner.nextInt();
        System.out.println(2 * (x + y));
        System.out.println(x * y);
    }

    public static void bai3() {
        Scanner scanner = new Scanner(System.in);
        String x = scanner.nextLine().replace(" ", "");

        int numbercount = 0;
        int numbernumber = 0;
        StringBuilder stringstring = new StringBuilder();

        for (char i : x.toCharArray()) {
            try {
                numbernumber += Character.getNumericValue(i);
                numbercount += 1;
            } catch (Exception e) {
                stringstring.append(i);
            }
        }

        System.out.println(numbercount);
        System.out.println(numbernumber);
        System.out.println(stringstring.toString());
    }

    public static void bai4() {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Gồm bao nhiêu số: ");
        String x = scanner.nextLine();
        System.out.print("Dãy số: ");
        String[] y = scanner.nextLine().split(" ");

        int sumy = 0;
        for (String i : y) {
            sumy += Integer.parseInt(i);
        }

        List<String> gotnumber = new ArrayList<>();
        Map<String, Integer> numbercount = new HashMap<>();
        for (String i : y) {
            if (!gotnumber.contains(i)) {
                gotnumber.add(i);
                int counted = 0;
                for (String i2 : y) {
                    if (i.equals(i2)) {
                        counted += 1;
                    }
                }
                numbercount.put(i, counted);
            }
        }

        System.out.println(sumy);
        for (String i : numbercount.keySet()) {
            System.out.println(i + ":" + numbercount.get(i));
        }
    }

    public static void main(String[] args) {
        // Uncomment the function you want to test
        bai1();
        bai2();
        bai3();
        bai4();
    }
}

