
import java.util.*;

class Solution {
    public List<Integer> busiestServers(int k, int[] arrival, int[] load) {

        int n = arrival.length;

        PriorityQueue<int[]> busy = new PriorityQueue<>(
            (a, b) -> Integer.compare(a[0], b[0])
        );

        TreeSet<Integer> available = new TreeSet<>();

        for (int i = 0; i < k; i++) {
            available.add(i);
        }

        int[] count = new int[k];

        for (int i = 0; i < n; i++) {

            int time = arrival[i];

            while (!busy.isEmpty() && busy.peek()[0] <= time) {
                int[] server = busy.poll();
                available.add(server[1]);
            }

            if (available.isEmpty()) {
                continue;
            }

            Integer server = available.ceiling(i % k);

            if (server == null) {
                server = available.first();
            }

            available.remove(server);

            count[server]++;

            busy.offer(new int[]{
                time + load[i], server
            });
        }

        int max = 0;

        for (int c : count) {
            max = Math.max(max, c);
        }

        List<Integer> result = new ArrayList<>();

        for (int i = 0; i < k; i++) {
            if (count[i] == max) {
                result.add(i);
            }
        }

        return result;
    }
}
