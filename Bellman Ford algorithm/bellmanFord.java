class Solution {
    
    public int networkDelayTime(int[][] times, int N, int K) {
        int[] dist = new int[N];
        for (int i = 0; i < dist.length; i++)
            dist[i] = (int)1e9;
        dist[K - 1] = 0;
        for (int i = 0; i < N; i++) {
            for (int[] time: times) {
                if (dist[time[0] - 1] + time[2] < dist[time[1] - 1]) {
                    dist[time[1] - 1] = dist[time[0] - 1] + time[2];                    
                }
            } 
        }
        if (Arrays.stream(dist).anyMatch(i -> i == (int)1e9)) return -1;
        return Arrays.stream(dist).max().orElse(-1);
    }
