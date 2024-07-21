public class Q {
    static class Que {
        static int arr[];
        static int size;
        static int rear = -1;

        Que(int n) {
            arr = new int[n];
            this.size = n;
        }

        public static Boolean isEmpty() {
            return rear == -1;
        }

        public static boolean isFull() { 
            if (rear == size - 1) {
                System.out.println("full q"); 
                return true;
            }
            return false;
        }

        public static void add(int data) {
            if (isFull()) {
                return;
            }
            rear++;
            arr[rear] = data;
        }

        public static int remove() {
            if (isEmpty()) {
                System.out.println("Queue is empty"); // Handle empty queue case
                return -1; // Return a value for an empty queue case
            }
            int f = arr[0];
            for (int i = 0; i < rear; i++) { 
                arr[i] = arr[i + 1]; 
            }
            rear--;
            return f;
        }

        public static int peek() {
            if (isEmpty()) {
                return -1;
            }
            return arr[0];
        }
    }

    public static void main(String args[]) {
        Que q = new Que(3); 
        q.add(1);
        q.add(2);
        q.add(3);
        while (!q.isEmpty()) {
            System.out.println(q.peek()); // Correct spelling: System
            q.remove();
        }
    }
}
