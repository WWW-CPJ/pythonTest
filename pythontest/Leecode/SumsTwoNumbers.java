package Leecode;

// 用于存储整数数组。
import java.util.ArrayList;
// 用于处理用户输入。
import java.util.Scanner;

// classname 与文件名 是一样的
public class SumsTwoNumbers {
    public static void main(String[] args) {

        // 设置控制台编码为 UTF-8
        System.setProperty("file.encoding", "UTF-8");

        // 创建 Scanner 对象以读取用户输入。
        Scanner scanner = new Scanner(System.in);
        
        // 读取目标数字
        System.out.print("输入目标数字： ");
        int target = scanner.nextInt();
        
        // 读取数组长度
        System.out.print("输入数组长度： ");
        int size = scanner.nextInt();
        
        // 使用 ArrayList<Integer> 来动态存储数组元素。
        ArrayList<Integer> array = new ArrayList<>();
        
        // 循环读取用户输入的数组元素，并添加到 ArrayList 中。
        for (int i = 0; i < size; i++) {
            System.out.print("输入第 " + i + " 个元素： ");
            int element = scanner.nextInt();
            array.add(element);
        }
        
        // 打印输入的数组
        System.out.println("输入的数组为： " + array);
        
        // 调用函数
        function(array, target);
        
        // 关闭扫描器
        scanner.close();
    }

    public static void function(ArrayList<Integer> array, int target) {
        boolean found = false;
        int size = array.size();
        
        for (int i = 0; i < size; i++) {
            for (int j = i + 1; j < size; j++) {  // j 从 i+1 开始，避免重复检查同一对元素
                if (array.get(i) + array.get(j) == target) {
                    System.out.println("array[" + i + "] + array[" + j + "] = " + target);
                    found = true;
                    // 你可以选择添加其他处理代码
                }
            }
        }
        
        // 如果需要根据 found 变量执行其他操作可以在这里添加
    }
}

// 注意事项
// 在 Java 中，数组的长度是固定的，使用 ArrayList 可以动态地添加元素。
// 使用 Scanner 处理用户输入时，记得关闭 Scanner 以释放资源。
// Java 的 ArrayList 使用 get() 方法来访问元素，add() 方法来添加元素。

